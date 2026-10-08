---
url: https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/
title: Build a single-tool Code Mode MCP server \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:15.117958+00:00
---

# Build a single-tool Code Mode MCP server · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Model Context Protocol (MCP)](https://developers.cloudflare.com/agents/model-context-protocol/)

  4. /Guides
  5. /Build a single-tool Code Mode MCP server



# Build a single-tool Code Mode MCP server

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesWrap the serverProtect upstream operationsLimit results

Use `codeMcpServer()` to wrap an existing Model Context Protocol (MCP) server. MCP clients receive one `code` tool instead of every upstream tool.

The `code` tool contains generated type definitions for the upstream tools. Model-written JavaScript can call several tools, process their results, and return one focused value.

Caution

Code Mode is experimental and may have breaking changes. Use caution in production.

## Prerequisites

You need a Cloudflare Workers project and an existing `McpServer`.

`codeMcpServer()` currently returns an SDK v1 server. Serve it through the explicit legacy `createLegacyMcpHandler` API.

## Wrap the server

  1. Install Code Mode and the MCP dependencies:

npmyarnpnpmbun
         
         npm i @cloudflare/codemode agents @modelcontextprotocol/sdk zod
         
         yarn add @cloudflare/codemode agents @modelcontextprotocol/sdk zod
         
         pnpm add @cloudflare/codemode agents @modelcontextprotocol/sdk zod
         
         bun add @cloudflare/codemode agents @modelcontextprotocol/sdk zod

  2. Add a Worker Loader binding and the `nodejs_compat` compatibility flag:
         
         {
           "$schema": "./node_modules/wrangler/config-schema.json",
           "name": "codemode-mcp-server",
           "main": "src/server.ts",
           // Set this to today's date
           "compatibility_date": "2026-10-08",
           "compatibility_flags": [
             "nodejs_compat"
           ],
           "worker_loaders": [
             {
               "binding": "LOADER"
             }
           ]
         }
         
         name = "codemode-mcp-server"
         main = "src/server.ts"
         # Set this to today's date
         compatibility_date = "2026-10-08"
         compatibility_flags = ["nodejs_compat"]
         
         [[worker_loaders]]
         binding = "LOADER"

  3. Create the upstream server and pass it to `codeMcpServer()`:

src/server.jsjs
         
         import { DynamicWorkerExecutor } from "@cloudflare/codemode";
         import { codeMcpServer } from "@cloudflare/codemode/mcp";
         import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
         import { createLegacyMcpHandler } from "agents/mcp";
         import { z } from "zod";
         
         function createOrderServer() {
         	const server = new McpServer({
         		name: "orders",
         		version: "1.0.0",
         	});
         
         	server.registerTool(
         		"get_order",
         		{
         			description: "Get an order by ID",
         			inputSchema: {
         				orderId: z.string().describe("Order ID"),
         			},
         		},
         		async ({ orderId }) => ({
         			structuredContent: {
         				id: orderId,
         				status: "processing",
         			},
         			content: [
         				{
         					type: "text",
         					text: JSON.stringify({ id: orderId, status: "processing" }),
         				},
         			],
         		}),
         	);
         
         	return server;
         }
         
         export default {
         	async fetch(request, env, ctx) {
         		const upstream = createOrderServer();
         		const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
         		const server = await codeMcpServer({
         			server: upstream,
         			executor,
         		});
         
         		return createLegacyMcpHandler(server, { route: "/mcp" })(request, env, ctx);
         	},
         };

src/server.tsts
         
         import { DynamicWorkerExecutor } from "@cloudflare/codemode";
         import { codeMcpServer } from "@cloudflare/codemode/mcp";
         import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
         import { createLegacyMcpHandler } from "agents/mcp";
         import { z } from "zod";
         
         function createOrderServer() {
         	const server = new McpServer({
         		name: "orders",
         		version: "1.0.0",
         	});
         
         	server.registerTool(
         		"get_order",
         		{
         			description: "Get an order by ID",
         			inputSchema: {
         				orderId: z.string().describe("Order ID"),
         			},
         		},
         		async ({ orderId }) => ({
         			structuredContent: {
         				id: orderId,
         				status: "processing",
         			},
         			content: [
         				{
         					type: "text",
         					text: JSON.stringify({ id: orderId, status: "processing" }),
         				},
         			],
         		}),
         	);
         
         	return server;
         }
         
         export default {
         	async fetch(request, env, ctx): Promise<Response> {
         		const upstream = createOrderServer();
         		const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
         		const server = await codeMcpServer({
         			server: upstream,
         			executor,
         		});
         
         		return createLegacyMcpHandler(server, { route: "/mcp" })(
         			request,
         			env,
         			ctx,
         		);
         	},
         } satisfies ExportedHandler<Env>;

  4. Deploy the Worker:

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

  5. In an MCP client, connect to `https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/mcp`. Verify that the server exposes one tool named `code`.




The model can use the generated `codemode` namespace inside the `code` tool:
    
    
    async () => {
    	const order = await codemode.get_order({ orderId: "order-123" });
    	return { id: order.id, status: order.status };
    };

When an upstream tool returns `structuredContent`, Code Mode exposes that value directly. Text-only content is joined and parsed as JSON when possible. Upstream MCP errors become exceptions that model-written code can catch. Mixed text and binary content remains in its MCP result structure.

If you provide a custom `description`, use `{{types}}` where the generated TypeScript declarations should appear. Use `{{example}}` where the SDK should insert an example call based on the first upstream MCP tool. Both placeholders are optional.

## Protect upstream operations

`codeMcpServer()` does not provide durable approval for each upstream tool call. It invokes upstream handlers from inside the outer `code` tool.

Enforce authorization and any required per-operation approval in each upstream handler before applying side effects. Do not include credentials in tool results.

`DynamicWorkerExecutor` blocks external `fetch()` and `connect()` calls by default. Generated code can reach external systems only through the upstream MCP tools.

## Limit results

Model-written code can select, map, aggregate, or paginate upstream data before returning. This prevents large intermediate results from entering the model context.

The publisher limits the final MCP response to approximately 6,000 estimated tokens. A larger response is cut off and includes a `--- TRUNCATED ---` marker. This does not reduce work already performed by upstream tools.

To publish an OpenAPI service with separate `search` and `execute` tools, refer to [Build a search and execute MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/).

[PreviousMigrate to MCP SDK v2](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/)[NextBuild a search and execute MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/model-context-protocol/guides/build-codemode-mcp-server.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
