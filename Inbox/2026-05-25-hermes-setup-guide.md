---
date: 2026-05-25
source: chatgpt
title: "Hermes setup guide"
category: "Coding & Dev Projects"
tags: [chatgpt-import, project/531-tracker]
status: pending-review
sensitive: false
---

**You:** how to setup hermes

**ChatGPT:** Hermes can mean a few different things. I’m going to assume you mean **Hermes/MQTT voice assistant setup for Home Assistant** unless you meant something like Hermes email, Hermes protocol, or a specific app.

**ChatGPT:** For **Home Assistant voice**, Hermes usually means **Rhasspy using MQTT/Hermes protocol**.

Basic setup:

1. **Install MQTT broker

**You:** hermes agent

**ChatGPT:** Ah — you mean urlHermes Agent by Nous Researchhttps://hermes-agent.org/, the self-hosted AI agent. citeturn0search3turn0search6

Given your setup (Ubuntu servers, Docker, Home Assistant, NUCs, Plex/NAS, Kalshi bot work), you’re actually in a really good spot to run it properly.

## Recommended Setup For You

Run Hermes on:
- your stronger Intel NUC
- Ubuntu
- inside its own VM or Docker container
- accessible through Telegram or Discord

Use:
- Ollama locally for free/private models
- or OpenRouter for stronger cloud models

For your use case, I’d recommend:
- **Hermes + Ollama locally** first
- then optionally OpenRouter later

---

# Minimum Requirements

Hermes officially supports:
- Ubuntu/Linux
- macOS
- WSL2 on Windows citeturn0search1turn0search4

You’ll want:
- 8GB+ RAM
- persistent uptime
- Python/Node handled automatically by installer

---

# Step 1 — Install Hermes

On Ubuntu:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Official installer docs:  
urlHermes Installation Docshttps://hermes-agent.nousresearch.com/docs/getting-started/installation citeturn0search1

After install:

```bash
source ~/.bashrc
```

Verify:

```bash
hermes --version
```

---

# Step 2 — Install Ollama (Recommended)

This gives you local/private AI models.

Install:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then pull a model:

```bash
ollama pull qwen3
```

or:

```bash
ollama pull gemma3
```

For your hardware:
- Qwen is probably the best balance
- Gemma works great too
- don’t start with giant 70B models

---

# Step 3 — Configure Hermes

Run:

```bash
hermes setup
```

Choose:
- Custom Endpoint
- URL:

```text
http://127.0.0.1:11434/v1
```

No API key needed for local Ollama. citeturn0search8turn0search4

---

# Step 4 — Start Hermes

```bash
hermes
```

Now you can talk to the agent locally.

Try:

```text
What files are in this directory?
```

or:

```text
Analyze my Docker containers
```

---

# Step 5 — Add Telegram (Highly Recommended)

This is where Hermes becomes actually useful.

Run:

```bash
hermes gateway
```

It walks you through:
- Telegram
- Discord
- Slack
- etc. citeturn0search3turn0search8

For you:
- Telegram is probably best
- lets you interact with your server remotely
- very useful for homelab + bot monitoring

---

# Step 6 — Make It Persistent

Since you already use Linux servers:

Use:
- tmux
- or systemd

tmux example:

```bash
tmux new -s hermes
hermes gateway
```

Detach:

```bash
CTRL+B then D
```

Reconnect:

```bash
tmux attach -t hermes
```

---

# What Hermes Is Actually Good At

It shines at:
- persistent memory
- terminal automation
- server management
- coding workflows
- scheduled tasks
- messaging integrations
- long-running personal AI assistant

It is NOT:
- magic AGI
- fully autonomous DevOps
- safe to blindly give root access

Treat it like:
> “An AI sysadmin assistant with memory.”

---

# For Your Homelab Specifically

You could realistically use it for:
- monitoring Kalshi bot logs
- summarizing Grafana alerts
- Home Assistant automations
- Docker/container management
- Plex/NAS administration
- Telegram notifications
- daily summaries

---

# One Important Warning

Do NOT immediately give Hermes:
- unrestricted sudo
- full SSH access everywhere
- exposed internet access

Start sandboxed.

Prefer:
- Docker
- limited Linux user
- scoped directories

Especially because agent frameworks can absolutely make bad decisions if over-permissioned.

---

# Your Best Architecture

For your setup, I’d do:

```text
NUC Ubuntu Server
 ├── Docker
 ├── Ollama
 ├── Hermes Agent
 ├── Grafana
 ├── Kalshi Bot
 └── Telegram Gateway
```

That’s honestly a very strong self-hosted AI stack.

GitHub repo:  
urlNousResearch Hermes Agent GitHubhttps://github.com/nousresearch/hermes-agent citeturn0search6

**You:** I have it setup with codex

**ChatGPT:** Perfect — that’s actually one of the best ways to run it right now.

Hermes has native support for OpenAI Codex authentication and can even import your existing Codex credentials automatically. citeturn0search10turn0search3

So your setup is probably something like:

```text
Hermes Agent
   ↓
Codex provider
   ↓
GPT/Codex models
```

Which means you already skipped the hardest part.

## What You Should Do Next

Since you already have Codex connected, the next step is making Hermes actually useful in your environment.

For your setup, I’d prioritize:

### 1. Docker Sandboxing

This is probably the MOST important thing.

Run:

```bash
hermes config set terminal.backend docker
```

Hermes can execute commands autonomously. You do not want it operating directly on the host initially. citeturn0search1turn0search3

---

### 2. Gateway Setup (Telegram)

This is where Hermes becomes powerful.

Run:

```bash
hermes gateway setup
```

Then connect:
- Telegram
- Discord
- Slack

Telegram is probably best for your homelab stack.

You’ll basically get:
> AI sysadmin in your pocket.

---

### 3. Give It Controlled Access To Your Stack

For example:

```bash
~/projects/
~/docker/
~/kalshi/
~/scripts/
```

Avoid:
- `/`
- unrestricted sudo
- full NAS access initially

---

### 4. Use Profiles

You can create different Hermes personalities/configs.

Example:
- `trading`
- `homelab`
- `coding`
- `research`

This prevents context pollution.

---

# What Hermes + Codex Is REALLY Good At

For you specifically:

## Kalshi Bot Monitoring

Example:

```text
Check my Kalshi bot logs for unusual market spikes.
```

or:

```text
Summarize today's highest severity alerts.
```

---

## Grafana + Infra

```text
Check if any Docker containers restarted today.
```

```text
Summarize resource usage across my servers.
```

---

## Home Assistant

```text
Find automations that triggered excessively this week.
```

---

## Project Memory

Hermes’ biggest differentiator is persistent memory/skills. citeturn0search1turn0search14

Over time it starts remembering:
- your projects
- workflows
- preferred commands
- directory structures
- debugging patterns

That’s where it separates itself from normal chatbots.

---

# One REALLY Important Recommendation

Since you already use Codex:

## Use Hermes as the orchestrator
## Use Codex as the reasoning engine

That’s honestly the strongest architecture right now.

Hermes handles:
- memory
- tooling
- agents
- automation
- gateways
- scheduling

Codex handles:
- high quality reasoning
- coding
- planning
- debugging

Very strong combo.

---

# Good Next Commands

Try these:

```bash
hermes --tui
```

The TUI is much better than the standard CLI. citeturn0search3

Then inside Hermes:

```text
Analyze this repository structure.
```

```text
Create a monitoring script for my Docker containers.
```

```text
Summarize recent logs from my Kalshi watcher.
```

```text
Build a tmux layout for my trading environment.
```

---

# Your Next Upgrade Path

Your ideal stack is probably:

```text
Hermes
 ├── Codex provider
 ├── Docker backend
 ├── Telegram gateway
 ├── Ollama fallback local models
 ├── Grafana monitoring
 ├── Kalshi bot integration
 └── Home Assistant hooks
```

That’s getting into genuinely advanced personal-agent territory.

**You:** It is on the machine with openclaw and kalshi bot

**ChatGPT:** That’s actually a pretty solid architecture already.

You basically have:

```text
AI / Agent Machine
├── OpenClaw
├── Hermes Agent
├── Kalshi Bot
├── Docker
├── Codex
└── likely tmux/systemd
```

Which is honestly approaching a real autonomous research/trading workstation.

The main thing now is preventing these systems from stepping on each other.

## What I’d Recommend

### Separate Them Logically

Even if they’re on the same physical machine, separate:

```text
/opt/openclaw
/opt/hermes
/opt/kalshi
```

and preferably:

```text
docker compose
```

for each stack independently.

That way:
- Hermes updates don’t break OpenClaw
- Kalshi bot restarts don’t impact agents
- dependencies stay isolated

---

# Biggest Risk In Your Current Setup

If Hermes has unrestricted terminal access on the same machine as:
- trading logic
- API keys
- autonomous agent frameworks
- Docker control

…you can accidentally create a VERY powerful feedback loop.

Not “AI takeover” nonsense.

More like:
- deleting configs
- rewriting scripts
- modifying watchers
- restarting containers
- runaway log generation
- filling storage
- accidentally trading wrong logic

Especially because both OpenClaw and Hermes are designed for long-horizon tool use. citeturn0academia18turn0search5

---

# What I Would Do Immediately

## 1. Dockerize Hermes Execution

Set:

```bash
hermes config set terminal.backend docker
```

This is one of the biggest safety upgrades possible. Hermes officially supports Docker sandbox execution. citeturn0search0turn0search10

---

## 2. Give Hermes READ-FIRST Access

Instead of:
- unrestricted shell
- unrestricted Docker socket

Start with:
- logs
- monitoring
- summaries
- analytics
- alerts

Good examples:

```text
Analyze Kalshi bot logs
```

```text
Summarize market anomalies today
```

```text
Check OpenClaw container health
```

That’s the sweet spot initially.

---

## 3. Keep OpenClaw and Hermes Separate

They overlap conceptually, but they’re good at different things.

### OpenClaw
Better for:
- benchmark-style agent tasks
- tool execution
- autonomous workflows
- experimentation

### Hermes
Better for:
- persistent memory
- orchestration
- messaging gateways
- personal assistant behavior
- long-term context

Together they complement each other pretty well.

---

# Your Machine Is Becoming “Agent Infrastructure”

You’re honestly reaching the point where you should think in layers:

```text
Layer 1 — Infrastructure
Docker
Ubuntu
Networking
Monitoring

Layer 2 — Core Services
Grafana
Databases
MQTT
Storage

Layer 3 — Autonomous Systems
Kalshi Bot
OpenClaw
Hermes

Layer 4 — Interfaces
Telegram
Discord
Dashboard
CLI/TUI
```

Once you think of it like that, the architecture decisions become much clearer.

---

# One VERY Smart Thing You Could Do

Use Hermes as the operator for the rest.

Example:

```text
Hermes
 ├── Reads Grafana alerts
 ├── Monitors Kalshi bot
 ├── Checks Docker health
 ├── Sends Telegram summaries
 └── Escalates anomalies
```

That’s where Hermes shines.

Not raw coding.

Persistent operational awareness.

---

# Another Recommendation

You should probably start using:

- systemd services
- healthchecks
- container restart policies
- persistent logging

for ALL three:
- OpenClaw
- Hermes
- Kalshi bot

The official Hermes Docker setup already uses restart policies and persistent volumes. citeturn0search7turn0search12

---

# What You’re Building Resembles

A lightweight private:
- AI operations center
- autonomous research environment
- homelab agent stack

Which is honestly one of the more interesting directions for homelabs right now.

You’re well past:
> “run ChatGPT locally”

and moving into:
> “persistent AI-assisted infrastructure.”
