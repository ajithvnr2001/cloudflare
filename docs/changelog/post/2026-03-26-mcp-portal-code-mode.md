---
url: https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/
title: Code Mode for MCP server portals \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:43.597661+00:00
---

# Code Mode for MCP server portals · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 26, 2026

## Code Mode for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support [Code Mode MCP server patterns](https://developers.cloudflare.com/agents/model-context-protocol/codemode/), a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.

To turn it off, edit the portal in **Access controls** > **AI controls** and turn off **Code Mode** under **Basic information**.

When Code Mode is active, the portal exposes a single `code` tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed `codemode.*` methods for each upstream tool. The generated code runs in an isolated [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) environment, keeping authentication credentials and environment variables out of the model context.

To use Code Mode, append `?codemode=search_and_execute` to your portal URL when connecting from an MCP client:
    
    
    https://<subdomain>.<domain>/mcp?codemode=search_and_execute

For more information, refer to [Code Mode](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode).
