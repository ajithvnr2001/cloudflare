---
url: https://developers.cloudflare.com/sandbox/get-started/dynamic-workers/
title: Run JavaScript \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:19.527513+00:00
---

# Run JavaScript · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/get-started/dynamic-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Get started](https://developers.cloudflare.com/sandbox/get-started/)
  4. /Run JavaScript



# Run JavaScript

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/get-started/dynamic-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesRun JavaScriptNext steps

You will POST JavaScript to a Worker and read `{"result":["Ada"]}`.

## Prerequisites

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

## Run JavaScript

  1. Create a Worker project:

npmyarnpnpm
         
         npm create cloudflare@latest -- sandbox-dynamic-worker --category=hello-world --type=hello-world --lang=ts --no-deploy
         
         yarn create cloudflare sandbox-dynamic-worker --category=hello-world --type=hello-world --lang=ts --no-deploy
         
         pnpm create cloudflare@latest sandbox-dynamic-worker --category=hello-world --type=hello-world --lang=ts --no-deploy

  2. Change into the project directory:
         
         cd sandbox-dynamic-worker

  3. Replace `wrangler.jsonc` to add a Worker Loader binding:
         
         {
         	"$schema": "node_modules/wrangler/config-schema.json",
         	"name": "sandbox-dynamic-worker",
         	"main": "src/index.ts",
         	// Set this to today's date
         	"compatibility_date": "2026-10-08",
         	"observability": {
         		"enabled": true,
         	},
         	"upload_source_maps": true,
         	"worker_loaders": [
         		{
         			"binding": "LOADER",
         		},
         	],
         }
         
         "$schema" = "node_modules/wrangler/config-schema.json"
         name = "sandbox-dynamic-worker"
         main = "src/index.ts"
         # Set this to today's date
         compatibility_date = "2026-10-08"
         upload_source_maps = true
         
         [observability]
         enabled = true
         
         [[worker_loaders]]
         binding = "LOADER"

  4. Generate types for the binding:

npmyarnpnpm
         
         npx wrangler types
         
         yarn wrangler types
         
         pnpm wrangler types

  5. Replace `src/index.ts`. Your Worker reads `code` from the JSON body and runs it in the sandbox:

src/index.jsjs
         
         export default {
         	async fetch(request, env) {
         		const { code } = await request.json();
         
         		const sandbox = env.LOADER.load({
         			compatibilityDate: "2026-10-08",
         			mainModule: "code.js",
         			modules: {
         				"code.js": `
         					import { WorkerEntrypoint } from "cloudflare:workers";
         
         					export class Code extends WorkerEntrypoint {
         						evaluate() {
         							${code}
         						}
         					}
         				`,
         			},
         			// Block `fetch()` and `connect()`
         			globalOutbound: null,
         			// Stop code that uses more than 50 milliseconds of CPU time
         			limits: { cpuMs: 50 },
         		});
         
         		const result = await sandbox.getEntrypoint("Code").evaluate();
         		return Response.json({ result });
         	},
         };

src/index.tsts
         
         import type { WorkerEntrypoint } from "cloudflare:workers";
         
         type CodeEntrypoint = WorkerEntrypoint & {
         	evaluate(): Promise<unknown>;
         };
         
         export default {
         	async fetch(request: Request, env: Env): Promise<Response> {
         		const { code } = (await request.json()) as { code: string };
         
         		const sandbox = env.LOADER.load({
         			compatibilityDate: "2026-10-08",
         			mainModule: "code.js",
         			modules: {
         				"code.js": `
         					import { WorkerEntrypoint } from "cloudflare:workers";
         
         					export class Code extends WorkerEntrypoint {
         						evaluate() {
         							${code}
         						}
         					}
         				`,
         			},
         			// Block `fetch()` and `connect()`
         			globalOutbound: null,
         			// Stop code that uses more than 50 milliseconds of CPU time
         			limits: { cpuMs: 50 },
         		});
         
         		const result = await sandbox
         			.getEntrypoint<CodeEntrypoint>("Code")
         			.evaluate();
         		return Response.json({ result });
         	},
         };

`code` is the body of `evaluate()`, so it needs a `return` statement. Code that waits without using CPU can still hold the request open, so add a timeout before you run code from other people. For an example, refer to [Build an AI code interpreter](https://developers.cloudflare.com/sandbox/get-started/build-an-ai-code-interpreter/).

  6. Run `wrangler dev`:

npmyarnpnpm
         
         npx wrangler dev
         
         yarn wrangler dev
         
         pnpm wrangler dev

  7. POST JavaScript to the URL Wrangler prints. The default is `http://localhost:8787`:
         
         curl http://localhost:8787 --request POST --json '{
           "code": "const users = [{ name: \"Ada\", role: \"admin\" }, { name: \"Grace\", role: \"user\" }]; return users.filter((u) => u.role === \"admin\").map((u) => u.name);"
         }'




The response body is `{"result":["Ada"]}`. The Worker ran the JavaScript you sent.

## Next steps

  * Let the code call methods that your Worker provides. Refer to [Bindings](https://developers.cloudflare.com/dynamic-workers/usage/bindings/).
  * Run a Linux command. Refer to [Run a Linux command](https://developers.cloudflare.com/sandbox/get-started/).
  * Use the [Loader API](https://developers.cloudflare.com/dynamic-workers/api-reference/) for `load()` and `get()`.



[PreviousRun a Linux command](https://developers.cloudflare.com/sandbox/get-started/)[NextBuild an AI code interpreter](https://developers.cloudflare.com/sandbox/get-started/build-an-ai-code-interpreter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/get-started/dynamic-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
