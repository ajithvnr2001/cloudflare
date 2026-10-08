---
url: https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/
title: Increased concurrency, creation rate, and queued instance limits for Workflows instances \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:47.350530+00:00
---

# Increased concurrency, creation rate, and queued instance limits for Workflows instances · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 15, 2026

## Increased concurrency, creation rate, and queued instance limits for Workflows instances

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) limits have been raised to the following:

Limit | Previous | New  
---|---|---  
Concurrent instances (running in parallel) | 10,000 | 50,000  
Instance creation rate (per account) | 100/second per account | 300/second per account, 100/second per workflow  
Queued instances per Workflow 1 | 1 million | 2 million  
  
These increases apply to all users on the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/). Refer to the [Workflows limits documentation](https://developers.cloudflare.com/workflows/reference/limits/) for more details.

#### Footnotes

  1. Queued instances are instances that have been created or awoken and are waiting for a concurrency slot. ↩



