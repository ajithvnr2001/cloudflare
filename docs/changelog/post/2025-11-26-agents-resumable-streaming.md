---
url: https://developers.cloudflare.com/changelog/post/2025-11-26-agents-resumable-streaming/
title: Agents SDK v0.2.24 with resumable streaming, MCP improvements, and schedule fixes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:30.595211+00:00
---

# Agents SDK v0.2.24 with resumable streaming, MCP improvements, and schedule fixes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-26-agents-resumable-streaming/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 26, 2025

## Agents SDK v0.2.24 with resumable streaming, MCP improvements, and schedule fixes

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-26-agents-resumable-streaming/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of [@cloudflare/agents ↗︎](https://github.com/cloudflare/agents) brings resumable streaming, significant MCP client improvements, and critical fixes for schedules and Durable Object lifecycle management.

#### Resumable streaming

`AIChatAgent` now supports resumable streaming, allowing clients to reconnect and continue receiving streamed responses without losing data. This is useful for:

  * Long-running AI responses
  * Users on unreliable networks
  * Users switching between devices mid-conversation
  * Background tasks where users navigate away and return
  * Real-time collaboration where multiple clients need to stay in sync



Streams are maintained across page refreshes, broken connections, and syncing across open tabs and devices.

#### Other improvements

  * Default JSON schema validator added to MCP client
  * [Schedules ↗︎](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/) can now safely destroy the agent



#### MCP client API improvements

The `MCPClientManager` API has been redesigned for better clarity and control:

  * **New`registerServer()` method**: Register MCP servers without immediately connecting
  * **New`connectToServer()` method**: Establish connections to registered servers
  * **Improved reconnect logic** : `restoreConnectionsFromStorage()` now properly handles failed connections


    
    
    // Register a server to Agent
    const { id } = await this.mcp.registerServer({
    	name: "my-server",
    	url: "https://my-mcp-server.example.com",
    });
    
    // Connect when ready
    await this.mcp.connectToServer(id);
    
    // Discover tools, prompts and resources
    await this.mcp.discoverIfConnected(id);

The SDK now includes a formalized `MCPConnectionState` enum with states: `idle`, `connecting`, `authenticating`, `connected`, `discovering`, and `ready`.

#### Enhanced MCP discovery

MCP discovery fetches the available tools, prompts, and resources from an MCP server so your agent knows what capabilities are available. The `MCPClientConnection` class now includes a dedicated `discover()` method with improved reliability:

  * Supports cancellation via AbortController
  * Configurable timeout (default 15s)
  * Discovery failures now throw errors immediately instead of silently continuing



#### Bug fixes

  * Fixed a bug where [schedules ↗︎](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/) meant to fire immediately with this.schedule(0, ...) or `this.schedule(new Date(), ...)` would not fire
  * Fixed an issue where schedules that took longer than 30 seconds would occasionally time out
  * Fixed SSE transport now properly forwards session IDs and request headers
  * Fixed AI SDK stream events conversion to UIMessageStreamPart



#### Upgrade

To update to the latest version:
    
    
    npm i agents@latest
