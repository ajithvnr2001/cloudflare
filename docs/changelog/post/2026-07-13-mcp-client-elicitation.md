---
url: https://developers.cloudflare.com/changelog/post/2026-07-13-mcp-client-elicitation/
title: Agents can respond to MCP elicitation requests \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:02.800907+00:00
---

# Agents can respond to MCP elicitation requests · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-13-mcp-client-elicitation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 13, 2026

## Agents can respond to MCP elicitation requests

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-13-mcp-client-elicitation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Agents connected to Model Context Protocol (MCP) servers with [`addMcpServer`](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/) can now handle [elicitation ↗︎](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation) requests.

Elicitation lets an MCP server request user input while it handles a tool call. Form mode collects structured, non-sensitive data. URL mode asks for consent before opening an out-of-band flow, such as third-party authorization or payment.
    
    
    sequenceDiagram
        participant User
        participant Agent as Agent (MCP client)
        participant Server as MCP server
        participant Browser
    
        Server->>Agent: elicitation/create
        Agent->>User: Show server, reason, and input or URL
        User->>Agent: Submit, open, decline, or cancel
        Agent->>Browser: Open URL after consent (URL mode)
        Agent->>Server: accept, decline, or cancel
        Server-->>Agent: Optional URL completion notification
    

Register a handler for each mode your Agent supports in `onStart()`:
    
    
    import { Agent } from "agents";
    
    export class MyAgent extends Agent {
    	onStart() {
    		this.mcp.configureElicitationHandlers({
    			form: (request, serverId) => this.forwardToUser(request, serverId),
    			url: (request, serverId) => this.forwardToUser(request, serverId),
    		});
    	}
    
    	forwardToUser(request, serverId) {
    		// Show the request in your UI and resolve after the user responds.
    		throw new Error(
    			`Implement elicitation for ${serverId}: ${request.params.message}`,
    		);
    	}
    }
    
    
    import { Agent } from "agents";
    import type { ElicitRequest, ElicitResult } from "agents/mcp";
    
    export class MyAgent extends Agent<Env> {
    	onStart() {
    		this.mcp.configureElicitationHandlers({
    			form: (request, serverId) => this.forwardToUser(request, serverId),
    			url: (request, serverId) => this.forwardToUser(request, serverId),
    		});
    	}
    
    	private forwardToUser(
    		request: ElicitRequest,
    		serverId: string,
    	): Promise<ElicitResult> {
    		// Show the request in your UI and resolve after the user responds.
    		throw new Error(
    			`Implement elicitation for ${serverId}: ${request.params.message}`,
    		);
    	}
    }

Connections advertise only the modes with configured handlers. An Agent without handlers advertises no elicitation capability, which lets the server use its fallback. The SDK stores the advertised modes with each MCP server registration so they survive Durable Object hibernation. Callback functions remain in memory and reattach when `onStart()` runs.

For implementation details and a browser forwarding pattern, refer to [MCP client elicitation](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/#elicitation). The [`mcp-client` ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp-client) and [`mcp-elicitation` ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation) examples implement both sides.

#### Upgrade

To update to this release:

npmyarnpnpmbun
    
    
    npm i agents@latest
    
    
    yarn add agents@latest
    
    
    pnpm add agents@latest
    
    
    bun add agents@latest
