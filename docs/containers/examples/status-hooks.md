---
url: https://developers.cloudflare.com/containers/examples/status-hooks/
title: Monitor container lifecycle \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:35.545305+00:00
---

# Monitor container lifecycle · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/examples/status-hooks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Examples
  4. /Monitor container lifecycle



# Monitor container lifecycle

Execute Workers code in reaction to Container status changes

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/examples/status-hooks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the WorkerObserve readiness and exitDefine the containerRun the example

Log when a Container becomes ready, exits successfully, or fails. The Durable Object starts a named image and uses `monitor()` to observe its exit.

## Configure the Worker
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "container-lifecycle",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "observability": {
        "enabled": true
      },
      "containers": [
        {
          "class_name": "MyContainer",
          "scheduling_policy": "durable_object",
          "images": {
            "base": {
              "dockerfile": "./Dockerfile"
            }
          }
        }
      ],
      "durable_objects": {
        "bindings": [
          {
            "name": "MY_CONTAINER",
            "class_name": "MyContainer"
          }
        ]
      },
      "exports": {
        "MyContainer": {
          "type": "durable-object",
          "storage": "sqlite"
        }
      }
    }
    
    
    name = "container-lifecycle"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [observability]
    enabled = true
    
    [[containers]]
    class_name = "MyContainer"
    scheduling_policy = "durable_object"
    
    [containers.images.base]
    dockerfile = "./Dockerfile"
    
    [[durable_objects.bindings]]
    name = "MY_CONTAINER"
    class_name = "MyContainer"
    
    [exports.MyContainer]
    type = "durable-object"
    storage = "sqlite"

## Observe readiness and exit

`start()` initiates startup. The Worker waits for a successful `/health` response before forwarding traffic. Concurrent requests share that readiness check, and a failed check can be retried by the next request.

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    const INACTIVITY_TIMEOUT_MS = 5 * 60 * 1000;
    
    export class MyContainer extends DurableObject {
    	starting;
    	monitoring;
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		const container = ctx.container;
    		if (container.running) {
    			void ctx.blockConcurrencyWhile(() =>
    				container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS),
    			);
    			this.observeExit();
    		}
    	}
    
    	async fetch(request) {
    		// Concurrent requests share startup and readiness checks.
    		this.starting ??= this.startAndWaitForPort().finally(() => {
    			this.starting = undefined;
    		});
    		await this.starting;
    
    		const url = new URL(request.url);
    		url.protocol = "http:";
    		url.host = "container";
    		const forwarded = new Request(url, request);
    		forwarded.headers.delete("host");
    		return this.ctx.container.getTcpPort(8080).fetch(forwarded);
    	}
    
    	async startAndWaitForPort() {
    		const container = this.ctx.container;
    		if (!container.running) {
    			container.start({
    				image: container.images.base,
    				instance: "lite",
    				enableInternet: false,
    			});
    		}
    		this.observeExit();
    		await container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS);
    
    		const port = container.getTcpPort(8080);
    		let lastError;
    		for (let attempt = 0; attempt < 100; attempt++) {
    			try {
    				const response = await port.fetch("http://container/health", {
    					signal: AbortSignal.timeout(1000),
    				});
    				await response.body?.cancel();
    				if (!response.ok) {
    					throw new Error(`Health check returned ${response.status}`);
    				}
    				console.log("Container is ready");
    				return;
    			} catch (error) {
    				lastError = error;
    				await scheduler.wait(200);
    			}
    		}
    		throw new Error("Container did not become ready on port 8080", {
    			cause: lastError,
    		});
    	}
    
    	observeExit() {
    		if (this.monitoring) return;
    		this.monitoring = this.ctx.container
    			.monitor()
    			.then(() => console.log("Container exited successfully"))
    			.catch((error) => console.error("Container failed:", error))
    			.finally(() => {
    				this.monitoring = undefined;
    			});
    		this.ctx.waitUntil(this.monitoring);
    	}
    }
    
    export default {
    	fetch(request, env) {
    		return env.MY_CONTAINER.getByName("demo").fetch(request);
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    interface Env {
    	MY_CONTAINER: DurableObjectNamespace<MyContainer>;
    }
    
    const INACTIVITY_TIMEOUT_MS = 5 * 60 * 1000;
    
    export class MyContainer extends DurableObject<Env> {
    	private starting: Promise<void> | undefined;
    	private monitoring: Promise<void> | undefined;
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		const container = ctx.container!;
    		if (container.running) {
    			void ctx.blockConcurrencyWhile(() =>
    				container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS),
    			);
    			this.observeExit();
    		}
    	}
    
    	async fetch(request: Request): Promise<Response> {
    		// Concurrent requests share startup and readiness checks.
    		this.starting ??= this.startAndWaitForPort().finally(() => {
    			this.starting = undefined;
    		});
    		await this.starting;
    
    		const url = new URL(request.url);
    		url.protocol = "http:";
    		url.host = "container";
    		const forwarded = new Request(url, request);
    		forwarded.headers.delete("host");
    		return this.ctx.container!.getTcpPort(8080).fetch(forwarded);
    	}
    
    	private async startAndWaitForPort(): Promise<void> {
    		const container = this.ctx.container!;
    		if (!container.running) {
    			container.start({
    				image: container.images.base,
    				instance: "lite",
    				enableInternet: false,
    			});
    		}
    		this.observeExit();
    		await container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS);
    
    		const port = container.getTcpPort(8080);
    		let lastError: unknown;
    		for (let attempt = 0; attempt < 100; attempt++) {
    			try {
    				const response = await port.fetch("http://container/health", {
    					signal: AbortSignal.timeout(1000),
    				});
    				await response.body?.cancel();
    				if (!response.ok) {
    					throw new Error(`Health check returned ${response.status}`);
    				}
    				console.log("Container is ready");
    				return;
    			} catch (error) {
    				lastError = error;
    				await scheduler.wait(200);
    			}
    		}
    		throw new Error("Container did not become ready on port 8080", {
    			cause: lastError,
    		});
    	}
    
    	private observeExit(): void {
    		if (this.monitoring) return;
    		this.monitoring = this.ctx
    			.container!.monitor()
    			.then(() => console.log("Container exited successfully"))
    			.catch((error: unknown) => console.error("Container failed:", error))
    			.finally(() => {
    				this.monitoring = undefined;
    			});
    		this.ctx.waitUntil(this.monitoring);
    	}
    }
    
    export default {
    	fetch(request: Request, env: Env): Promise<Response> {
    		return env.MY_CONTAINER.getByName("demo").fetch(request);
    	},
    } satisfies ExportedHandler<Env>;

`monitor()` resolves without a value after a successful exit. It rejects for failures, including nonzero process exits. The constructor restores monitoring and the inactivity timeout when the Durable Object restarts with a running Container.

A pending monitor can keep the Durable Object active for up to 15 minutes. The five-minute inactivity timeout starts after the Durable Object becomes inactive, not five minutes after the last HTTP request. Monitoring is not a durable event subscription across restarts. Refer to [`monitor()`](https://developers.cloudflare.com/containers/api/durable-object-container/#monitor).

## Define the container

Save these files in the project root. The server listens on `0.0.0.0:8080` and exposes a readiness endpoint at `/health`.

server.mjsjs
    
    
    import { createServer } from "node:http";
    
    createServer((request, response) => {
    	if (request.url === "/health") {
    		response.writeHead(200).end();
    		return;
    	}
    	response.setHeader("Content-Type", "application/json");
    	response.end(
    		JSON.stringify({
    			message: "Hello from a Container",
    			environment: process.env.ENV_VAR,
    			kvValue: process.env.KV_VALUE,
    		}),
    	);
    }).listen(8080, "0.0.0.0");

Dockerfiledockerfile
    
    
    FROM node:24-bookworm-slim
    WORKDIR /app
    COPY server.mjs .
    EXPOSE 8080
    CMD ["node", "server.mjs"]

## Run the example

Start a Docker-compatible engine. Install Wrangler in your project, using version 4.136.0 or later for [local development](https://developers.cloudflare.com/containers/guides/local-dev/).

npmyarnpnpmbun
    
    
    npm i -D wrangler
    
    
    yarn add -D wrangler
    
    
    pnpm add -D wrangler
    
    
    bun add -d wrangler

npmyarnpnpm
    
    
    npx wrangler dev
    
    
    yarn wrangler dev
    
    
    pnpm wrangler dev

Visit `http://localhost:8787/` and inspect the Worker logs for readiness. Container completion or failure is logged when observed by `monitor()`.

[PreviousCron container](https://developers.cloudflare.com/containers/examples/cron/)[NextEnvironment variables and secrets](https://developers.cloudflare.com/containers/examples/env-vars-and-secrets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/examples/status-hooks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
