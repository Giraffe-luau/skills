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
