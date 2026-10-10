---
url: https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/
title: United States jurisdiction \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.419536+00:00
---

# United States jurisdiction · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 2, 2026

## United States jurisdiction

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can create D1 databases with the `us` jurisdiction. These databases run and persist data within the United States.

Use this option for regional data residency requirements.

To create a database with the `us` jurisdiction, run:
    
    
    npx wrangler@latest d1 create db-with-us-jurisdiction --jurisdiction=us

For more information, refer to [D1 data location](https://developers.cloudflare.com/d1/configuration/data-location/).
