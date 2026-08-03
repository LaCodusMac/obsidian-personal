---
date: 2026-06-02
source: chatgpt
title: "Increase candidate evaluation"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Let the trader evaluate more than 1 candidate per minute
   - Right now it bottlenecks at one top signal.
   - Change hermes_bridge.py line 334 from:
     
Python

     signals = get_signals(limit=min(limit, 1), lookback_minutes=lookback_minutes)
     
     to:
     
Python

     signals = get_signals(limit=limit, lookback_minutes=lookback_minutes)
     
   - Then change the systemd service from --limit 1 to maybe --limit 5 or --limit 10.
   - This is the safest volume increase because it doesn’t weaken risk rules; it just gives the bot more chances to find a pass.

**ChatGPT:** Yes — that’s the right next move.

It increases **candidate evaluation volume**, not trade risk.

Do this:

```bash
cd ~/kalshi-watch
nano hermes_bridge.py
```

Change:

```python
signals = get_signals(limit=min(limit, 1), lookback_minutes=lookback_minutes)
```

to:

```python
signals = get_signals(limit=limit, lookback_minutes=lookback_minutes)
```

Then update your systemd service:

```bash
sudo nano /etc/systemd/system/hermes-demo-trader.service
```

Find the `ExecStart=` line and change something like:

```ini
ExecStart=/usr/bin/python3 /home/YOUR_USER/kalshi-watch/hermes_bridge.py --limit 1
```

to:

```ini
ExecStart=/usr/bin/python3 /home/YOUR_USER/kalshi-watch/hermes_bridge.py --limit 5
```

I’d start with **5**, not 10.

Then reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl restart hermes-demo-trader.service
```

Check it:

```bash
journalctl -u hermes-demo-trader.service -n 100 --no-pager
```

Expected result: Hermes should still only trade candidates that pass risk, but it will now evaluate up to 5 signals per run instead of only the single top signal.
