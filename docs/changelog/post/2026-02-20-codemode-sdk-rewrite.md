---
url: https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/
title: @cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:38.021124+00:00
---

# @cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 20, 2026

## @cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [`@cloudflare/codemode` ↗︎](https://www.npmjs.com/package/@cloudflare/codemode) package has been rewritten into a modular, runtime-agnostic SDK.

[Code Mode ↗︎](https://blog.cloudflare.com/code-mode/) enables LLMs to write and execute code that orchestrates your tools, instead of calling them one at a time. This can (and does) yield significant token savings, reduces context window pressure and improves overall model performance on a task.

The new `Executor` interface is runtime agnostic and comes with a prebuilt `DynamicWorkerExecutor` to run generated code in a [Dynamic Worker Loader](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/).

#### Breaking changes

  * Removed `experimental_codemode()` and `CodeModeProxy` — the package no longer owns an LLM call or model choice
  * New import path: `createCodeTool()` is now exported from `@cloudflare/codemode/ai`



#### New features

  * **`createCodeTool()`** — Returns a standard AI SDK `Tool` to use in your AI agents.
  * **`Executor` interface** — Minimal `execute(code, fns)` contract. Implement for any code sandboxing primitive or runtime.



#### `DynamicWorkerExecutor`

Runs code in a [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/). It comes with the following features:

  * **Network isolation** — `fetch()` and `connect()` blocked by default (`globalOutbound: null`) when using `DynamicWorkerExecutor`
  * **Console capture** — `console.log/warn/error` captured and returned in `ExecuteResult.logs`
  * **Execution timeout** — Configurable via `timeout` option (default 30s)



#### Usage
    
    
    import { createCodeTool } from "@cloudflare/codemode/ai";
    import { DynamicWorkerExecutor } from "@cloudflare/codemode";
    import { streamText } from "ai";
    
    const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
    const codemode = createCodeTool({ tools: myTools, executor });
    
    const result = streamText({
    	model,
    	tools: { codemode },
    	messages,
    });
    
    
    import { createCodeTool } from "@cloudflare/codemode/ai";
    import { DynamicWorkerExecutor } from "@cloudflare/codemode";
    import { streamText } from "ai";
    
    const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
    const codemode = createCodeTool({ tools: myTools, executor });
    
    const result = streamText({
    	model,
    	tools: { codemode },
    	messages,
    });

#### Wrangler configuration
    
    
    {
    	"worker_loaders": [{ "binding": "LOADER" }],
    }
    
    
    [[worker_loaders]]
    binding = "LOADER"

See the [Code Mode documentation](https://developers.cloudflare.com/agents/tools/codemode/) for full API reference and examples.

#### Upgrade
    
    
    npm i @cloudflare/codemode@latest
