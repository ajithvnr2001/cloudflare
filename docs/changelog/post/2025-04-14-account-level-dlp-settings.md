---
url: https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/
title: DLP account-level settings \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.927670+00:00
---

# DLP account-level settings · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-14-account-level-dlp-settings/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 14, 2026

## DLP account-level settings

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Account-level DLP settings are now available** in Cloudflare One. You can now configure advanced DLP settings at the account level, including OCR, AI context analysis, and payload masking. This provides consistent enforcement across all DLP profiles and simplifies configuration management.

Key changes:

  * **Consistent enforcement** : Settings configured at the account level apply to all DLP profiles
  * **Simplified migration** : Settings enabled on any profile are automatically migrated to account level
  * **Deprecation notice** : Profile-level advanced settings will be deprecated in a future release



**Migration details:**

During the migration period, if a setting is enabled on any profile, it will automatically be enabled at the account level. This means profiles that previously had a setting disabled may now have it enabled if another profile in the account had it enabled.

Settings are evaluated using OR logic - a setting is enabled if it is turned on at either the account level or the profile level. However, profile-level settings cannot be enabled when the account-level setting is off.

For more details, refer to the [DLP settings documentation](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/).
