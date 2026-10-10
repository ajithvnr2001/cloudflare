---
url: https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/
title: @cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.408811+00:00
---

# @cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 17, 2026

## @cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest releases of [`@cloudflare/codemode` ↗︎](https://www.npmjs.com/package/@cloudflare/codemode) add a new MCP barrel export, remove `ai` and `zod` as required peer dependencies from the main entry point, and give you more control over the sandbox.

#### New `@cloudflare/codemode/mcp` export

A new `@cloudflare/codemode/mcp` entry point provides two functions that wrap MCP servers with Code Mode:

  * **`codeMcpServer({ server, executor })`** — wraps an existing MCP server with a single `code` tool where each upstream tool becomes a typed `codemode.*` method.
  * **`openApiMcpServer({ spec, executor, request })`** — creates `search` and `execute` MCP tools from an OpenAPI spec with host-side request proxying and automatic `$ref` resolution.


    
    
    import { codeMcpServer } from "@cloudflare/codemode/mcp";
    import { DynamicWorkerExecutor } from "@cloudflare/codemode";
    
    const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
    
    // Wrap an existing MCP server — all its tools become
    // typed methods the LLM can call from generated code
    const server = await codeMcpServer({ server: upstreamMcp, executor });
    
    
    import { codeMcpServer } from "@cloudflare/codemode/mcp";
    import { DynamicWorkerExecutor } from "@cloudflare/codemode";
    
    const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
    
    // Wrap an existing MCP server — all its tools become
    // typed methods the LLM can call from generated code
    const server = await codeMcpServer({ server: upstreamMcp, executor });

#### Zero-dependency main entry point

**Breaking change in v0.2.0:** `generateTypes` and the `ToolDescriptor` / `ToolDescriptors` types have moved to `@cloudflare/codemode/ai`:
    
    
    // Before
    import { generateTypes } from "@cloudflare/codemode";
    
    // After
    import { generateTypes } from "@cloudflare/codemode/ai";
    
    
    // Before
    import { generateTypes } from "@cloudflare/codemode";
    
    // After
    import { generateTypes } from "@cloudflare/codemode/ai";

The main entry point (`@cloudflare/codemode`) no longer requires the `ai` or `zod` peer dependencies. It now exports:

Export | Description  
---|---  
`sanitizeToolName` | Sanitize tool names into valid JS identifiers  
`normalizeCode` | Normalize LLM-generated code into async arrow functions  
`generateTypesFromJsonSchema` | Generate TypeScript type definitions from plain JSON Schema  
`jsonSchemaToType` | Convert a single JSON Schema to a TypeScript type string  
`DynamicWorkerExecutor` | Sandboxed code execution via Dynamic Worker Loader  
`ToolDispatcher` | RPC target for dispatching tool calls from sandbox to host  
  
The `ai` and `zod` peer dependencies are now optional — only required when importing from `@cloudflare/codemode/ai`.

#### Custom sandbox modules

`DynamicWorkerExecutor` now accepts an optional `modules` option to inject custom ES modules into the sandbox:
    
    
    const executor = new DynamicWorkerExecutor({
    	loader: env.LOADER,
    	modules: {
    		"utils.js": `export function add(a, b) { return a + b; }`,
    	},
    });
    
    // Sandbox code can then: import { add } from "utils.js"
    
    
    const executor = new DynamicWorkerExecutor({
    	loader: env.LOADER,
    	modules: {
    		"utils.js": `export function add(a, b) { return a + b; }`,
    	},
    });
    
    // Sandbox code can then: import { add } from "utils.js"

#### Internal normalization and sanitization

`DynamicWorkerExecutor` now normalizes code and sanitizes tool names internally. You no longer need to call `normalizeCode()` or `sanitizeToolName()` before passing code and functions to `execute()`.

#### Upgrade
    
    
    npm i @cloudflare/codemode@latest

See the [Code Mode documentation](https://developers.cloudflare.com/agents/tools/codemode/) for the full API reference.
