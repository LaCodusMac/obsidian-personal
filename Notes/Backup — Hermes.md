---
title: "Backup — Hermes"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: critical
host: "Lenovo P3 Mini"
related_projects: ["[[Hermes Agent]]"]
related_areas: ["[[Backups]]"]
---

# Backup — Hermes

**Why it's #1:** the memory is the irreplaceable part of [[Hermes Agent]] — lose it and you have a fresh install, not your agent. Everything here lives on the P3 Mini with no copy.

## What to back up
- Hermes memory store (⚠️ **locate exact path first** — this is the open task on [[Hermes Agent]]).
- Agent config / secrets / connected-model keys.
- Any per-user Telegram config for [[Mom]] / [[Nana]] ([[Family Bots]]).
- Systemd unit files for Hermes.

## Pre-backup hook
- If memory is in **SQLite**: `sqlite3 /path/hermes.db ".backup '/tmp/hermes.db.bak'"` and back up the `.bak` (safe copy of a live DB).
- If it's **flat files / a vector store dir**: no hook needed, just include the dir. If it's a running service holding files open, consider a quick `systemctl stop`/`start` around the copy, or snapshot.

## Fill into the pattern ([[Backups]])
- `<name>` = `hermes`
- `<PATHS>` = memory dir + config dir (+ the `.bak` if SQLite)
- Schedule: daily is fine; consider twice-daily given how often memory changes.

## Restore test
Restore to `/tmp/restore-test-hermes`, point a throwaway Hermes config at it, confirm it recalls recent context.

## Status
- [ ] Locate memory path
- [ ] Init repo on P3 Mini
- [ ] Script + timer
- [ ] First test-restore
- [ ] Off-site leg
