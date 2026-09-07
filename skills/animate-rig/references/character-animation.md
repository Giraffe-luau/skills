# Authored Roblox character animation

Read for player/NPC humanoid clips such as crouch, walk and sprint. Character pose style is a separate choice from the approved fish procedural-motion style.

## Current user direction: expressive R6 crouch

The user rejected a technically working crouch with a small shuffle and barely moving arms. They want distinctive readable poses: forward torso lean, opposing raised arm positions, one leg reaching forward while the other folds back, and a clear exchange of these roles while walking. Support the stride with body twist and a stable head; increasing leg amplitude alone does not produce the requested style.

Visual references: [front](images/r6-crouch-front.png), [back](images/r6-crouch-back.png). These are user-supplied style targets, not evidence that a generated clip has been approved.

The revised example lives in the consuming project at `scrolling-mechanism/animations/crouch-r6-02/`: editable Blender actions, native clip exports, source references, runtime scripts and validation notes. The user explicitly approved this revised crouch on 2026-09-07 ("okay this amazing") and asked to carry its expressive style into sprint. Approval applies to this crouch, not to future animations automatically. The first pass in `crouch-r6-01` was rejected visually.

## Inspect the actual reference

- Confirm the live Humanoid.RigType and each joint's Part0, Part1, C0 and C1. R6 has rigid limbs without knees or elbows. Deliberate joint translations can suggest a folded leg; do not constrain the motion to tiny hip rotations merely because knees are absent.
- A posed dummy may store its pose in modified C1 offsets, while its saved KeyframeSequence contains different motion. Inspect both. In this example, `Workspace["Ventcover(CanOpen)and Crouch"]["Del me"].R6` matched the screenshots; `Anim.AnimSaves.Crouch` was a lower crawl. Using the latter without comparison lost the intended arm silhouette.
- Derive a posed part's world transform from the model itself. For a standard target Motor6D, the required animation transform is `C0:Inverse() * parentWorld:Inverse() * childWorld * C1`. Preserve the target's bind offsets; express the retargeted motion in the clip.

## Author and transfer clips

For this user's character animations, produce actual editable keyframe actions and Animator clips. Do not substitute per-frame Motor6D posing because earlier fish loops used procedural code. Code may build the authoring rig and key poses; runtime should play the resulting Animation assets.

Use contact, down, passing and opposite-contact poses. Make the opposite arm accompany each forward leg, with a little follow-through rather than all limbs reversing in one beat. Inspect front, side and back silhouettes, ground contact, intermediate poses, limb intersections and the loop seam. Match cadence to movement speed.

Roblox coordinates map to Blender as `(X, -Z, Y)`. Distinguish a Blender bone's rest-axis matrix from its associated part's orientation; bake evaluated bone transforms back into the joint-local hierarchy. Native R6 KeyframeSequence poses are nested `HumanoidRootPart > Torso > Head/Arms/Legs`. Keep the root container weight zero and animated child weights one.

Open Cloud successfully uploaded these native `.rbxmx` KeyframeSequences with assetType `Animation` and content type `model/x-rbxm`. Recheck [current supported formats](https://create.roblox.com/docs/cloud/guides/usage-assets) when changing the pipeline. Retain editable sources and asset IDs. Temporary registered clip IDs only prove Studio playback; verify the published Animation IDs load through Animator.

## Integrate and verify the requested controls

Keep the scope the user requested. A crouch animation trial does not require a reusable component framework, sprint system or unrelated skills.

Let the server own movement state and speed; let the character owner play tracks through a server-created Animator so supported animation replication works. Clip priority and blending must override normal locomotion while crouched and release it cleanly afterward. Per-frame camera/track-weight updates are distinct from procedural joint posing.

Treat animated root offsets and Humanoid.HipHeight together. Lowering both independently can bury the character. The current trial lowers R6 HipHeight by 1 stud and offsets the authored pose upward by the same amount to retain the intended world pose. This is an example, not a universal rig constant.

Exercise real hold/release input, stationary and moving poses, speed restoration, jump-state restoration and any installed ceiling check. Release held input on focus loss or typing, and reset state across respawn. If standing is blocked, retain crouch until space clears. Confirm client tracks appear on the server; do not claim a multi-client visual test from that alone.

Record which checks actually ran. Separate runtime correctness, visual self-review and user style approval. Animation errors from imported reference scripts may concern different asset IDs; identify the source before replacing or disabling unrelated reference content.
