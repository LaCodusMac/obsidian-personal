---
date: 2026-07-17
source: chatgpt
title: "Email Relay Access Denied"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Opportunity

Error Details
Error:
*550 5.7.367 Remote server returned not permitted to relay -> 554 5.7.1 <info@longislanddoorco.com>: Relay access denied*
Message rejected by:
fwd1.porkbun.com

Notification Details
Sent by:
*SJ0PR02MB11769.namprd02.prod.outlook.com*

Message Hops
HOP
TIME \(UTC\)
FROM
TO
WITH
RELAY TIME
1
7/17/2026
11:44:07 AM
DS0PR02MB9483.namprd02.prod.outlook.com
DS0PR02MB9483.namprd02.prod.outlook.com
mapi
\*

**ChatGPT:** I’m tracing where the rejection occurred and what configuration is most likely responsible. The key clue is that Porkbun—not Microsoft 365—issued the relay denial.

**ChatGPT:** This is a **recipient-side email routing problem**, not an Outlook issue.

Microsoft 365 successfully sent the message outward, but **Porkbun’s forwarding server (`fwd1.porkbun.com`) refused mail for `info@longislanddoorco.com`**:

> `554 5.7.1 Relay access denied`

That usually means one of these:

1. `info@longislanddoorco.com` is not currently configured as a valid Porkbun forwarding address.
2. The forwarding address was deleted, disabled, misspelled, or its destination is invalid.
3. The domain’s MX records still point to Porkbun even though email was moved to Microsoft 365 or another provider.
4. The domain uses Porkbun forwarding, but its forwarding/DNS configuration is broken.

Porkbun’s forwarding service only accepts mail for addresses explicitly configured in its Email Forwarding section. citeturn703706search1turn703706search3

## What to check

In the Porkbun account for `longislanddoorco.com`:

1. Open **Domain Management**.
2. Select the envelope under **Email**.
3. Under **Porkbun Email Forwarding**, verify that this exact address exists:
   `info@longislanddoorco.com`
4. Confirm that it forwards to a valid destination mailbox.
5. If it is already present, delete and recreate the forwarding entry, then test again.

Also inspect the domain’s MX records. If the company is supposed to use Microsoft 365, the MX record should point to the Microsoft 365 tenant—not `fwd1.porkbun.com`. Porkbun has separate DNS configuration instructions for domains hosted in Microsoft 365. citeturn703706search20

## Ticket summary

**Root cause:** The receiving domain’s Porkbun mail-forwarding server rejected the recipient as an unauthorized relay. The `info@longislanddoorco.com` forwarding alias or MX routing is likely missing or misconfigured.

**Action:** The administrator of `longislanddoorco.com` needs to correct the Porkbun forwarding entry or update the domain’s MX records. Retrying from Outlook will not resolve it until the recipient configuration is fixed. Microsoft identifies 5.7.367 as a rejection by the downstream or non-Microsoft gateway during forwarding/relay. citeturn703706search9turn703706search28
