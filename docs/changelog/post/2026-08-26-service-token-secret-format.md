---
url: https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/
title: Access service token secrets use a scannable format \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.061520+00:00
---

# Access service token secrets use a scannable format · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 26, 2026

## Access service token secrets use a scannable format

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format `cfast_[40 alphanumeric characters][8-character checksum]`. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.

Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same `CF-Access-Client-Id` and `CF-Access-Client-Secret` authentication headers.

For more information, refer to [Service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).
