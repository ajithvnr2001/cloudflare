---
url: https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/
title: Automated Cease and Desist templates for Brand Protection \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:57.091439+00:00
---

# Automated Cease and Desist templates for Brand Protection · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 10, 2026

## Automated Cease and Desist templates for Brand Protection

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**TL;DR:** Brand Protection now features an **Automated Cease & Desist (C&D)** workflow. When you discover an infringing domain hosted outside of Cloudflare, you can instantly generate, review, and download a custom-branded, pre-filled legal notice in seconds.

#### Why this matters

This update introduces a major shift from pure detection to actionable enforcement, eliminating the manual burden for your Trust & Safety and Legal teams:

  * **Instant WHOIS and Recipient Lookup:** We automatically scrape registrar data and WHOIS contact information (such as the registrant or registrar abuse email) behind the scenes, highlighting exactly where your notice needs to be sent
  * **Smart Template Automation:** We pre-fill your custom-branded templates with essential metadata, including the infringing domain, registrar name, and discovery date.
  * **Tailored Enforcement Tones:** Choose from three default layout strategies depending on the severity of the infrastructure match: 
    * _Exact Match:_ A formal demand for identical trademark infringements
    * _Similar Match:_ A standard notice optimized for typosquatting (one-character distance matches)
    * _Friendly Tone:_ An amicable initial outreach for potential unintentional or accidental infringements
  * **Full Editing Control:** Before creating the final PDF, a real-time review screen allows you to fine-tune the messaging, modify placeholders, and ensure your text aligns perfectly with internal legal standards



#### How it works

When reviewing a malicious domain match inside your dashboard, your enforcement path splits depending on where the attacker is located:

  1. **On the Cloudflare Network:** If the domain uses Cloudflare’s network or registrar, trigger our existing integrated abuse reporting flow with one click.
  2. **Hosted Elsewhere:** If the domain is hosted on an external provider, click the **Generate C &D Letter** option to launch the new document builder, pick your template, verify the auto-populated recipient data, and download your finalized PDF.



You can manage your templates and enforce matches by going to the **Cloudflare Dashboard > Application Security > Brand Protection** and selecting your detected Brand Protection matches. For more information, read the [Brand Protection documentation](https://developers.cloudflare.com/security-center/brand-protection/).

> **Note:** Cloudflare does not represent you and cannot provide you with legal advice. Only you can decide whether your rights have been infringed, whether a cease and desist letter is appropriate, and what that letter should say.
