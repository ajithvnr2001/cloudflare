---
url: https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/
title: Worker version rollback limit increased from 10 to 100 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:22.637269+00:00
---

# Worker version rollback limit increased from 10 to 100 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 11, 2025

## Worker version rollback limit increased from 10 to 100

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-11-increased-version-rollback-limit/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The number of recent versions available for a Worker rollback has been increased from 10 to 100.

This allows you to:

  * Promote any of the 100 most recent versions to be the active deployment.

  * Split traffic using [gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/) between your latest code and any of the 100 most recent versions.




You can do this through the Cloudflare dashboard or with [Wrangler's rollback command](https://developers.cloudflare.com/workers/wrangler/commands/general/#rollback)

Learn more about [versioned deployments](https://developers.cloudflare.com/workers/versions-and-deployments/) and [rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/).
