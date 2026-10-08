---
url: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/
title: Dynamic Workers Playground \u00b7 Cloudflare Dynamic Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:11.048630+00:00
---

# Dynamic Workers Playground · Cloudflare Dynamic Workers docs

> Source: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/)
  3. /Examples
  4. /Dynamic Workers Playground



# Dynamic Workers Playground

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat this demo showsBundling code at runtimeCaching Dynamic WorkersObservability with Tail WorkersRunning locally

Try the Dynamic Workers [playground ↗︎](https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground) to write or import code from GitHub, bundle it at runtime, execute it in a Dynamic Worker, and view real-time logs.

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground)

![Dynamic Workers Playground UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2324,height=1610,format=webp/_astro/dw-playground.DqwBO_zZ.png)

## What this demo shows

  * **Runtime bundling** — Uses [`@cloudflare/worker-bundler` ↗︎](https://www.npmjs.com/package/@cloudflare/worker-bundler) to resolve npm dependencies and compile TypeScript inside a Worker
  * **Dynamic execution** — Loads bundled code into an isolated Dynamic Worker
  * **Caching** — Reuses previously bundled Workers when the source has not changed
  * **Real-time output** — Streams the response body, console logs, execution timing, and bundle metadata back to the client



## Bundling code at runtime

The playground uses [`@cloudflare/worker-bundler` ↗︎](https://www.npmjs.com/package/@cloudflare/worker-bundler) to compile TypeScript, resolve npm dependencies, and produce modules the Worker Loader can execute.

Pass source files and a `package.json` to `createWorker()`, which resolves dependencies and returns bundled modules ready to load as a Dynamic Worker:
    
    
    import { createWorker } from "@cloudflare/worker-bundler";
    
    const { mainModule, modules, warnings } = await createWorker({
    	files: {
    		"src/index.ts": userCode,
    		"package.json": JSON.stringify({
    			dependencies: { hono: "^4.0.0" },
    		}),
    	},
    	bundle: true,
    	minify: false,
    });
    
    
    import { createWorker } from "@cloudflare/worker-bundler";
    
    const { mainModule, modules, warnings } = await createWorker({
    	files: {
    		"src/index.ts": userCode,
    		"package.json": JSON.stringify({
    			dependencies: { hono: "^4.0.0" },
    		}),
    	},
    	bundle: true,
    	minify: false,
    });

## Caching Dynamic Workers

`env.LOADER.load()` creates a new Dynamic Worker on every call. To avoid re-bundling unchanged code, use `env.LOADER.get(id, callback)` instead. The runtime returns an existing Worker on a cache hit, or calls your callback to build one on a miss:
    
    
    const worker = env.LOADER.get(workerId, async () => {
    	// This callback only runs on cache miss
    	const { mainModule, modules } = await createWorker({ files });
    
    	return {
    		mainModule,
    		modules,
    		compatibilityDate: "2026-05-01",
    		tails: [contextExports.DynamicWorkerTail({ props: { workerId } })],
    	};
    });
    
    const response = await worker.getEntrypoint().fetch(request);
    
    
    const worker = env.LOADER.get(workerId, async () => {
    	// This callback only runs on cache miss
    	const { mainModule, modules } = await createWorker({ files });
    
    	return {
    		mainModule,
    		modules,
    		compatibilityDate: "2026-05-01",
    		tails: [
    			contextExports.DynamicWorkerTail({ props: { workerId } }),
    		],
    	};
    });
    
    const response = await worker.getEntrypoint().fetch(request);

In the playground, you can see this in action — run the same Dynamic Worker twice and the second request shows a cached result with 0ms cold start, since the build and load phases are skipped entirely.

## Observability with Tail Workers

When you run code in the playground, console output from the Dynamic Worker streams back to the browser in real time. Under the hood, this works through a [Tail Worker](https://developers.cloudflare.com/workers/observability/logs/tail-workers/) pipeline:

  1. A Tail Worker (`DynamicWorkerTail`) captures `console.log` output from the Dynamic Worker.
  2. Logs are forwarded to a `LogSession` Durable Object.
  3. The Durable Object streams them to the client over WebSocket.



To wire this up, include the Tail Worker in the `tails` array when creating the Dynamic Worker:
    
    
    const worker = env.LOADER.get(workerId, async () => ({
    	mainModule,
    	modules,
    	compatibilityDate: "2026-05-01",
    	tails: [contextExports.DynamicWorkerTail({ props: { workerId } })],
    }));
    
    
    const worker = env.LOADER.get(workerId, async () => ({
    	mainModule,
    	modules,
    	compatibilityDate: "2026-05-01",
    	tails: [contextExports.DynamicWorkerTail({ props: { workerId } })],
    }));

For more information on how to capture and stream logs from Dynamic Workers, refer to [Observability with Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/usage/observability/).

## Running locally

Clone the repo and start the dev server:
    
    
    npm install
    npm run dev

[PreviousDynamic Workers Starter](https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/)[NextCode Mode Example](https://developers.cloudflare.com/dynamic-workers/examples/codemode/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dynamic-workers/examples/dynamic-workers-playground.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
