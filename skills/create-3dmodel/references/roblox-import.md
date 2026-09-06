# Standalone Roblox import

## Export

The established FBX route uses one source Blender unit per target stud and `global_scale=0.01`. Export selected meshes only, apply mesh modifiers, and exclude cameras/lights. This scale compensates for the current Blender FBX/Open Cloud route; verify imported dimensions rather than assuming it applies to all importers. GLB is a separate portable export with native dimensions.

Keep an object-name-to-display-color map in `part_colors.json`. Roblox may import geometry without the intended material colors, so tint the actual imported MeshParts from this map. Do not guess names when they differ: inspect the descendants and resolve the mapping.

## Upload

Use the included `scripts/upload_to_roblox.py` for FBX uploads when Open Cloud credentials are available and the user has requested an import. It is a separate copy of the working create-assets uploader. It takes file paths as arguments and configuration from the environment:

- `ROBLOX_OPENCLOUD_KEY` or `ROBLOX_OPENCLOUD_KEY_FILE`
- `ROBLOX_CREATOR_ID`
- `ROBLOX_CREATOR_TYPE` (`user` or `group`)
- optional `ROBLOX_ASSET_DESCRIPTION`

Use the authenticated creator appropriate to the requested game. Reuse known configuration without exposing secret values. Do not commit credentials or embed them in scripts or command arguments. If setup is missing, keep the finished files and report precisely what is needed for import.

The helper records IDs beside the exported files. Inspect its output and `asset_ids.json` for a successful ID; process completion alone is insufficient. If an upload is pending or insertion fails, check the existing asset before issuing another upload. Do not duplicate assets in an automatic retry loop. A successful upload is not proof of a successful rendered import.

## Studio

1. List Studio sessions and match the user's requested name/place. Confirm the place ID through a read-only call. Reuse a name already supplied by the user; ask only if the target is still ambiguous. Always send the matched `studio_id` on subsequent calls.
2. Check that the target supports the Edit DataModel. Do not automatically switch other sessions or run a playtest.
3. Insert the uploaded asset into a fresh, clearly named review container in Workspace. Place it on a known clear surface near a useful review location. Avoid moving existing content.
4. Create shallow, descriptive Folder groups inside the imported Model for its components (for example `Hoops`, `Staves`, `LidPlanks`, and `Base`). Reparent existing MeshParts into the appropriate folders while preserving their CFrames and the model pivot. Verify every part appears exactly once in the intended group. Inspect every inserted descendant. Remove imported `PackageLink` objects, apply the recorded colors, and anchor the model for review. For a decorative preview, disable collision and cast shadows. A requested physical/gameplay model needs settings chosen for that function instead.
5. Measure the resulting dimensions against `model-info.json`. Correct a demonstrated importer scale mismatch uniformly, and record it. Orient the model upright with a sensible pivot, then select it and frame the Studio camera.
6. Capture and inspect the actual Studio view after its mesh and texture content has loaded. An assigned asset ID alone does not prove that the geometry is visible; if the first capture is blank, check the existing import and allow a bounded loading check before considering another upload. Check all parts render, materials match reasonably, dimensions are correct, and the prop is above the surface. Record place/session, asset ID, instance path, and verification in the model's README and metadata.

Do not place this prop in a skin's Decor folder unless the user explicitly requests that placement. Do not add gameplay scripts, labels, or preview infrastructure that the model does not need.

## Textured foliage

The measured leaf-card route uses UVs exported in the FBX, an original RGBA PNG, and a SurfaceAppearance on each foliage MeshPart. Upload the PNG through the Studio bridge's `upload_image` from a temporary loopback-only HTTP server; use the returned image ID for `SurfaceAppearance.ColorMap`. Set `AlphaMode = Enum.AlphaMode.Transparency` and `MeshPart.DoubleSided = true`, and keep the part color white. Remove conflicting imported texture/appearance assignments before applying the intended material. Stop the temporary server after upload. Inspect the actual Studio result to verify alpha-cutout edges, readable leaf size, UVs and back faces; retain the texture source and asset mapping beside the model.
