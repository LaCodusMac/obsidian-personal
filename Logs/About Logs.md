---
title: About Logs
type: meta
---

Dated entries that repeat — workouts, print runs, sales, incidents. One note per entry, not
one note per subject: the subject already has an article in `Notes/`, and this folder is the
timeline against it.

This folder is currently empty apart from this file. That's expected — nothing has started
being logged yet. It is kept (rather than deleted) because `Home.md`, `Templates/MOC.md`, and
several MOCs query it, and because git does not track empty directories, so an empty `Logs/`
would silently vanish on a fresh clone.

## When to add a log entry instead of editing the article

| | Article in `Notes/` | Entry in `Logs/` |
|---|---|---|
| Answers | "What is true now?" | "What happened on this date?" |
| Count | One, forever | Many, one per event |
| Example | [[Prusa Mini]] — the printer, its setup, known-good profiles | A specific print run: filament, settings, outcome |

If a fact keeps getting overwritten in an article, that's the signal it should be a log
instead — the article should carry the current state, the log carries the history.

## Format

Use `Templates/Log Entry.md`. Filename `YYYY-MM-DD-short-slug.md`. Required frontmatter:

```yaml
---
date: 2026-08-03
type: log
domain: Fitness        # which MOC this belongs to — drives the MOC's activity table
tags: []
---
```

`domain:` is what connects an entry back to its area. `MOCs/Fitness.md` queries
`FROM "Logs" WHERE domain = this.file.name`, so the value must match the MOC's filename
exactly or the entry won't show up anywhere.

Open the body with a link to the subject: `Subject: [[Prusa Mini]]`.

## Candidate domains

Matching the current MOCs: `Fitness`, `3D-Printing`, `Hardware-Sales`, `Content`,
`Homelab`, `Self-Hosted`, `AI-Stack`.
