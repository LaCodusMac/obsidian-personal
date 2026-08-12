---
title: Home
type: hub
---

Dashboard. Everything branches from here.

## Areas

```dataview
LIST
FROM "MOCs"
SORT file.name ASC
```

## Recently touched

```dataview
TABLE file.mtime AS "Edited", type
FROM "Notes" OR "Logs" OR "MOCs" OR "People"
SORT file.mtime DESC
LIMIT 15
```

## Stale — no edit in 90+ days

```dataview
TABLE file.mtime AS "Last edited", type
FROM "Notes"
WHERE file.mtime < date(today) - dur(90 days)
SORT file.mtime ASC
LIMIT 20
```

## Orphans — nothing links in or out

```dataview
LIST
FROM "Notes"
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
SORT file.name ASC
```

## Library — conversation corpus

584 conversations, 2023–2026. Permanent and searchable; see
[[About the Library]] and [[Conversation Index]].

```dataview
TABLE length(rows) AS "Conversations"
FROM "Library"
WHERE category
GROUP BY category
SORT length(rows) DESC
```

Unfiled — no category set, needs classifying:

```dataview
LIST
FROM "Library"
WHERE !category AND type != "meta"
SORT file.name ASC
```

## Open loops

- [ ] **Set up backups** — Hermes memory, KalshiWatch DB, and this vault all live on single machines with no backup job. Start with Hermes.
- [ ] Confirm Hermes memory is scoped per user (no bleed across me / Mom / Nana)
- [ ] Locate Hermes memory on disk so the backup job can target it
- [ ] Self-hosted services not yet documented

---
See [[AI Maintenance Guide]] for the rules an AI assistant follows here, and [[Changelog]] for what it's changed.
