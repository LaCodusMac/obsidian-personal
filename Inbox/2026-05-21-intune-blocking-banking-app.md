---
date: 2026-05-21
source: chatgpt
title: "Intune Blocking Banking App"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000fb8071fd811c21587d2d4a18", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 909303, "width": 709}
Is intune blocking this banking app?

**ChatGPT:** Yes — that message strongly suggests some kind of corporate device management policy is interfering, and entity["software","Microsoft Intune","Microsoft endpoint management platform"] is one of the most common causes on Android devices.

The wording:

> “This action is not allowed by your organization”

usually comes from:
- Intune App Protection Policies (MAM)
- A Work Profile restriction
- Microsoft Defender / Company Portal policies
- Samsung Knox enterprise policies
- Device Administrator restrictions

A few clues:
- The banking site is opening inside an embedded browser/webview (`login.mtb.com`)
- The error appears like a managed Android policy popup, not an M&T Bank error
- You mentioned earlier this machine came from work and you do IT support, so there’s a decent chance some management policies still exist on the phone or account

Things that commonly trigger this:
- Blocking copy/paste into financial apps
- Blocking opening external links from managed apps
- Preventing screenshots/downloads
- Preventing personal browser access from a work container
- Requiring access only from approved browsers like entity["mobile_app","Microsoft Edge","Microsoft mobile browser"]

Quick ways to verify if Intune is involved:

1. Check for these apps:
   - entity["mobile_app","Microsoft Intune Company Portal","Microsoft device management app"]
   - entity["mobile_app","Microsoft Defender","Microsoft security app"]
   - Knox Manage / Workspace ONE / MobileIron

2. Check Android settings:
   - Settings → Security & Privacy → Device admin apps
   - Settings → Accounts → Work profile
   - Settings → Apps → Company Portal

3. Try opening the bank site:
   - in Chrome directly
   - in Samsung Internet
   - outside any work profile/browser

4. Try disabling:
   - VPN
   - Work profile temporarily
   - “Open in work browser” options

5. If this is a former work-managed phone:
   - There may still be lingering MDM enrollment
   - Removing the work account alone sometimes does not fully remove policies

A very common scenario:
- You clicked the banking link from a managed Microsoft app (Outlook/Teams)
- Intune attempted to enforce “open only in managed browser”
- The banking page rejected or the policy blocked the action

If you want, I can also help you:
- determine whether your phone still has an active Intune enrollment
- fully remove old corporate management safely
- identify whether this is Intune vs Samsung Knox vs another MDM
- explain why it only happens on certain apps/sites like banking apps

**You:** This is on the personal side of an android owned by a employee at my company

**ChatGPT:** Then yes — this is very likely caused by an Intune App Protection Policy or Android work profile separation policy, even though the user is on the “personal” side.

What’s probably happening:
- The employee clicked/opened the bank site from a managed app like:
  - entity["mobile_app","Microsoft Outlook","Microsoft email app"]
  - entity["mobile_app","Microsoft Teams","Microsoft collaboration app"]
  - entity["mobile_app","Microsoft Edge","Microsoft mobile browser"]
- Intune is enforcing:
  - “Only open links in managed browser”
  - “Block unmanaged data transfer”
  - “Restrict personal-side interaction”

On Android work profile devices, even the personal side can hit these prompts if:
- the app initiating the action is managed
- the browser is unmanaged
- the policy blocks cross-profile launches

This does NOT necessarily mean the whole personal side is managed. More likely:
- the work profile is active
- the originating app is managed by Intune
- Conditional Launch/App Protection Policy is blocking the handoff

The exact popup style looks very consistent with Android Enterprise + Intune behavior.

Things to test immediately:
- Copy the URL manually into personal Chrome instead of tapping the link
- Open the link from a non-work app
- Long press → “Open in browser”
- Try disabling “Open web links in work profile”
- Try from Samsung Internet instead of Edge
- Check if the little “briefcase/work” icon appears on the app used to launch it

From an admin side in entity["software","Microsoft Intune","Microsoft endpoint management platform"], this is usually tied to:
- Managed browser requirement
- Data transfer policy
- “Send org data to other apps” restriction
- Work/personal profile boundary enforcement

If you want, I can also tell you:
- exactly which Intune policy setting usually causes this
- how to reproduce it intentionally
- how to exempt banking apps/sites safely
- whether this is happening at MAM level vs full MDM/work profile level

**You:** M&T app opens a browser for its login page

**ChatGPT:** That lines up almost perfectly with an Intune-managed app handoff issue.

What’s likely happening:

1. User opens the entity["mobile_app","M&T Mobile Banking","M&T Bank mobile app"] app
2. The app launches an external browser/webview for authentication
3. Android/Intune sees:
   - managed app → unmanaged browser transition
   - or cross-profile launch attempt
4. Policy blocks the action with:
   > “This action is not allowed by your organization”

This is especially common when:
- Outlook/Teams/Edge are managed with App Protection Policies
- The default browser is inside the work profile
- Edge is required as a managed browser
- Personal apps attempt to invoke a managed authentication session

The important part:
- The bank app itself probably is NOT blocked directly
- The browser/authentication redirect is what’s being blocked

I would specifically check:
- Default browser app
- Whether entity["mobile_app","Microsoft Edge","Microsoft mobile browser"] exists in both personal + work profiles
- If the work profile version is set as default
- Intune App Protection Policy:
  - “Restrict web content transfer”
  - “Open data into org apps only”
  - “Managed browser required”

A very common fix:
- Set personal Chrome/Samsung Internet as default browser on the personal side
- Clear defaults for Edge
- Launch the bank app again

Another good test:
- Temporarily pause the work profile
- Then open the M&T app again

If it suddenly works, you’ve basically confirmed it’s Intune/work-profile policy interaction rather than the banking app itself.

**You:** Shouldn’t personal apps not need edge?

**ChatGPT:** Correct — personal apps generally should *not* require entity["mobile_app","Microsoft Edge","Microsoft mobile browser"] just because a work profile exists.

That’s why this behavior points to one of these situations:

- The browser handling the login redirect is actually the *managed/work* browser
- Intune policy is intercepting the redirect incorrectly
- Android is trying to cross from personal app → work-managed browser
- The app protection policy is overly broad/misconfigured

On a properly configured Android Enterprise setup:
- Personal apps should stay personal
- Work policies should stay inside the work profile
- A personal banking app should normally authenticate with personal Chrome/Samsung Internet without issue

So the key issue is likely not:
> “M&T requires Edge”

but instead:
> “Android/Intune thinks the auth flow is entering the managed environment.”

This happens surprisingly often because:
- Edge became default browser globally
- Authenticator/Edge/Outlook registered link handlers
- Work profile Chrome is handling URLs
- Samsung “Open supported links” crosses profiles weirdly
- App Protection Policies are set to strict containment

The biggest clue:
If pausing the work profile makes the bank app work immediately, then the problem is almost certainly:
- browser association
- managed link handling
- or Intune MAM policy interaction

From an Intune admin perspective, I’d investigate:
- Managed browser policy
- App protection “Send org data to other apps”
- Android Enterprise cross-profile settings
- Whether Edge is deployed with “set as default browser”
- Conditional Access requiring approved client apps

But from the end-user side, the fastest fixes are usually:
1. Clear default browser
2. Set personal Chrome/Samsung Internet default
3. Clear M&T app cache
4. Pause work profile and retest
5. Remove managed Edge as default handler

This actually looks more like a policy side effect than intentional blocking of banking apps.

**You:** It says running in edge

**ChatGPT:** Then that’s almost certainly the issue.

The entity["mobile_app","M&T Mobile Banking","M&T Bank mobile app"] app is launching authentication inside managed entity["mobile_app","Microsoft Edge","Microsoft mobile browser"], and Intune policies attached to Edge are blocking the login flow.

So even though:
- the banking app is personal
- the device is BYOD
- the user is on the personal side

…the actual browser session is occurring inside the managed Edge context.

That explains the exact message.

Most likely causes:
- Edge is set as default browser
- Edge exists only as the managed/work version
- Edge has App Protection Policies applied
- Edge is configured to require organizational compliance rules

This is a pretty classic BYOD Intune side effect.

The cleanest fixes:
- Set personal Chrome or Samsung Internet as default browser
- Disable “Open supported links” for Edge
- Ensure the personal version of Edge is installed separately if needed
- Remove Edge as the default handler for banking/auth links

On Samsung:
Settings → Apps → Edge → Set as default → Clear defaults

Then:
Settings → Apps → Chrome (or Samsung Internet) → Set as default

Also potentially:
Settings → Work Profile → turn off “Use work apps for web links” if present.

If after changing the default browser the banking app works normally, you’ve basically confirmed:
- Intune is not directly blocking M&T
- Managed Edge policy containment is causing the failure during auth redirect.
