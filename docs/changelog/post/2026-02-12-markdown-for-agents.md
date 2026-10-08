---
url: https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/
title: Introducing Markdown for Agents \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:36.589533+00:00
---

# Introducing Markdown for Agents · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 12, 2026

## Introducing Markdown for Agents

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's network now supports real-time content conversion at the source, for enabled zones using [content negotiation ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation) headers. When AI systems request pages from any website that uses Cloudflare and has Markdown for Agents enabled, they can express the preference for `text/markdown` in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.

Here is a curl example with the `Accept` negotiation header requesting this page from our developer documentation:
    
    
    curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \
      -H "Accept: text/markdown"

The response to this request is now formatted in markdown:
    
    
    HTTP/2 200
    date: Wed, 11 Feb 2026 11:44:48 GMT
    content-type: text/markdown; charset=utf-8
    content-length: 2899
    vary: accept
    x-markdown-tokens: 725
    content-signal: ai-train=yes, search=yes, ai-input=yes
    
    ---
    title: Markdown for Agents · Cloudflare Agents docs
    ---
    
    ## What is Markdown for Agents
    
    Markdown has quickly become the lingua franca for agents and AI systems
    as a whole. The format’s explicit structure makes it ideal for AI processing,
    ultimately resulting in better results while minimizing token waste.
    ...

Refer to our [developer documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) and our [blog announcement ↗︎](https://blog.cloudflare.com/markdown-for-agents/) for more details.
