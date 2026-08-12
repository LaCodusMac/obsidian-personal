---
title: "Hermes Agent"
aliases: [Hermes]
type: project
status: active
priority: high
started: 2026-01-01
tags: [project, hermes, telegram, agent]
---

Hermes is my personal AI agent — **one agent**, not a chatbot. It takes plain-language instructions and turns them into real actions using built-in tools plus connected AI models: file handling, coding, web search, and more, run directly from the terminal or other platforms. It uses **memory** to improve its responses over time based on past interactions, which makes it an active assistant rather than a simple chatbot. I reach it through Telegram.

## Current Status
Active. Runs on my **Lenovo P3 Mini** as a Linux desktop instance. Connected via Telegram to three people: me, [[Mom]], and [[Nana]]. The [[KalshiWatch]] trading/monitoring stack is the most built-out thing it runs (its own systemd services, control bot, Grafana dashboards); [[Workout Tracker]] was itself created *through* Hermes over Telegram.

## How I interact with it
Through Telegram. The control bot ([[KalshiWatch]] `hermes_telegram_bot.py`) authorizes specific user IDs and responds to commands like `/status`, `/positions`, `/top`, `/pause_auto`, `/resume_auto`, `/kill_switch`, and manual `/buy_yes` `/buy_no` `/sell` order commands. Other modules add their own commands.

## Capabilities
- **File handling** — read/write/organize files on the host.
- **Coding** — writes and runs code; built [[Workout Tracker]] this way.
- **Web search** — pulls live information.
- **Connected AI models** — routes tasks to external models as needed.
- **Memory** — retains context from past interactions to improve over time.
- **Interfaces** — terminal directly, or remotely via Telegram (and "other platforms").

## What it runs
- **[[KalshiWatch]]** — Kalshi prediction-market signal + demo-trading + position-monitoring system. The heavy one.
- **[[Workout Tracker]]** — created *through* Hermes over Telegram; logs/tracks workouts.
- **[[Family Bots]]** — the [[Mom]] and [[Nana]] instances, so they can work with agentic AI the same way.

## Where it runs
On my **Lenovo P3 Mini**, as a Linux desktop instance (see [[Hardware Inventory]]). This is the Hermes host — distinct from the [[Home Lab]] NUC/Synology stack, though it lives on the same network ([[Network Stack]]). **[[KalshiWatch]]'s systemd services run here too**, on the P3 Mini alongside Hermes — not on a NUC.

## ⚠️ Not backed up
**Nothing is currently backing up Hermes** — not the memory store, not the configs, not the [[KalshiWatch]] data. Since the entire agent lives on one Lenovo P3 Mini, a drive failure or lost machine means losing the memory it's accumulated (the thing that makes it *Hermes* and not a fresh chatbot) plus all module state. This is the highest-value gap in the whole setup. **Plan: [[Backup — Hermes]]** (part of the [[Backups]] area).

## Open Questions
- Shared config/secrets model across what it runs? (KalshiWatch uses `config.demo.env` with Telegram bot tokens + allowed user IDs.)
- Does the single agent partition **memory per Telegram user**, or is it one shared memory pool? (It's one agent with separate Telegram processes — see [[Family Bots]] — so this determines whether my context and Mom's/Nana's stay separate.)
- Deployment/update flow — git pull + restart, or containerized?
- Where exactly does the memory live on disk (so a backup job can target it)?

## Related
- Projects: [[KalshiWatch]], [[Workout Tracker]], [[Family Bots]]
- People: [[Mom]], [[Nana]]
- Areas: [[Home Lab]]
- Resources: [[Self-Hosted Software]], [[Hardware Inventory]], [[Network Stack]]

## Log
- 2026-07-28: Note created. Hermes established as the parent hub for the Telegram agent; modules linked out.
- 2026-07-28: Corrected hosting to Lenovo P3 Mini (not NUC10). Added real capabilities (file handling, coding, web search, connected models, memory). Confirmed connected to me, Mom, and Nana via Telegram.
- 2026-07-28: Confirmed KalshiWatch systemd services run on the P3 Mini alongside Hermes. Confirmed single agent w/ separate Telegram processes per person. Recorded that nothing is currently backed up (flagged as top risk).
