# Giraffe skills

Reusable skills for Claude Code and Codex.

Upcoming skill topics and deferred work are recorded in [ROADMAP.md](ROADMAP.md).

## Available skills

| Skill | Purpose |
| --- | --- |
| [create-3dmodel](skills/create-3dmodel/SKILL.md) | Build and rig stylised low-poly models in Blender, with soft painted gradients, editable geometry, exports and optional Roblox Studio import. |
| [animate-rig](skills/animate-rig/SKILL.md) | Animate existing rigs and verify them in a working Roblox playtest, including swimming and environmental motion such as wind sway. |
| [create-icon](skills/create-icon/SKILL.md) | Generate chunky, angular game icons with a heavy #161616 outline, colored depth planes, and broad highlights. |

The icon skill includes the working prompt, subject examples, and original four-icon reference board. Generated icon collections are kept in the consuming project and are not included here.

## Install

Clone the repository:

```sh
git clone https://github.com/Giraffe-luau/skills.git
cd skills
```

For Claude Code, copy the skill to your personal skills directory:

```sh
mkdir -p ~/.claude/skills
cp -R skills/create-icon ~/.claude/skills/
```

Then invoke:

```text
/create-icon a red shopping basket
/create-icon a carrot, a tomato, and a pineapple
```

Claude Code supports personal skills across projects through `~/.claude/skills/`. See the [official skill documentation](https://code.claude.com/docs/en/skills).

For Codex, install the same folder under its user skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/create-icon "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Start a new Codex session if the new skill is not listed, then invoke:

```text
$create-icon a red shopping basket
```

If you already have a `create-icon` folder, compare or back it up before copying an update over it. Run `git pull` in this checkout and copy the skill again to update installed copies.

## 3D model skill checkpoint

`create-3dmodel` includes construction and review guidance for standalone props and small asset packs, approved modelling examples, Roblox import instructions, and an optional FBX uploader. Soft painted gradients are the default across model families, while preserving functional Neon, transparency and approved artwork. The checkpoint covers deliberate facets versus smooth surfaces, sparse tree geometry, fitted tool and cable joints, separate lamp housing/bulbs, simple logs, and the approved unicorn floatie, castle crowns and chunky beach chest. It also documents current pack folders, archived iterations and preservation of user-adjusted scales and placements.

Rigging is part of model creation when the intended movement calls for bending or articulation, including trees and foliage responding to wind. The rigging reference covers skin weights, preserved gradient UVs, the measured Blender-to-Roblox scale and pivot workflow, and deformation checks. Rigid whole-object movement can use the model pivot without adding a skeleton.

The uploader saves each successful model ID beside its own FBX, preserves existing records and completed uploads in partially failed batches, and identifies pending operations before a retry. Generated models, screenshots and credentials are not included.

Install an independent copy for either assistant:

```sh
cp -R skills/create-3dmodel ~/.claude/skills/
cp -R skills/create-3dmodel "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Compare or back up an existing installation before replacing it. These are manual copies; pulling or editing this repository does not automatically update user skills, and user-skill edits do not automatically update this repository.

Invoke `/create-3dmodel a barrel` in Claude Code, or `$create-3dmodel a barrel` in Codex. Blender must be available locally or through a connected execution tool. Roblox import additionally needs access to the intended Studio session and upload credentials; the skill itself does not install these integrations. `create-assets` remains a separate skin-design workflow and is not included here.

## Animation skill checkpoint

`animate-rig` covers procedural bone/joint motion or authored clips, a usable runtime preview, and actual Play-mode verification. Its fish reference records the user-approved body-to-tail wave, independent fin strokes, swim paths and preview controls, plus jumping, caught-fish struggles and landed flops. The approved fishing rod adds a flexible shaft and fitted line guides; the caught fish stays attached through its posed mouth. Tree wind response is included as guidance for future work; it has not yet been implemented or approved as an example.

Install independent local copies:

```sh
cp -R skills/animate-rig ~/.claude/skills/
cp -R skills/animate-rig "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Invoke `/animate-rig make these fish swim in a playtest` in Claude Code, or `$animate-rig make these fish swim in a playtest` in Codex. The assistant needs access to the intended Roblox Studio session. The skill distinguishes client-side visual previews from server-authoritative gameplay and does not install a fishing system.

## Image-generation requirement

The skill supplies instructions, a prompt, and a visual reference. Your assistant also needs an image-generation tool that can receive the reference image. The original recipe uses Codex's built-in image generator. Claude Code needs an image-generation integration with equivalent image-reference support; installing this skill alone does not add one.

Use the unchanged [prompt](skills/create-icon/references/prompt.txt), replace `{SUBJECT}`, and attach the [original board](skills/create-icon/references/style-board.png). Results vary between runs and image models. The skill preserves the original PNG and exact prompt so iterations can be reviewed.

Default outputs go to the project's established icon folder, or `art/faceted-icons/`: originals and prompts under `tests/<subject-number>/`, plus a PNG-only collection under `icon-sets/`. The default background is green chroma, or magenta for green subjects. No Roblox uploads are performed by this skill.

## Add another skill

Add a folder under `skills/<name>/` containing a `SKILL.md` with `name` and `description` frontmatter. Bundle only the supporting files needed to run it. Keep paths relative to the skill and generated deliverables in the consuming project.
