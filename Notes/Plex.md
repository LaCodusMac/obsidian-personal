---
title: "Plex"
aliases: [Plex Media Server, plex, media server]
type: service
host: "[[NUC10]] (`server`, 192.168.1.29) — Docker"
tags: [homelab, media, selfhosted, docker]
---

The media server — a Docker container on [[NUC10]] serving movies and TV read over NFS from [[Synology NAS]]. It is the most-linked service in this vault and, until 2026-08-11, the only one with no article: `[[Plex]]` resolved to an empty stray file at the vault root.

## Current state

- Host: [[NUC10]] (`server`, `192.168.1.29`), Docker, **host networking**, port **32400**
- Config: `plex/` on NUC10 — `compose.yaml` plus config/movies/tv mounts
- Media source: `/mnt/media` on NUC10, an **NFS** mount of `192.168.1.82:/volume1/media` from [[Synology NAS]] (`movies/`, `tv/`, `downloads/`)
- `transcode/` — empty, root-owned Plex scratch directory on NUC10
- Helper scripts on the host: `check-plex-storage.sh` and `recover-plex-storage.sh` — see [[Plex Storage Recovery]]
- Not backed up. See [[Backup — Plex]]
- ⚠️ Unrecorded: Plex Pass status, remote access configuration, claim token / server name, transcoding settings (hardware vs. software), which clients are in regular use

## Depends on

- [[NUC10]] — the container host
- [[Synology NAS]] — all media lives there, not on the NUC
- [[Network Stack]] — the NFS path between the two

## Gotchas

- **An empty library usually means the mount, not Plex.** If content disappears, check that `/mnt/media` is still mounted before touching anything in Plex itself. This has happened and there is a runbook for it: [[Plex Storage Recovery]].
- Host networking means port 32400 is bound directly on `server` — no Docker port mapping to inspect, and no isolation from the host's network stack.
- The library database is on NUC10, the media is on the NAS. **Losing the NUC loses watch history, metadata, and collections even though every file survives** — that asymmetry is what [[Backup — Plex]] exists to address, and it isn't done.

## Related

- [[NUC10]] · [[Synology NAS]] · [[Self-Hosted Software]] · [[Plex Storage Recovery]] · [[Backup — Plex]] · [[Home Lab]]

## Log

- 2026-08-11 — Note created by filling in the 0-byte `Plex.md` that had been sitting at the vault root since earlier that day. That file was capturing every `[[Plex]]` link in the vault — from `MOCs/Self-Hosted`, [[Synology NAS]], [[NUC10]] and others — and resolving them to nothing. Moved to `Notes/` per [[VAULT]] §2 and written from the detail already recorded in those notes. No new facts asserted.
