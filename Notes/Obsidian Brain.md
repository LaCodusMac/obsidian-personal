---
title: "Obsidian Brain"
aliases: [The Brain]
type: project
status: active
priority: medium
started: 2026-07-28
tags: [project, meta, obsidian, pkm]
---

This vault itself — a personal wiki plus a permanent AI-conversation corpus, maintained
jointly by me and an AI assistant. This note documents what the brain is made of, so the
system that runs it is itself in the wiki.

## Current state

Two layers, deliberately different in kind:

- **Articles** — `Notes/`, `People/`, `MOCs/`, `Logs/`. Curated, authoritative, state what
  is true now. Flat namespaces; classification lives in frontmatter.
- **Library** — 584 verbatim AI conversation transcripts, 2023–2026. Append-only, never
  edited, never cited as fact. Exists so no single provider holds the only copy of my
  context. See [[About the Library]].

Governed by [[VAULT]], the canonical spec. [[CLAUDE]] is the agent entry point, loaded
automatically by Claude Code and Cowork sessions. [[Changelog]] is the audit log.

## Components

- **Spec**: [[VAULT]] — structure, frontmatter, conventions, imports, sensitive handling
- **Dashboard**: [[Home]] — stale notes, orphans, corpus breakdown
- **Templates**: `Templates/` — Entity, Runbook, MOC, Person, Project, Log Entry
- **AI layer**: [[CLAUDE]] + [[AI Maintenance Guide]] + [[Changelog]]
- **Tooling**: `_AI/regenerate_index.py` — rebuilds Library indexes, checks that every
  sensitive transcript is actually excluded from git
- **Linking model**: inline `[[wikilinks]]` only. `related_*` frontmatter is banned — the
  same relationship recorded twice drifts, and a drifting query fails silently.

## How it's AI-controlled

Plain markdown, so any agent with file access can read and edit directly — Claude Code or
Cowork pointed at the folder. It reads [[CLAUDE]] automatically, follows [[VAULT]], and logs
what it changed to [[Changelog]]. Fully auditable in git.

[[Hermes Agent]] is the separate always-on agent stack; it doesn't currently touch this
vault, though pointing it at the Library for retrieval is an open question below.

## Gotchas

- **No query engine installed.** [[Home]] is raw query blocks until Dataview is added or
  Bases is wired up. Undecided — see `README.md`.
- Sensitive transcripts rely on a `.private.md` filename suffix to stay out of git. The
  suffix is the whole mechanism; a sensitive file without it looks normal and gets committed.

## Open questions

- A scheduled "gardener" pass — weekly, flags stale notes and proposes links?
- Should [[Hermes Agent]] query the Library directly, making the corpus live memory rather
  than something I search by hand?
- Versioned backups on the [[Home Lab]] — see [[Backup — Obsidian Vault]]. Obsidian Sync and
  the GitHub remote are replication, not backup; a bad edit propagates to both.

## Related

- Areas: [[Home Lab]]
- Projects: [[Hermes Agent]]

## Log

- 2026-08-03 — Rewritten. Previously described the vault as PARA (`01-Projects/` etc.) with
  the `related_*` linking model; both were superseded in the 2026-07-31 restructure and
  formally retired 2026-08-03.
- 2026-07-28 — Vault scaffolded and this meta-note created.
