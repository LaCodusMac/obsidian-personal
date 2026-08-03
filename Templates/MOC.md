---
title: 
type: moc
---

# TITLE

What this area covers, in one sentence.

## Core notes

- [[ ]]

## Runbooks in this area

```dataview
LIST
FROM "Notes"
WHERE type = "runbook" AND contains(file.outlinks, this.file.link)
```

## Recent activity

```dataview
TABLE file.mtime AS "Edited"
FROM "Logs"
WHERE domain = this.file.name
SORT file.mtime DESC
LIMIT 10
```

## Open questions

- 
