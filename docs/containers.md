---
url: https://developers.cloudflare.com/containers/
title: Overview \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:32.976425+00:00
---

# Overview · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/

  1. [Home](https://developers.cloudflare.com/)
  2. /Containers



# Containers

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNext stepsMore resources

Enhance your Workers with serverless containers

Available on Workers Paid plan

Run code written in any programming language, built for any runtime, as part of apps built on [Workers](https://developers.cloudflare.com/workers).

Deploy your container image to `Region:Earth` without worrying about managing infrastructure - just define your Worker and [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy).

With Containers you can run:

  * Resource-intensive applications that require CPU cores running in parallel, large amounts of memory or disk space
  * Applications and libraries that require a full filesystem, specific runtime, or Linux-like environment
  * Existing applications and tools that have been distributed as container images



Container instances are spun up on-demand and controlled by code you write in your [Worker](https://developers.cloudflare.com/workers). Instead of chaining together API calls or writing Kubernetes operators, you just write TypeScript or JavaScript.

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    import { rewriteRequestForContainer, startAndWaitForPort } from "./utils";
    
    export class MyContainer extends DurableObject {
    	async fetch(request) {
    		const container = this.ctx.container;
    		await startAndWaitForPort(container, {
    			port: 4000,
    			inactivityTimeout: 10 * 60 * 1000,
    		});
    
    		const forwarded = rewriteRequestForContainer(request);
    		const response = await container.getTcpPort(4000).fetch(forwarded);
    		return response;
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		const containerRequest = request.clone();
    		const { "session-id": sessionId } = await request.json();
    		return env.MY_CONTAINER.getByName(sessionId).fetch(containerRequest);
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    import { rewriteRequestForContainer, startAndWaitForPort } from "./utils";
    
    interface Env {
    	MY_CONTAINER: DurableObjectNamespace<MyContainer>;
    }
    
    export class MyContainer extends DurableObject<Env> {
    	async fetch(request: Request): Promise<Response> {
    		const container = this.ctx.container!;
    		await startAndWaitForPort(container, {
    			port: 4000,
    			inactivityTimeout: 10 * 60 * 1000,
    		});
    
    		const forwarded = rewriteRequestForContainer(request);
    		const response = await container.getTcpPort(4000).fetch(forwarded);
    		return response;
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const containerRequest = request.clone();
    		const { "session-id": sessionId } = await request.json<{
    			"session-id": string;
    		}>();
    		return env.MY_CONTAINER.getByName(sessionId).fetch(containerRequest);
    	},
    };

src/utils.jsjs
    
    
    export function rewriteRequestForContainer(request) {
    	const url = new URL(request.url);
    	url.protocol = "http:";
    	url.host = "container";
    	const forwarded = new Request(url, request);
    	forwarded.headers.delete("host");
    	return forwarded;
    }
    
    export async function startAndWaitForPort(container, options) {
    	await container.setInactivityTimeout(options.inactivityTimeout);
    	if (!container.running) {
    		container.start();
    	}
    
    	// start() returns before the container is ready, so poll its health endpoint.
    	const port = container.getTcpPort(options.port);
    	let lastError;
    	for (let attempt = 0; attempt < 100; attempt++) {
    		try {
    			const response = await port.fetch("http://container/health");
    			if (!response.ok) {
    				throw new Error(`Health check returned ${response.status}`);
    			}
    			return;
    		} catch (error) {
    			lastError = error;
    			await scheduler.wait(200);
    		}
    	}
    	throw new Error(`Container did not become ready on port ${options.port}`, {
    		cause: lastError,
    	});
    }

src/utils.tsts
    
    
    interface ReadinessOptions {
    	port: number;
    	inactivityTimeout: number;
    }
    
    type ContainerInstance = NonNullable<DurableObjectState["container"]>;
    
    export function rewriteRequestForContainer(request: Request): Request {
    	const url = new URL(request.url);
    	url.protocol = "http:";
    	url.host = "container";
    	const forwarded = new Request(url, request);
    	forwarded.headers.delete("host");
    	return forwarded;
    }
    
    export async function startAndWaitForPort(
    	container: ContainerInstance,
    	options: ReadinessOptions,
    ): Promise<void> {
    	await container.setInactivityTimeout(options.inactivityTimeout);
    	if (!container.running) {
    		container.start();
    	}
    
    	// start() returns before the container is ready, so poll its health endpoint.
    	const port = container.getTcpPort(options.port);
    	let lastError: unknown;
    	for (let attempt = 0; attempt < 100; attempt++) {
    		try {
    			const response = await port.fetch("http://container/health");
    			if (!response.ok) {
    				throw new Error(`Health check returned ${response.status}`);
    			}
    			return;
    		} catch (error) {
    			lastError = error;
    			await scheduler.wait(200);
    		}
    	}
    	throw new Error(`Container did not become ready on port ${options.port}`, {
    		cause: lastError,
    	});
    }
    
    
    {
    	"name": "container-starter",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"containers": [
    		{
    			"class_name": "MyContainer",
    			"image": "./Dockerfile",
    			"max_instances": 5,
    		},
    	],
    	"durable_objects": {
    		"bindings": [
    			{
    				"class_name": "MyContainer",
    				"name": "MY_CONTAINER",
    			},
    		],
    	},
    	"exports": {
    		"MyContainer": {
    			"type": "durable-object",
    			"storage": "sqlite",
    		},
    	},
    }
    
    
    name = "container-starter"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[containers]]
    class_name = "MyContainer"
    image = "./Dockerfile"
    max_instances = 5
    
    [[durable_objects.bindings]]
    class_name = "MyContainer"
    name = "MY_CONTAINER"
    
    [exports.MyContainer]
    type = "durable-object"
    storage = "sqlite"

[Get started](https://developers.cloudflare.com/containers/get-started/) [Containers dashboard](https://dash.cloudflare.com/?to=/:account/workers/containers)

* * *

## Next steps

[Get started](https://developers.cloudflare.com/containers/get-started/)

Build and push an image, call a Container from a Worker, and try scaling and routing.

Deploy a Container

[Examples](https://developers.cloudflare.com/containers/examples/)

Stateless and stateful routing, regional placement, Workflow and Queue integrations, AI-generated code execution, and short-lived workloads.

See Examples

[Local development](https://developers.cloudflare.com/containers/guides/local-dev/)

Run your Worker and container together with `wrangler dev` or `vite dev` before you deploy.

Develop locally

[Deploy](https://developers.cloudflare.com/containers/guides/deploy/)

Ship from your machine or Workers Builds, and confirm the deploy.

Deploy Containers

* * *

## More resources

### [Scheduling policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/)

Choose whether image and instance configuration is managed centrally or from Durable Object code.

### [Rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/)

How container instances update after you deploy.

### [Image management](https://developers.cloudflare.com/containers/guides/image-management/)

Build, push, and pull images for Containers.

### [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/)

How a container is scheduled, started, routed, and shut down.

### [Limits](https://developers.cloudflare.com/containers/platform/limits/)

Instance counts, image size, and other platform limits.

### [Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers)

CLI commands for images and containers.

### [APIs](https://developers.cloudflare.com/containers/api/)

Use the Durable Object Container API or reference the Container class.

### [SSH](https://developers.cloudflare.com/containers/guides/ssh/)

Connect to running container instances with SSH through Wrangler.

### [Containers Discord](https://discord.cloudflare.com)

Ask questions, show what you are building, and talk with other Containers developers.

[NextGet started](https://developers.cloudflare.com/containers/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
