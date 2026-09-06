---
name: create-3dmodel
description: Build or modify standalone stylised low-poly 3D game props and small asset packs in Blender, with editable geometry, previews, and mesh exports. Skin design and skin decoration kits belong to create-assets; raster UI icons belong to create-icon.
---

# Create 3D Model

Create the requested standalone prop or small asset pack in the established chunky style, using deliberate facets, fitted joints and smooth surfaces where the reference calls for them. Keep this workflow separate from skin layout, skin configuration, and UI icon generation. It works in Claude Code and Codex with local Blender or a connected Blender execution tool.

## Build

Read [references/modelling.md](references/modelling.md) before modelling. Use the user's reference and intended function to choose the silhouette, materials, scale, and separately editable parts. If no size is given, state a reasonable game-scale assumption and proceed. Ask only when an unknown dimension or function affects compatibility with an existing object.

Locate Blender on the current machine; prefer its installed executable and a fresh headless process for a reproducible build. On macOS the usual application path is `/Applications/Blender.app/Contents/MacOS/Blender`. Inspect the actual version and reuse compatible local examples. Do not install or replace Blender merely to match a recorded version.

Keep the modelling script as the source of truth. Save into the consuming project's established model directory, or `assets/models/<subject>-<revision>/` when none exists:

```text
build_<subject>.py
<Subject>.blend
<Subject>.fbx
<Subject>.glb          # useful portable preview/export when supported
preview.png
front.png             # choose a second view that exposes likely defects
model-info.json
part_colors.json
README.md
```

Use a new revision for a new visual attempt; preserve existing work. Group the model independently from cameras and lights. Give parts meaningful names and one material per mesh object; use a single display color for untextured parts or an explicit UV texture for textured parts. Retain functionally distinct parts even when they share a material. A barrel's hoops, lid, and body must remain independently editable. Apply object scale before bevels and export. Put the prop's placement origin at its base center unless its use calls for another pivot.

Inside the Roblox Model, organise parts into clearly named Folder instances by function or component type instead of leaving a flat list of MeshParts. For example, a barrel can contain `Hoops`, `Staves`, `LidPlanks`, and `Base`. Choose groups appropriate to each object; keep the hierarchy shallow and do not make a folder for every individual part. Preserve meaningful part names and independent editability. When organising an existing model, reparent its parts without changing their transforms, appearance, or model pivot. Record the grouping in the model metadata so it can be recreated after import.


## Construction quality

Build the form that makes the object work: a cupped shovel blade, a continuous handle fork, a tapered pick head, or a genuinely hollow trophy bowl. A recognizable outline alone is insufficient. Before modelling, identify the defining silhouette, cross-section, junctions, openings, frame thickness and colour regions; choose the simplest geometry that expresses them. Prefer a few deliberate faces and controlled taper/flare loops over dense remeshed surfaces for simple stylised forms.

Use the construction and upgrade guidance in [references/modelling.md](references/modelling.md). Keep distinct functional components editable, while making each manufactured component coherent. Check attachments from the side and at each endpoint, curved forms in profile, and special items as silhouettes before adding surface details. Follow the approved reference: retain broad facets when they define the style; otherwise smooth continuous curved surfaces while retaining intentional hard edges. Match leaf-texture detail when foliage references call for it.

## Verify and review

Render and actually inspect the geometry from its intended gameplay view and at least one revealing alternate view. Use Blender renders, not an AI-generated image of what the model might look like. Correct visible intersections, floating details, unusable proportions, and broken shading in the source model before delivering it.

Check dimensions, evaluated triangle counts after modifiers, material assignments, and closed/well-oriented geometry where the part is intended to be solid. Record the measured results and tool version in `model-info.json`. Start simple and add geometry only where it improves the required silhouette, curvature or joints. A simple component may need only tens or hundreds of triangles; do not treat a few thousand as a target. Record evaluated counts per component and for the whole model. Do not confuse the local budget with a current platform limit.

Deliver the model and previews for user review. Do not claim approval or in-game verification from a render alone. Make requested revisions in the source and rebuild the outputs; keep original attempts unless removal is requested. Preserve models and features the user explicitly approves. A correction to one object or to the skill does not call for regenerating approved objects.

## Roblox import when requested

Read [references/roblox-import.md](references/roblox-import.md) when the user asks to upload or place the model in Studio. Reuse explicit session and upload authorization from the conversation. Verify the requested Studio session before making any changes; do not fall back to a different open game.

Place new assets within the project's established pack/review structure, select and frame them for review. When replacing a current model, preserve the user's latest scale and placement and archive its earlier revision; follow the organisation guidance in the import reference. Skin folders and skin assembly remain the responsibility of `create-assets`. Do not enter Play mode to preview a prop.

## Learn from user feedback

When the user corrects an output or explicitly approves an improvement, save the reusable finding in this skill during that task without waiting for a separate reminder. Apply this to the active installed copy. Update another installation only when the user has authorised it. Update the relevant existing guidance instead of appending a transcript or duplicate rules, and briefly tell the user what was saved.

Distinguish explicit approval from the assistant's own visual checks. Record why an accepted revision works, including meaningful measurements when available; preserve approved components. Apply the lesson to comparable subjects without turning an example's polygon count, palette or topology into a universal requirement. New user references take precedence over earlier defaults.

## Local skill copies

Installed user skills and any shared skill repository are independent copies. Feedback capture in the active installation does not imply repository publishing. Update other installations or publish to the shared repository only when requested or already authorised by the user. Never create automatic syncs or replace independent copies with symlinks. Keep generated models in the consuming project, outside the installed skill.
