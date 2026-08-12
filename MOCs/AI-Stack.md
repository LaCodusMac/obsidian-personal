---
title: AI Stack
type: moc
---

Local models, agents, and the context I hand to any AI so it knows my setup.

## Core notes

- [[Hermes Agent]]
- [[Family Bots]]
- [[Portable Context Pack]]

## Runbooks in this area

```dataview
LIST
FROM "Notes"
WHERE type = "runbook" AND contains(file.outlinks, this.file.link)
```

## Open questions

- Is Hermes memory scoped per user? No bleed across me / Mom / Nana.
- Where does Hermes memory live on disk? Backup job needs the path.
