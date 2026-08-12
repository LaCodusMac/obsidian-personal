---
title: "NUC10"
aliases: [server, Intel NUC10i5FNK, media server, app host]
type: device
tags: [homelab, hardware, docker]
---

The Intel NUC10i5FNK mini-PC (hostname `server`) that runs [[Plex]] and the rest of the media/monitoring Docker stack. This is the confirmed identity of the machine the [[Network Stack]] doc calls the "main app host" — the doc had the model number wrong (FNH vs. the actual FNK) and undersold what actually runs here.

## Current state

- Hostname: `server` · Model: Intel NUC10i5FNK, physical mini-PC (not a VM)
- CPU: Core i5-10210U @ 1.60GHz, 4 cores / 8 threads
- RAM: 30 GiB (mostly idle — 28 GiB free/cached)
- Swap: 8 GiB swapfile, barely used
- Storage: 233 GB NVMe SSD — EFI (1G) + `/boot` (2G) + LVM root `ubuntu--vg-ubuntu--lv` (100G, 23% used)
- OS: Ubuntu 25.04 "Plucky Puffin," kernel 6.14.0-37-generic
- Firmware: `FNCML357.0052.2021.0409.1144` — dated 2021, ~5 years old
- LAN: `eno1` (wired), `192.168.1.29/24` — primary interface. `wlp0s20f3` (Wi-Fi) present but down/unused.
- Tailscale: `100.121.218.72` (node `nr2zshmdjg`) on the same tailnet as `jacobs-macbook-air` and `llamaswithhats`; `iphone-15-pro-max` is also a tailnet member but was offline at inventory time.
- No hypervisor — bare Ubuntu + Docker (snap-installed), **not Proxmox**. [[Proxmox]] does exist in the lab, on a separate machine (confirmed 2026-08-11) — it's whatever is plugged into USW 24 PoE port 20.

## Mounts (from [[Synology NAS]])

- `/mnt/media` ← `192.168.1.82:/volume1/media` (NFS) — `movies/`, `tv/`, `downloads/`, `EBooks/`, `#recycle`. 3.5T total, 1.8T used.
- `/mnt/ebooks` ← `//192.168.1.82/media/EBooks` (SMB)
- `/mnt/plexmedia`, `/mnt/synology` — legacy/duplicate mount points, currently mostly empty except `plexmedia/movies` and `/tv`. Candidates for cleanup once confirmed unused.
- `/opt/unifi` — UniFi Network Controller compose file + data/logs present, but no container running, and **it shouldn't be**: the real controller lives on the [[UniFi Cloud Key]]. Stale leftover, safe to remove.
- `/Container` (filesystem root) — empty directory, vestige of a prior setup, unused.

## Docker containers

| Container | Image | Port(s) | Role |
|---|---|---|---|
| plex | linuxserver/plex | host networking (32400) | Media server |
| sonarr | linuxserver/sonarr | 8989 | TV automation |
| radarr | linuxserver/radarr | 7878 | Movie automation |
| prowlarr | linuxserver/prowlarr | 9696 | Indexer manager for Sonarr/Radarr |
| qbittorrent | linuxserver/qbittorrent | via gluetun | Torrent client, routed through gluetun |
| gluetun | qmcgaw/gluetun | 8080, 6881 | VPN gateway tunneling qBittorrent |
| calibre-web | linuxserver/calibre-web | 8083 | Ebook library web UI |
| prometheus | prom/prometheus | 9090 | Metrics collection, 30-day retention |
| grafana | grafana/grafana | 3000 | Metrics dashboards |
| node-exporter | prom/node-exporter | 9100 | Host metrics for Prometheus |

One `docker0`/`br-*`/`veth*` bridge per Compose project — normal for a multi-stack Docker host.

## Home directory layout (`/home/ubuntu`)

One folder per app config: `plex/` (compose.yaml + config/movies/tv mounts), `sonarr/`, `radarr/`, `prowlarr/`, `qbittorrent/`, `gluetun/` (gluetun.env), `calibre-web-config/` (DB, logs, Google Drive keys), `prometheus/` (prometheus.yml, alerts.yml, compose.yaml, data/, grafana/), `config/` (holds a `Library` subfolder, likely another app's data dir, unconfirmed), `transcode/` (empty, root-owned Plex scratch dir), `arr-setup.md` (personal notes on the *arr/VPN cutover). Also `check-plex-storage.sh` / `recover-plex-storage.sh` — see [[Plex Storage Recovery]].

## Gotchas

- **`kalshi-demo.pem` sits in `/home/ubuntu`.** File permissions were locked down on 2026-08-08. Still worth noting that it's unrelated to anything running on this host — [[KalshiWatch]] runs on the Lenovo P3 Mini — so it's a stray copy on the wrong machine. Permissions are the immediate risk and that's handled; removing it once you've confirmed the P3 Mini has what it needs would close it out properly.
- Firmware is ~5 years old (2021) — worth checking for a NUC BIOS update.
- Legacy mounts (`/mnt/plexmedia`, `/mnt/synology`) and `/Container` are dead weight; confirm nothing depends on them before removing.
- Don't start the `/opt/unifi` stack. The controller runs on the [[UniFi Cloud Key]]; a second one here would fight it for the same devices.
- Not currently backed up — see [[Backup — Plex]] and [[Backups]].

## Depends on

- [[Synology NAS]] — all media/ebook storage over NFS + SMB
- [[Network Stack]]

## Used by

- [[Self-Hosted Software]] — this host runs nearly the entire confirmed stack

## Log

- 2026-08-08 — Full live inventory captured (hardware, OS, network, mounts, Docker containers). Corrects the [[Network Stack]] doc's "NUC10i5FNH" assumption (actual model FNK) and confirms it as the real Plex/Docker host — but running far more than the doc assumed (full *arr stack + monitoring, not just Plex).
