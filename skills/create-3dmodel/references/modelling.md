# Standalone prop construction

Derived from the successful create-assets modelling workflow, without its skin assembly steps.

## Shape and finish

- Chunky, low-poly geometry with moulded, softened edges and readable proportions. Use a small material palette, broad faces, and real bevel highlights. No thick black icon outlines on 3D models.
- Model the object's actual silhouette. A barrel needs tapered ends, a bulging middle, and hoops following that changing radius. A plain cylinder with floating rings loses those cues.
- Use geometry for seams and raised details that must hold up from multiple angles. Keep small features thick enough to read at game distance. Avoid dense realism or decorative detail unless requested.
- Scale bevel width to the object and keep it below seam spacing. On a roughly 3-stud prop, widths around 0.02-0.03 units with 2 segments are a useful starting point. Preserve deliberate hard edges when smoothing normals; do not confuse normal smoothing with smoothing the geometry.
- Apply transforms before bevels. With `primitive_cube_add(size=1)`, object scale corresponds to the desired full dimensions, not half dimensions.
- For untextured props, keep colors separate by material/object for the established Roblox upload pipeline, where vertex-color-only materials did not survive. Use UV-mapped image materials when the reference needs painted surface detail; a single textured material can contain multiple colors. Preserve functional separation as well: same color is not a reason to fuse a lid with a handle.
- Measure a prop against the world, not a contact sheet that resizes everything to fill its own tile. Treat one Blender unit as one intended Roblox stud in this workflow.

## Materials and renders

The working local baseline is Blender 5.1.2, EEVEE, Standard color management, transparent film, and PNG RGBA. Inspect the installed Blender API when another version is present.

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

AgX changes the saturation and brightness of this style. Set the intended view transform before tuning the palette. EEVEE property names change between Blender versions; do not blindly set old `use_gtao` properties.

Use a broad area key above and to one side, a weaker fill opposite it, and moderate world illumination. Aim the lights at the object. Adjust energy to the model's actual scale and distance; no single wattage fits every model. Plastic-like roughness around 0.4-0.5 is a starting point. Reserve metallic material response for metal components.

When a palette is written as display hex/sRGB colors, convert to linear RGB before assigning Principled BSDF base colors. Store the original display colors separately for Roblox Color3 assignment.

Frame an angled view to show depth and an alternate view that can reveal what the first conceals. Use front views for silhouettes and faces, top views for flat props, and back views for objects visible from all sides. Keep lighting and cameras out of mesh exports.

## Geometry checks

Evaluate meshes after modifiers for triangle counts. Check boundary/non-manifold edges and normals for pieces intended to be solid. Intentional openings in a hollow object still require wall thickness and properly connected rim geometry. Validate the intended design, not a universal requirement that all models be sealed solids.

Watch for z-fighting, buried raised details, excessive seam gaps, detached attachments, and bevel self-intersections. Rendered inspection is required alongside numerical checks.

The first barrel example uses 12 shaped staves, two fitted hoops, six inset lid planks, and a base. These are subject-specific choices, not a template for every prop.


## Lessons from reviewed model revisions

- **Choose the correct representation.** Flat extrusions suit genuinely plate-like pieces. A curved tool head needs a swept, changing cross-section; a scoop needs an actual concave surface and thickness. Model curvature across depth as well as in the outline. Taper sharp ends in both dimensions so they do not become broad chisel tips unintentionally.
- **Construct continuous components.** A D-grip is a coherent fork/socket with a real opening, not two diagonal bars touching a shaft. Use connected topology or a verified union where the manufactured part should be continuous. Keep separate parts where the real design has a joint or material boundary. Joining objects in a list does not make their geometry continuous.
- **Fit the junctions.** Insert a shaft into a fitted socket, blend necks into the supported form, and terminate caps cleanly. Avoid exposed pegs, collars cutting through heads, or decorative pieces visibly stuck on without a seat. Watch coplanar surfaces after booleans and bevels. On the revised shovel, unioning clean base meshes before bevels avoided fragmented junctions.
- **Measure protrusion relative to neighbours.** The crate brace belongs against the plank face and within the outer frame's depth. A nonzero gap is not evidence of a proper fit. Check front, side and oblique views and compare the actual face planes before export.
- **Preserve deliberate roundness.** Low-poly describes the economy of geometry, not a requirement to make every surface flat. Use enough outline segments for a rounded blade and smooth shading where continuous bowl curvature should read clearly. Keep bevels and intentionally planar surfaces crisp.
- **Special tiers need shape design.** When a user asks for a rare, upgraded, celestial or similarly special item, develop a stronger silhouette, proportions, material treatment and one or two thematic features. Recoloring a basic shape and attaching a badge is insufficient. The accepted direction for the celestial axe added twin crescents, dimensional feathers/crystals and a shaped haft. Treat those as an example of meaningful upgrade design, not details to copy onto every special item.
- **Review the vulnerable view.** Front views can conceal a protruding brace or a paper-thin head. Add side/oblique inspection for attachments and section changes; look into bowls and handle openings. Fix the geometry demonstrated to be wrong instead of hiding it with camera angle or shading.

For new subjects, apply the same reasoning: a saw needs a coherent pierced grip and teeth integrated into its cutting edge; a trophy needs an open cup with connected handles; logs need end faces that fit the bark; a tree needs convincing trunk/branch transitions. Avoid accumulating extra surface decoration as a substitute for those forms.

## Shading, foliage, and attachment review

When references call for broad visible facets, model those faces deliberately and retain their shading; this overrides the general smooth-surface default. Otherwise default to smooth shading on continuous curved surfaces: bowls, stems, organic trunks, rounded handles, and moulded forms. Preserve sharp normals at deliberate creases, rims, planar bases and cutting edges. Flat shading is an intentional visual choice, not the default consequence of low polygon count. Set smooth face shading and intentional sharp edges in the source, and verify that their normals survive export. Smooth shading changes the lighting interpolation, not the silhouette or topology. Use geometry smoothing only when the form itself needs correction, such as rough remeshed branch junctions; recheck their thickness afterward. Judge normals in the exported Studio mesh as well as Blender; smooth shading cannot repair a jagged silhouette or a poorly joined branch.

Inspect each attachment endpoint at close range after bevels. Compute the supporting surface at the actual endpoint height: a tapered cup has a different radius at its lower handle joint than at the rim. Check the full handle cross-section against the wall, not just its center point. Seat handle ends within the wall without exposing their ends inside the bowl. Inspect both lower joints from a low oblique view and the bowl interior from above. A wide overview does not validate these junctions.

When tree references show recognizable leaves, use original leaf textures with UV-mapped clusters/cards or shaped leaves, rather than substituting solid green spheres. Choose the foliage treatment from the reference: painted clumps, layered leaf cards, or shaped fronds need different geometry. Preserve the requested canopy silhouette and use smooth trunk/branch shading. Carry supporting branches into the foliage so their cut or pointed ends do not stop visibly below it. Inspect the rear and underside as well as the front; keep leaf scale and density readable at gameplay distance. Alpha-cutout foliage cards are intentional open surfaces: validate their UVs, normals and two-sided rendering instead of requiring sealed volume. Export and verify the actual texture in Studio; a local Blender material alone is not a delivered textured model.

## Approved example: broad faceted tree trunk

The user explicitly preferred OakTree_03's simple trunk over both the dense remeshed original and the smooth-shaded revision. The successful form used six broad radial faces, a few taper/flare rings, a widened foot, and angular connected branches. Its visible roundness came from an intentionally shaped cross-section. Broad flat shading was part of the requested design; neither adding vertices nor applying smooth shading alone solved the problem.

The trunk used 109 vertices and 214 evaluated triangles, down from 3,202 triangles in the preceding revision. The whole tree used 998 triangles. The previously approved textured foliage was preserved. These measurements are evidence of an effective simplification, not fixed limits for other trees.

For comparable simple stylised forms, build the main silhouette from sparse rings or controlled profiles first. Avoid voxel remeshing as the default. Spend geometry on silhouette changes and fitted junctions, then measure each component after modifiers. Preserve intentional facets when the reference shows them; keep smooth shading for genuinely continuous surfaces such as the approved trophy bowl.

The measured example is named OakTree_03 in the originating project. Generated models are not included in this skill checkpoint; the construction guidance and measurements above are self-contained.


## Match the reference's construction and colour structure

Identify the object's subtype and its solid-to-empty balance before building it. In the street set, a slim open rail barricade was incorrectly replaced by a thick panel with capsule holes, dark feet and added reflector strips. Match rail/post thickness, opening proportions and support shape; omit details absent from the chosen reference when they materially change the design. Likewise, a compact faceted globe lamp is a different design from a square lantern with a pitched roof.

Read colour regions as part of the design. A predominantly red hydrant can still require contrasting body, flanges, recessed bands and caps. Preserve those purposeful tonal differences instead of assigning almost identical reds and relying on smooth shading. Compare head/body proportions, outlet length and game-world scale alongside the silhouette. Use broad flat facets where the reference calls for them; the accepted smooth trophy does not imply every manufactured prop should be smooth.

## Approved street-set direction

The user approved FireHydrant_02 and RoadBarricade_02. The hydrant uses broad facets, purposeful red tonal regions, stepped flanges, shorter outlets and a larger overall scale. The barricade uses narrow rails and uprights, large rectangular openings and matching yellow supports. Carry forward their simplified proportions, economical topology and colour separation when developing comparable street props. These approvals do not extend to every item in the set.

For a lamp, model its outer housing and internal light source separately. Keep the cap, socket and enclosing frame or glass readable around a smaller Neon bulb. Do not make the entire outer globe Neon: the resulting glare erases the housing and changes the silhouette. Check both the bulb's visibility and the surrounding structure in the actual Studio view; tune transparency and emission without changing global scene lighting.

When defining a new asset family, use the requested small review set to establish the style before expanding it. Preserve accepted items while iterating on the specific remaining issues; record further approvals and corrections here as they occur.
