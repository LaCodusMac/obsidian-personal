---
title: "Family Bots"
aliases: [Family Hermes]
type: project
status: active
priority: low
started: 2026-01-01
tags: [project, hermes, telegram, family]
---

Hermes instances set up for [[Mom]] and [[Nana]], so they can work with agentic AI the same way I do — via Telegram. Same [[Hermes Agent]] foundation, just pointed at them. Used on and off.

## The instances
- **[[Mom]]** — her own Hermes access over Telegram, to use agentic AI similarly to how I use mine.
- **[[Nana]]** — same, for her.

## Architecture
**One Hermes agent, separate Telegram processes per person.** It's not three separate agents — it's the same [[Hermes Agent]] on the Lenovo P3 Mini, fronted by a distinct Telegram process for me, for [[Mom]], and for [[Nana]].

## ⚠️ Memory isolation
Because it's a single shared agent, the open question that matters is whether memory is **partitioned per Telegram user** inside that one agent. If it isn't, context could bleed across people — e.g. something from my chat surfacing in Mom's, or her details in mine. Worth confirming and, if needed, scoping memory by user ID. (Tracked in [[Hermes Agent]].)

## Open Questions
- Is memory scoped per user, or one shared pool? (see above)
- Anything specific they lean on it for (reminders, Q&A, media), or general-purpose?

## Related
- Parent: [[Hermes Agent]]
- People: [[Mom]], [[Nana]]

## Log
- 2026-07-28: Note created. Linked to Mom and Nana.
- 2026-07-28: Clarified these are Hermes instances for Mom/Nana to use agentic AI similarly, via Telegram.
- 2026-07-28: Confirmed architecture — one Hermes agent, separate Telegram processes per person. Flagged per-user memory isolation as the remaining question.
