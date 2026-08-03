---
date: 2026-04-15
source: chatgpt
title: "Anti-Spam Policy Solution"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Mike O'Brien is working with two companies from Taiwan. Their emails are being blocked by Language Filter from policy. Should I whitelist their domain in Defender or is there a different preferred way to stop them from being blocked? ———-Best way to solve this without whitelisting

**ChatGPT:** Short answer: **don’t whitelist the domain** unless you absolutely have to. That’s the least controlled option and creates unnecessary risk.

Here’s the **better, Microsoft-recommended approach** for this exact situation:

---

## ✅ Best Practice (Targeted + Secure)

### 1. Adjust the Anti-Spam Policy (Language Filter)
The issue is coming from the **language filter**, not the sender’s reputation.

- Go to **Microsoft 365 Defender → Email & Collaboration → Policies & Rules → Threat Policies → Anti-spam**
- Find the policy applied to Mike O’Brien (likely Default or a custom one)
- Edit **Allowed languages**
  - Either:
    - Add the relevant language (e.g., Chinese)
    - OR remove strict language filtering if it’s too aggressive

👉 This fixes the root cause without opening the door to all mail from that domain.

---

### 2. Create a Mail Flow Rule (Preferred for Precision)
Instead of whitelisting a domain globally:

- Go to **Exchange Admin Center → Mail flow → Rules**
- Create a rule:
  - **If sender is** → specific email(s) or domain
  - **AND recipient is** → Mike O’Brien
  - **THEN** → set spam confidence level (SCL) to `-1` (bypass spam filtering)

✅ Why this is better:
- Only applies to **specific users + senders**
- Doesn’t weaken org-wide protections
- Fully auditable and reversible

---

### 3. Use Tenant Allow/Block List (Only if Needed)
In **Microsoft 365 Defender → Tenant Allow/Block List**

- Add sender/domain under **Allow**
- Set expiration (don’t make it permanent)

⚠️ This is stronger than a rule and bypasses more protections → use sparingly

---

## 🚫 What NOT to Do
- ❌ Don’t globally whitelist the domain in Defender (too broad)
- ❌ Don’t disable anti-spam protections org-wide
- ❌ Don’t allow all languages unless there’s a real business need

---

## 🔥 My Recommendation for You
Given your environment (Microsoft-focused, security-conscious):

👉 **Use a Mail Flow Rule scoped to Mike + those senders**  
👉 If more users need it later, expand the rule gradually  
👉 Only adjust language filter if this becomes a recurring pattern

---

If you want, I can write the **exact rule config (copy/paste ready)** based on their domains or emails.

**You:** What language might it be

**ChatGPT:** If the companies are from **entity["country","Taiwan","country in East Asia"]**, the language filter is almost certainly getting triggered by:

## 🇹🇼 Most Likely Language: Traditional Chinese
image_group{"aspect_ratio":"1:1","query":["traditional chinese text example taiwan email","taiwan chinese characters traditional vs simplified comparison","email written in traditional chinese business example","taiwan mandarin chinese characters"],"num_per_query":1}

- Taiwan uses **Traditional Chinese (繁體中文)**
- This is **different from Simplified Chinese** used in mainland China
- Microsoft Defender typically just labels it as:
  - **Chinese**
  - Sometimes not split between traditional vs simplified

---

## Other Possibilities (Less Likely)

### 1. English (with Chinese characters mixed in)
- Many Taiwanese companies send emails like:
  - English body + Chinese signature/footer
- Even a **small amount of Chinese text** can trigger the filter

### 2. Bilingual Emails
- Common format:
  - English paragraph
  - Then full Chinese translation below

### 3. Japanese (rare but possible)
- If the company has Japanese ties, you might see:
  - Kanji (looks similar to Chinese)
  - Hiragana/Katakana (distinct)

---

## 💡 How to Confirm (Fast)
Have Mike:
- Open one of the blocked emails in quarantine
- Look at:
  - **Preview text**
  - Or copy a line into Google → it’ll auto-detect language

---

## 🔥 What You Should Do
When adjusting Defender:
- Add **“Chinese”** to allowed languages (that covers it)
- You don’t need to worry about traditional vs simplified in policy

---

If you want, send me a screenshot of the quarantine details (or the message trace), and I’ll tell you exactly what triggered it so you can fix it cleanly without weakening security.
