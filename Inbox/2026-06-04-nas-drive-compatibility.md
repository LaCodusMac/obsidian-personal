---
date: 2026-06-04
source: chatgpt
title: "NAS Drive Compatibility"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000ed7c71fd99ba8ce49c11358a", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 233835, "width": 709}
Can I use these in a NAS

**ChatGPT:** Yes, most likely. From the photo I can identify:

- 2 × 2 TB Dell EMC SATA drives
- 1 × 2 TB Dell-branded SATA drive
- 1 × 2 TB Seagate Barracuda
- 1 × 4 TB Seagate Barracuda
- 1 × 3 TB Seagate Desktop HDD
- 1 × 3 TB Seagate Barracuda

Total raw capacity: about **18 TB**.

A few things to consider:

### Good news
All of these appear to be standard 3.5" SATA hard drives, so they should physically work in:
- Your Synology NAS (if you have free bays)
- A repurposed Dell/HP/Lenovo NAS build
- Unraid
- TrueNAS
- OpenMediaVault

### Potential issues
1. **Mixed sizes**
   - 2 TB, 3 TB, and 4 TB drives don't make the most efficient RAID set.
   - Traditional RAID uses the smallest drive size across all disks.

2. **Enterprise vs consumer mix**
   - The Dell EMC drives may be enterprise pulls.
   - The Seagates are mostly desktop drives.
   - Mixing is fine for a homelab but not ideal for critical storage.

3. **Unknown health**
   - The biggest question is age and SMART health.
   - A used drive with 50,000+ hours may not be worth trusting with important data.

### What I'd do
Since you already have a Synology and homelab:

**Option 1 (recommended)**
- Test every drive with SMART.
- Keep the healthiest drives as cold backups.
- Use the best 3–4 drives in a secondary NAS.

**Option 2**
- Build a cheap backup NAS from your spare Dell/HP/Lenovo.
- Install TrueNAS or OpenMediaVault.
- Use these drives as a backup target for your Synology.

### Before using them
On Linux:

```bash
sudo smartctl -a /dev/sdX
```

Run a long test:

```bash
sudo smartctl -t long /dev/sdX
```

Look for:
- Reallocated_Sector_Count
- Current_Pending_Sector
- Offline_Uncorrectable
- Power_On_Hours

Any non-zero pending sectors are a red flag.

### Capacity examples

If all drives are healthy:

| Configuration | Usable Capacity |
|--------------|----------------|
| Single drives | 18 TB |
| RAID1 pairs | ~8 TB |
| Unraid | ~14 TB with one parity disk |
| Synology SHR | ~12–14 TB depending on layout |

Given your setup (Synology DS423 + Plex + spare hardware), I'd probably turn these into a **backup NAS** rather than trust them as primary storage until the SMART data looks good.
