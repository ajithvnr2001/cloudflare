---
url: https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/
title: Agents SDK adds MCP Specification 2026-07-28 support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:05.213700+00:00
---

# Agents SDK adds MCP Specification 2026-07-28 support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 27, 2026

## Agents SDK adds MCP Specification 2026-07-28 support

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Agents SDK v0.20.0 adds client and server support for the [MCP 2026-07-28 release candidate ↗︎](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Workers can serve tools, prompts, resources, and elicitation without an MCP transport session or Durable Object. Agents can connect to both MCP 2026-07-28 servers and existing legacy servers.

#### Client support

The MCP client manager now uses `@modelcontextprotocol/client`. For each connection, it probes for MCP 2026-07-28 support with `server/discover`. If the server does not support the stateless protocol, the client continues with the legacy `initialize` handshake on the same connection. Existing `addMcpServer` calls do not need a protocol-version setting or separate clients for each protocol generation.

For stateless requests, elicitation uses `input_required` through multi-round-trip requests (MRTR). The legacy path uses the same form and URL handlers for pushed requests. The SDK collects input, retries the original operation, and resolves the original `callTool`, `getPrompt`, or `readResource` promise with its final result.

OAuth callbacks now validate issuer metadata through the v2 SDK. Discovery state and issuer-bound credentials persist across browser redirects and Durable Object hibernation.

#### Run stateless servers

`createMcpHandler` now accepts a factory that returns a server from `@modelcontextprotocol/server`. The factory creates an isolated server for each request.
    
    
    import { McpServer } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    
    function createServer() {
    	return new McpServer({ name: "example", version: "1.0.0" });
    }
    
    export default {
    	fetch(request, env, ctx) {
    		return createMcpHandler(createServer)(request, env, ctx);
    	},
    };
    
    
    import { McpServer } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    
    function createServer() {
    	return new McpServer({ name: "example", version: "1.0.0" });
    }
    
    export default {
    	fetch(request, env, ctx) {
    		return createMcpHandler(createServer)(request, env, ctx);
    	},
    } satisfies ExportedHandler;

The isolated `agents/mcp/server` entry keeps `McpAgent`, `WorkerTransport`, MCP client transports, and SDK v1 modules out of stateless server bundles.

The Workers wrapper validates present browser Origins, supports explicit delegation to trusted Origin middleware, and exposes request handling plus typed change notifications.

#### Backward compatibility

The same `createMcpHandler(createServer)(request, env, ctx)` route serves MCP 2026-07-28 clients and legacy clients that use stateless requests. You do not need separate routes or tool definitions for ordinary tools, prompts, and resources.

`McpAgent` is deprecated and feature-frozen. Migrate existing `McpAgent` servers to the stateless handler at your earliest convenience. If a server depends on protocol sessions, RPC, pushed server-to-client requests, standalone streams, or replay, use the [migration guide](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/) to design stateless equivalents and run both routes while clients transition.

#### Migrate existing SDK v1 servers

Upgrade the Agents SDK:

npmyarnpnpmbun
    
    
    npm i agents@latest
    
    
    yarn add agents@latest
    
    
    pnpm add agents@latest
    
    
    bun add agents@latest

Move ordinary SDK v1 server definitions into an SDK v2 factory and serve them with `createMcpHandler`. The handler's default legacy compatibility means most stateless deployments need only one route.

If an existing `McpAgent` server still needs sessionful features, add the stateless path beside it. Use `isLegacyRequest()` to send only legacy traffic to the existing route:
    
    
    import { isLegacyRequest } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    import { MyMcpAgent } from "./legacy-server";
    import { createServer } from "./server";
    
    const stateless = createMcpHandler(createServer, {
    	route: "/mcp",
    	legacy: "reject",
    });
    const legacy = MyMcpAgent.serve("/mcp");
    
    export default {
    	async fetch(request, env, ctx) {
    		if (await isLegacyRequest(request)) {
    			return legacy.fetch(request, env, ctx);
    		}
    		return stateless(request, env, ctx);
    	},
    };
    
    
    import { isLegacyRequest } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    import { MyMcpAgent } from "./legacy-server";
    import { createServer } from "./server";
    
    const stateless = createMcpHandler(createServer, {
    	route: "/mcp",
    	legacy: "reject",
    });
    const legacy = MyMcpAgent.serve("/mcp");
    
    export default {
    	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    		if (await isLegacyRequest(request)) {
    			return legacy.fetch(request, env, ctx);
    		}
    		return stateless(request, env, ctx);
    	},
    } satisfies ExportedHandler<Env>;

Migrate the remaining sessionful features, allow existing sessions to drain, then remove the legacy route. Refer to [Migrate to MCP SDK v2](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/) for package changes, compatibility limits, and rollout steps.

#### Deprecations in v0.20.0

This release deprecates the following Agents SDK APIs:

Deprecated API | Replacement | Status  
---|---|---  
`McpAgent` | Use an SDK v2 factory with `createMcpHandler` for stateless servers. Use the migration guide to replace stateful features before removing a legacy route. | Feature-frozen. No removal version is announced.  
`createMcpHandler(v1Server, options)` | Move the server to an SDK v2 factory and call `createMcpHandler(factory, options)`. Use `createLegacyMcpHandler` only as a temporary bridge for sessionful features. | Scheduled for removal in the next major version.  
`MCPClientManager.callTool(params, resultSchema, options)` and the equivalent `withX402Client` overload | Use `callTool(params, options)` or `callTool(confirm, params, options)`. | Compatibility overload. No removal version is announced.  
  
The MCP 2026-07-28 draft separately deprecates Roots, Sampling, Logging, the old HTTP+SSE transport, and Dynamic Client Registration.
