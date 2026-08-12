---
title: "Self-Hosted Software"
aliases: [Self-Hosted Services]
type: resource
tags: [resource, homelab, software, selfhosted]
---

Everything I have running on the [[Home Lab]] — from Pi-hole to Plex. Confirmed items first, doc-suggested items flagged.

## Confirmed running — on [[NUC10]], via Docker
- **[[Plex]]** — media server (host networking, port 32400).
- **Sonarr** (8989) / **Radarr** (7878) / **Prowlarr** (9696) — TV/movie automation + indexer management.
- **qBittorrent** (via gluetun) — torrent client. **Correction to the doc:** this is a container on [[NUC10]] itself, not a separate "torrent laptop."
- **gluetun** (8080, 6881) — VPN gateway tunneling qBittorrent's traffic.
- **calibre-web** (8083) — ebook library UI, reading `/mnt/ebooks` from [[Synology NAS]].
- **Prometheus** (9090) + **Grafana** (3000) + **node-exporter** (9100) — lab monitoring stack. This Grafana is a *separate instance* from `kalshi-grafana.service` below — don't conflate the two.

## Confirmed running — elsewhere
- **[[Hermes Agent]] + [[KalshiWatch]]** — Telegram agent and trading/monitoring stack, on the **Lenovo P3 Mini** (systemd services; see [[KalshiWatch]] for the unit list), including its own `kalshi-grafana.service` dashboard.
- **[[Pi-hole]]** — DNS filtering, on `Pi-hole-1`, one of the three [[Raspberry Pi 5]] boards. Single resolver, so it's a LAN-wide single point of failure.
- **UniFi Network Controller** — on the [[UniFi Cloud Key]] appliance. The `/opt/unifi` compose file on [[NUC10]] is a stale leftover; don't start it.
- **[[Home Assistant]]** — home automation, a VM at `192.168.1.169` under [[Proxmox]]. Confirmed 2026-08-11. The Proxmox host itself is on **USW 24 PoE port 20** but has not yet been identified as a specific machine.

## Still unconfirmed
- Reverse proxy (Nginx Proxy Manager / Traefik / Caddy)? Vaultwarden? Nextcloud? Watchtower? Nothing confirmed either way — add here as you remember.
- **Other [[Proxmox]] guests** — `homeassistant` is the only VM confirmed so far, but nobody has run `qm list`. There may be more.

## To capture per service
Host it runs on · container vs bare · port · config/data location · backup status · depends-on. NUC10 services above now have host + port; config/data location and backup status are still open — see [[NUC10]] for the folder layout.

## Related
- Area: [[Home Lab]]
- Projects: [[Hermes Agent]], [[KalshiWatch]]
- Resources: [[Hardware Inventory]], [[Network Stack]], [[NUC10]]
