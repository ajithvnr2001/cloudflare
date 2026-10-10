---
url: https://developers.cloudflare.com/changelog/post/2026-10-09-markdown-for-agents-in-process-conversion/
title: More efficient Markdown for Agents conversion \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T07:57:29.185271+00:00
---

# More efficient Markdown for Agents conversion · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-09-markdown-for-agents-in-process-conversion/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 9, 2026

## More efficient Markdown for Agents conversion

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) now converts HTML with an in-process streaming engine at the edge. It processes content as it arrives instead of buffering the HTML response and sending it to a separate conversion service. This reduces conversion overhead and memory use.

This release also changes the conversion limit and response headers:

  * Conversion supports up to 6 MiB (6,291,456 bytes) of decompressed HTML, increased from 2 MiB (2,097,152 bytes). The limit applies after decompression, not to the compressed response size.
  * Converted responses no longer generate the `x-markdown-tokens` or `x-original-tokens` headers. Clients that use these values need to calculate token counts themselves.
  * `Content-Length` is removed from converted responses rather than recalculated, because the Markdown body is streamed.



For more information, refer to the [Markdown for Agents documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/).
