---
date: 2026-06-28
source: chatgpt
title: "Obsidian Sync Linux Mac"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** I want to connect obsidian between Linux and Mac devices

**ChatGPT:** That's a great setup. If you're already using Linux for development and a Mac as your daily device, Obsidian syncs very well as long as you choose the right storage backend.

## Option 1 (Recommended): Git + Obsidian Git Plugin
This is the option I'd recommend for you because you already work with Git and development projects.

**Pros**
- Free
- Full version history
- Works on Linux and macOS
- Great backup
- Private GitHub repo or self-hosted Git server

**How it works**
```
Mac
   ↓
GitHub Private Repository
   ↑
Linux
```

Setup:
1. Create a private GitHub repository.
2. Put your Obsidian vault inside the repository.
3. Install the **Obsidian Git** community plugin.
4. Configure automatic:
   - Pull on startup
   - Commit every few minutes
   - Push after commit

This makes syncing nearly automatic.

---

## Option 2: Syncthing ⭐ (My favorite for local-first users)

Since you already have a homelab, this fits your style very well.

```
Mac
     \
      Syncthing
     /
Linux
```

Pros
- Completely free
- No cloud required
- Peer-to-peer
- Very fast
- End-to-end encrypted during transfer
- Can also sync to your NAS

If both devices are on your network, changes appear almost instantly.

You can even add your Synology as a third device for redundancy.

---

## Option 3: Obsidian Sync

If you don't mind paying a subscription:

Pros
- Easiest setup
- Handles conflicts well
- Encrypted
- Mobile support

Cons
- Monthly subscription

---

## Option 4: iCloud / Dropbox / OneDrive

These work, but I generally don't recommend them for Linux because Linux support is less seamless than Git or Syncthing.

---

# What I'd build for your setup

Knowing your homelab and interest in reliable infrastructure, I'd use:

```
Synology NAS
        │
   Syncthing
   ┌────┴────┐
 MacBook   Linux Desktop
      │
   GitHub Private Repo
      │
 Nightly backup
```

This gives you:
- Instant sync between devices.
- A local backup on your NAS.
- Off-site version history in GitHub.
- The ability to restore any previous version of a note.

It's fast, resilient, and aligns well with the infrastructure you've already built.

If you're planning to use Obsidian as a long-term "second brain" for things like your finances, homelab, Kalshi research, work documentation, and personal knowledge, this setup is hard to beat. I can also help you design an Obsidian vault structure tailored to those areas so it stays organized as it grows.

**You:** Git instructions

**ChatGPT:** ## Git setup for Obsidian sync

### 1. Create private GitHub repo
Create a new **private** repo, for example:

```bash
obsidian-vault
```

Do **not** add a README if your vault already exists.

---

### 2. On your main device

Go to your Obsidian vault folder:

```bash
cd /path/to/your/ObsidianVault
```

Initialize Git:

```bash
git init
git branch -M main
```

Add a `.gitignore`:

```bash
nano .gitignore
```

Paste:

```gitignore
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.trash/
.DS_Store
```

Save, then run:

```bash
git add .
git commit -m "Initial Obsidian vault sync"
git remote add origin git@github.com:YOUR_USERNAME/obsidian-vault.git
git push -u origin main
```

---

### 3. On the second device

Clone the vault:

```bash
cd ~/Documents
git clone git@github.com:YOUR_USERNAME/obsidian-vault.git
```

Then open that folder as a vault in Obsidian.

---

### 4. Install Obsidian Git plugin

In Obsidian:

**Settings → Community plugins → Turn off restricted mode → Browse → Obsidian Git → Install → Enable**

Recommended settings:

```text
Auto pull interval: 5 minutes
Auto commit interval: 10 minutes
Auto push: enabled
Pull updates on startup: enabled
Commit message: vault backup: {{date}}
```

---

### 5. Daily use rule

Before editing on a device:

```bash
git pull
```

After editing:

```bash
git add .
git commit -m "Update notes"
git push
```

The plugin can automate most of this, but this manual flow helps when something looks off.

---

### Conflict rule

Do not edit the same note on both devices before syncing.

If Git says there is a conflict, open the file and look for:

```text
<<<<<<< HEAD
your version
=======
other version
>>>>>>> branch
```

Keep what you want, delete the markers, then:

```bash
git add .
git commit -m "Resolve sync conflict"
git push
```
