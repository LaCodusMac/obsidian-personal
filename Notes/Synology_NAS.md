---
title: Synology NAS
aliases: [NAS, Synology, DS920+, the NAS]
type: device
tags: [homelab, storage]
---

# Synology NAS

Bulk storage for the homelab — media for [[Plex]], backup target, and SHR array.
This is the worked example of the note conventions; copy the shape, not the content.

Note the `aliases:` above. That is the redirect mechanism, and it is the single
habit that prevents duplicate notes. When you type `[[NAS` the autocomplete lands
here instead of tempting you into a second article.

## Current state

- Model: 
- Volume: SHR, ~ TB usable
- Drives: 
- Shares exported over NFS to [[Proxmox]]

## Depends on

- [[Network Stack]]

## Used by

- [[Plex]]

## Gotchas

- SHR went degraded once — see the runbook before touching a drive.
- If Plex loses its library, check the NFS mount before blaming Plex.

## Log

- 2026-04-19 — SHR reported degraded.
