---
name: animate-rig
description: Animate existing rigged Roblox models with bone or joint motion, reusable animation code or clips, and a verified Studio playtest. Use for authored character clips, swimming, wind-driven trees and foliage, idle loops, articulated prop actions, and requests to see a rig moving; mesh creation and skin weighting belong to create-3dmodel.
---

# Animate Rig

Turn an existing rig into visibly working motion while preserving its approved mesh, textures, gradients and scale. Match the requested scope: a swimming preview, an animation clip and a gameplay movement system are different deliverables.

## Inspect and choose the motion

Identify the target model, bind pose, bone/joint hierarchy, forward axis and existing animation controller. Check that skin weights actually deform the mesh before writing motion. If the rig is missing or broken, repair it with the installed create-3dmodel skill when available; do not disguise a rigid model's movement as bone animation.

Choose controls from the action: a fish needs a travelling body-to-tail wave, whereas a chest needs a lid pivot and a sensible stop angle. Use smaller stabilising motion near the head/body and deliberate follow-through toward free ends. Keep contact points and mechanical hinges fitted. Whole-model movement and articulation should support the same action; a swimming fish faces its travel direction.

For humanoid character animations such as crouch, walk, sprint and jump, read [references/character-animation.md](references/character-animation.md). It records the approved expressive R6 pose style, authored-clip workflow and character playtest checks.

For fish and similar swimming creatures, read [references/fish-swimming.md](references/fish-swimming.md), which records the user-approved example. Adapt it to the creature's anatomy instead of copying fish controls into unrelated rigs.

For environmental motion such as trees in wind, anchor the base, use slower trunk sway with increasing branch/tip response, and vary phases so foliage does not move as one rigid piece. Relate motion direction and intensity to the environment when a wind source exists. Keep this separate from deliberate whole-model travel: a rooted tree should not drift across the ground. Tree wind motion remains design guidance. The fish/rod previews and R6 character animations have separate verified examples; their approval does not imply that wind motion has been tested.

Use procedural motion for adjustable loops and immediate previews; use Animator tracks/clips when authored timing, transitions or animation-asset integration calls for them. Inspect existing tracks and scripts so two systems do not fight over the same controls.

## Consider supporting feedback

Consider subtle feedback that helps the action read and feel complete: eased camera/FOV response, contact reactions, fitted line tension, or a small timed splash. Choose effects that support the current interaction, keep them restrained and reversible, and test their timing with the animation. This is a consideration, not a requirement to add every effect or expand the task. Respect deferred work such as audio. The approved sprint-camera example and its integration lessons are in [references/character-animation.md](references/character-animation.md).

## Implement for Roblox

Bone.Transform is local animation state and does not replicate. A client preview must animate on each viewing client. For gameplay, separate server-authoritative movement/interactions from visual pose updates; client-only preview motion is not a multiplayer gameplay system.

Preserve Bone.CFrame bind transforms. Derive rotation axes from the actual bind pose and model orientation rather than assuming every imported bone uses the same axis. Cache those axes before moving the model. Drive loops from elapsed time, never fixed angles per frame. For a procedural preview, one named render binding can update the small group after animation evaluation; unbind it during cleanup.

Keep animation scripts in the consuming project, alongside an explanation of controls and installation. Preserve model placement in Edit mode; apply temporary display offsets at runtime. Handle removed models, missing controls and repeated installation without accumulating render connections or duplicate scripts. Use meaningful warnings for incomplete rigs.

## Make the requested playtest usable

When the user asks to press Play and see the animation, install a working runtime entry point and test that exact path. For a preview in an asset display scene, frame the subjects automatically and provide an exit back to the player camera. Pause/resume and a stationary motion mode help inspect articulation when travel would obscure it. Fit the view to all subjects and the viewport; avoid unrelated scene or UI changes.

Check streaming: a camera pointing toward distant models does not guarantee that those models are present on the client. For a few small preview rigs, Persistent model streaming is a measured option; use an appropriate streaming strategy for larger scenes. Keep preview-only camera takeover scoped to Studio unless a game-facing showcase was requested.

Confirm the intended Studio session and current mode before changing it. Starting Play is within a requested playtest; do not stop a user-started session just to install into Edit without existing authorization. Test the installed version, not a separate tool-only animation. Preserve independent project files and edits.

## Verify and deliver

Watch the actual textured mesh in Play, including a side view that reveals bending and attachments. Sample bone/joint transforms across time to confirm animation and sample model pivots separately to confirm travel. Changing bone values alone is insufficient: inspect visible deformation for detached fins, eyes, seams, intersections and texture distortion.

Exercise the preview controls: pause freezes pose and travel; resume restarts; stationary mode holds horizontal position while articulation continues; exit restores a usable player camera and return reopens the preview. Check the runtime console. Restore or leave Play running according to the user's intended review, and clearly state the final state.

Record the implemented motion, parameters, runtime location and what was actually verified. Distinguish procedural animation from uploaded clips, and visual previews from physics/gameplay. Save explicit user approval and reusable corrections in both independent local Claude and Codex skill copies. Publishing a shared repository requires a repository update request; generated game assets remain in the consuming project.
