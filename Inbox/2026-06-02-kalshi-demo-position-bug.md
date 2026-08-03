---
date: 2026-06-02
source: chatgpt
title: "Kalshi Demo Position Bug"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** I was talking with my kalshi trading bot and What’s actually open live on Kalshi demo

The live Kalshi demo API shows 1 active position, matching what you see on the website:

- KXSAVEACT-27-JAN04
- position_fp = -1.00
- exposure: $0.904
- no resting orders

Why I said “3 open positions”

That came from the local table:

SQL

position_lifecycle_metrics

It has 3 rows marked lifecycle_status='open':

- KXAAAGASM-26MAY31-4.40
- KXUSAIRANAGREEMENT-27-26JUN
- KXSAVEACT-27-JAN04

But the live demo_market_positions table / Kalshi API only shows 1 actual nonzero position.

So the local lifecycle table has stale open rows that weren’t reconciled/closed correctly. The website/API is authoritative here.

Important bug found

frequency_rules.py currently counts “open positions” from old trade_recommendations history, not from live Kalshi positions. That means stale local rows can incorrectly trigger:

text

open position limit reached

even when the website only has 1 live position.

Best fix: change the open-position limit check to use demo_market_positions where abs(position_fp) > 0 or live API-synced positions, not stale lifecycle history.

**ChatGPT:** Yes — your read is right.

**Kalshi/API = truth.**  
Right now you only have **1 real live demo position**:

`KXSAVEACT-27-JAN04`

The other “open” positions are **local stale state**, not actual Kalshi exposure.

The bug is basically:

```text
frequency_rules.py is asking:
"How many trades did my local history think are open?"

But it should ask:
"How many positions does Kalshi currently say are nonzero?"
```

So stale rows like:

```text
KXAAAGASM
KXUSAIRANAGREEMENT
```

can wrongly block new trades with:

```text
open position limit reached
```

even though they are not actually open anymore.

Best fix:

```sql
SELECT COUNT(*)
FROM demo_market_positions
WHERE ABS(position_fp) > 0;
```

Or even better: before frequency checks, sync live demo positions from Kalshi, then count only those.

The local `position_lifecycle_metrics` table should be treated as **analytics/history**, not the source of truth for active exposure.

**You:** The current stuck position exposed some NO-side weirdness. The DB shows position_fp=-1.0 for long NO, but market snapshots are stored as YES bid/ask. The exit logic mostly computes from YES bid/ask, then maps to NO orders.

That is error-prone.

- Normalize every position into its actual side book:
  - long YES: exit using YES bid/ask
  - long NO: exit using NO bid/ask = 100 - YES ask, 100 - YES bid
- Store both in snapshots or derive consistently:
  - no_bid = 100 - yes_ask
  - no_ask = 100 - yes_bid
- Log exit decision as:
  - side
  - side_bid
  - side_ask
  - selected exit price
  - marketable or passive

This will make stuck exits much easier to debug.

**ChatGPT:** Exactly. This is the right fix.

Your bot should stop thinking in “YES price, then flip later” terms. It should normalize to the **position’s real held side** first.

Core rule:

```python
yes_bid = snapshot["yes_bid"]
yes_ask = snapshot["yes_ask"]

no_bid = 100 - yes_ask
no_ask = 100 - yes_bid
```

Then:

```python
if position_fp > 0:
    held_side = "yes"
    side_bid = yes_bid
    side_ask = yes_ask
elif position_fp < 0:
    held_side = "no"
    side_bid = no_bid
    side_ask = no_ask
```

Exit logic should then use only:

```python
side_bid
side_ask
held_side
```

For selling a held side:

```python
passive_exit_price = side_ask
marketable_exit_price = side_bid
```

So for long NO, you are no longer mentally doing “YES ask means NO bid.” You just say:

```text
I hold NO.
NO bid = 100 - YES ask.
NO ask = 100 - YES bid.
To exit immediately, sell NO at NO bid.
To exit passively, sell NO at NO ask.
```

And every exit alert/log should include:

```text
held_side: NO
yes_bid / yes_ask
no_bid / no_ask
side_bid / side_ask
exit_style: passive or marketable
selected_exit_price
order_action: SELL_DEMO_NO
```

This also makes your stuck order obvious:

```text
If selected_exit_price is above side_ask, it is too expensive.
If selected_exit_price is below/equal side_bid, it should be marketable.
If side_bid/ask changed after placement, the order may now be stale.
```

The important architecture change:

```text
Snapshots can store YES prices.
But position/exits should operate on normalized side prices.
```

That will remove most of the NO-side confusion.

**You:** Implemented the side-book normalization and exit decision logging.

  Changed:

  - kalshi-watch/hermes_position_monitor.py:370
      - Normalizes snapshots into the actual position side book.
      - Long NO now derives side_bid = 100 - yes_ask, side_ask = 100 - yes_bid.
      - Adds book_side, side_bid, side_ask, side_spread.
      - Exit pricing/style now reads side-book fields.
      - Exit responses now log: side, side_bid, side_ask, selected_exit_price, placement=marketable|passive.
      - Monitor migration adds missing no_bid/no_ask columns for older snapshot tables.

  - kalshi-watch/collect_kalshi.py:1378
      - Stores no_bid/no_ask consistently from YES quotes:
          - no_bid = 100 - yes_ask
          - no_ask = 100 - yes_bid

  - kalshi-watch/test_position_monitor.py:306
      - Added focused NO-side normalization/logging tests.
      - Updated stuck-exit expectation for long NO from YES-side 95 to normalized NO-side 6.

  Verification:

  - python3 -m py_compile hermes_position_monitor.py collect_kalshi.py test_position_monitor.py passed.
  - pytest could not be run because pytest is not installed in this environment, and direct imports also lack python-
    dotenv. I did run a stubbed direct probe confirming YES 94/95 -> NO 5/6 and maybe_place_exit_order(...
    TIME_EXIT ...) -> price 6 with placement=passive.

**ChatGPT:** That’s a strong fix. The key confirmation is this:

```text
YES 94/95 -> NO 5/6
long NO TIME_EXIT -> passive exit at 6
```

That means the bot is now pricing the **NO book**, not accidentally treating YES 95 as the NO exit price.

One thing I’d still add next:

```text
For marketable exits:
long YES -> sell YES at yes_bid
long NO  -> sell NO at no_bid

For passive exits:
long YES -> sell YES at yes_ask
long NO  -> sell NO at no_ask
```

And log the comparison:

```text
placement=passive
selected_exit_price=6
side_bid=5
side_ask=6
is_marketable=false
```

Next best cleanup: fix `frequency_rules.py` so open-position counting comes from live `demo_market_positions` / API positions only. That stale local open-state bug can still block otherwise valid trades.

**You:** Add explicit “entry quality tiers” and only size up after proof

Right now all real demo entries are basically 1 contract, which is good. But the bot has mixed regimes:
- illiquid
- liquidity_vacuum
- event-driven geopolitics
- low-liquidity moves

The closed PnL suggests the current edge is not proven enough to increase size.

Recommended:
- Keep size at 1 contract until a tier has at least:
  - 30+ closed demo trades
  - positive net PnL after fees
  - median hold time under target
  - exit fill rate above maybe 90%
- Add tier labels:
  - A: high-trust narrative + positive expectancy + good depth + spread clear
  - B: good stats but weak narrative/depth
  - C: exploratory/paper-only
- Only auto-trade A; paper-log B/C.

**ChatGPT:** Yes — this is the right risk upgrade.

Do **not** size up globally. Size up only by **proven entry tier**.

I’d implement it like this:

```text
Tier A = allowed to demo trade
Tier B = paper trade only
Tier C = paper trade only / research only
```

Size rule:

```text
Default size = 1 contract

Can size above 1 only if that exact tier/regime has:
- 30+ closed demo trades
- net PnL > 0 after fees
- median hold time <= target hold window
- exit fill rate >= 90%
- no unresolved stuck-exit bug for that side/regime
```

Tier logic:

```text
A:
- positive expectancy
- strong/high-trust narrative confirmation
- good depth near touch
- acceptable spread
- clean exit liquidity
- proven closed-trade stats

B:
- positive or promising stats
- but weak narrative, thin depth, weaker source trust, or small sample

C:
- exploratory
- no regime proof
- low sample
- weird liquidity
- event-driven/geopolitical uncertainty
```

The key architecture change:

```text
entry_quality_tier controls whether the bot may trade.
confidence controls sizing only after the tier is proven.
```

So the bot should not say:

```text
high confidence = larger order
```

It should say:

```text
high confidence + Tier A + proven exits + positive realized PnL = maybe size up
```

For now, I’d set:

```text
A -> demo trade, size 1
B -> paper log
C -> paper log
```

Then later:

```text
A with proof -> size 2+
B with proof -> promote to A
C with proof -> promote to B
```

This prevents the bot from scaling into exactly the regimes that are currently causing problems: illiquid, stale, hard-to-exit, low-trust narrative moves.

**You:** - escalate passive exits to marketable exits
- exclude UNEXITABLE_DEMO dust from MAX_OPEN_POSITIONS
- log every exit decision with side-specific bid/ask and reason

**ChatGPT:** Yes. Make those the next 3 fixes.

Priority order:

```text
1. Log every exit decision
2. Escalate passive exits to marketable exits
3. Exclude UNEXITABLE_DEMO dust from MAX_OPEN_POSITIONS
```

Suggested rules:

```text
Passive exit:
sell held side at side_ask

If not filled after N minutes or N replacements:
cancel passive order
sell held side at side_bid
placement = marketable
reason = passive_exit_stale_escalated
```

For dust:

```text
If position is tiny, non-exitable, or below min contract/value threshold:
lifecycle_status = UNEXITABLE_DEMO
exclude_from_open_position_count = true
exclude_from_frequency_limits = true
still show in diagnostics
```

Open-position count should become:

```sql
SELECT COUNT(*)
FROM demo_market_positions
WHERE ABS(position_fp) > 0
  AND COALESCE(lifecycle_status, '') != 'UNEXITABLE_DEMO';
```

Every exit decision log should include:

```text
ticker
held_side
position_fp
yes_bid / yes_ask
no_bid / no_ask
side_bid / side_ask
side_spread
state
suggested_action
exit_reason
selected_exit_price
placement
previous_exit_order_age
replacement_count
```

This gives you the missing audit trail: **what side did it think it held, what book did it price from, why passive vs marketable, and why it did or didn’t escalate.**

**You:** Implemented the three changes.

  - Passive exits now escalate to marketable on the final allowed passive attempt:
      - STALLED / TIME_EXIT now cross side_bid before hitting the stuck cap.
      - TAKE_PROFIT already crossed on the third attempt when profitable.
      - See kalshi-watch/hermes_position_monitor.py:1032.

  - UNEXITABLE_DEMO dust no longer counts against MAX_OPEN_POSITIONS.
      - The open-position cap query now treats a later UNEXITABLE_DEMO row as excluding that buy from the cap.
      - See kalshi-watch/frequency_rules.py:28.

  - Every exit decision response now logs:
      - side
      - side_bid
      - side_ask
      - selected_exit_price
      - placement
      - is_marketable
      - reason
      - This is included in skipped, stuck, dry-run, submitted, rejected, and failed exit paths.

  Added tests:

  - kalshi-watch/test_position_monitor.py:306 for passive escalation and exit decision logging.
  - kalshi-watch/test_frequency_rules.py:65 for UNEXITABLE_DEMO cap exclusion.

  Verification:

  - python3 -m py_compile hermes_position_monitor.py frequency_rules.py test_position_monitor.py
    test_frequency_rules.py passed.

  - python3 -m unittest -q test_frequency_rules.py passed.
  - Stubbed direct probe confirmed STALLED final passive attempt selects side_bid=94 and logs placement=marketable;
    is_marketable=true; reason=stalled exit.

**ChatGPT:** Good. That fixes the main “stuck forever” loop.

What you have now:

```text
Passive first
→ retry/replace
→ final attempt crosses side_bid
→ logs exact side-book decision
→ dust no longer blocks new trades
```

The important confirmation is:

```text
STALLED final attempt -> side_bid=94
placement=marketable
is_marketable=true
```

That means the bot can now force an exit instead of repeatedly posting passive orders.

Next thing I’d check live:

```text
1. Run Hermes monitor once
2. Confirm open-position count is 1, not 3
3. Confirm KXSAVEACT exit alert shows:
   side=NO
   side_bid / side_ask
   selected_exit_price
   placement
   is_marketable
4. Confirm no stale KXAAAGASM / KXUSAIRAN rows block new entries
```

After that, the next upgrade should be **entry tier gating**: A trades demo, B/C paper only.

**You:** How to run hermes monitor or set something up.

**ChatGPT:** Run it manually first from the bot folder:

```bash
cd ~/kalshi-watch
python3 hermes_position_monitor.py
```

If you use a `.env` file:

```bash
cd ~/kalshi-watch
set -a
source .env
set +a
python3 hermes_position_monitor.py
```

What to look for:

```text
open positions
position state
exit decision
side=NO/YES
side_bid / side_ask
selected_exit_price
placement=passive/marketable
```

To run it continuously every minute, use a simple loop:

```bash
cd ~/kalshi-watch

while true; do
  echo "Running Hermes monitor at $(date)"
  python3 hermes_position_monitor.py
  sleep 60
done
```

Better long-term: make it a systemd service/timer.

Create service:

```bash
sudo nano /etc/systemd/system/hermes-monitor.service
```

Paste:

```ini
[Unit]
Description=Hermes Kalshi Position Monitor
After=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/home/YOUR_USER/kalshi-watch
EnvironmentFile=/home/YOUR_USER/kalshi-watch/.env
ExecStart=/usr/bin/python3 /home/YOUR_USER/kalshi-watch/hermes_position_monitor.py
```

Create timer:

```bash
sudo nano /etc/systemd/system/hermes-monitor.timer
```

Paste:

```ini
[Unit]
Description=Run Hermes Monitor every minute

[Timer]
OnBootSec=30
OnUnitActiveSec=60
Unit=hermes-monitor.service

[Install]
WantedBy=timers.target
```

Enable it:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hermes-monitor.timer
```

Check it:

```bash
systemctl status hermes-monitor.timer
journalctl -u hermes-monitor.service -n 100 --no-pager
```

Replace `YOUR_USER` with your Linux username.

**You:** Where can i find the contents

**ChatGPT:** If you're asking **where to find the Hermes monitor code**, it depends where your Kalshi bot is installed.

On your Ubuntu NUC/server, start with:

```bash
cd ~
find . -name "hermes_position_monitor.py" 2>/dev/null
```

or

```bash
find /home -name "hermes_position_monitor.py" 2>/dev/null
```

That should return something like:

```text
/home/jake/kalshi-watch/hermes_position_monitor.py
```

Once you find it, view the contents with:

```bash
nano hermes_position_monitor.py
```

or

```bash
less hermes_position_monitor.py
```

or search for the new logic:

```bash
grep -n "placement" hermes_position_monitor.py
grep -n "side_bid" hermes_position_monitor.py
grep -n "marketable" hermes_position_monitor.py
```

If you're asking **where the logs are**, that depends on how you're running Hermes:

### If running manually

The output is usually just in the terminal:

```bash
python3 hermes_position_monitor.py
```

### If running via systemd

Check:

```bash
journalctl -u hermes-monitor.service -n 100 --no-pager
```

### If logging to a file

Look for code like:

```python
logging.FileHandler(...)
```

or search:

```bash
grep -R "FileHandler" .
grep -R "logging.basicConfig" .
```

Since your bot appears to be using SQLite heavily, I would also check whether Hermes is writing decisions into tables such as:

```text
sell_recommendations
position_lifecycle_metrics
trade_recommendations
```

You can inspect those with:

```bash
sqlite3 kalshi.db
.tables
```

Then:

```sql
SELECT *
FROM sell_recommendations
ORDER BY id DESC
LIMIT 20;
```

If you tell me:
- Where the bot is running (NUC, Proxmox VM, Ubuntu server, etc.)
- Whether you launch it manually, via cron, or via systemd

I can tell you exactly where to look for the logs and monitor output.

**You:** the contents of that command

**ChatGPT:** If you mean the command:

```bash
find . -name "hermes_position_monitor.py" 2>/dev/null
```

it doesn't show the contents of the file. It only tells you **where the file is located**.

Example output:

```text
./kalshi-watch/hermes_position_monitor.py
```

or

```text
/home/jake/kalshi-watch/hermes_position_monitor.py
```

Once you have the path, view the contents with:

```bash
cat /home/jake/kalshi-watch/hermes_position_monitor.py
```

or, better for a large file:

```bash
less /home/jake/kalshi-watch/hermes_position_monitor.py
```

or edit/view it:

```bash
nano /home/jake/kalshi-watch/hermes_position_monitor.py
```

If you mean the contents of the systemd service file I suggested, you can view it with:

```bash
cat /etc/systemd/system/hermes-monitor.service
```

or

```bash
sudo nano /etc/systemd/system/hermes-monitor.service
```

If you're referring to a different command, paste the exact command and I'll tell you what output to expect and how to inspect it.

**You:** What does this do Create service:

sudo nano /etc/systemd/system/hermes-monitor.service

Paste:

[Unit]
Description=Hermes Kalshi Position Monitor
After=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/home/YOUR_USER/kalshi-watch
EnvironmentFile=/home/YOUR_USER/kalshi-watch/.env
ExecStart=/usr/bin/python3 /home/YOUR_USER/kalshi-watch/hermes_position_monitor.py

Create timer:

sudo nano /etc/systemd/system/hermes-monitor.timer

Paste:

[Unit]
Description=Run Hermes Monitor every minute

[Timer]
OnBootSec=30
OnUnitActiveSec=60
Unit=hermes-monitor.service

[Install]
WantedBy=timers.target

Enable it:

sudo systemctl daemon-reload
sudo systemctl enable --now hermes-monitor.timer

Check it:

systemctl status hermes-monitor.timer
journalctl -u hermes-monitor.service -n 100 --no-pager

Replace YOUR_USER with your Linux username.

**ChatGPT:** What this does is turn Hermes into a **background service that automatically runs every minute**, even after reboots.

### 1. The Service File

```ini
[Unit]
Description=Hermes Kalshi Position Monitor
After=network-online.target
```

This says:

- This service is called "Hermes Kalshi Position Monitor"
- Don't run it until networking is up

---

```ini
[Service]
Type=oneshot
```

`oneshot` means:

```text
Start
→ Run hermes_position_monitor.py once
→ Exit
```

It does **not** stay running.

---

```ini
WorkingDirectory=/home/YOUR_USER/kalshi-watch
```

Equivalent to:

```bash
cd /home/YOUR_USER/kalshi-watch
```

before executing the script.

---

```ini
EnvironmentFile=/home/YOUR_USER/kalshi-watch/.env
```

Loads environment variables such as:

```text
KALSHI_API_KEY
DATABASE_PATH
TELEGRAM_BOT_TOKEN
```

before starting Hermes.

---

```ini
ExecStart=/usr/bin/python3 /home/YOUR_USER/kalshi-watch/hermes_position_monitor.py
```

Actually runs:

```bash
python3 hermes_position_monitor.py
```

---

### 2. The Timer File

This is the equivalent of a smarter cron job.

```ini
[Timer]
OnBootSec=30
```

Run 30 seconds after boot.

---

```ini
OnUnitActiveSec=60
```

Run again 60 seconds after the last run completed.

So:

```text
00:00 run Hermes
00:01 run Hermes
00:02 run Hermes
...
```

---

```ini
Unit=hermes-monitor.service
```

Each time the timer fires it executes:

```text
hermes-monitor.service
```

---

### 3. Enable It

```bash
sudo systemctl daemon-reload
```

Reload systemd after creating the files.

---

```bash
sudo systemctl enable --now hermes-monitor.timer
```

Two things happen:

```text
enable = start automatically after reboot
now    = start immediately
```

---

### 4. View Status

```bash
systemctl status hermes-monitor.timer
```

Shows:

```text
Active: active (waiting)
Next run: ...
```

---

```bash
journalctl -u hermes-monitor.service -n 100 --no-pager
```

Shows the last 100 log lines from Hermes.

Example:

```text
Running Hermes monitor

Position:
KXSAVEACT-27-JAN04

State: TIME_EXIT
Side: NO
Side bid: 5
Side ask: 6
Selected exit price: 5
Placement: marketable

Exit order submitted
```

---

### For Your Bot Specifically

Given what you've been building, I'd do this only after:

1. Open-position counting is fixed.
2. Exit escalation is tested.
3. Side-book normalization is verified.

Right now I'd first run manually:

```bash
cd ~/kalshi-watch
python3 hermes_position_monitor.py
```

and inspect the output.

Once you confirm it's behaving correctly, then move it to a systemd timer so it watches positions automatically every minute and sends alerts or exits without you having to start it manually.
