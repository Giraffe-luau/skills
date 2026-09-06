---
name: create-icon
description: Generate standalone raster game UI icons in the Giraffe angular, faceted style using the bundled prompt and reference board. Use for individual icons or themed icon sets, including objects, crops, weather, tools, and social symbols.
---

# Create Icon

Generate an icon of the requested subject using the established visual recipe. Accept the subject and optional destination from the invoking message, for example `/create-icon a red shopping basket` in Claude Code or `$create-icon a red shopping basket` in Codex.

## Prompt and reference

1. Read [references/prompt.txt](references/prompt.txt) in full. Replace only `{SUBJECT}` with a concrete description of the requested object, colors, and essential features. Keep the shared style wording unchanged unless the user requests a style revision.
2. View [references/style-board.png](references/style-board.png) and attach that actual file to the image generator as the sole style reference. Resolve paths relative to this skill's directory, regardless of the current working directory. The board contains a frame, cash, document, and purple social symbol. Generate the requested object only.
3. Generate one fresh, square raster image per requested icon. For a set, use a separate request per object with the same prompt and board. Do not generate an icon sheet and crop it apart.

Use the host's available image-generation tool with image-reference support. In Codex, prefer the built-in image generator. In Claude Code, use an available image-generation integration and pass both the complete prompt and reference image to it. A text-only request does not reproduce this workflow. If no such tool is available, save the completed prompt and identify the missing capability; do not claim an image was generated or substitute SVG, procedural drawing, or a Blender render. Do not silently switch providers or models during iteration. Record the tool and model if exposed; never invent a model identifier.

The original recipe was developed with Codex's built-in image generator. The same prompt and board establish a repeatable style target, not identical outputs across tools or runs.

## Visual checks

- The exterior is a very thick, angular **#161616** band. The prompt's visible single-edge width target is **10–12% of the icon's shorter dimension**. Check it at thumbnail size rather than assuming the generator obeyed.
- Preserve broad highlights, darker colored side planes, and underside shading. These give the object thickness. Do not flatten all shading to make an icon simpler.
- Use a few large readable features. Avoid elaborate hardware, ornament, fine texture, soft inflated outlines, and excessive small facets.
- Check the depth direction against the board's purple symbol and document: the visible dark depth is on the left/lower-left. Choose a compatible view for the subject; do not mirror a logo or text to fix its depth. Mention visible deviations honestly.
- Check the object's proportions. A basket should be compact and roomy, not a long squeezed trough. Subject-specific feedback belongs in `{SUBJECT}`, not in new global style rules. Relevant examples are in [references/subjects.md](references/subjects.md).

Show one candidate per requested icon for review. When the user requests another attempt, change the subject description narrowly and make a fresh generation from the master prompt and original board. Preserve earlier attempts. Do not start an unsolicited chain of edits or regenerations. Follow an explicit request to edit an existing image when given.

## Save and deliver

Use the user's requested output root. Otherwise reuse an established project icon directory with `tests/` and `icon-sets/`; if none exists, use `art/faceted-icons/` in the current project.

For each icon, choose the next unused subject slug and number, checking both destinations, such as `shopping-basket-01`:

```text
<output-root>/tests/<slug>/<subject>.png
<output-root>/tests/<slug>/prompt.txt
<output-root>/tests/<slug>/generation.md
<output-root>/icon-sets/<slug>.png
```

Keep the original generated PNG unchanged in `tests/` and copy identical bytes to `icon-sets/`. Store the exact submitted prompt. In `generation.md`, record the reference file's SHA-256, tool/model when known, and any observed mismatch. The flat `icon-sets/` folder contains PNGs only. Never overwrite a different existing output; allocate the next number instead.

Preserve the prompt's green chroma background, or magenta for green subjects. Do not automatically remove backgrounds, redraw outlines, resize, clean up, or retouch originals. A user request for transparency overrides this default; ask the image generator for it and preserve the raw output.

Return the generated preview and saved paths, with any material visual limitation. Do not claim the user's approval. Uploading to Roblox or altering Studio UI requires a separate user request.

Keep this skill repository limited to instructions, prompts, and the reference board. Write generated icons into the consuming project, never into the installed skill folder. Do not replace or rebuild the board, or add generated examples to it, unless the user explicitly asks.
