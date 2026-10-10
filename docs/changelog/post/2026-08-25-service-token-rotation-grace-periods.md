---
url: https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/
title: Grace periods for service token rotation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.323735+00:00
---

# Grace periods for service token rotation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 25, 2026

## Grace periods for service token rotation

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.

The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.

For configuration instructions, refer to [Rotate service token secrets](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets).
