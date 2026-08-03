---
date: 2026-06-09
source: chatgpt
title: "Telegram notification bug"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** The full run did print an existing Telegram send failed: can't parse entities message from a notifier path, but the
  suite still passed.

**ChatGPT:** That means your tests passed, but you still have a **real production bug in the Telegram notification formatter**.

Telegram is rejecting one notification because the message contains characters that conflict with `parse_mode`, usually Markdown or HTML.

Most likely causes:

- `_`, `*`, `[`, `]`, `(`, `)`, `~`, `` ` ``, `>`, `#`, `+`, `-`, `=`, `|`, `{`, `}`, `.`, `!`
- market titles with special chars
- ticker names with hyphens
- pasted JSON / traces
- `<`, `>`, or `&` if using HTML mode
- notification body mixing Markdown formatting with unescaped dynamic values

What I would do now:

1. **Find the notifier path**
   ```bash
   grep -R "parse_mode" -n .
   grep -R "send_message" -n telegram trading services position_monitor
   grep -R "Telegram send failed" -n .
   ```

2. **Centralize Telegram escaping**
   
   You want one safe helper, probably in `telegram/formatting.py` or `telegram/bot.py`.

   For MarkdownV2:

   ```python
   def escape_markdown_v2(text: object) -> str:
       value = "" if text is None else str(text)
       escape_chars = r"_*[]()~`>#+-=|{}.!"
       return "".join("\\" + c if c in escape_chars else c for c in value)
   ```

3. **Escape only dynamic values, not the whole template**

   Good:

   ```python
   msg = (
       f"*Trade submitted*\n"
       f"Ticker: `{escape_markdown_v2(ticker)}`\n"
       f"Market: {escape_markdown_v2(market_title)}\n"
       f"Reason: {escape_markdown_v2(reason)}"
   )
   ```

   Bad:

   ```python
   msg = escape_markdown_v2(full_message)
   ```

   Escaping the full message breaks your intentional Markdown formatting.

4. **Add a fallback send path**

   Your notifier should not fail entirely because formatting broke.

   ```python
   def send_telegram_message(text: str, parse_mode: str | None = "MarkdownV2") -> None:
       try:
           _send(text, parse_mode=parse_mode)
       except Exception as exc:
           if "can't parse entities" in str(exc):
               _send(text, parse_mode=None)
           else:
               raise
   ```

5. **Add a regression test**

   Test with exactly the kind of Kalshi strings that will break Telegram:

   ```python
   def test_telegram_notification_escapes_market_text():
       text = format_trade_notification(
           ticker="KXUSAIRANAGREEMENT-27-26JUN",
           market_title="Will Iran-Israel agreement happen before Jun 26?",
           reason="Narrative repricing: price moved +7¢ (spread ok)"
       )

       assert "\\-" in text or "KXUSAIRANAGREEMENT" in text
       assert "Iran" in text
   ```

My recommendation: **fix this before adding more notification types**. Your new explainability notifications will include market names, JSON-ish traces, percentages, arrows, parentheses, and tickers, so this bug will become much more common.

**You:** I centralized the Markdown escaping in kalshi-watch/telegram_notifier.py:1 with escape_markdown(...) and routed the
  existing formatter helpers through it:

  - kalshi-watch/demo_trader.py:12
  - kalshi-watch/reporting/reporter.py:8

  That means dynamic values like market titles, tickers, reasons, and narrative text now use one escape path instead of
  the previous fragmented helpers.

  I also kept the plain-text fallback in the notifier and added a regression test in kalshi-watch/
  test_telegram_notifier.py:6 for problematic dynamic text containing brackets, parentheses, underscores, asterisks, and
  backticks.

  Verification:

  - venv/bin/python -m unittest -v test_telegram_notifier.py test_reporter.py test_telegram_bot.py
  - 12/12 tests passed

  One note: you still see Telegram send failed: can't parse entities printed during the notifier test run because that
  test intentionally mocks a Telegram 400 response to verify the fallback path. That print is from the simulated failure
  case, not a failing test.

**ChatGPT:** Good fix. That is exactly the right direction.

The key thing: **the remaining “Telegram send failed” line is acceptable only because it is coming from a deliberate fallback test**. I would still clean it up so future test output does not look scary.

What I would do next:

### 1. Silence expected fallback noise during tests

Right now the test passes, but the output makes it look like something is wrong. Change the notifier so logging/printing is injectable or uses Python logging instead of raw `print`.

Preferred pattern:

```python
import logging

logger = logging.getLogger(__name__)

# instead of:
print("Telegram send failed:", exc)

# use:
logger.warning("Telegram send failed: %s", exc)
```

Then in the regression test:

```python
with self.assertLogs("telegram_notifier", level="WARNING"):
    send_telegram_message(...)
```

Or, if you do not care about asserting the warning:

```python
with self.assertLogs("telegram_notifier", level="WARNING"):
    ...
```

This keeps the test intentional without making normal test output look broken.

### 2. Add one “real notification shape” test

Your current test proves escaping works on nasty characters. Add one test using your future explainability format:

```text
Ticker:
KXUSAIRANAGREEMENT-27-26JUN

Market:
Will Iran-Israel agreement happen before Jun 26?

Decision:
BUY YES

Signal:
Narrative Repricing

Evidence:
✓ News narrative detected
✓ Price moved +7¢
✓ Spread acceptable

Risk:
✓ Position limit passed
✓ Exposure limit passed
```

That catches the actual style you want to use going forward.

### 3. Make sure you are not double-escaping

This is the only thing I would watch carefully. Since you routed `demo_trader.py` and `reporting/reporter.py` through the same helper, make sure no dynamic value is escaped twice.

Bad symptom:

```text
KXUSAIRANAGREEMENT\\-27\\-26JUN
```

Instead of:

```text
KXUSAIRANAGREEMENT\-27\-26JUN
```

If messages look ugly in Telegram, this is probably why.

### 4. Run full discovery once

Since this touches shared notification formatting:

```bash
cd /home/carlthellama/kalshi-watch
./venv/bin/python -m unittest discover -p 'test_*.py'
```

If that passes, I would commit it.

```bash
git status
git add telegram_notifier.py demo_trader.py reporting/reporter.py test_telegram_notifier.py
git commit -m "Centralize Telegram markdown escaping"
```

Then your next pass should be the **new notification templates**: position watch, trade explainability, narrative checks, and opportunity summaries. This escaping work is now the foundation for those.
