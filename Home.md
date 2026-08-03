---
title: Home
type: hub
---

# Home

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

## Inbox — oldest unmined imports

```dataview
TABLE file.mtime AS "Imported"
FROM "Inbox"
SORT file.mtime ASC
LIMIT 10
```

If this list isn't shrinking, the Inbox is a graveyard. Mine or bulk-delete it.

## Open loops

- [ ] **Set up backups** — Hermes memory, KalshiWatch DB, and this vault all live on single machines with no backup job. Start with Hermes.
- [ ] Confirm Hermes memory is scoped per user (no bleed across me / Mom / Nana)
- [ ] Locate Hermes memory on disk so the backup job can target it
- [ ] Workout Tracker storage + commands
- [ ] Self-hosted services not yet documented

---
See [[AI Maintenance Guide]] for the rules an AI assistant follows here, and [[Changelog]] for what it's changed.
