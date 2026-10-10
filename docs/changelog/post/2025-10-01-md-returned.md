---
url: https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/
title: Return markdown \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.166267+00:00
---

# Return markdown · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-01-md-returned/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2025

## Return markdown

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Users can now specify that they want to retrieve Cloudflare documentation as markdown rather than the previous HTML default. This can significantly reduce token consumption when used alongside Large Language Model (LLM) tools.
    
    
    curl https://developers.cloudflare.com/workers/ -H 'Accept: text/markdown'  -v

If you maintain your own site and want to adopt this practice using Cloudflare Workers for your own users you can follow the example [here ↗︎](https://github.com/cloudflare/cloudflare-docs/pull/25493).
