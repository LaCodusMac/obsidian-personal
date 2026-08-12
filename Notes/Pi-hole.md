---
title: "Pi-hole"
aliases: [Pihole, PiHole, DNS filtering, Pi-hole-1, the resolver]
type: service
host: "Pi-hole-1 (Raspberry Pi 5) — 192.168.1.18"
tags: [homelab, dns, selfhosted, networking]
---

The LAN's DNS resolver and ad/tracker filter, running on `Pi-hole-1` at static **`192.168.1.18`** — one of the three [[Raspberry Pi 5]] boards. It is the **only** resolver on the network, which makes it the lab's most exposed single point of failure.

## Current state

- Host: `Pi-hole-1`, a CanaKit [[Raspberry Pi 5]], static `192.168.1.18`
- Confirmed **Pi-hole**, not AdGuard Home — this was checked on 2026-08-08
- Clients reach it via DNS handed out by the [[UniFi Cloud Key]] gateway (⚠️ unverified — confirm whether DHCP option 6 points here, or whether clients are set manually)
- **Install method: bare-metal `pihole` package**, not a container (confirmed 2026-08-11). Config lives directly on the Pi's filesystem — see [[Backup — Pi-hole]]
- **Admin UI: `https://192.168.1.18/admin/login`** — HTTPS on the standard port, no `:8080` or `:81`
- **Not on the tailnet** — LAN-only, deliberately, as of 2026-08-11. See [[Tailscale]]
- Custom DNS entries / local DNS records: ⚠️ unrecorded
- Not backed up. See [[Backup — Pi-hole]]

## Adlists

Two, both in the `Default` group (confirmed 2026-08-11):

| List | URL | Notes |
|---|---|---|
| StevenBlack unified hosts | `https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts` | The standard baseline — adware + malware. Carries the comment *"Migrated from `/etc/pihole/adlists.list`"* |
| HaGeZi DNS blocklists (multi) | `https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/multi.txt` | Substantially more aggressive than StevenBlack, and overlaps it heavily |

Two lists is a sensible number — more lists mostly adds overlap and false positives rather than coverage.

**The "Migrated from `/etc/pihole/adlists.list`" comment is a dating clue.** Pi-hole moved adlists out of that flat file and into the gravity database in **v5**; the comment is what the migration writes. So this install has been **upgraded in place from a v4-era Pi-hole**, not built fresh. Practical consequence: the thing worth backing up is `gravity.db`, and an in-place-upgraded install may carry leftover config that a fresh one wouldn't.

⚠️ **Aggressive lists cause hard-to-diagnose breakage.** HaGeZi's larger tiers are known for it, and the corpus (see [[About the Library]]) already contains a conversation about Pi-hole blocking a UFC stream (`2026-04-05-pi-hole-blocking-ufc-stream`) — that is this list, most likely. When something breaks in a way that looks like a network problem, disable blocking for 30 seconds (`pihole disable 30s`) before debugging anything else. It costs nothing and rules out the most likely cause first.

## Depends on

- [[Raspberry Pi 5]] — the physical host
- [[Network Stack]] — for the static lease and DHCP DNS advertisement

## Used by

- Every device on the LAN, by virtue of being the resolver. See [[Self-Hosted Software]]

## Gotchas

- **Single resolver.** If `Pi-hole-1` is down, unplugged, or mid-upgrade, name resolution stops LAN-wide. `Pi-hole-2` on a spare Pi is planned and the hardware is already on hand — it is not built.
- **Not backed up.** Rebuilding adlists and custom DNS by hand is tedious and easy to get subtly wrong. `pihole -a -t` produces a Teleporter archive; see [[Backup — Pi-hole]] for the pattern.
- SD-card wear is the classic Pi failure mode. Worth confirming whether this board boots from SD or NVMe, because it changes how likely a silent failure is.
- A resolver that half-works is worse than one that's down — if DNS gets slow or intermittent rather than dead, check here before blaming the ISP or the gateway.

## Version — worth confirming, it changes the backup paths

⚠️ **Probably Pi-hole v6, ~70% confidence.** The inference is from the admin URL alone: `https://192.168.1.18/admin/login` is the v6 pattern — v6 replaced lighttpd with a built-in web server and serves a `/admin/login` route over HTTPS on the standard port. Pi-hole v5 used lighttpd and landed on `/admin/index.php`, typically over plain HTTP. That's suggestive, not conclusive — a v5 install behind a manually-configured HTTPS vhost could look similar.

The adlist migration comment above doesn't settle it either way — it dates the install as *at least* v5, which is consistent with both. It does tell us this is a long-lived upgraded install, which is a reason to check rather than assume.

It matters because v6 moved the configuration:

| | v5 | v6 |
|---|---|---|
| Main config | `/etc/pihole/setupVars.conf` | `/etc/pihole/pihole.toml` |
| dnsmasq config | `/etc/dnsmasq.d/` | managed internally; `/etc/dnsmasq.d/` no longer the source of truth |
| Teleporter (CLI) | `pihole -a -t` | `pihole-FTL --teleporter` |

[[Backup — Pi-hole]] currently specifies the **v5** paths and the v5 teleporter command. If this is v6, that runbook backs up the wrong things and its export command may not exist.

One command settles it:

```bash
pihole -v
```

## Second resolver — open decisions

Building `Pi-hole-2` needs two calls made, neither of which is settled:

1. **How clients find both.** Two DNS servers handed out by DHCP from the UniFi gateway, or a shared virtual IP with keepalived. The DHCP route is simpler; the VIP route fails over faster.
2. **How the two stay in sync.** `gravity-sync` or equivalent, so adlists and custom DNS don't silently diverge. Two resolvers that disagree is a harder problem to debug than one resolver that's down.

## Log

- 2026-08-11 — Mac confirmed **bare-metal package install** (not a container) and the admin URL `https://192.168.1.18/admin/login`. Flagged the likely-v6 question that URL raises, because it puts [[Backup — Pi-hole]]'s paths in doubt. Also recorded as deliberately not on the tailnet.
- 2026-08-11 — Note created. Resolves the `[[Pi-hole]]` links that had been sitting broken in [[Self-Hosted Software]], [[Hardware Inventory]], [[Raspberry Pi 5]], and `MOCs/Self-Hosted`. Content consolidated from those notes; no new facts asserted beyond what they already recorded.
- 2026-08-08 — Confirmed running on `Pi-hole-1`, not on NUC8 or NUC10 as the [[Network Stack]] doc had assumed.
