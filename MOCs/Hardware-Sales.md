---
title: Hardware Sales
type: moc
---

# Hardware Sales

Buying used, reselling, and what I paid vs. what it went for.

## Active listings

Keep this as a table until it stops being enough. Promote a row to its own note
only when an item has real history worth tracking.

| Item | Source | Paid | Asking | Status | Listed |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Sold

```dataview
TABLE file.mtime AS "Logged"
FROM "Logs"
WHERE domain = "Hardware Sales"
SORT file.mtime DESC
LIMIT 15
```

## Related

- [[Hardware Inventory]]
