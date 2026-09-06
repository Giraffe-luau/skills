# Standalone prop construction

Use the approved shapes and finish as a starting point, then let the current reference determine the object's construction. Broad facets, smooth curves and textured foliage can coexist in the same pack. Skin layouts and raster icon recipes are separate workflows.

## Read the reference before building

Identify the subtype, silhouette, cross-section, openings, proportions and colour regions. Compare the ratio of solid material to empty space, the thickness of framing, the height of lids, and how attachments meet their supports. A recognizable outline is only the start.

An open rail barricade is not a thick panel with rounded holes. A lantern with a pitched roof is not a globe lamp. A low stepped chest with chunky blue framing is not a tall domed chest with thin bands. Do not add details such as reflectors or a gold latch when they materially change the supplied design.

Read colour blocks as part of the construction. A red hydrant still needs deliberate differences between its body, bands, flanges and caps. Do not assign nearly identical colours and expect smooth shading to provide the missing separation. Judge scale in the game world: contact-sheet tiles often resize different objects to the same apparent height.

For a new family, resolve one representative asset's construction and vulnerable views before multiplying recolours. A shared helper must not impose a generic cube, spherical canopy, thin loop bow or branching plant when the reference calls for a different subtype. Distinguish a style experiment awaiting review from a user-approved example.

## Spend geometry on the form

Start with sparse cross-sections, shaped profiles, extrusions and sweeps. Add loops where taper, flare, curvature or a joint requires them. Avoid voxel remeshing as the default for simple stylised shapes. Measure evaluated triangles per component after modifiers; a few thousand is not a target or a claimed Roblox platform limit.

Use the representation the form requires:

- A barrel needs bulging staves and hoops fitted to their changing radius.
- A shovel blade needs a concave scoop with thickness and a rounded outline. A narrow wedge or flat plate cannot express the same form.
- A D-grip needs a coherent fork/socket and real opening. Two diagonal bars meeting a shaft are insufficient.
- A pick head needs a changing section; taper its tips in width and thickness.
- A trophy needs an open bowl, shaped stem and fitted handles.
- An inflatable animal needs a dimensional muzzle and neck. Increasing the thickness of a flat silhouette does not supply anatomy.

Keep functional pieces independently editable: barrel hoops, chest lid, wheels, handles, foliage and hardware. Within a continuous manufactured or inflated component, use connected topology or verified unions when overlapping pieces would create visible seams. Joining objects in a list does not connect their geometry. Do not merge everything merely because it shares a colour.

Apply transforms before bevels. With `primitive_cube_add(size=1)`, object scale is the full intended dimension, not half of it. Scale bevel width to the prop and keep it below seam spacing; around 0.02–0.03 units on a roughly 3-stud prop is a useful starting point. One or two segments often suffice. Preserve broad planar faces and avoid tiny bevels becoming the main source of polygon count.

## Fit joints and prevent flicker

Check the full attachment section against the actual receiving surface, including taper, bevels and endpoint direction. A centreline touching a surface is not a fitted joint.

- Seat shafts within sockets and cap them cleanly. Keep a crate brace against its plank face and inside the frame's depth.
- An open chest or gift needs actual walls, floor and rim; opening its lid above a solid body block does not create a cavity. Detached lids need a deliberate resting point or hinge. Fit loose contents to the receiving surface so a mound does not bury them.
- When scaling a compound helper, scale its profile heights, radii and attachment offsets consistently. Check both small and large uses: scaling only a bell's radius while scaling its loop on all axes produces stretched miniature bells and detached full-size loops.
- Compute the trophy wall radius at each handle's attachment height. Bury both lower handle ends within that wall without exposing them inside the bowl.
- Put a cable's complete end section inside its insulator. A centreline near the block's upper face leaves the cable perched on top. Check its radius and entry angle from above and the side.
- Make castle crowns thick enough for short, broad battlements. Cutting notches into an integral crown preserves the tower contour and avoids thin tabs, perched blocks and overhangs.
- Give adjacent coloured strips real thickness and separate them where appropriate. Side-by-side mane and tail strips avoid the z-fighting caused by stacked coplanar sheets. Check both sides and the rear, including every bend.

For closed tubes, use a continuous radial/vertical frame or a verified transported frame. Switching a sweep's reference axis near tangent alignment can twist the cross-section even when manifold and volume checks pass. Inspect the whole inflatable ring and the whole curved tail; checking only their endpoints misses this failure.

## Choose shading deliberately

Use smooth normals for continuous rounded surfaces such as trophy bowls and inflated bodies. Keep deliberate hard edges at rims, creases, cut faces and planar bases. When the reference calls for broad visible facets, retain those faces and their flat shading. Neither smoothing everything nor leaving everything flat reproduces the approved style.

Normal smoothing changes lighting interpolation, not silhouette or topology. It cannot repair a jagged outline, dense rough remesh, unsupported attachment or disconnected branch. Check that intended normals survive the exported Studio mesh, not just the Blender viewport.

## Trees, foliage and logs

Use a few broad radial faces, sparse taper/flare rings, a widened foot and angular connected branches for the approved faceted trunk direction. Carry supporting branches into the canopy instead of ending them visibly underneath it.

Choose foliage geometry from the reference:

- Recognizable textured oak leaves need original UV-mapped leaf clusters/cards or shaped leaves, not solid green spheres. Preserve canopy shape, leaf scale and density. Check the back and underside. Alpha-cutout cards are intentional open surfaces; validate UVs, normals, alpha and two-sided rendering rather than requiring sealed volume.
- Solid clustered canopies use a few coarse, deliberately faceted masses with varied size and placement when that is what the reference shows. Keep their trunks sparse and carry a continuous support through every stacked tier; isolated upper foliage must not float above an unfinished stem. This treatment is separate from textured oak leaves.
- Solid beach palms use broad folded blades with thickness, a raised centre ridge, taper and drooping tips. Keep their fronds long and narrow enough to read as a palm; the oak's textured-card treatment is not a default for every tree. Segmented angular trunks and coconut clusters follow the beach reference.
- The approved loose logs use orange/coral bark, broad longitudinal facets, pale polygonal cuts, a narrow bark lip and a few fitted branch stubs. Keep cuts nearly flush. Dense tubular growth rings and realistic dark bark were inappropriate for this reference.

## Upgrade design

Rare or celestial tools need a distinctive silhouette, proportions and thematic features. Recolouring a basic tool and attaching a badge is not enough. The celestial axe direction used twin crescents, dimensional feather/crystal forms and a shaped haft. Treat those as evidence of a meaningful upgrade, not required decorations for every special tool.

## Approved examples and their transferable lessons

These are user-reviewed examples, not fixed recipes for every new subject. The generated models remain in the consuming project; this skill does not require or redistribute them.

| Example | What worked |
| --- | --- |
| OakTree_03 | Six broad trunk faces, sparse taper/flare rings and connected branches; approved textured foliage preserved. Trunk: 109 vertices / 214 triangles, reduced from 3,202 triangles. Whole tree: 998 triangles. |
| Revised shovel, pickaxe and crate | Coherent grip, actual rounded scoop, tapered pick tips, and a brace fitted within the crate frame. |
| HandSaw_01 and Wrench_01 | Accepted tool silhouettes and construction; preserve them when revising other tools. |
| Trophy_02 | Smooth bowl/stem normals with handles seated into the actual tapered wall. |
| FireHydrant_02 and RoadBarricade_02 | Broad facets and purposeful red tonal regions; narrow open rails, rectangular gaps and matching yellow supports. |
| Streetlamp_04 | Straight tapered lantern sides, corner framing and pitched roof around a separate small Neon bulb; enclosing housing stays non-Neon. |
| UtilitySpan_02 and LogPile_02 | Cable sections seated in insulator blocks; simple loose logs with pale cuts. The three-log model uses 504 triangles versus 5,396 in the first attempt. |
| UnicornFloatie_02 | Rounded fused ring/neck/muzzle, pointed ears and forehead horn; separate coloured mane and tail strips with continuous sweep frames. |
| Sandcastle_02 and BeachChest_02 | Integral thick crowns with short notches; low stepped chest lid, chunky blue framing, broad corner feet and no invented gold latch. |

Approval of these replacements does not approve every other item in their packs. Preserve accepted components and apply new user feedback to the specific subject it concerns.

## Materials and preview setup

The tested local baseline is Blender 5.1.2 with EEVEE, Standard colour management, transparent film and PNG RGBA. Inspect the installed version rather than replacing it to match this example. Relevant baseline settings:

```python
scene.render.engine = "BLENDER_EEVEE"
scene.render.film_transparent = True
scene.view_settings.view_transform = "Standard"
scene.view_settings.look = "None"
scene.eevee.taa_render_samples = 96
scene.eevee.use_raytracing = True
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGBA"
```

AgX changes this palette's saturation and brightness; set the view transform before tuning colours. EEVEE properties vary by version, so do not blindly reuse removed options. Light with a broad area key above/to one side, a weaker opposing fill and moderate world illumination. Scale light energy to the object. Roughness around 0.4–0.5 is a starting point; reserve metallic response for components that need it.

Convert display hex/sRGB colours to linear values for Blender's Principled BSDF. Preserve the original display colours separately for Roblox Color3 assignment. In the established uploader route, vertex-colour-only materials did not survive reliably: use explicit part colours for untextured pieces, or UV textures when painted detail is required.

For lamps, keep the shell/frame, socket and small light source separate. Tune housing transparency and the bulb's Neon colour in Studio. Change global scene lighting when the user requests it; preserve the previous properties and compare the same assets/camera before and after. Use readable ambient fill and restrained bloom so lighting does not erase colour regions or conceal model faults. Record these property overrides; an FBX material alone does not reproduce the Studio setup.

## Painted curved surfaces

For a cambered board or other curved painted panel, triangulate the riding surface and surrounding rail deliberately. A single non-planar ngon can bridge across the intended curvature and hide portions of an inset texture even when both meshes are manifold. Triangulating alone is not sufficient: rail and inset must follow compatible curvature and maintain clearance over the whole surface, especially nose and tail. Check the full graphic from above in Blender and again on the imported UV-mapped mesh. Smooth normals across a continuous cambered riding surface while retaining hard rail and sidewall edges; flat fan triangles can leave visible diagonal shading across otherwise correct artwork in Studio. Keep raised silhouette details separately editable. If the user plans to add a material pattern in Studio, retain plain coloured geometry instead of baking that pattern into the asset.

The user approved the soft painted gradients on the fish and requested that treatment across the asset packs. The user subsequently approved the full gradient revision and explicitly requested gradients on everything. Use soft painted gradients by default across all new model families, rather than only the fish or selected props; preserve intentional material regions, readable details and existing approved geometry unless a shape correction is requested. Use a UV-mapped colour atlas for broad hue/value transitions that complement the form, preserving deliberate facets and functional colour regions. Judge gradients under consistent lighting and keep their strength appropriate to each material. Inspect UV seams on both sides and around boolean cuts; cylindrical angle wrapping can accidentally sample another atlas region. Where the intended colouring is symmetric, a continuous projected mapping can avoid that seam. Keep scene-specific cast shadows out of the colour map.

## Review the vulnerable views

Use actual Blender renders and actual Studio captures. Inspect a gameplay view plus views that expose the likely failure: crate side, shovel profile, bowl interior, both handle joints, cable entry, crown top, foliage underside, or floatie rear. A distant overview and a successful asset ID do not validate those details.

Check evaluated dimensions, triangle counts, winding, non-manifold edges and positive volume for intended solids. Hollow objects still need wall thickness and connected rims. Inspect gaps, z-fighting, bevel intersections, colour boundaries and shading after export. Fix defects in the source and rebuild the affected models; do not regenerate approved neighbours as part of an unrelated correction.

Keep technical validation separate from visual approval. Closed individual meshes can still form a solid-filled chest, intersecting frames or floating fittings. During a requested pack audit, record coverage per asset and distinguish observed visual defects, source-confirmed risks and subjective reference/proportion judgments. Do not describe a coplanarity risk as observed flicker without seeing it, or call a full pack correct based on distant overviews.

Use textures for small flush surface markings such as strawberry seeds, pineapple skin and birch bark. Do not model them as protruding beads or thin pieces that intersect tapered surfaces. Fruit species need distinct silhouettes and species-appropriate leaves/crowns; do not reuse one generic leaf on every fruit. Judge fruit sizes together in world units so a grape bunch does not dwarf the collection. The pineapple needs a recognisable stiff crown and diamond skin treatment; a yellow cylinder with palm fronds is insufficient.
