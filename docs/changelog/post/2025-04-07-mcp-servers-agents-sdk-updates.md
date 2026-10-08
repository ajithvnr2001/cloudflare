---
url: https://developers.cloudflare.com/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/
title: Build MCP servers with the Agents SDK \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:08.658382+00:00
---

# Build MCP servers with the Agents SDK · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 7, 2025

## Build MCP servers with the Agents SDK

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Agents SDK now includes built-in support for building remote MCP (Model Context Protocol) servers directly as part of your Agent. This allows you to easily create and manage MCP servers, without the need for additional infrastructure or configuration.

The SDK includes a new `MCPAgent` class that extends the `Agent` class and allows you to expose resources and tools over the MCP protocol, as well as authorization and authentication to enable remote MCP servers.
    
    
    export class MyMCP extends McpAgent {
    	server = new McpServer({
    		name: "Demo",
    		version: "1.0.0",
    	});
    
    	async init() {
    		this.server.resource(`counter`, `mcp://resource/counter`, (uri) => {
    			// ...
    		});
    
    		this.server.tool(
    			"add",
    			"Add two numbers together",
    			{ a: z.number(), b: z.number() },
    			async ({ a, b }) => {
    				// ...
    			},
    		);
    	}
    }
    
    
    export class MyMCP extends McpAgent<Env> {
    	server = new McpServer({
    		name: "Demo",
    		version: "1.0.0",
    	});
    
    	async init() {
    		this.server.resource(`counter`, `mcp://resource/counter`, (uri) => {
    			// ...
    		});
    
    		this.server.tool(
    			"add",
    			"Add two numbers together",
    			{ a: z.number(), b: z.number() },
    			async ({ a, b }) => {
    				// ...
    			},
    		);
    	}
    }

See [the example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp) for the full code and as the basis for building your own MCP servers, and the [client example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp-client) for how to build an Agent that acts as an MCP client.

To learn more, review the [announcement blog ↗︎](https://blog.cloudflare.com/building-ai-agents-with-mcp-authn-authz-and-durable-objects) as part of Developer Week 2025.

#### Agents SDK updates

We've made a number of improvements to the [Agents SDK](https://developers.cloudflare.com/agents/), including:

  * Support for building MCP servers with the new `MCPAgent` class.
  * The ability to export the current agent, request and WebSocket connection context using `import { context } from "agents"`, allowing you to minimize or avoid direct dependency injection when calling tools.
  * Fixed a bug that prevented query parameters from being sent to the Agent server from the `useAgent` React hook.
  * Automatically converting the `agent` name in `useAgent` or `useAgentChat` to kebab-case to ensure it matches the naming convention expected by [`routeAgentRequest`](https://developers.cloudflare.com/agents/runtime/communication/routing/).



To install or update the Agents SDK, run `npm i agents@latest` in an existing project, or explore the `agents-starter` project:
    
    
    npm create cloudflare@latest -- --template cloudflare/agents-starter

See the full release notes and changelog [on the Agents SDK repository ↗︎](https://github.com/cloudflare/agents/blob/main/packages/agents/CHANGELOG.md) and
