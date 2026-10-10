---
url: https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/
title: Cloudflare MCP servers support the new MCP 2026-07-28 Specification \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.179661+00:00
---

# Cloudflare MCP servers support the new MCP 2026-07-28 Specification · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 28, 2026

## Cloudflare MCP servers support the new MCP 2026-07-28 Specification

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's [product-specific MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers) now support the new MCP 2026-07-28 Specification. Each request runs on a fresh stateless server without an MCP protocol session or protocol-specific Durable Object.

The `/mcp` endpoint also accepts stateless requests from 2025 Streamable HTTP clients. Most clients can reconnect without configuration changes.

Use `/mcp` for new connections. Historical `/sse` URLs continue to work as aliases for the same Streamable HTTP handler, but they no longer serve the deprecated HTTP+SSE transport. If a client forces SSE transport, change it to Streamable HTTP or automatic transport detection.
