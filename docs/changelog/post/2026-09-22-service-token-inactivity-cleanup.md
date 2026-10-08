---
url: https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/
title: Automatically manage inactive Access service tokens \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:15.489837+00:00
---

# Automatically manage inactive Access service tokens · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 22, 2026

## Automatically manage inactive Access service tokens

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access administrators can now automatically disable or delete inactive service tokens. Administrators can set an inactivity period from 30 to 365 days and choose what Access does when a token reaches that limit.

To be eligible for cleanup, a token must be older than the configured period, must not have successfully authenticated during that period, and must not be directly referenced by an Access policy rule. Cleanup runs gradually in the background, so eligible tokens may not be disabled or deleted immediately.

For configuration instructions, refer to [Manage inactive service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#manage-inactive-service-tokens).
