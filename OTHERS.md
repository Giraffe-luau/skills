# Skill & command master list

Everything raised across the conversation, including ideas you didn't pick and ones I argued against. Delete rows freely.

**Split rule used:** a **Skill** needs bundled references (style boards, approved examples, reference docs) or a multi-step procedure that produces an artifact. A **Command** is one-shot, fast, no bundled files, mostly reads/analyses/answers. It's a judgement call on the borderline ones — move rows between tables as you see fit.

**Markers:** `[built]` already in the repo · `[roadmap]` already on your ROADMAP · `[low]` I'd argue against building it

---

## Skills

| Name | Description | Notes |
| --- | --- | --- |
| concept | Concept art variants for a subject before any 3D work, in your own model style | Same as skill just auto-triggered |
| turnaround | Front, side and back views of an approved concept as a modelling reference |
| silhouette | Black-shape-only pass to check a design reads at distance |
| variants | Colourways, tiers and rarity sets generated from one approved concept |
| sheet | A whole asset pack designed in one consistent pass before modelling starts |
| moodboard | Assemble reference boards before anything gets built |
| style-guide | Extract a written visual style guide from your already-approved assets |
| palette | Lock a game-wide colour palette and apply it across models, UI and icons |
| texture | Surface appearance and material work matching your gradient finish |
| modular-kit | Build a tileable modular building kit instead of one-off props |
| terrain | Terrain sculpting and painting passes |
| lod | Generate low-detail variants of models for mobile |
| rig-check | Validate attachments, Motor6D and humanoid setup before animating |
| pose | Key poses sketched out before rigging or animating |
| emote-pack | Reusable character animation sets |
| avatar-item | UGC accessories and clothing as a separate revenue line |
| decal | Signage, posters and in-world 2D art |
| building `[roadmap]` | Environments, structures and scene composition |
| blockout | Grey-shape environment pass to test scale, sightlines and flow before building |
| paintover | Paint over a screenshot of your real game to show what it could look like |
| lighting | Lighting rig, atmosphere and colour grading, driven conversationally |
| mood | Colour and lighting keys, same scene at three times of day, before lighting it |
| vfx `[roadmap]` | Visual effects and feedback, with particles folded in as a reference file |
| particles `[roadmap]` | Particles and auras — merge into vfx rather than shipping separately |
| vfx-preset | Reusable named effect presets for hit, pickup, level-up and similar |
| vfx-key | A still frame of an effect at peak impact before building the particles |
| ui `[roadmap]` | Screenshot-driven UI work — redo this frame, add a button here |
| ui-concept | Styled screen mockups to choose between before building |
| wireframe | Grey-box layout and hierarchy before any styling |
| thumbnail | Thumbnail ideation, generation in a locked style, and CTR performance review |
| screenshot-set | The full store-page image set, consistent across all five |
| sfx `[roadmap]` | Sound design and implementation, coordinated with visual feedback |
| music | Ambient and loop tracks, including licensing check |
| audio-mix | SoundGroups, spatial falloff, ducking and volume balance pass |
| scripting `[roadmap]` | Code conventions, project structure and maintainable implementation |
| scaffold | First iteration of a new game — core loop, vertical slice, architecture locked |
| module | Write a new service singleton to house conventions |
| data-service | Save systems: session locking, schema versioning, migration, failure handling |
| migrate | Live data schema migration on a game with real players |
| npc | Pathfinding and behaviour trees |
| combat | Hit detection, hitboxes, lag compensation |
| inventory | Inventory and equip systems |
| leaderboard | Global boards via OrderedDataStore |
| quest | Quest and objective systems |
| shop | In-game store, UI and product wiring |
| matchmaking | Reserved servers, teleports, lobby flow |
| cross-server | MessagingService events and global announcements |
| admin | In-game moderation and admin commands |
| feature-flag | Remote config so you can kill a broken feature without republishing |
| state-machine | Player and NPC state handling |
| telemetry | Design the custom event schema before you need the data |
| localize | Translation setup and string extraction |
| studio-plugin | Write Roblox Studio plugins to automate repetitive editor tasks |
| open-cloud | Programmatic asset upload, DataStore access, place publishing, analytics pulls |
| exploit-audit | Remote validation and client-trust boundary review |
| perf | Per-device performance profile: parts, draw calls, streaming, texture memory |
| mobile-pass | Phone-specific checks: tap targets, thumbstick overlap, FOV |
| accessibility | Colourblind safety, text size on phone, one-handed controls |
| playtest | Launch Play mode, drive the game, capture screenshots and Output errors, report |
| simulate-player | Play the game as a bored nine-year-old and report where it got stuck or quit |
| regression | Re-run a saved set of playtests after a change |
| game-design `[roadmap]` | Overall concept, complete game loop, feel and progression |
| game-idea | Concepts scored on saturation, two-person buildability and monetisation shape |
| trend-scan | Fetch live chart data and decompose top games into hook, loop, monetisation |
| onboarding | Design and audit the first sixty seconds of play |
| update-spec | Turn a prioritised problem into one concrete change with acceptance criteria |
| feedback-digest | Nightly Discord and comment pull, clustered and cross-referenced with the funnel |
| plan-update | Prioritised change list tied to a specific metric, from analytics plus feedback |
| ship | Full pre-release sweep including policy, age rating and compliance checks |
| monetise | Analytics-driven monetisation review: conversion, ARPPU, dead products |
| event | Timed content drops, plus the countdown icon swap workflow |
| notifications | Experience notifications to pull lapsed players back |
| subscriptions | Recurring revenue instead of one-off passes |
| rewarded-ads | Monetise the ninety-five percent who never spend |
| badges | Badge design as a retention hook rather than an afterthought |
| ugc-drop | Limited avatar items tied to in-game events |
| social-hooks | Friend joins, party play and invite loops |
| creator-store | Sell the asset packs your modelling skill already produces |
| ad-campaign | Sponsored ads setup and budget maths |
| creator-outreach | Find small Roblox creators and draft the pitch |
| group-page | Roblox group branding, store and comms |
| keyword | Title and description against actual Roblox search behaviour |
| competitor | Deep-dive one rival game rather than the whole chart |
| clip | Cut playtest footage into a postable short-form edit with captions |
| trailer | The longer game-page video |
| storyboard | Frames for a trailer or short before shooting any footage |
| learn | Turn a tutorial, video or DevForum thread into a reference file in the library |
| skill-new | Scaffold a new skill in your house style, with the boundary-declaring frontmatter |
| skill-audit | Test whether skill descriptions actually trigger, catch overlaps |
| skill-eval | Regression-test a skill against saved example prompts |
| checkpoint | Update README and ROADMAP, record approvals, reconcile Claude/Codex/repo copies, publish |
| client-skill | Build a bespoke skill for a consultancy client |

---

## Commands

| Name | Description |
| --- | --- |
| [/concept](https://www.reddit.com/r/OpenAI/comments/1w8y3uh/astra_generates_an_image_of_a_concept_then/#lightbox) | Concept art variants for a subject before any 3D work, in your own model style |
| /fix | Paste an error, stack trace or Output screenshot, get the diagnosis and corrected code |
| /why | Explain Roblox's weird semantics: replication timing, deferred events, load order |
| /review | Point at code, get conventions plus exploit plus perf in one pass |
| /explain | Read a system back to me, I wrote it three weeks ago and forgot |
| /clean | Dead code, unused instances, orphaned assets |
| /convert | Format and asset juggling in either direction |
| /error-triage | Read error analytics, group crashes, rank by players affected |
| /replication-check | Find things running server-side that should be client-side and vice versa |
| /asset-audit | Unused meshes, duplicate uploads and oversized textures in a place |
| /audio-feedback | Map every player action to a sound, find the silent ones |
| /next | What should I work on, given backlog, metrics and what's half-finished |
| /wrap | End of session: what changed, what's broken, what's next, checkpoint it |
| /note | Capture a decision, bug or idea mid-flow without breaking focus |
| /todo | Add to, reprioritise and prune the backlog |
| /stats | Thirty-second glance at CCU, revenue and errors |
| /decide | Record an architecture decision so the next session doesn't re-litigate it |
| /approve | Capture an approved output into a skill's references properly |
| /devlog | Running log of what changed each session |
| /daily-report | Scheduled — yesterday's CCU, revenue, D1, error rate in one digest |
| /watchdog | Scheduled — alert when CCU drops past a threshold or errors spike |
| /competitor-watch | Scheduled — diff a rival game's updates, thumbnails, description and prices |
| /algo-watch | Scheduled — track where your game appears on discovery rows over time |
| /comment-sweep | Scheduled — daily pull and triage of new comments and reviews |
| /backup | Scheduled — place file archive on a timer |
| /changelog | Track Roblox platform release notes for changes that affect your game |
| /sentiment | Classify comments, reviews and Discord chatter into themes |
| /patch-notes | Write the update announcement in your game's voice |
| /post-mortem | Why a metric moved this week |
| /pricing-test | Structured robux price experiments |
| /rev-forecast | Project revenue from current CCU and conversion rate |
| /revenue-report | Earnings pull, DevEx maths, summary you can hand an accountant |
| /moderation-risk | Pre-flag asset names, decals and text that could get moderated before upload |
| /chat-safety | Audit that all user-generated text goes through TextFilter |
| /age-check | Content against Roblox age guidelines before moderation flags it |
| /data-request | Handle a player data deletion request, UK and GDPR shaped |
| /clone-check | Detect someone reuploading your game or assets |
| /dmca | File the takedown when they have |
| /standup | What each of you did, what's blocked |
| /split-work | Break a feature into your lane and Luau's |
| /handover | Write enough context for Luau to pick up your half cold |
| /estimate | Time estimates calibrated against what you two actually shipped before |
| /split | Collaborator revenue-split agreement |
| /commission-brief | Brief for a freelance artist or dev, with rates |
| /scope | Cut a feature list to what two people can ship in a month |
| /premortem | Assume the launch flopped, list why, before you start |
| /kill | Argue against your own game idea as hard as possible before committing months |
| /steal | Break down exactly how a top game builds one mechanic, then spec your version |
| /cold-read | Hand someone zero-context your game page, see if they can describe the game |
| /first-impression | Three-second look at thumbnail and title, would you click, why. Cheap CTR proxy |
| /sunset | Decide when a game is dead and what's worth salvaging |
| /name | Game name generation checked against Roblox search collisions |
| /balance `[low]` | Tuning numbers — no fetch step, no reference, just a prompt |
| /name-my-game `[low]` | Duplicate of name, and thin on its own |
| /write-description `[low]` | Belongs inside ship or keyword, not standalone |

---

## Notes worth keeping

- Every expensive production skill should have a cheap sketch counterpart, and the sketch's output becomes the production skill's input. Concept to model. Blockout to build. Wireframe to UI. Storyboard to clip.
- Planning skills need a named data source and a file output, or they produce confident nonsense from stale priors.
- Rename anything called `update` — description-based triggering will fire it on "update my model".
- Merge vfx and particles. Two skills covering one thing will contradict each other.
- Things folded into bigger skills should be `references/*.md` that the parent is told to read at a named point, otherwise they silently never happen.
- Daily skills have to return in one shot and ask nothing, or they don't survive a week.
- Skills fire on demand, conventions fire always. House style belongs in CLAUDE.md, not a command you have to remember to type.
