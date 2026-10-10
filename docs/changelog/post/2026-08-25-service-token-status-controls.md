---
url: https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/
title: Temporarily turn off Access service tokens \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.251259+00:00
---

# Temporarily turn off Access service tokens · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 25, 2026

## Temporarily turn off Access service tokens

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.

Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.

For configuration instructions, refer to [Turn a service token on or off](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off).
