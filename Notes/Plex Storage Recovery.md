---
title: "Plex Storage Recovery"
aliases: [Remount Plex, Plex Libraries Empty, Plex Storage Mount Fix]
type: runbook
tags: [homelab, plex, storage]
host: "NUC10 (per network doc)"
---

Fixes: **Plex libraries look empty or stale after a power outage or reboot**, because the NFS mount to the [[Synology NAS]] didn't come back before [[Plex]]'s Docker container started.

## Symptoms

- Plex shows no movies/TV, or a stale library, after the host or the Synology reboots / loses power.
- `/mnt/media` is unmounted, or mounted but empty.

## Check first

1. Confirm the Synology is powered on.
2. `mountpoint /mnt/media`
3. `findmnt /mnt/media`
4. `ls /mnt/media/movies | head`
5. `ls /mnt/media/tv | head`

Script shortcut — checks the same things, makes no changes:
```bash
/home/ubuntu/check-plex-storage.sh
```
If it shows `/mnt/media` mounted and both directories populated, done. If Plex still looks stale despite that, add `--restart-plex`.

## Fix

With the helper script (preferred):
```bash
cd /home/ubuntu
./recover-plex-storage.sh
```
Enter the sudo password if prompted. It mounts `/mnt/media` if needed, verifies `movies` and `tv` are populated, restarts the Plex container, and shows container status.

Without the script:
```bash
sudo mount -a
ls /mnt/media/movies | head
ls /mnt/media/tv | head
cd /home/ubuntu/plex
docker compose restart plex
```

Open Plex and confirm the libraries are back. **Do not rescan or rebuild libraries before confirming the mount** — wastes time and risks Plex re-indexing against empty folders.

## If that didn't work

- Re-check the Synology is actually reachable on the network, not just powered on.
- Confirm Plex is being managed from `/home/ubuntu/plex` — never `/home/ubuntu`.
- `cd /home/ubuntu/plex && docker compose ps` to check container state directly.

## Root cause (if known)

- The NFS mount to the Synology (`/mnt/media`) doesn't reliably come back on its own after a power outage. Plex's Docker container can start before the mount is ready, so it sees empty local directories instead of the Synology share.

## Good habits

- Manage Plex only from `/home/ubuntu/plex` (`docker compose up -d` / `docker compose ps`). A stale `docker-compose.yml` used to live directly at `/home/ubuntu/` — delete it if it ever reappears so it can't get used by accident.
- After any reboot, assume mount first, Plex second: verify storage before touching Plex.
- If Plex looks empty, don't rescan yet — confirm the mount first.

## Related

- [[Synology NAS]], [[Self-Hosted Software]], [[Self-Hosted]], [[Homelab]]
