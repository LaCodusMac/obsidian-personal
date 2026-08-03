---
title: 3D Printing
type: moc
---

# 3D Printing

The printer, the profiles that work, and what's come off it.

## Core notes

- [[Prusa Mini]]

## Known-good profiles

| Material | Nozzle | Bed | Speed | Notes |
|---|---|---|---|---|
| PLA |  |  |  |  |
| PETG |  |  |  |  |

## Print log

```dataview
TABLE file.mtime AS "Printed"
FROM "Logs"
WHERE domain = "3D Printing"
SORT file.mtime DESC
LIMIT 15
```

## Open questions

- 
