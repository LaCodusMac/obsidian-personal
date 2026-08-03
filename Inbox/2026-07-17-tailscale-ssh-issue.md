---
date: 2026-07-17
source: chatgpt
title: "Tailscale SSH Issue"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** When I use tailscale I can’t ssh into other devices on my network to work with codex. What is your suggestion to bypass that

**ChatGPT:** This is a pretty common issue with Codex/SSH when Tailscale changes how your machine reaches other devices.

A few approaches work well, depending on what you're trying to accomplish.

### Option 1 (What I'd recommend): Use Tailscale IPs everywhere
Instead of SSHing to:
```bash
ssh user@192.168.1.50
```

SSH to:
```bash
ssh user@100.x.x.x
```

or

```bash
ssh user@hostname.tailnet-name.ts.net
```

Advantages:
- Works anywhere
- No port forwarding
- Encrypted
- Codex can use the same hostname whether you're home or away

---

### Option 2: Enable LAN Access (Split Routing)

If you're connected to your own Wi-Fi and only want remote access when you're away:

Disable the "Use Tailscale for local network access" blocking.

Depending on OS:

- Enable **Allow LAN Access**
- Or advertise only specific routes instead of an exit node.

If you're using an Exit Node, this is often the culprit.

---

### Option 3: SSH over Tailscale

Enable Tailscale SSH on your Linux boxes.

Then:

```bash
ssh server
```

works through Tailscale itself.

No firewall rules.
No exposed SSH.

---

### Option 4: Tell SSH which interface to use

Sometimes SSH resolves the hostname to the wrong IP.

Example:

```
server
    HostName 192.168.1.50
```

becomes

```
server-lan
    HostName 192.168.1.50

server-ts
    HostName 100.101.102.103
```

Then Codex can choose the correct target.

---

### Option 5 (My favorite for a homelab)

Since I remember your setup:

- UniFi
- Proxmox
- Synology
- Ubuntu Docker server
- Raspberry Pis
- Tailscale already installed

I'd do this:

- Keep every server on Tailscale.
- SSH using MagicDNS names:
  ```
  ssh ubuntu
  ssh proxmox
  ssh synology
  ssh pihole
  ```
- Leave local networking alone (don't use an Exit Node while at home unless necessary).
- Let Codex connect over Tailscale instead of the LAN.

You'll get the same connection whether you're at home, work, or on your phone.

---

### One thing I'd like to narrow down

When you say **"I can't SSH into other devices"**, which behavior are you seeing?

- **A.** `ssh 192.168.1.x` just hangs.
- **B.** You get `Connection refused`.
- **C.** `No route to host`.
- **D.** It only fails when Tailscale is connected.
- **E.** Codex itself can't connect, but manual SSH from the terminal works.

That answer will usually pinpoint the exact cause within a minute.

**You:** It says wrong password and won’t let me connect

**ChatGPT:** That means **networking is working**—you reached the SSH server. The problem is authentication, most likely the **username**, not Tailscale.

Try explicitly specifying the Linux account that exists on the destination device:

```bash
ssh jacob@100.x.x.x
```

or:

```bash
ssh jacob@server-name
```

Check your current command. If you run only:

```bash
ssh server-name
```

SSH automatically uses the username from your current computer, which may not exist on the server.

On the destination device, confirm the username with:

```bash
whoami
```

Then test with verbose output:

```bash
ssh -v username@server-name
```

Look for:

```text
Authentications that can continue:
```

### My recommendation for Codex

Set up SSH keys rather than passwords:

```bash
ssh-keygen -t ed25519
ssh-copy-id username@server-name
```

Then verify:

```bash
ssh username@server-name
```

Once working, add an alias to `~/.ssh/config`:

```sshconfig
Host docker-server
    HostName 100.x.x.x
    User username
    IdentityFile ~/.ssh/id_ed25519
```

Codex can then connect with:

```bash
ssh docker-server
```

If you enabled **Tailscale SSH** using `sudo tailscale set --ssh`, it normally authenticates using your Tailscale identity rather than the server password, but you still must specify a valid local Linux username. citeturn867498search0turn867498search4

Based on the wrong-password message, first try:

```bash
ssh carlthellama@TAILSCALE-IP
```

using the exact username you normally use on that Linux device.

**You:** What about larger work arounds

**ChatGPT:** The cleaner “big workaround” is to stop making your laptop directly reach every homelab device. Use one trusted development host as the gateway and let Codex work there.

**ChatGPT:** Yes—there are bigger architectural workarounds that are better than fighting password authentication on every box.

## Best option for your homelab: one Codex jump/development server

Pick your Ubuntu Docker NUC or create a dedicated Ubuntu VM on Proxmox. Install Codex, Git, SSH keys, and your development tools there.

Your workflow becomes:

```text
Laptop
  ↓ Tailscale/SSH
Ubuntu development host
  ↓ local LAN SSH
Pi-hole / Proxmox / other Linux servers
```

Codex runs **on the development host**, so when it executes:

```bash
ssh pihole
ssh proxmox
ssh media-server
```

those connections originate from inside your home network. Tailscale only has to get you into one machine.

OpenAI now supports remote Codex connections over SSH, specifically allowing the Codex app to start and manage its server on a remote host. OpenAI cautions against exposing the app-server transport directly; use SSH as the transport. citeturn485588search4

This is what I would choose for you.

### Set it up

On the Ubuntu development host:

```bash
sudo apt update
sudo apt install openssh-server git tmux
```

Create a dedicated account:

```bash
sudo adduser codex
sudo usermod -aG sudo codex
```

Install Tailscale and Codex there, then generate a key:

```bash
sudo -iu codex
ssh-keygen -t ed25519
```

Copy that key to each internal Linux device:

```bash
ssh-copy-id carlthellama@192.168.1.50
ssh-copy-id jacob@192.168.1.51
```

Create `/home/codex/.ssh/config`:

```sshconfig
Host pihole
    HostName 192.168.1.50
    User carlthellama
    IdentityFile ~/.ssh/id_ed25519

Host docker
    HostName 192.168.1.51
    User jacob
    IdentityFile ~/.ssh/id_ed25519

Host proxmox
    HostName 192.168.1.52
    User root
    IdentityFile ~/.ssh/id_ed25519
```

Now Codex can simply run:

```bash
ssh pihole
```

No repeated passwords.

## Second option: Tailscale subnet router

Instead of installing Tailscale on every device, make one Raspberry Pi or Ubuntu server advertise your LAN subnet:

```bash
sudo tailscale set --advertise-routes=192.168.1.0/24
```

Approve the route in the Tailscale admin console, then enable route acceptance on your remote computer:

```bash
tailscale set --accept-routes=true
```

Your remote laptop can then connect directly to:

```bash
ssh user@192.168.1.50
```

This solves **routing**, but it does not solve wrong passwords. You should still deploy SSH keys.

A subnet router is particularly useful for Synology, UniFi, printers, IPMI interfaces, or other devices where installing Tailscale directly is undesirable.

## Third option: VS Code Remote SSH or Remote Tunnels

Connect your editor to the Ubuntu development host and work as though its filesystem were local. VS Code Remote SSH opens the remote directory and runs the development tooling on the remote host. citeturn485588search11

With Remote Tunnels, you can connect without maintaining a normal inbound SSH route. citeturn485588search50

That creates this workflow:

```text
Laptop VS Code
      ↓
Remote Ubuntu workspace
      ↓
Codex + Git + Docker + LAN access
```

This is excellent if your main goal is coding rather than general server administration.

## Fourth option: Git-driven management

Avoid giving Codex interactive access to every device.

Codex modifies configuration in a Git repository on your development server. Deployment scripts, Ansible, Docker Compose, or GitHub Actions then apply those changes.

Example:

```text
Codex edits repository
        ↓
Git commit
        ↓
Ansible applies changes
        ↓
Servers update
```

A basic Ansible inventory could look like:

```ini
[pihole]
192.168.1.50 ansible_user=carlthellama

[docker]
192.168.1.51 ansible_user=jacob

[proxmox]
192.168.1.52 ansible_user=root
```

Then:

```bash
ansible all -m ping
```

This is safer and more repeatable than letting Codex freely SSH around and manually change files.

## My recommended final architecture

Use your **NUC10 Ubuntu Docker server as the Codex control host**:

```text
Your Mac/Windows PC
        │
        │ Tailscale SSH using an SSH key
        ▼
NUC10 Ubuntu “dev-control”
        │
        ├── Git repositories
        ├── Codex CLI/server
        ├── Ansible
        ├── SSH keys
        └── tmux
              │
              ├── Proxmox
              ├── Pi-hole
              ├── Docker hosts
              └── Raspberry Pis
```

Use the Tailscale identity only for entry into that host. Use separate SSH keys from the control host to internal machines. Keep Synology and UniFi management available through a subnet router.

That gives you one authentication point, one Codex workspace, consistent network access, and much less troubleshooting. Tailscale SSH can also manage authentication and authorization for the initial connection to that host instead of relying on its normal SSH password. citeturn485588search3turn485588search25

**You:** You’re not fixing any issue

**ChatGPT:** You're right. Those are architectural improvements, not fixes for the problem you're actually having.

The key detail is this:

> **"It says wrong password."**

That means:
- ✅ Tailscale is connecting to the SSH server.
- ✅ Port 22 is open.
- ✅ The server is responding.
- ❌ SSH authentication is failing.

No workaround can bypass SSH authentication unless you change how authentication works.

There are only a few real possibilities:

1. **Wrong username.** SSH is trying to log in as the wrong Linux user.
2. **Password authentication is disabled** (`PasswordAuthentication no` in `sshd_config`), so even the correct password won't work.
3. **You're connecting via Tailscale SSH**, which doesn't accept the local account password the way you expect.
4. **The account is locked** or PAM is denying logins.

If your goal is **"I don't care why, I just want Codex to work,"** then there are only two genuine bypasses:

- **Use SSH keys instead of passwords.** This bypasses password prompts entirely but still authenticates securely.
- **Run Codex directly on the remote machine** so it doesn't need to SSH to that machine at all.

Neither bypasses authentication—they replace the password mechanism.

### What I'd like to pinpoint

Can you answer these three questions?

1. **From where are you SSHing?**
   - Mac
   - Windows
   - Linux

2. **To what device?**
   - Ubuntu server
   - Raspberry Pi
   - Proxmox
   - Synology
   - Something else

3. **What exact command are you running?**
   For example:
   ```bash
   ssh carlthellama@100.x.x.x
   ```
   or
   ```bash
   ssh 192.168.1.50
   ```

With those three pieces, we can determine whether this is a Tailscale issue or a plain SSH configuration issue. Based on the "wrong password" message, I suspect it's the latter.

**You:** I need codex to be on the machine with all the files

**ChatGPT:** Exactly—then **Codex must stay installed on the machine containing the files**. SSH is only needed so that machine can reach your other devices.

The immediate workaround is:

## Keep Codex local, replace password SSH with keys

From the machine where Codex and the files are located, create a key:

```bash
ssh-keygen -t ed25519
```

Press Enter through the prompts. Then copy it to the device you need to manage:

```bash
ssh-copy-id actualusername@192.168.1.50
```

If you’re connecting through Tailscale:

```bash
ssh-copy-id actualusername@100.x.x.x
```

You’ll enter the password once. After that:

```bash
ssh actualusername@100.x.x.x
```

should connect without asking for a password.

Codex remains on your main machine, reads and modifies the local files, and can execute SSH commands against the servers. Codex CLI operates on the selected local directory and can run commands from that machine. citeturn433726search1turn433726search13

## If the password is rejected during `ssh-copy-id`

Use physical access, Proxmox console, Synology console, or another working login to manually install the key.

On your Codex machine:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the full output.

On the destination Linux server, while logged in through its console:

```bash
mkdir -p ~/.ssh
nano ~/.ssh/authorized_keys
```

Paste the key, save it, and then run:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

Test from the Codex machine:

```bash
ssh actualusername@100.x.x.x
```

## Make Codex use predictable names

On the Codex machine, edit:

```bash
nano ~/.ssh/config
```

Add:

```sshconfig
Host pihole
    HostName 100.x.x.x
    User carlthellama
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host proxmox
    HostName 100.x.x.x
    User root
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

Then both you and Codex can use:

```bash
ssh pihole
ssh proxmox
```

## The actual larger workaround

For devices that do not have Tailscale installed, configure a **Tailscale subnet router**. Your Codex machine still keeps all its local files, but can reach every homelab IP directly:

```bash
ssh carlthellama@192.168.1.50
```

However, the subnet router only fixes routing. **SSH keys are what fix the rejected-password issue.**

So the right setup is:

```text
Codex + project files on your current machine
          │
          │ Tailscale or subnet route
          ▼
Remote homelab devices
          │
          └── SSH key authentication
```

Do not move Codex or the files. Install the SSH public key from the Codex machine onto each destination device.

**You:** No I am going on vacation and need my laptop to reach that device

**ChatGPT:** Ah—that changes the problem completely.

Your setup is:

- **Home PC/server** → has the project files and runs Codex.
- **Laptop** → you're taking it on vacation.
- You want the **laptop to remotely control the home Codex machine** and have that machine access everything else.

That's actually a common remote development setup.

## Option 1 (the one I'd recommend): Remote desktop into your home machine

Instead of trying to recreate the environment on the laptop, leave Codex running on the home machine and remote into it.

Examples:
- Tailscale + RDP (Windows)
- Tailscale + RustDesk
- Tailscale + NoMachine
- Tailscale + Sunshine/Moonlight (very fast if you have a decent GPU)

Then you're literally using your home computer from vacation.

---

## Option 2: SSH into the home machine and run Codex there

From the laptop:

```bash
ssh home-pc
```

Then:

```bash
cd ~/your-project
codex
```

Everything runs on the home machine. The laptop is just the terminal.

---

## Option 3: VS Code Remote SSH

This is one of the best developer experiences.

Your laptop connects to the home machine over SSH, but:
- all the files stay at home
- all terminals run at home
- Codex runs at home
- your laptop is just the interface

It feels almost like the files are local.

---

## Option 4: Tailscale Funnel/Serve (for web UIs)

If Codex or your tooling has a web interface, you can expose it securely through Tailscale.

---

### What I would do if I had your homelab

Knowing you have:
- Ubuntu server
- Proxmox
- Synology
- Tailscale
- Codex project at home

I'd leave **everything running at home**.

From vacation I'd simply:

```text
Laptop
   │
Tailscale
   │
Home Codex machine
   │
SSH
   ├── Proxmox
   ├── Pi-hole
   ├── Synology
   └── Docker hosts
```

No syncing files. No copying repositories. No changing your workflow.

### One question:

When you say **Codex**, are you referring to:
1. **OpenAI Codex CLI** running in a terminal on your project, or
2. **VS Code with the Codex extension/agent**?

That changes what the smoothest remote workflow looks like.
