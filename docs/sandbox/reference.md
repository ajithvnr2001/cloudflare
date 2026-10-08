---
url: https://developers.cloudflare.com/sandbox/reference/
title: @cloudflare/sandbox \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:20.483395+00:00
---

# @cloudflare/sandbox · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/reference/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /Reference



# @cloudflare/sandbox

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/reference/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallRequirementsExample configurationClasses

`@cloudflare/sandbox` works with a container you start from a Durable Object. Its classes run helper processes in the running container through [`exec()`](https://developers.cloudflare.com/containers/api/durable-object-container/#exec). The package does not start, stop, or monitor the container.

For `start()`, `exec()`, snapshots, and the other methods of the container itself, refer to the [Durable Object container API](https://developers.cloudflare.com/containers/api/durable-object-container/).

## Install

npmyarnpnpmbun
    
    
    npm i @cloudflare/sandbox
    
    
    yarn add @cloudflare/sandbox
    
    
    pnpm add @cloudflare/sandbox
    
    
    bun add @cloudflare/sandbox

## Requirements

Every class in the package has these requirements. A class page lists any others.

  * The container image contains the helper binary at `/usr/local/bin/sandbox-shim`. Copy it from the `cloudflare/sandbox` image whose tag matches the installed `@cloudflare/sandbox` version:
        
        COPY --from=docker.io/cloudflare/sandbox:<VERSION> /usr/local/bin/sandbox-shim /usr/local/bin/sandbox-shim

The helper is a statically linked `linux/amd64` binary. It runs in any `linux/amd64` image.

  * The Worker has the [`nodejs_compat`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) compatibility flag. The package reads Linux error names through `node:os`.

  * The container is running when a method is called.




## Example configuration

This configuration meets every requirement. The `Dockerfile` copies the helper into a Debian Trixie image with Node.js 24, and `sleep infinity` keeps the container running:

Dockerfiledockerfile
    
    
    FROM node:24-trixie-slim
    
    COPY --from=docker.io/cloudflare/sandbox:1.0.0 /usr/local/bin/sandbox-shim /usr/local/bin/sandbox-shim
    
    RUN mkdir /workspace
    CMD ["sleep", "infinity"]

The Wrangler configuration sets `nodejs_compat`, builds the `Dockerfile` as the image named `workspace`, and declares `MyContainer` as a Durable Object class:
    
    
    {
    	"$schema": "node_modules/wrangler/config-schema.json",
    	"name": "sandbox-files",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"compatibility_flags": ["nodejs_compat"],
    	"containers": [
    		{
    			"class_name": "MyContainer",
    			"scheduling_policy": "durable_object",
    			"images": {
    				"workspace": {
    					"dockerfile": "./Dockerfile",
    				},
    			},
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
    
    
    "$schema" = "node_modules/wrangler/config-schema.json"
    name = "sandbox-files"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "nodejs_compat" ]
    
    [[containers]]
    class_name = "MyContainer"
    scheduling_policy = "durable_object"
    
    [containers.images.workspace]
    dockerfile = "./Dockerfile"
    
    [[durable_objects.bindings]]
    class_name = "MyContainer"
    name = "MY_CONTAINER"
    
    [exports.MyContainer]
    type = "durable-object"
    storage = "sqlite"

The Durable Object starts the `workspace` image and passes the container to a class from the package:

src/index.jsjs
    
    
    import { Files } from "@cloudflare/sandbox";
    import { DurableObject } from "cloudflare:workers";
    
    const INACTIVITY_TIMEOUT_MS = 10 * 60 * 1000;
    
    export class MyContainer extends DurableObject {
    	container;
    	files;
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		const container = ctx.container;
    
    		if (!container) {
    			throw new Error("The container binding is not configured");
    		}
    
    		this.container = container;
    		// ctx.container stays the same object while the Durable Object runs.
    		this.files = new Files(container);
    
    		// A restarted Durable Object sets the timeout again.
    		if (container.running) {
    			void ctx.blockConcurrencyWhile(() =>
    				container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS),
    			);
    		}
    	}
    
    	async listWorkspace() {
    		// Files does not start the container.
    		if (!this.container.running) {
    			this.container.start({
    				image: this.container.images.workspace,
    				enableInternet: false,
    			});
    			await this.container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS);
    		}
    
    		return this.files.readDirectory("/workspace");
    	}
    }

src/index.tsts
    
    
    import { Files } from "@cloudflare/sandbox";
    import { DurableObject } from "cloudflare:workers";
    
    const INACTIVITY_TIMEOUT_MS = 10 * 60 * 1000;
    
    export class MyContainer extends DurableObject<Env> {
    	private readonly container: Container;
    	private readonly files: Files;
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		const container = ctx.container;
    
    		if (!container) {
    			throw new Error("The container binding is not configured");
    		}
    
    		this.container = container;
    		// ctx.container stays the same object while the Durable Object runs.
    		this.files = new Files(container);
    
    		// A restarted Durable Object sets the timeout again.
    		if (container.running) {
    			void ctx.blockConcurrencyWhile(() =>
    				container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS),
    			);
    		}
    	}
    
    	async listWorkspace() {
    		// Files does not start the container.
    		if (!this.container.running) {
    			this.container.start({
    				image: this.container.images.workspace,
    				enableInternet: false,
    			});
    			await this.container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS);
    		}
    
    		return this.files.readDirectory("/workspace");
    	}
    }

For more information about building images, refer to [`images`](https://developers.cloudflare.com/containers/api/durable-object-container/#images).

## Classes

  * [Files API](https://developers.cloudflare.com/sandbox/reference/files/)
  * [S3Mount API](https://developers.cloudflare.com/sandbox/reference/s3-mounts/)
  * [DirectoryBackup API](https://developers.cloudflare.com/sandbox/reference/directory-backups/)



[PreviousOpenAI Agents API](https://developers.cloudflare.com/sandbox/coding-agents/openai-agents-api/)[NextFiles](https://developers.cloudflare.com/sandbox/reference/files/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/reference/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
