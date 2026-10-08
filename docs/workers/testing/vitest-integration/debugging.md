---
url: https://developers.cloudflare.com/workers/testing/vitest-integration/debugging/
title: Debugging \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:57.787586+00:00
---

# Debugging · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/vitest-integration/debugging/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)

  4. /[Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/)
  5. /Debugging



# Debugging

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/vitest-integration/debugging/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOpen inspector with VitestCustomize the inspector portSetup VS Code to use breakpoints

This guide shows you how to debug your Workers tests with Vitest and `@cloudflare/vitest-plugin`.

## Open inspector with Vitest

To start debugging, run Vitest with the following command and attach a debugger to port `9229`:
    
    
    vitest --inspect --no-file-parallelism

## Customize the inspector port

By default, the inspector will be opened on port `9229`. If you need to use a different port (for example, `3456`), you can run the following command:
    
    
    vitest --inspect=3456 --no-file-parallelism

Alternatively, you can define it in your Vitest configuration file:
    
    
    import { cloudflareTest } from "@cloudflare/vitest-plugin";
    import { defineConfig } from "vitest/config";
    
    export default defineConfig({
    	plugins: [
    		cloudflareTest({
    			// ...
    		}),
    	],
    	test: {
    		inspector: {
    			port: 3456,
    		},
    	},
    });

## Setup VS Code to use breakpoints

To setup VS Code for breakpoint debugging in your Worker tests, create a `.vscode/launch.json` file that contains the following configuration:
    
    
    {
    	"configurations": [
    		{
    			"type": "node",
    			"request": "launch",
    			"name": "Open inspector with Vitest",
    			"program": "${workspaceRoot}/node_modules/vitest/vitest.mjs",
    			"console": "integratedTerminal",
    			"args": ["--inspect=9229", "--no-file-parallelism"]
    		},
    		{
    			"name": "Attach to Workers Runtime",
    			"type": "node",
    			"request": "attach",
    			"port": 9229,
    			"cwd": "/",
    			"resolveSourceMapLocations": null,
    			"attachExistingChildren": false,
    			"autoAttachChildProcesses": false
    		}
    	],
    	"compounds": [
    		{
    			"name": "Debug Workers tests",
    			"configurations": [
    				"Open inspector with Vitest",
    				"Attach to Workers Runtime"
    			],
    			"stopAll": true
    		}
    	]
    }

Select **Debug Workers tests** at the top of the **Run & Debug** panel to open an inspector with Vitest and attach a debugger to the Workers runtime. Then you can add breakpoints to your test files and start debugging.

[PreviousIsolation and concurrency](https://developers.cloudflare.com/workers/testing/vitest-integration/isolation-and-concurrency/)[NextKnown issues](https://developers.cloudflare.com/workers/testing/vitest-integration/known-issues/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/vitest-integration/debugging.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
