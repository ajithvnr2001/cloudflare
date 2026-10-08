---
url: https://developers.cloudflare.com/containers/examples/websocket/
title: WebSocket to container \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:35.356413+00:00
---

# WebSocket to container · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/examples/websocket/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Examples
  4. /WebSocket to container



# WebSocket to container

Forwarding a Websocket request to a Container

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/examples/websocket/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the WorkerForward the upgradeDefine the WebSocket serverRun the example

Forward WebSocket upgrade requests through a Durable Object to a Container. This example runs an echo server with the `durable_object` scheduling policy.

## Configure the Worker
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "websocket-container",
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
    
    
    name = "websocket-container"
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

## Forward the upgrade

`start()` initiates startup. The Worker waits for a successful `/health` response before forwarding traffic. Concurrent requests share that readiness check, and a failed check can be retried by the next request.

Return the port response directly to preserve the WebSocket upgrade.

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    const INACTIVITY_TIMEOUT_MS = 2 * 60 * 1000;
    
    export class MyContainer extends DurableObject {
    	starting;
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		const container = ctx.container;
    		if (container.running) {
    			void ctx.blockConcurrencyWhile(() =>
    				container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS),
    			);
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
    
    const INACTIVITY_TIMEOUT_MS = 2 * 60 * 1000;
    
    export class MyContainer extends DurableObject<Env> {
    	private starting: Promise<void> | undefined;
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		const container = ctx.container!;
    		if (container.running) {
    			void ctx.blockConcurrencyWhile(() =>
    				container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS),
    			);
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
    }
    
    export default {
    	fetch(request: Request, env: Env): Promise<Response> {
    		return env.MY_CONTAINER.getByName("demo").fetch(request);
    	},
    } satisfies ExportedHandler<Env>;

## Define the WebSocket server

Save these files in the project root. The HTTP server handles `/health`, while `/ws` accepts WebSocket upgrades.

package.jsonjson
    
    
    {
    	"private": true,
    	"type": "module",
    	"dependencies": { "ws": "^8.18.0" }
    }

server.mjsjs
    
    
    import { createServer } from "node:http";
    import { WebSocketServer } from "ws";
    
    const server = createServer((request, response) => {
    	if (request.url === "/health") {
    		response.writeHead(200).end();
    	} else {
    		response.writeHead(404).end();
    	}
    });
    const sockets = new WebSocketServer({ server, path: "/ws" });
    sockets.on("connection", (socket) => {
    	socket.on("error", console.error);
    	socket.on("message", (data, isBinary) => {
    		socket.send(data, { binary: isBinary });
    	});
    });
    server.listen(8080, "0.0.0.0");

Dockerfiledockerfile
    
    
    FROM node:24-bookworm-slim
    WORKDIR /app
    COPY package.json .
    RUN npm install --omit=dev
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

Connect a WebSocket client to `ws://localhost:8787/ws`. Send a message and check that the same message returns. For a deployed Worker, use `wss://<WORKER_HOST>/ws`.

An open WebSocket can keep the Durable Object active. The inactivity timeout applies after the Durable Object becomes inactive. Refer to [Container lifecycle](https://developers.cloudflare.com/containers/concepts/architecture/).

[PreviousEnvironment variables and secrets](https://developers.cloudflare.com/containers/examples/env-vars-and-secrets/)[NextMount R2 buckets with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/examples/websocket.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
