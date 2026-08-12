---
title: "Tailscale"
aliases: [tailnet, MagicDNS, the VPN, WireGuard mesh]
type: service
tags: [homelab, networking, vpn, remote-access]
---

The WireGuard-based mesh VPN that lets every machine reach every other machine by name regardless of which network it's physically on. This is how the lab is reached from outside the house, and it is why no service here needs a port forwarded.

## Current state

- Confirmed tailnet members: `server` ([[NUC10]], `100.121.218.72`, node `nr2zshmdjg`), `jacobs-macbook-air`, `llamaswithhats` (the Lenovo P3 Mini running [[Hermes Agent]] and [[KalshiWatch]]), and `iphone-15-pro-max` (offline at inventory time)
- MagicDNS: enabled — machines are addressable by hostname, no IP memorisation
- **Confirmed NOT on the tailnet** (Mac, 2026-08-11): [[Synology NAS]], [[UniFi Cloud Key]], `Pi-hole-1`, the [[Proxmox]] host, and the [[Home Assistant]] VM. The tailnet is currently four general-purpose computers and a phone — no infrastructure or appliances.
- ⚠️ Unrecorded: ACL policy (default allow-all vs. scoped), whether any node is an exit node, whether any node advertises subnet routes, and key-expiry settings per node

## Depends on

- Tailscale's coordination server (the one genuinely external dependency in the lab — if it's unreachable, existing connections persist but new ones can't be established)
- [[Network Stack]] for outbound connectivity

## Used by

- Remote access to [[NUC10]] and everything in its Docker stack
- Reaching [[Hermes Agent]] and [[KalshiWatch]] on the P3 Mini from the MacBook
- The Obsidian vault sync path between the P3 Mini and `jacobs-macbook-air` — though that sync runs over **git via SSH to GitHub**, not directly over the tailnet. See [[Obsidian Brain]]

## Gotchas

- **Key expiry will bite eventually.** Nodes have expiring keys by default; a machine that drops off the tailnet months from now, for no apparent reason, is almost always this. Disabling expiry on always-on infrastructure nodes is the usual fix and is worth deciding deliberately rather than discovering.
- **A flat tailnet is a flat trust domain.** If the default ACL is allow-all, any node on the tailnet can reach any other — including the family-facing machines. Worth checking against the [[Family Bots]] exposure question.
- MagicDNS names and [[Pi-hole]] both answer DNS, for different scopes. If a name resolves unexpectedly, establish which resolver answered before debugging further.

## Expanding the tailnet — the decision, 2026-08-11

The question was whether to put [[Synology NAS]], `Pi-hole-1`, the [[UniFi Cloud Key]] and the [[Proxmox]] host on the tailnet. The framing that matters is **not** "which devices deserve access" but **"native client or subnet router,"** because those have different failure modes.

**Option A — native Tailscale client on each device.** Every node gets its own tailnet IP, MagicDNS name, and ACL identity. Precise, survives a single node dying, works from anywhere.

**Option B — one subnet router.** Install Tailscale on one always-on machine, `--advertise-routes=192.168.1.0/24`, approve it in the admin console. Every device on the LAN becomes reachable from the tailnet without touching any of them. One install, done. Trade-offs: that node becomes a single point of failure for all remote access, subnet-routed devices get no MagicDNS names (raw IPs only) and no per-device ACL identity.

The usual answer is **both, split by whether you can safely install on the device**:

| Device | Call | Why |
|---|---|---|
| [[Proxmox]] host | **Native client — do this first** | It's plain Debian; installs cleanly. Highest value on the list: hypervisor console access from anywhere means you can rescue [[Home Assistant]] or any other guest without being home. Right now, a hung VM means the automation is down until you physically return. |
| [[Synology NAS]] | **Native client — yes** | Official Synology package. Real payoff: it becomes a restic target reachable off-LAN, and it lets you stop using QuickConnect, which is a worse remote-access posture than a WireGuard mesh. This matters more given the relocation — if machines end up temporarily split across two locations, an off-LAN-reachable backup target is the difference between backups continuing and backups quietly stopping. |
| [[UniFi Cloud Key]] | **No — use the subnet router** | Locked-down appliance firmware; installing Tailscale on it is unsupported and gets wiped by controller updates. Reach it through a subnet route instead. A network controller is also precisely the thing you want behind one extra deliberate step. |
| `Pi-hole-1` | **Yes, but see the trap below** | Cheap to add. The trap is what you do *with* it afterwards. |

### The Pi-hole trap

The obvious next move after putting Pi-hole on the tailnet is to set it as the tailnet's global nameserver, so your phone gets ad-blocking everywhere. That's the standard recipe and it is worth thinking twice about here.

`Pi-hole-1` is already the LAN's single resolver with no redundancy — a known and accepted risk, because its blast radius is "devices at home." Making it the tailnet nameserver converts a **LAN-scope** single point of failure into a **global** one: the Pi reboots, and your phone loses DNS in a coffee shop three states away. You'd be widening the blast radius of the one component you've already flagged as the lab's most exposed dependency.

If you want it anyway, build `Pi-hole-2` first — the spare hardware is already on hand — and point Tailscale at both. Order matters more than the individual steps.

Second, smaller trap: Pi-hole only answers on interfaces it's configured to listen on, so it will ignore tailnet queries until told otherwise. The lazy fix in the UI is "Permit all origins," which also makes it an open resolver if the LAN side is ever exposed. Bind it to the `tailscale0` interface specifically instead.

### Cost

Zero. Tailscale's free tier covers 100 devices and 3 users; this adds four. No budget consideration either way — the entire cost of this decision is the failure modes above, not money.

### Suggested order

1. [[Proxmox]] host — native client. Biggest win, no downside.
2. [[Synology NAS]] — native client via the Package Center.
3. Subnet router on [[NUC10]] (always-on, already a tailnet member) for the Cloud Key and anything else you won't install on.
4. Scope ACLs *before* the node count grows — see below.
5. `Pi-hole-1` last, and do **not** make it the tailnet nameserver until `Pi-hole-2` exists.

## Open decisions

- Whether to scope ACLs rather than leave the tailnet flat. Currently the tailnet is all general-purpose computers, so a flat allow-all is defensible. The moment infrastructure and the family-facing [[Family Bots]] machine share a flat tailnet, it stops being defensible — do this before step 3 above, not after.
- Whether any node should be an exit node

## Log

- 2026-08-11 — Mac confirmed the NAS, Cloud Key, Pi-hole, and Proxmox host are **not** on the tailnet, and asked whether they should be. Recorded the native-client vs. subnet-router split and the Pi-hole-as-tailnet-nameserver trap. Nothing acted on yet — this is a decision record, not a state record.
- 2026-08-11 — Note created to resolve the broken `[[Tailscale]]` link in `MOCs/Self-Hosted`. Membership list drawn from the 2026-08-08 [[NUC10]] inventory; everything not in that inventory is marked unverified rather than assumed.
