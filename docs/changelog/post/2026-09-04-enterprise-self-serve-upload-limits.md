---
url: https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/
title: Enterprise customers can self-serve CDN upload limits up to 5 GB \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.669792+00:00
---

# Enterprise customers can self-serve CDN upload limits up to 5 GB · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 4, 2026

## Enterprise customers can self-serve CDN upload limits up to 5 GB

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now configure a zone's CDN **Maximum Upload Size** up to 5 GB directly from the **Network** page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.

The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.

Refer to [Cache upload limits](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#upload-limits) and [Workers request body size limits](https://developers.cloudflare.com/workers/platform/limits/#request-and-response-limits) for details.
