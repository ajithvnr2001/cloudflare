---
url: https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/
title: Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.393449+00:00
---

# Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 22, 2026

## Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release reduces repeated MCP schema conversion and adds an opt-out for Think's automatic MCP tool exposure. It also lets non-AI-SDK hosts invoke the durable Code Mode runtime directly.

#### Control direct MCP tool exposure in Think

Agents SDK MCP clients now reuse converted input and output schemas while a live connection keeps the same tool catalog. This avoids converting every MCP JSON Schema to Zod again for each model turn.

`@cloudflare/think` also adds `includeMcpTools`. Set it to `false` when you expose MCP tools through Code Mode or another mechanism outside Think's automatic tool set:
    
    
    import { Think } from "@cloudflare/think";
    
    export class MyAgent extends Think {
    	includeMcpTools = false;
    	waitForMcpConnections = true;
    }
    
    
    import { Think } from "@cloudflare/think";
    
    export class MyAgent extends Think<Env> {
    	includeMcpTools = false;
    	waitForMcpConnections = true;
    }

This setting skips Think's automatic `getAITools()` call. MCP registration, restoration, discovery, raw catalog access, direct calls, and Code Mode connectors continue to work.

Use [`listTools()`](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/#thismcplisttools) when you only need the raw MCP catalog. For connector setup, refer to [Use MCP tools with Code Mode](https://developers.cloudflare.com/agents/tools/codemode/mcp/).

#### Invoke the Code Mode runtime without the AI SDK

`@cloudflare/codemode@latest` adds `execute()`, `search()`, and `describe()` to the durable runtime handle. MCP servers and other hosts can now execute code and discover connector methods without adapting the runtime to an AI SDK tool.
    
    
    const matches = await runtime.search("create issue");
    const docs = await runtime.describe(matches.results[0].path);
    const outcome = await runtime.execute({
    	code: `async () => github.create_issue({ title: "Bug" })`,
    });
    
    
    const matches = await runtime.search("create issue");
    const docs = await runtime.describe(matches.results[0].path);
    const outcome = await runtime.execute({
    	code: `async () => github.create_issue({ title: "Bug" })`,
    });

Search and describe results include `requiresApproval: true` for protected connector methods. Resolve a paused execution with the existing `approve()` and `reject()` methods.

For setup and exact method types, refer to [Create a durable Code Mode runtime](https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/) and the [Code Mode API reference](https://developers.cloudflare.com/agents/tools/codemode/api-reference/).

#### Upgrade

npmyarnpnpmbun
    
    
    npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
    
    
    yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
    
    
    pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
    
    
    bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
