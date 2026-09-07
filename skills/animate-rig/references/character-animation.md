# Authored Roblox character animation

Read for player/NPC humanoid clips such as crouch, walk, sprint and jump. Character pose style is a separate choice from the approved fish procedural-motion style.

## Approved character style and checkpoint

The approved set combines distinct arm and leg silhouettes, opposing strides, torso weight shifts and visible head follow-through. Keep walking calmer than sprinting; make jump takeoff, air and landing visibly different. The target is readable, expressive R6 movement rather than restrained limb rotation or a motionless head. Adapt the degree of expression to each action instead of copying the crouch pose into every clip.

The user approved crouch and then the revised walk/run/jump set on 2026-09-07. These published clips identify the exact checkpoint in Scrolling Mechanism; ownership/access must be checked before reusing IDs in a different experience.

| Clip | Animation ID |
| --- | --- |
| CrouchIdle | 115149728349128 |
| CrouchWalk | 121938816258462 |
| ExpressiveWalk | 88911655018911 |
| ExpressiveRun | 119721740009543 |
| JumpStart | 94009355231418 |
| FallLoop | 87057410438552 |
| Land | 79803826118806 |

Editable Blender actions, native exports and runtime sources remain in the consuming project's `scrolling-mechanism/animations/crouch-r6-02/` and `locomotion-r6-02/` folders. The portable construction lessons and visual references are bundled here. Retain original reference attribution when adapting supplied clips.

## Current user direction: expressive R6 crouch

The user rejected a technically working crouch with a small shuffle and barely moving arms. They want distinctive readable poses: forward torso lean, opposing raised arm positions, one leg reaching forward while the other folds back, and a clear exchange of these roles while walking. Support the stride with body twist and a readable gaze with authored head follow-through; a stable gaze does not mean a static head. Increasing leg amplitude alone does not produce the requested style.

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

## Sprint integration example

The first sprint pass is in `scrolling-mechanism/animations/sprint-r6-01/`. It carries the approved crouch's expressive motion into upright running: forward torso lean, opposing arm pumps and a visibly folded recovery leg. The user subsequently rejected this first sprint visually for insufficient arm/leg expression and a nearly static head; its runtime integration checks still apply.

When adding sprint to crouch, use one owner for movement speed. Independently saving/restoring WalkSpeed in two scripts can restore the sprint speed after crouching or multiply an already reduced speed. The tested implementation preserves the spawn baseline and derives walk/crouch/sprint speeds from one server state; crouch takes priority, including while standing is blocked by a ceiling.

The actual Play checks covered Shift+C transitions in both release orders, stationary track suppression, jump-animation handoff, server-visible tracks and respawn followed by working input/animation on the new character. Left Shift uses a higher-priority ContextActionService binding so it does not also toggle camera lock. Preserve other camera controls.

Audio and footsteps are explicitly deferred by the user to a future audio skill and refinement pass. Do not add them opportunistically while making movement animations.

## Second locomotion pass: walk, run and jump

The user rejected the first sprint visually: its arms/legs lacked expression and the head appeared static. Keep the earlier runtime checks as evidence of functionality only. Head motion needs authored pitch, yaw and roll with stride-related follow-through; merely enlarging limbs or translating the whole body is insufficient.

Visual targets: [run](images/r6-run-target.png), [walk/run comparison](images/r6-walk-run-comparison.png).

The next pass in `scrolling-mechanism/animations/locomotion-r6-02/` studied all seven user-provided walk/run clips. It adapts `Run1 [by M0rsDev]` and `Walk2 [by emm1gar]`, retaining attribution, adding head motion and correcting ground contact. It also authors JumpStart, FallLoop and Land. The user explicitly approved this revised walk, run and jump set on 2026-09-07 ("these look so good") and requested that the skill and repository be updated. Use this set, alongside the approved crouch, as the current character-style baseline. Approval does not extend to every future animation or to unperformed runtime tests.

Do not assume the first same-named Workspace model is the intended reference: this scene had two BestRunAnimR6 containers, one without a rig. Inspect children and select the actual rig. Compare stride/contact poses rather than selecting whichever frame is closest to standing; the latter conceals the distinctive motion. Some saved frames omit individual poses: interpolate each joint's own keyed timeline instead of inserting identity transforms.

The jump controller uses separate takeoff, sustained-air and landing clips, switching back into walk/run afterward while preserving normal Humanoid physics. Keep those mutually exclusive states explicit, and let crouch suppress the locomotion tracks. The installed Play test verified the five uploaded clips, visible head movement, front/back motion and JumpStart → FallLoop → Land → run transitions. New-controller respawn and multi-client visual tests were not run in this pass.

## Approved supporting camera feedback

On 2026-09-07 the user approved the subtle sprint-camera feedback as making the action feel more complete, and asked that skills consider such finishing touches. The tested example adds 12° FOV (70° → 82°) with exponential easing, about ±0.35° stride-related roll, and small positional bob. Use these as an example to tune, not universal defaults. Read actual movement and the existing Sprinting/Crouching state; held Shift alone must not activate motion. Fade ground bob in the air and restore the normal view on stopping/crouching.

Remove the previous additive camera offset before the standard camera update and apply the new one afterward. Preserve the crouch CameraOffset, honor Scriptable-camera handoffs and external baseline FOV changes, reduce close-camera motion and expose independent FOV/shake controls. The sprint example verified walking, sprinting, jump, crouch, stationary Shift, Scriptable handoff and respawn; first-person comfort and multiple clients were not tested. Project source: `scrolling-mechanism/camera/sprint-camera-01/`.

## Held tools, full-body effort and locomotion layers

The user rejected a fishing system whose character stood still, then approved the authored winding motion but requested a holding idle, walking with the rod, moving legs and increasing lean as the pull intensifies. Author the whole interaction: carrying, action entry, working loop and return to carrying. For an R6 reel, derive the hand target from the real RightGrip/Tool Grip and crank pivot; rotate the prop crank from the evaluated hand angle rather than allowing independent animation clocks to drift.

Use partial-joint clips for carrying and moving actions so held arms coexist with walk/run legs. Use full-body clips for a planted action, including staggered feet, leg rocking and torso weight shifts. For varying effort, synchronize compatible light/heavy loops and blend their weights from the interaction state. Transition to a locomotion-compatible action layer when moving and back to the full-body stance when planted. Keep movement modifiers in the existing speed owner and restore them on completion/cancellation. The tested fishing pass used 16 studs/s for carrying and 8 during a cast, not a permanent immobilization. These speeds and the fishing action are examples, not universal tool defaults.


## Animated idles and distinct tool carries

A held pose repeated across keyframes is still visually static. The user explicitly rejected this for both the fishing rod and empty-handed standing. Give an idle a restrained breathing cycle, weight transfer, arm response and head follow-through; inspect samples separated in time and the complete loop. Keep planted feet stable while the torso shifts. Do not claim an idle is animated merely because an AnimationTrack is playing.

For this fishing example, walking keeps the rod in front with both arms, while sprinting carries it back over the right shoulder and frees the left arm to swing. A right-arm-only sprint clip preserves the approved run's torso, head, left arm and legs. The prop grip eases between fitted orientations and is restored when walking, stopping, casting or unequipping. Replicate grip changes so other clients can see the same hold. Confirm the shaft direction and clearance from a side view; a rear screenshot can hide a forward-facing rod. These poses are this user's requested fishing style, not requirements for every held tool.

Route stationary empty-handed idle, stationary held idle, walking carry, sprint carry and active interaction explicitly. Require actual movement for shoulder carry; held Shift alone must stay idle. Full-body idles must yield to crouch, jumping and working clips. Preserve approved locomotion rather than overriding every joint with a carry pose. The current authored example lives in `scrolling-mechanism/animations/character-idles-01/`, with controllers in `gameplay/fishing-prototype-03/`. Runtime and side-view checks are recorded with the project; user style approval remains pending.
