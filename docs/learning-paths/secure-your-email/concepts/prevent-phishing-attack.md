---
url: https://developers.cloudflare.com/learning-paths/secure-your-email/concepts/prevent-phishing-attack/
title: How Cloudflare prevents email-based phishing attacks \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:58.352171+00:00
---

# How Cloudflare prevents email-based phishing attacks · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-your-email/concepts/prevent-phishing-attack/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Your Email

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/secure-your-email/concepts/)
  5. /How Cloudflare prevents email-based phishing attacks



# How Cloudflare prevents email-based phishing attacks

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-your-email/concepts/prevent-phishing-attack/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Email security uses a variety of factors to determine whether a given email message attachment, URL, or specific network traffic is part of a phishing campaign.

These small pattern assessments are dynamic in nature. Cloudflare's automated systems use a combination of factors to clearly distinguish between a valid phishing campaign and benign traffic.

Cloudflare's vast global network detects emergent campaign infrastructure and aggregates data for Cloudflare's proprietary analytics engine SPARSE.

SPARSE uses AI and ML models to make effective detections for all types of malicious emails, including Business Email Compromise (BEC).

In a BEC attack, the attacker falsifies an email message to trick the victim into performing some action - most often transferring money to an account or location the attacker controls.

To detect these low volume, malicious emails that do not contain malware, malicious links or email attachments, Cloudflare analyzes the email thread, content, sentiment and context via message lexical analysis, subject analysis and sender analysis. Display names are also compared with known executive names for similarity using several matching models.

Refer to [How we detect phish](https://developers.cloudflare.com/email-security/reference/how-we-detect-phish/#sample-attack-types-and-detections) to learn more about additional attack types and detections.

[PreviousWhat is Email security?](https://developers.cloudflare.com/learning-paths/secure-your-email/concepts/what-is-email-security/)[NextProtect your organization from phishing attacks](https://developers.cloudflare.com/learning-paths/secure-your-email/concepts/protect-from-phishing-attacks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-your-email/concepts/prevent-phishing-attack.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
