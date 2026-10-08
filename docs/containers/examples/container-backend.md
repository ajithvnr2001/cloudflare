---
url: https://developers.cloudflare.com/containers/examples/container-backend/
title: Static frontend, container backend \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:34.767047+00:00
---

# Static frontend, container backend · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/examples/container-backend/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Examples
  4. /Static frontend, container backend



# Static frontend, container backend

A simple frontend app with a containerized backend

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/examples/container-backend/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the WorkerAdd the frontendRoute API requestsDefine a backend containerRun the example

Serve a static frontend with [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/). Route API requests to a pool of three Containers using the `durable_object` scheduling policy.

## Configure the Worker
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "static-frontend-container-backend",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "observability": {
        "enabled": true
      },
      "assets": {
        "directory": "./dist",
        "binding": "ASSETS",
        "run_worker_first": [
          "/api",
          "/api/*"
        ]
      },
      "containers": [
        {
          "class_name": "Backend",
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
            "name": "BACKEND",
            "class_name": "Backend"
          }
        ]
      },
      "exports": {
        "Backend": {
          "type": "durable-object",
          "storage": "sqlite"
        }
      }
    }
    
    
    name = "static-frontend-container-backend"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [observability]
    enabled = true
    
    [assets]
    directory = "./dist"
    binding = "ASSETS"
    run_worker_first = ["/api", "/api/*"]
    
    [[containers]]
    class_name = "Backend"
    scheduling_policy = "durable_object"
    
    [containers.images.base]
    dockerfile = "./Dockerfile"
    
    [[durable_objects.bindings]]
    name = "BACKEND"
    class_name = "Backend"
    
    [exports.Backend]
    type = "durable-object"
    storage = "sqlite"

## Add the frontend

Create a simple `index.html` file in the `./dist` directory.

index.html
    
    
    <!DOCTYPE html>
    <html lang="en">
    	<head>
    		<meta charset="UTF-8" />
    		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
    		<title>Widgets</title>
    		<script
    			defer
    			src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.13.3/cdn.min.js"
    		></script>
    	</head>
    
    	<body>
    		<div x-data="widgets()" x-init="fetchWidgets()">
    			<h1>Widgets</h1>
    			<div x-show="loading">Loading...</div>
    			<div x-show="error" x-text="error" style="color: red;"></div>
    			<ul x-show="!loading && !error">
    				<template x-for="widget in widgets" :key="widget.id">
    					<li>
    						<span x-text="widget.name"></span> - (ID:
    						<span x-text="widget.id"></span>)
    					</li>
    				</template>
    			</ul>
    
    			<div x-show="!loading && !error && widgets.length === 0">
    				No widgets found.
    			</div>
    		</div>
    
    		<script>
    			function widgets() {
    				return {
    					widgets: [],
    					loading: false,
    					error: null,
    
    					async fetchWidgets() {
    						this.loading = true;
    						this.error = null;
    
    						try {
    							const response = await fetch("/api/widgets");
    							if (!response.ok) {
    								throw new Error(
    									`HTTP ${response.status}: ${response.statusText}`,
    								);
    							}
    							this.widgets = await response.json();
    						} catch (err) {
    							this.error = err.message;
    						} finally {
    							this.loading = false;
    						}
    					},
    				};
    			}
    		</script>
    	</body>
    </html>

The frontend uses [Alpine.js ↗︎](https://alpinejs.dev/) to fetch a list of widgets from `/api/widgets`.

This is meant to be a very simple example, but you can get significantly more complex. See [examples of Workers integrating with frontend frameworks](https://developers.cloudflare.com/workers/framework-guides/web-apps/) for more information.

## Route API requests

`start()` initiates startup. The Worker waits for a successful `/health` response before forwarding traffic. Concurrent requests share that readiness check, and a failed check can be retried by the next request.

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    const INSTANCE_COUNT = 3;
    
    const INACTIVITY_TIMEOUT_MS = 2 * 60 * 60 * 1000;
    
    export class Backend extends DurableObject {
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
    		const pathname = new URL(request.url).pathname;
    		if (pathname === "/api" || pathname.startsWith("/api/")) {
    			const index = Math.floor(Math.random() * INSTANCE_COUNT);
    			return env.BACKEND.getByName(`instance-${index}`).fetch(request);
    		}
    		return env.ASSETS.fetch(request);
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    interface Env {
    	BACKEND: DurableObjectNamespace<Backend>;
    	ASSETS: Fetcher;
    }
    
    const INSTANCE_COUNT = 3;
    
    const INACTIVITY_TIMEOUT_MS = 2 * 60 * 60 * 1000;
    
    export class Backend extends DurableObject<Env> {
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
    		const pathname = new URL(request.url).pathname;
    		if (pathname === "/api" || pathname.startsWith("/api/")) {
    			const index = Math.floor(Math.random() * INSTANCE_COUNT);
    			return env.BACKEND.getByName(`instance-${index}`).fetch(request);
    		}
    		return env.ASSETS.fetch(request);
    	},
    } satisfies ExportedHandler<Env>;

The Worker selects one of three named instances for each API request. Each instance uses the configured `base` image and the `lite` instance size.

## Define a backend container

Your container should be able to handle requests to `/api/widgets`.

In this case, we'll use a simple Golang backend that returns a hard-coded list of widgets.

server.go
    
    
    package main
    
    import (
    	"encoding/json"
    	"log"
    	"net/http"
    )
    
    func handler(w http.ResponseWriter, r *http.Request) {
    	widgets := []map[string]interface{}{
    		{"id": 1, "name": "Widget A"},
    		{"id": 2, "name": "Sprocket B"},
    		{"id": 3, "name": "Gear C"},
    	}
    
    	w.Header().Set("Content-Type", "application/json")
    	w.Header().Set("Access-Control-Allow-Origin", "*")
    	json.NewEncoder(w).Encode(widgets)
    
    }
    
    func main() {
    	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
    		w.WriteHeader(http.StatusOK)
    	})
    	http.HandleFunc("/api/widgets", handler)
    	log.Fatal(http.ListenAndServe(":8080", nil))
    }

The health endpoint lets the Worker wait for the backend before forwarding requests. Build the backend image with this Dockerfile in the project root:

Dockerfile
    
    
    FROM golang:1.25-alpine AS build
    WORKDIR /app
    COPY server.go .
    RUN CGO_ENABLED=0 go build -o /server server.go
    
    FROM alpine:3.20
    COPY --from=build /server /server
    EXPOSE 8080
    CMD ["/server"]

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

Visit `http://localhost:8787/` to load the frontend and its list of widgets.

[PreviousStateless instances](https://developers.cloudflare.com/containers/examples/stateless/)[NextCron container](https://developers.cloudflare.com/containers/examples/cron/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/examples/container-backend.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
