---
url: https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/
title: MCP server portals \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.572201+00:00
---

# MCP server portals · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 26, 2025

## MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

![MCP server portal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1557,height=420,format=webp/_astro/mcp-server-portal.BOKqTCoI.png)

An [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) centralizes multiple Model Context Protocol (MCP) servers onto a single HTTP endpoint. Key benefits include:

  * **Streamlined access to multiple MCP servers** : MCP server portals support both unauthenticated MCP servers as well as MCP servers secured using any third-party or custom OAuth provider. Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.
  * **Customized tools per portal** : Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.
  * **Observability** : Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal.



This is available in an open beta for all customers across all plans! For more information check out our [blog ↗︎](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) for this release.
