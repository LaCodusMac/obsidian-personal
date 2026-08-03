---
title: Fitness
type: moc
---

# Fitness

Current program, and the log of sessions against it.

## Current program

- Program: 
- Started: 
- Goal: 

## Recent sessions

```dataview
TABLE file.mtime AS "Date"
FROM "Logs"
WHERE domain = "Fitness"
SORT file.mtime DESC
LIMIT 15
```

## Related

- [[Workout Tracker]]
