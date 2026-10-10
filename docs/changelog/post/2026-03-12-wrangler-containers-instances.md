---
url: https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/
title: List Container instances with `wrangler containers instances` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.485847+00:00
---

# List Container instances with `wrangler containers instances` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 12, 2026

## List Container instances with `wrangler containers instances`

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new [`wrangler containers instances`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-instances) command lists all instances for a given Container application. This mirrors the instances view in the Cloudflare dashboard.

The command displays each instance's ID, name, state, location, version, and creation time:
    
    
    wrangler containers instances <APPLICATION_ID>

Use the `--json` flag for machine-readable output, which is also the default format in non-interactive environments such as CI pipelines.

For the full list of options, refer to the [`containers instances` command reference](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-instances).
