---
url: https://developers.cloudflare.com/sandbox/get-started/
title: Run a Linux command \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:18.620476+00:00
---

# Run a Linux command · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /Get started



# Run a Linux command

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesRun a command in LinuxNext steps

You will POST `uname -a` to a Worker and read stdout that contains `Linux`.

## Prerequisites

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

## Run a command in Linux

  1. Create a Worker project:

npmyarnpnpm
         
         npm create cloudflare@latest -- sandbox-linux --category=hello-world --type=hello-world --lang=ts --no-deploy --no-git --no-agents
         
         yarn create cloudflare sandbox-linux --category=hello-world --type=hello-world --lang=ts --no-deploy --no-git --no-agents
         
         pnpm create cloudflare@latest sandbox-linux --category=hello-world --type=hello-world --lang=ts --no-deploy --no-git --no-agents

  2. Change into the project directory:
         
         cd sandbox-linux

  3. Replace `wrangler.jsonc` so a Durable Object can start a container:
         
         {
         	"$schema": "node_modules/wrangler/config-schema.json",
         	"name": "sandbox-linux",
         	"main": "src/index.ts",
         	// Set this to today's date
         	"compatibility_date": "2026-10-08",
         	"observability": {
         		"enabled": true,
         	},
         	"upload_source_maps": true,
         	"containers": [
         		{
         			"class_name": "MyContainer",
         			"scheduling_policy": "durable_object",
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
         name = "sandbox-linux"
         main = "src/index.ts"
         # Set this to today's date
         compatibility_date = "2026-10-08"
         upload_source_maps = true
         
         [observability]
         enabled = true
         
         [[containers]]
         class_name = "MyContainer"
         scheduling_policy = "durable_object"
         
         [[durable_objects.bindings]]
         class_name = "MyContainer"
         name = "MY_CONTAINER"
         
         [exports.MyContainer]
         type = "durable-object"
         storage = "sqlite"

  4. Replace `src/index.ts`. The Worker reads `argv` from the JSON body and runs it in Linux:

src/index.jsjs
         
         import { DurableObject } from "cloudflare:workers";
         
         export class MyContainer extends DurableObject {
         	async exec(argv) {
         		const container = this.ctx.container;
         		if (!container) {
         			throw new Error("The container binding is not configured");
         		}
         
         		if (!container.running) {
         			container.start({
         				// Debian Trixie with Node.js 24
         				image: "cloudflare/debian-trixie",
         				// Keep the instance running so it can accept commands
         				entrypoint: ["sleep", "infinity"],
         				// Block commands in the sandbox from reaching the Internet
         				enableInternet: false,
         			});
         		}
         
         		const process = await container.exec(argv);
         		const output = await process.output();
         		return {
         			stdout: new TextDecoder().decode(output.stdout),
         			exitCode: output.exitCode,
         		};
         	}
         }
         
         export default {
         	async fetch(request, env) {
         		const { argv } = await request.json();
         		const sandbox = env.MY_CONTAINER.getByName("sandbox");
         		return Response.json(await sandbox.exec(argv));
         	},
         };

src/index.tsts
         
         import { DurableObject } from "cloudflare:workers";
         
         export class MyContainer extends DurableObject<Env> {
         	async exec(argv: string[]) {
         		const container = this.ctx.container;
         		if (!container) {
         			throw new Error("The container binding is not configured");
         		}
         
         		if (!container.running) {
         			container.start({
         				// Debian Trixie with Node.js 24
         				image: "cloudflare/debian-trixie",
         				// Keep the instance running so it can accept commands
         				entrypoint: ["sleep", "infinity"],
         				// Block commands in the sandbox from reaching the Internet
         				enableInternet: false,
         			});
         		}
         
         		const process = await container.exec(argv);
         		const output = await process.output();
         		return {
         			stdout: new TextDecoder().decode(output.stdout),
         			exitCode: output.exitCode,
         		};
         	}
         }
         
         export default {
         	async fetch(request: Request, env: Env): Promise<Response> {
         		const { argv } = (await request.json()) as { argv: string[] };
         		const sandbox = env.MY_CONTAINER.getByName("sandbox");
         		return Response.json(await sandbox.exec(argv));
         	},
         };

  5. Generate types for the binding. Wrangler reads the `MyContainer` class from `src/index.ts` to type `env.MY_CONTAINER`:

npmyarnpnpm
         
         npx wrangler types
         
         yarn wrangler types
         
         pnpm wrangler types

  6. Run `wrangler dev`:

npmyarnpnpm
         
         npx wrangler dev
         
         yarn wrangler dev
         
         pnpm wrangler dev

`wrangler dev` runs the instance in [Docker ↗︎](https://www.docker.com/) on your machine, so Docker must be running. Running `cloudflare/debian-trixie` locally needs Wrangler 4.141.0 or later.

  7. POST a command to the URL Wrangler prints. The default is `http://localhost:8787`:
         
         curl http://localhost:8787 --request POST --json '{"argv":["uname","-a"]}'




The JSON body includes `"exitCode":0`. `stdout` contains `Linux`. The Worker started a Linux VM and ran the command you sent.

## Next steps

  * Run another process in the instance. Refer to [`exec()`](https://developers.cloudflare.com/containers/api/durable-object-container/#exec).
  * Deploy your Worker. Refer to [Deploy Containers](https://developers.cloudflare.com/containers/guides/deploy/). A deploy does not replace a running instance. Refer to [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/#deploys-keep-instances-running).
  * Run JavaScript. Refer to [Run JavaScript](https://developers.cloudflare.com/sandbox/get-started/dynamic-workers/).
  * Use the [Durable Object container API](https://developers.cloudflare.com/containers/api/durable-object-container/) for `start()` and `exec()`.
  * Start a project from the [minimal sandbox template ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/main/examples/minimal). It adds a `Dockerfile`, a sandbox for each name in the URL, and file reads and writes with `@cloudflare/sandbox`.



[PreviousOverview](https://developers.cloudflare.com/sandbox/)[NextRun JavaScript](https://developers.cloudflare.com/sandbox/get-started/dynamic-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/get-started/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
