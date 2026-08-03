---
title: Homelab
type: moc
---

# Homelab

Physical machines, the hypervisor, storage, and the network they sit on.

## Core notes

- [[Synology NAS]]
- [[Proxmox]]
- [[Hardware Inventory]]
- [[Network Stack]]

## Runbooks in this area

```dataview
LIST
FROM "Notes"
WHERE type = "runbook" AND contains(file.outlinks, this.file.link)
```

## Open questions

- Nothing here is backed up. Fix order: Hermes memory → KalshiWatch DB → this vault.
