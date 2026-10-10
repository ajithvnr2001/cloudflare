---
url: https://developers.cloudflare.com/changelog/post/2026-10-10-cloudflare-mcp-skills/
title: Cloudflare API MCP server serves Cloudflare skills \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T07:57:29.114497+00:00
---

# Cloudflare API MCP server serves Cloudflare skills · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-10-cloudflare-mcp-skills/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 10, 2026

## Cloudflare API MCP server serves Cloudflare skills

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#cloudflare-api-mcp-server) now serves [Cloudflare skills ↗︎](https://github.com/cloudflare/skills) through the [Skills over MCP extension ↗︎](https://modelcontextprotocol.io/extensions/skills/overview). MCP clients that support the extension discover the skills with `skills/list` and read their files at `skill://<name>/<path>`.

To use them, add `https://mcp.cloudflare.com/mcp` to an [MCP client that supports the extension ↗︎](https://modelcontextprotocol.io/extensions/client-matrix).
