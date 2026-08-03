---
date: 2026-05-25
source: chatgpt
title: "Demo API Setup"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** what information do i enter for my demo api account to be connected

**ChatGPT:** For your demo entity["company","Kalshi","prediction market platform"] API connection, you usually need these four things inside your bot/service config:

1. **API Key ID**
2. **Private Key File** (the `.pem` file you downloaded)
3. **API Base URL**
4. **Environment selection** (demo vs production)

For the demo environment specifically:

- Base URL:
  `https://demo-api.kalshi.co`

You generally do **not** use your website password directly for API auth.

Typical setup looks something like:

```env
KALSHI_API_KEY_ID=your_key_id_here
KALSHI_PRIVATE_KEY_PATH=/path/to/kalshi-key.pem
KALSHI_API_URL=https://demo-api.kalshi.co
```

Or sometimes:

```env
KALSHI_ENV=demo
```

depending on how Hermes or your service is coded.

The most important part:
- the **Key ID**
- and the matching **private key PEM file**

Those are generated from the API section of your urlKalshi Demo Account Settingshttps://demo.kalshi.co/account/api

For your stack specifically (Hermes + Kalshi bot on Ubuntu), the clean approach is:

### Recommended structure

```bash
~/kalshi-bot/
├── .env
├── keys/
│   └── kalshi-demo.pem
```

Example `.env`:

```env
KALSHI_API_KEY_ID=abc123
KALSHI_PRIVATE_KEY_PATH=/home/ubuntu/kalshi-bot/keys/kalshi-demo.pem
KALSHI_API_URL=https://demo-api.kalshi.co
```

Then your Python app loads it with dotenv.

A few common mistakes:
- Using production URL instead of demo URL
- Wrong permissions on `.pem` file
- Copy/pasting the PEM contents instead of file path
- Using Windows line endings in the PEM file
- Forgetting to enable API access in the demo account

You can verify connectivity with a simple request like:

```bash
curl https://demo-api.kalshi.co/trade-api/v2/exchange/status
```

If you want, next I can help you:
- wire the credentials into Hermes
- test authentication
- place a fake demo trade safely
- send Telegram notifications after fills
- build a paper-trading flow before live deployment

**You:** It is showing a .txt file

**ChatGPT:** That usually means your browser downloaded the private key incorrectly or renamed it.

The file should still work if the contents look like this:

```txt
-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
```

or

```txt
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
```

If that text is inside the file, you can simply rename it from:

```bash
something.txt
```

to:

```bash
kalshi-demo.pem
```

On Ubuntu:

```bash
mv something.txt kalshi-demo.pem
```

Then lock permissions down:

```bash
chmod 600 kalshi-demo.pem
```

And point your bot to:

```env
KALSHI_PRIVATE_KEY_PATH=/full/path/kalshi-demo.pem
```

You can verify the file is correct with:

```bash
cat kalshi-demo.pem
```

You should see the BEGIN/END PRIVATE KEY blocks.

If instead the `.txt` file contains:
- JSON
- HTML
- an error page
- or random text

then the key did not download properly and you should regenerate it from the urlKalshi Demo API Settingshttps://demo.kalshi.co/account/api page.

**You:** Now how do i do it that it is pem

**ChatGPT:** If the file already contains the private key text, you only need to rename the extension to `.pem`.

On Ubuntu/Linux:

```bash
mv yourfile.txt kalshi-demo.pem
```

Example:

```bash
mv APIKey.txt kalshi-demo.pem
```

Then verify:

```bash
ls
```

You should now see:

```bash
kalshi-demo.pem
```

Then secure it:

```bash
chmod 600 kalshi-demo.pem
```

And test contents:

```bash
cat kalshi-demo.pem
```

You should see something like:

```txt
-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
```

If you're doing it from the GUI/file browser:
1. Right click the file
2. Rename
3. Change `.txt` → `.pem`

Example:

```txt
APIKey.txt
```

becomes

```txt
kalshi-demo.pem
```

The extension itself is what makes it a PEM file — the important part is the content inside being a valid private key.

**You:** WHat do i give to herme

**ChatGPT:** For Hermes, you generally provide these three values from your entity["company","Kalshi","prediction market platform"] demo API account:

```env
KALSHI_API_KEY_ID=your_key_id
KALSHI_PRIVATE_KEY_PATH=/full/path/to/kalshi-demo.pem
KALSHI_API_URL=https://demo-api.kalshi.co
```

Example:

```env
KALSHI_API_KEY_ID=ck_demo_abcd1234
KALSHI_PRIVATE_KEY_PATH=/home/ubuntu/kalshi-bot/keys/kalshi-demo.pem
KALSHI_API_URL=https://demo-api.kalshi.co
```

What each one is:

- `API_KEY_ID`
  → from the Kalshi API page

- `PRIVATE_KEY_PATH`
  → path to the `.pem` file you renamed

- `API_URL`
  → demo environment endpoint

If Hermes asks for:
- **Key** → use API Key ID
- **Secret / PEM / Private Key** → either:
  - paste the PEM contents
  - OR give the file path
  depending on how Hermes is built

If there’s a field for:
- Environment
- Base URL
- Endpoint

use:

```txt
https://demo-api.kalshi.co
```

NOT the regular website URL.

If you paste the PEM directly, it should look like:

```txt
-----BEGIN PRIVATE KEY-----
abc123...
-----END PRIVATE KEY-----
```

including the BEGIN/END lines.

A lot of Hermes setups also expect environment variables loaded automatically from a `.env` file in the project folder. So if Hermes is running in Docker or Python, you may only need:

```env
KALSHI_API_KEY_ID=...
KALSHI_PRIVATE_KEY_PATH=...
KALSHI_API_URL=https://demo-api.kalshi.co
```

inside `.env`.

If you want, send:
- the Hermes config screen
- or the config file fields it’s asking for

and I can tell you exactly what goes in each field.

**You:** where do i get api url

**ChatGPT:** For the entity["company","Kalshi","prediction market platform"] **demo environment**, the API URL is fixed — you don’t generate it yourself.

Use:

```txt id="td5h3v"
https://demo-api.kalshi.co
```

For live production trading later, it becomes:

```txt id="cl4it6"
https://api.elections.kalshi.com
```

But for your testing setup with Hermes, use the demo one:

```txt id="k1w8mr"
https://demo-api.kalshi.co
```

You get:
- the **API Key ID**
- and the **private key (.pem)**

from the urlKalshi Demo API Settingshttps://demo.kalshi.co/account/api page.

The API URL itself is just the standard endpoint their API uses.

**You:** The path is on my machine not the server with my program

**ChatGPT:** Then Hermes/the bot cannot access the key file yet. The `.pem` must exist on the same machine/container where the program runs.

So you need to transfer the PEM file from your local machine to the Ubuntu server running:
- Hermes
- your Kalshi bot
- Docker container (if applicable)

Simplest method:

### From your Mac/local machine

Run:

```bash id="vwv1i4"
scp /path/to/kalshi-demo.pem ubuntu@YOUR_SERVER_IP:/home/ubuntu/
```

Example:

```bash id="9yr4t0"
scp ~/Downloads/kalshi-demo.pem ubuntu@100.121.xxx.xxx:/home/ubuntu/
```

Then SSH into the server:

```bash id="9rgl1q"
ssh ubuntu@YOUR_SERVER_IP
```

Verify it exists:

```bash id="8t9r9f"
ls /home/ubuntu
```

Then secure it:

```bash id="8xzbq3"
chmod 600 /home/ubuntu/kalshi-demo.pem
```

Now Hermes can use:

```env id="7imxkh"
KALSHI_PRIVATE_KEY_PATH=/home/ubuntu/kalshi-demo.pem
```

If Hermes is inside Docker, you either:
- mount the PEM into the container
- OR place it inside the project directory the container already mounts

Example Docker compose volume:

```yaml id="1v9i6t"
volumes:
  - ./keys:/app/keys
```

then:

```env id="utkt0l"
KALSHI_PRIVATE_KEY_PATH=/app/keys/kalshi-demo.pem
```

A very common clean structure for your setup would be:

```txt id="aj66hf"
/opt/kalshi-bot/
├── .env
├── keys/
│   └── kalshi-demo.pem
```

with:

```env id="t38k1f"
KALSHI_PRIVATE_KEY_PATH=/opt/kalshi-bot/keys/kalshi-demo.pem
```

That keeps your API credentials organized and separate from the code.

**You:** jacobmcnamara@Mac ~ % scp /Users/jacobmcnamara/Documents/kalshi-demo.pem carlthellama@192.168.1.10:/home/ubuntu/
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:78t2eaQa6QZeWGYVon/dvp+1lW41hS/VD+7fikdNh7Q.
Please contact your system administrator.
Add correct host key in /Users/jacobmcnamara/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /Users/jacobmcnamara/.ssh/known_hosts:6
Host key for 192.168.1.10 has changed and you have requested strict checking.
Host key verification failed.
scp: Connection closed

**ChatGPT:** This is usually normal after:
- reinstalling Ubuntu
- regenerating SSH keys
- changing SSH configuration
- replacing the server
- reinstalling Tailscale/OpenSSH

Your Mac saved an old fingerprint for `192.168.1.10`, and now the server is presenting a different one.

Since this is your own server on your LAN, you can remove the old fingerprint entry safely if you know the machine was rebuilt or changed.

Run this on your Mac:

```bash id="fjxmqf"
ssh-keygen -R 192.168.1.10
```

Then retry:

```bash id="rf5f8v"
scp /Users/jacobmcnamara/Documents/kalshi-demo.pem carlthellama@192.168.1.10:/home/ubuntu/
```

You’ll probably get:

```txt id="kwwbhw"
Are you sure you want to continue connecting (yes/no)?
```

Type:

```txt id="w8w1cc"
yes
```

Then enter your password.

One more thing:
you are copying as user `carlthellama` but uploading to `/home/ubuntu/`.

That may fail if:
- the `ubuntu` user does not exist
- or `carlthellama` lacks permissions there

Cleaner approach:

```bash id="nlj8u2"
scp /Users/jacobmcnamara/Documents/kalshi-demo.pem carlthellama@192.168.1.10:/home/carlthellama/
```

Then on the server:

```bash id="d5z92o"
chmod 600 ~/kalshi-demo.pem
```

and use:

```env id="g9gvft"
KALSHI_PRIVATE_KEY_PATH=/home/carlthellama/kalshi-demo.pem
```

That is likely the correct path for your setup.

**You:** scp: dest open "/home/ubuntu/": Failure
scp: failed to upload file /Users/jacobmcnamara/Documents/kalshi-demo.pem to /home/ubuntu/

**ChatGPT:** That means the `ubuntu` home folder either:
- does not exist
- or your `carlthellama` user cannot write there.

Since you’re logging in as `carlthellama`, upload it to your own home directory instead.

Use:

```bash id="4bjlwm"
scp /Users/jacobmcnamara/Documents/kalshi-demo.pem carlthellama@192.168.1.10:/home/carlthellama/
```

or even shorter:

```bash id="v4j4gm"
scp /Users/jacobmcnamara/Documents/kalshi-demo.pem carlthellama@192.168.1.10:~
```

Then SSH into the server:

```bash id="g3slx8"
ssh carlthellama@192.168.1.10
```

Verify:

```bash id="i6wvho"
ls ~
```

You should see:

```txt id="v1kz4u"
kalshi-demo.pem
```

Then secure it:

```bash id="eb0u3p"
chmod 600 ~/kalshi-demo.pem
```

Now the path for Hermes becomes:

```env id="g3ijqx"
KALSHI_PRIVATE_KEY_PATH=/home/carlthellama/kalshi-demo.pem
```

or:

```env id="lh3ylc"
KALSHI_PRIVATE_KEY_PATH=~/kalshi-demo.pem
```

depending on how Hermes reads environment variables.
