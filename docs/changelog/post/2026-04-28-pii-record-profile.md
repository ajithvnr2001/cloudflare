---
url: https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/
title: Detect PII records with a new predefined DLP profile \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:39.371257+00:00
---

# Detect PII records with a new predefined DLP profile · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-28-pii-record-profile/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 28, 2026

## Detect PII records with a new predefined DLP profile

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare DLP now includes a new predefined profile designed to detect PII records that contain multiple types of personal data: **Personally Identifiable Information (PII) Record**.

Most predefined and custom DLP profiles match when any enabled detection entry matches. The **Personally Identifiable Information (PII) Record** profile is different. It only matches when at least three unique detection entries are found in close proximity, which reduces false positives from standalone values that may not represent a real PII record.

Detection entries included in the profile:

  * AU Passport Number
  * American Express Card Number
  * Diners Club Card Number
  * US Driver's License Number
  * Email Address
  * Full Name
  * US Mailing Address
  * Mastercard Card Number
  * US Individual Tax Identification Number (ITIN)
  * US Passport Number
  * US Phone Number
  * Union Pay Card Number
  * United States SSN Numeric Detection
  * Visa Card Number



For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).
