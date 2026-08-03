---
date: 2026-06-24
source: chatgpt
title: "Enterprise Response to Lost Phone"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Last Thursday Gary accidently left his work phone onsite at Fayerweather Hall Dartmouth College. When he realized he left it, he called it and one of the contractors answered it and told Gary they would leave it in the trailer for him. Upon arrival yesterday his phone was MIA. He will keep on the lookout for it this Thursday and Friday when he is back, but if it does not turn up, he will either need a replacement or opt for using his personal with a stipend. Gary can speak to which he prefers, and update this thread at the end of the week if the phone turns up

What would be an enterprise companies response to
This

**ChatGPT:** For an enterprise-style response, you'd typically acknowledge the issue, clarify next steps, assign ownership, and set expectations. Something like:

:::writing{variant="chat_message" id="58371"}
Thanks for the update.

Given the circumstances, let's continue monitoring for the device through the end of the week. Gary, please provide an update after your Thursday/Friday site visits regarding whether the phone has been recovered.

If the device is not located, we can evaluate replacement options at that time. This may include issuing a replacement company device or reviewing a BYOD (Bring Your Own Device) arrangement with an appropriate stipend, depending on business needs and your preference.

In the meantime, please notify IT if there is any concern that the device may have been lost or accessed by an unauthorized party so appropriate security measures can be taken.

We'll revisit next steps once we have a final status update.
:::

A larger company's response would also usually include a note to IT/security to verify the phone's management status, location tracking, and whether a remote lock or wipe may be necessary if it remains missing.

**You:** Should I remote lock or wipe. The phone has no location

**ChatGPT:** If this is a company-managed phone and its location is unknown, I'd generally recommend:

1. **Remote lock it immediately** if that option is available.
   - Low risk.
   - Preserves the chance of recovery.
   - Prevents casual access if someone finds it.

2. **Attempt recovery for a defined period** (e.g., through the end of this week, since Gary has a reasonable lead that it may still be onsite).

3. **Remote wipe only if:**
   - The phone is confirmed stolen.
   - Recovery efforts fail after the agreed period.
   - The device contains sensitive company data and your organization's policy requires it.
   - The device begins showing suspicious activity (new sign-ins, MDM alerts, etc.).

Since a contractor answered the phone and said they would leave it in the trailer, this currently sounds more like a misplaced device than a confirmed theft. In that scenario, locking it now and delaying the wipe until after Gary checks Thursday/Friday is usually the balanced approach.

A few questions for your IT decision:
- Is it enrolled in Intune or another MDM?
- Is BitLocker/File-Based Encryption enabled (most modern iPhones and Androids are encrypted by default)?
- Does it require a PIN/passcode?
- Does it have access to email, Teams, VPN, or other sensitive systems?

If it's Intune-managed with a passcode and encryption enabled, the risk is significantly lower, which supports **lock now, wipe later if not recovered**.

**You:** Intune with app protection and PIN

**ChatGPT:** With **Intune management, App Protection Policies, and a PIN**, I'd lean toward:

**✔ Remote lock now**
- Prevents access if someone has the device.
- Doesn't destroy evidence or recovery options.
- Aligns with most corporate security practices for a misplaced device.

**✖ Don't wipe yet**
- There is a credible recovery path (contractor answered the phone and claimed it was left in the trailer).
- Gary is returning to the site within days.
- App Protection Policies already help protect company data inside managed apps.
- The device is likely encrypted and protected by the PIN.

I would also:
- Verify the device is still checking into Intune (if possible).
- Review recent sign-in activity for unusual access.
- Consider requiring a password reset if you have any concern the PIN was compromised.
- Set a firm deadline (e.g., end of Friday) for recovery before deciding whether to retire/wipe the device and issue a replacement.

From a security perspective, this currently sounds like a **lost device with a reasonable chance of recovery**, not a confirmed compromise. Most enterprise IT teams would **lock immediately, monitor, and wipe only if it remains unrecovered or evidence of compromise appears**.
