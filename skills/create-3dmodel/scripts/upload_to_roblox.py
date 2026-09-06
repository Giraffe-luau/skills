#!/usr/bin/env python3
"""Upload .fbx models to Roblox as Model assets via Open Cloud, print asset ids.

    python upload_to_roblox.py <file.fbx> [more.fbx ...]

Configuration comes from the ENVIRONMENT, never from argv, so a key cannot leak
into a shell history or a process list:

    ROBLOX_OPENCLOUD_KEY        the API key itself, or
    ROBLOX_OPENCLOUD_KEY_FILE   path to a file containing only the key
    ROBLOX_CREATOR_ID           your Roblox user id, or a group id
    ROBLOX_CREATOR_TYPE         "user" (default) or "group"
    ROBLOX_ASSET_DESCRIPTION    optional description stamped on each upload

Run with python3 and configure the environment as described above.

The key is never printed, and nothing is written anywhere except the
asset_ids.json beside the files you uploaded.

Open Cloud upload is asynchronous: the POST returns an operation which must be
polled until it reports done. A freshly uploaded asset is also subject to
moderation, so an id coming back does NOT guarantee it is renderable yet.

NOTE: this uploads MODELS. Do not use it for PNGs -- an Open Cloud upload with
assetType "Decal" returns a wrapper id that renders blank. Images go through the
Studio bridge's upload_image instead; see the skill's references/roblox-import.md.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid

API = "https://apis.roblox.com/assets/v1/assets"
OPS = "https://apis.roblox.com/assets/v1/operations/"


def config():
    key = os.environ.get("ROBLOX_OPENCLOUD_KEY", "").strip()
    key_file = os.environ.get("ROBLOX_OPENCLOUD_KEY_FILE", "").strip()
    if not key and key_file:
        try:
            with open(os.path.expanduser(key_file), "r", encoding="utf-8") as fh:
                key = fh.read().strip()
        except OSError as exc:
            sys.exit(f"could not read ROBLOX_OPENCLOUD_KEY_FILE: {exc}")
    if not key:
        sys.exit("set ROBLOX_OPENCLOUD_KEY or ROBLOX_OPENCLOUD_KEY_FILE "
                 "(see references/roblox-import.md)")

    creator = os.environ.get("ROBLOX_CREATOR_ID", "").strip()
    if not creator.isdigit():
        sys.exit("set ROBLOX_CREATOR_ID to your numeric Roblox user or group id "
                 "(see references/roblox-import.md)")

    ctype = os.environ.get("ROBLOX_CREATOR_TYPE", "user").strip().lower()
    if ctype not in ("user", "group"):
        sys.exit('ROBLOX_CREATOR_TYPE must be "user" or "group"')

    desc = os.environ.get("ROBLOX_ASSET_DESCRIPTION", "").strip() or "Prop kit"
    return key, creator, ctype, desc


def multipart(fields, filename, blob, content_type):
    boundary = "----" + uuid.uuid4().hex
    parts = []
    for name, value in fields.items():
        parts.append(
            f"--{boundary}\r\nContent-Disposition: form-data; "
            f'name="{name}"\r\n\r\n{value}\r\n'.encode()
        )
    parts.append(
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"fileContent\"; "
        f'filename="{filename}"\r\nContent-Type: {content_type}\r\n\r\n'.encode()
    )
    parts.append(blob)
    parts.append(f"\r\n--{boundary}--\r\n".encode())
    return b"".join(parts), f"multipart/form-data; boundary={boundary}"


def request(url, key, data=None, ctype=None, method="GET"):
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("x-api-key", key)
    if ctype:
        req.add_header("Content-Type", ctype)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {"raw": body[:400]}


# Roblox wants the asset type and the MIME type to agree with the file. A .png
# uploaded as "Model" is rejected outright, so both come from the extension.
KIND = {".fbx": ("Model", "model/fbx")}


def upload(path, key, creator, creator_type, description):
    name = os.path.splitext(os.path.basename(path))[0]
    ext = os.path.splitext(path)[1].lower()
    if ext not in KIND:
        return None, (f"unsupported file type {ext} -- this uploader handles .fbx only; "
                      "images go through the Studio bridge's upload_image")
    asset_type, mime = KIND[ext]
    with open(path, "rb") as fh:
        blob = fh.read()
    meta = {
        "assetType": asset_type,
        "displayName": name,
        "description": description,
        "creationContext": {"creator": {f"{creator_type}Id": creator}},
    }
    body, ctype = multipart({"request": json.dumps(meta)},
                            os.path.basename(path), blob, mime)
    status, res = request(API, key, body, ctype, "POST")
    if status not in (200, 201):
        return None, f"HTTP {status} {json.dumps(res)[:300]}"

    op = res.get("operationId") or (res.get("path", "").split("/")[-1])
    if not op:
        return None, f"no operationId in {json.dumps(res)[:300]}"

    # poll: uploads are async, and the first few polls normally 404 or say done=false
    for _ in range(40):
        time.sleep(2.0)
        st, r = request(OPS + op, key)
        if st == 200 and r.get("done"):
            asset_id = (r.get("response") or {}).get("assetId")
            if asset_id:
                return str(asset_id), None
            return None, f"done but no assetId: {json.dumps(r)[:300]}"
        if st not in (200, 404):
            return None, f"poll HTTP {st} {json.dumps(r)[:200]}"
    return None, f"operation {op} still pending after polling; inspect {OPS + op} before retrying"


def record_asset(path, asset_id):
    """Persist each success beside its own source, including partial batches."""
    name = os.path.splitext(os.path.basename(path))[0]
    out = os.path.join(os.path.dirname(os.path.abspath(path)), "asset_ids.json")
    existing = {}
    if os.path.exists(out):
        with open(out, "r", encoding="utf-8") as fh:
            existing = json.load(fh)
    existing[name] = asset_id
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(existing, fh, indent=2, sort_keys=True)
        fh.write("\n")
    return out


def main():
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    key, creator, creator_type, description = config()
    failed = False
    for path in files:
        name = os.path.splitext(os.path.basename(path))[0]
        asset_id, err = upload(path, key, creator, creator_type, description)
        if err:
            failed = True
            print(f"FAIL {name}: {err}", flush=True)
        else:
            print(f"OK   {name} -> {asset_id}", flush=True)
            out = record_asset(path, asset_id)
            print(f"wrote {out}", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
