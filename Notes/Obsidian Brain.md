---
title: "Obsidian Brain"
type: project
status: active
priority: medium
started: 2026-07-28
updated: 2026-07-28
tags: [project, meta, obsidian, pkm]
related_projects: ["[[Hermes Agent]]"]
related_people: []
related_areas: ["[[Home Lab]]"]
related_resources: []
---

# Obsidian Brain

## Summary
This vault itself — my personal wiki tying every project, person, and system together, maintained jointly by me and an AI assistant. This note documents *what the brain is made of* so the system that runs it is itself in the wiki.

## What makes it up
- **Structure**: PARA-ish folders — `01-Projects`, `02-People`, `03-Areas`, `04-Resources`, `05-Archive`, plus `Templates/` and `_AI/`.
- **Hub**: [[Home]] — a Dataview dashboard (active projects, recent edits, stale-project warnings).
- **Templates**: `Project Template`, `Person Template` — consistent frontmatter for linking.
- **AI layer**: [[AI Maintenance Guide]] (rules the AI follows) + [[Changelog]] (audit log of AI edits).
- **Linking model**: every note carries `related_projects` / `related_people` / `related_areas` / `related_resources` frontmatter **and** inline `[[wikilinks]]`, so the graph stays connected and nothing is orphaned.

## Plugins it relies on
- **Dataview** — the live tables on [[Home]].
- **Templater** (optional) — one-click new notes from templates.

## How it's AI-controlled
An AI with file access (Claude Desktop / Cowork / Claude Code pointed at the folder) reads [[AI Maintenance Guide]] first, then edits the markdown directly and logs to [[Changelog]]. Fully plain-text, so it stays human-readable and auditable.

## Open Questions
- Do I want a scheduled AI "gardener" pass (e.g. weekly) that updates [[Home]], flags stale notes, and proposes new links?
- Should the vault live on the [[Home Lab]] with versioned backups (git repo on the NAS)?

## Related
- Related: [[Home]], [[AI Maintenance Guide]], [[Changelog]]
- Areas: [[Home Lab]]

## Log
- 2026-07-28: Vault scaffolded and this meta-note created.
