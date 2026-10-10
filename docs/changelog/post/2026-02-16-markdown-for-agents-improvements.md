---
url: https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/
title: Content encoding support for Markdown for Agents and other improvements \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.638294+00:00
---

# Content encoding support for Markdown for Agents and other improvements · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-16-markdown-for-agents-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 16, 2026

## Content encoding support for Markdown for Agents and other improvements

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When AI systems request pages from any website that uses Cloudflare and has [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) enabled, they can express the preference for `text/markdown` in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.

This release adds the following improvements:

  * The origin response limit was raised from 1 MB to 2 MB (2,097,152 bytes).
  * We no longer require the origin to send the `content-length` header.
  * We now support content encoded responses from the origin.



If you haven’t enabled automatic Markdown conversion yet, visit the [AI Crawl Control ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/ai) section of the Cloudflare dashboard and enable **Markdown for Agents**.

Refer to our [developer documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) for more details.
