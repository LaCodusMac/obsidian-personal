---
title: "Proxmox"
aliases: [PVE, Proxmox VE, the hypervisor]
type: service
status: active
host: "Intel NUC8i7BEH — 192.168.1.10"
tags: [homelab, virtualization]
---

The lab's hypervisor, running on the **Intel NUC8i7BEH at `192.168.1.10`**. It hosts the [[Home Assistant]] VM. Three vault notes previously stated no Proxmox host existed anywhere in the lab; that was wrong, and the reason it went unnoticed is instructive — the hypervisor was only ever visible through its guest.

## Current state

- **Host: Intel NUC8i7BEH, `192.168.1.10`** (confirmed 2026-08-11). This is the machine [[Hardware Inventory]] listed for months as "secondary utility / lab node" with nothing recorded against it
- Physical path: **USW 24 PoE, port 20** — shared with its bridged guests
- Confirmed guest: [[Home Assistant]] (HAOS VM, `192.168.1.169`)
- Web UI: `https://192.168.1.10:8006`
- ⚠️ **Hostname reported by UniFi is `DESKTOP-G3JQ8MO`** — that is a Windows-generated name, and Proxmox is Debian. Almost certainly a **stale DHCP lease** from when this NUC ran Windows, not the machine's actual hostname. Confirm with `hostname -f` on the box before writing it anywhere as fact; if it *is* the real hostname, it's worth changing to something meaningful
- **Addressing: DHCP reservation ("Fixed IP") set in UniFi**, not a static configured on the host itself (confirmed 2026-08-11). Consistent with how the rest of the lab is addressed — see the gotcha below for the one case where it matters
- ⚠️ Unrecorded: Proxmox version, storage layout, other VMs/containers, whether `vzdump` runs at all

## Remaining discovery

```bash
ssh root@192.168.1.10
pveversion            # version
qm list               # VMs — is homeassistant the only one?
pct list              # LXC containers
hostname -f           # settles the DESKTOP-G3JQ8MO question
cat /etc/network/interfaces   # confirm static vs. DHCP
```

## Why the vault got this wrong

Worth recording, because the failure mode will recur. Three notes — [[NUC10]], [[Synology NAS]], [[Network Stack]] — each correctly reported "no Proxmox **here**," and that got aggregated into "no Proxmox **anywhere**." Absence of evidence on the machines that were inventoried was read as evidence of absence across machines that were not. The NUC8 was never checked; it has no hostname, no IP, and no recorded services in [[Hardware Inventory]] to this day.

The general lesson: an inventory's coverage and its conclusions are different things. Notes that say "not found on X" should not be summarised as "does not exist."

## Gotchas

- **The gateway is a boot dependency for the hypervisor.** Because `192.168.1.10` comes from a UniFi reservation rather than a static on the host, this machine needs DHCP to be answering before it has an address. Almost always fine. The two cases where it isn't: a **cold boot after a power cut**, where the NUC may come up before the gateway is serving DHCP, and a **gateway restore or replacement**, where reservations can be lost (the corpus already has `2026-02-23-unifi-cloud-key-restore`). A statically-configured host doesn't care about either.

  Not worth changing remotely — editing `/etc/network/interfaces` on a headless Proxmox box is how people lock themselves out, and it needs a keyboard and monitor to undo. If you're ever physically at the NUC anyway, setting the static there *and* keeping the UniFi reservation is the belt-and-braces version: the host boots independently, and UniFi still documents the address and prevents collisions.
- **Addressing convention: infrastructure below the pool.** The DHCP pool is **`.100`–`.200`**, and the infrastructure sits deliberately beneath it — `.10` (this host), `.18` ([[Pi-hole]]), `.29` ([[NUC10]]), `.82` ([[Synology NAS]]). That's the right pattern: a lost reservation on any of these can't cause a collision, because the DHCP server never hands out addresses below `.100`. Worst case the machine moves, it doesn't conflict.

  **[[Home Assistant]] at `.169` is the one exception** — that address is *inside* the pool, so a lost reservation there means another device can take `.169` while HA moves elsewhere. Worth renumbering it below `.100` (`.11`, next to its hypervisor, would be tidy) to match the convention. Cheapest to do **now**, before the planned Hermes → Home Assistant integration starts referencing it by address.
- **Guests hide their host.** A bridged VM appears on the LAN as an ordinary client with an ordinary IP. Nothing about `homeassistant` at `192.168.1.169` announces that a hypervisor is underneath it — which is exactly how this went unrecorded.
- Whatever machine this is, it is running the house's automation and is currently **outside all monitoring and all backup coverage**. See [[Backups]].

## Open

- [x] Identify the host machine — **NUC8i7BEH at `192.168.1.10`**, confirmed 2026-08-11
- [x] Confirm static vs. reservation — **UniFi DHCP reservation**, confirmed 2026-08-11
- [ ] Resolve the `DESKTOP-G3JQ8MO` hostname question (`hostname -f`)
- [ ] Give the NUC8 its own device note with specs, once `pveversion` / storage layout are known
- [ ] Enumerate all VMs/LXCs — `homeassistant` may not be the only guest
- [ ] Confirm whether `vzdump` is configured, and to where. Nothing currently backs this host up
- [ ] Add to [[Tailscale]] — highest-value node on the list, see that note

## Related

- [[Home Assistant]] · [[Home Lab]] · [[Hardware Inventory]] · [[Network Stack]] · [[Backups]] · [[Tailscale]]

## Log

- 2026-08-11 — **Host confirmed: NUC8i7BEH at `192.168.1.10`** (Mac). Closes a gap that had been open in [[Hardware Inventory]] since the vault was built — the NUC8 had no hostname, IP, or recorded service. Flagged the `DESKTOP-G3JQ8MO` hostname as probably a stale Windows-era DHCP lease rather than the real one.
- 2026-08-11 — **Existence confirmed**, host still open at the time. Note had been created earlier the same day stating no Proxmox host was confirmed anywhere; Mac corrected this with a UniFi screenshot of the [[Home Assistant]] VM.
