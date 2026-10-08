---
url: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/
title: Detect Cloudflare API tokens with DLP \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:46.326015+00:00
---

# Detect Cloudflare API tokens with DLP · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 14, 2026

## Detect Cloudflare API tokens with DLP

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The **Credentials and Secrets** DLP profile now includes three new predefined entries for detecting Cloudflare API credentials:

Entry name | Token prefix | Detects  
---|---|---  
Cloudflare User API Key | `cfk_` | User-scoped API keys  
Cloudflare User API Token | `cfut_` | User-scoped API tokens  
Cloudflare Account Owned API Token | `cfat_` | Account-scoped API tokens  
  
These detections target the new [Cloudflare API credential format](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/), which uses a structured prefix and a CRC32 checksum suffix. The identifiable prefix makes it possible to detect leaked credentials with high confidence and low false positive rates — no surrounding context such as `Authorization: Bearer` headers is required.

Credentials generated before this format change will not be matched by these entries.

#### How to enable Cloudflare API token detections

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **DLP** > **DLP Profiles**.
  2. Select the **Credentials and Secrets** profile.
  3. Turn on one or more of the new Cloudflare API token entries.
  4. Use the profile in a Gateway HTTP policy to log or block traffic containing these credentials.



Example policy:

Selector | Operator | Value | Action  
---|---|---|---  
DLP Profile | in | _Credentials and Secrets_ | Block  
  
You can also enable individual entries to scope detection to specific credential types — for example, enabling **Account Owned API Token** detection without enabling **User API Key** detection.

For more information, refer to [predefined DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).
