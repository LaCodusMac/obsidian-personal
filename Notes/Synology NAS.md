---
title: Synology NAS
aliases: [NAS, Synology, DS920+, the NAS]
type: device
tags: [homelab, storage]
---

Bulk storage for the homelab — media for [[Plex]], backup target, and SHR array.
This is the worked example of the note conventions; copy the shape, not the content.

Note the `aliases:` above. That is the redirect mechanism, and it is the single
habit that prevents duplicate notes. When you type `[[NAS` the autocomplete lands
here instead of tempting you into a second article.

## Current state

- IP: `192.168.1.82`
- Model: 
- Volume: SHR — 3.5T total, 1.8T used (`volume1/media`)
- Drives: 
- `volume1/media` exported over **NFS** to [[NUC10]] at `/mnt/media` (movies/, tv/, downloads/, EBooks/, `#recycle`) — not to [[Proxmox]]. (Corrected 2026-08-11: this line used to add "no Proxmox host has been confirmed anywhere in the lab yet," which was wrong. Proxmox exists and hosts [[Home Assistant]]; the NFS export still goes to NUC10 directly, which is the part that mattered here.)
- `media/EBooks` also exported over **SMB** to [[NUC10]] at `/mnt/ebooks`, for calibre-web.

## Depends on

- [[Network Stack]]

## Used by

- [[Plex]] and the rest of the [[NUC10]] Docker stack (media + ebooks)

## Gotchas

- SHR went degraded once — see the runbook before touching a drive.
- If Plex loses its library, check the NFS mount before blaming Plex — see [[Plex Storage Recovery]].

## Log

- 2026-04-19 — SHR reported degraded.
