# Approved fish swimming example

The user explicitly approved the four-fish rig and swimming preview on 2026-09-07. The successful result preserved the soft painted gradients while adding visible body bends, tail swishes and independent fin strokes. This is an approved starting point for comparable fish, not a universal skeleton or animation budget.

## Rig and appearance

The example has an unweighted Root, then Body; Head and Spine branch from Body; TailBase and TailTip continue from Spine. Dorsal, Anal, PectoralLeft and PectoralRight control the fins. Fin roots blend into body weights and eye details follow Head. The original silhouette, texture pixels and triangle counts were preserved.

The imported fish face model +X, with +Y up in Studio. For each bone, convert the model's up and forward vectors into the bone's bind-local coordinates before applying pose rotations. Derive these from the actual model; the exported bone axes need not match world axes.

## Measured motion

At about 1.35 tail cycles per second, the tested yaw angles were:

| Control | Amplitude | Phase relative to wave |
| --- | ---: | ---: |
| Body | 1.5° | +0.5 radians |
| Head | −2° | +0.5 radians |
| Spine | 7° | 0 |
| TailBase | 13° | −0.55 radians |
| TailTip | 20° | −1.1 radians |
| Dorsal | 3° | −0.3 radians |
| Anal | −4° | −0.5 radians |

Each angle is amplitude × sin(wave + phase). Tail angles are relative to their parent bones, so accumulated bend is greater than a single control's value. Side fins use opposing 14° strokes about the fish's forward axis at 0.65 times the wave frequency. A slight 3° body roll and 0.16-stud vertical bob add movement without hiding the main swim cycle. Different phase offsets prevent all fish stroking together.

For the display, fish follow 2-by-3-stud ellipse radii at 0.38 radians per second, face the path tangent, and float 3 studs above the authored display positions. Sharing the travel phase preserves the row's spacing while separate stroke phases add variation. These are demonstration dimensions; adjust speed, clearance and turning radius to the actual scene.

## Reuse and limits

Provide swimming in place as well as travel so the user can judge skin deformation. Use an exit/reopen camera control and pause/resume. Keep the original Edit-time poses and placements intact. The verified example used client-side Bone.Transform motion with no uploaded animation clip, and Persistent streaming for the four small fish. It demonstrated swimming; it did not implement water collision, navigation, catching or server-authoritative fish simulation.

The original project implementation is FishSwimPreview.client.luau beside the fish-rig-01 assets. Its project-specific paths, names and camera layout should be adapted to a new project. This reference is sufficient to reproduce the motion without access to that project.

## Approved additional variants

The user also approved the completed fishing rod and the extended preview on 2026-09-07: jumping, a caught fish struggling on a line, and a landed flop. Give them separate timing and poses: continuous launch/arc/dive paths with tangent-facing orientation and timed splashes; short faster struggling bursts for a catch; a side-lying curl/release and small hop for a landed fish. Preserve the gradient appearance and the fitted line/rod/fish relationship when extending these accepted examples.

For the catch, compute the mouth through the posed Head bone and solve the model pivot from that point each frame. Moving only a fixed model origin lets the mouth drift off the line as the head bends. Update the line through the rod's transformed guide bones and include gentle shaft flex. Pose sampling on all four fish kept mouth error below 0.00002 studs. A jump path should match position and velocity across phase boundaries; check submerged return clearance as well as the visible airborne arc. Choose landed height from the fish's rotated thickness and actual ground surface.

## Gameplay integration checkpoint

The next playable prototype (2026-09-07) reused these accepted fish/rod assets with a proximity-prompt pickup, welded Tool grip, cast float, timed bite, reel-in and landed flop. The server owns cast eligibility, deadlines and catch count; each client renders the replicated session's fish, posed guide lines and small timed water reactions. This is a separate integration example, not a change to the approved rig design.

Preserve a functional model pivot when converting the rod to a Tool: a PrimaryPart with a fitted PivotOffset lets the butt pivot follow the welded mesh. Solve the animated mouth against the line, including while blending from hanging to the side-lying landed pose. Check the hand grip and dock contact visually. The installed prototype verified a real E/F-input catch, early retrieval, missed bite, unequip cleanup and respawn/re-equip. Reeling samples measured a maximum mouth attachment error of 0.0000044 studs. Multiple real clients and touch/gamepad were not tested; gameplay feel awaits user review. Sources remain in `scrolling-mechanism/gameplay/fishing-prototype-01/`.

The user rejected the first gameplay presentation: the E prompt/HUD was unwanted, the character did not reel, and the 2.4-second fish transfer read as teleportation. The revised interaction uses direct clicks, an authored reeling character, an independently weighted crank, a clear water breach and a longer resisted path before the lift. Preserve spatial continuity at jump/struggle/lift/landing boundaries and make transitions legible at normal gameplay camera distance. A tiny decorative ripple is not sufficient evidence of a powerful water exit. The first winding motion was approved; progressive stance and carrying refinements remain a subsequent review.
