---
url: https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/
title: Control where your Containers run with regional and jurisdictional placement \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:44.787305+00:00
---

# Control where your Containers run with regional and jurisdictional placement · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 5, 2026

## Control where your Containers run with regional and jurisdictional placement

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now specify placement constraints to control where your [Containers](https://developers.cloudflare.com/containers/) run.

Constraint | Values | Use case  
---|---|---  
`regions` | `ENAM`, `WNAM`, `EEUR`, `WEUR` | Geographic placement  
`jurisdiction` | `eu`, `fedramp` | Compliance boundaries  
  
Use `regions` to limit placement to specific geographic areas. Use `jurisdiction` to restrict containers to compliance boundaries — `eu` maps to European regions (EEUR, WEUR) and `fedramp` maps to North American regions (ENAM, WNAM).

Refer to [Containers placement](https://developers.cloudflare.com/containers/concepts/placement/) for more details.
