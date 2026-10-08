---
url: https://developers.cloudflare.com/workers/testing/test-harness/configure/
title: Configure the test harness \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:57.023978+00:00
---

# Configure the test harness · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/test-harness/configure/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)

  4. /[Integration test harness](https://developers.cloudflare.com/workers/testing/test-harness/)
  5. /Configure the test harness



# Configure the test harness

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/test-harness/configure/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure Worker projectsSelect a Wrangler environmentOverride variables and secretsConfigure the harness after setupReset the harness between testsPrint debug output when tests failSpecify types for Worker handles

`createTestHarness()` runs one or more Workers in a single local server. Each Worker can come from a Wrangler project or a Vite project that uses the Cloudflare Vite plugin.

## Configure Worker projects

Point each entry in the `workers` array to the Wrangler configuration file for a project:
    
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc" }],
    });
    
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc" }],
    });

For Workers built by the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), run `vite build` first so tests use the production build output:

npmyarnpnpm
    
    
    npx vite build
    
    
    yarn vite build
    
    
    pnpm vite build

The generated Wrangler configuration works like any other `configPath`. Each Worker is configured independently, so one harness can run both project types:
    
    
    const server = createTestHarness({
    	workers: [
    		// Wrangler project
    		{ configPath: "./workers/api/wrangler.jsonc" },
    		// Vite project (built output from the Cloudflare Vite plugin)
    		{ configPath: "./dist/web_worker/wrangler.json" },
    	],
    });
    
    
    const server = createTestHarness({
    	workers: [
    		// Wrangler project
    		{ configPath: "./workers/api/wrangler.jsonc" },
    		// Vite project (built output from the Cloudflare Vite plugin)
    		{ configPath: "./dist/web_worker/wrangler.json" },
    	],
    });

## Select a Wrangler environment

By default, the test harness loads the top-level Wrangler configuration. Set `env` if you want to load a specific environment from the configuration.
    
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc", env: "test" }],
    });
    
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc", env: "test" }],
    });

## Override variables and secrets

You can override `vars` and `secrets` for each Worker in the harness if you want to avoid creating a separate Wrangler environment for testing.
    
    
    const server = createTestHarness({
    	workers: [
    		{
    			configPath: "./wrangler.jsonc",
    			vars: { API_HOST: "http://identity.example.com" },
    			secrets: { API_TOKEN: "test-token" },
    		},
    	],
    });
    
    
    const server = createTestHarness({
    	workers: [
    		{
    			configPath: "./wrangler.jsonc",
    			vars: { API_HOST: "http://identity.example.com" },
    			secrets: { API_TOKEN: "test-token" },
    		},
    	],
    });

## Configure the harness after setup

If part of the Worker configuration depends on the test setup, you can call `createTestHarness()` without options and configure the harness with `server.update()` before starting the server.
    
    
    const server = createTestHarness();
    let upstream;
    
    beforeAll(async () => {
    	upstream = await startLocalApi();
    
    	await server.update({
    		workers: [
    			{
    				configPath: "./wrangler.jsonc",
    				vars: { API_HOST: upstream.url },
    			},
    		],
    	});
    
    	await server.listen();
    });
    
    afterAll(async () => {
    	await server.close();
    	await upstream.close();
    });
    
    
    const server = createTestHarness();
    let upstream: { url: string; close(): Promise<void> };
    
    beforeAll(async () => {
    	upstream = await startLocalApi();
    
    	await server.update({
    		workers: [
    			{
    				configPath: "./wrangler.jsonc",
    				vars: { API_HOST: upstream.url },
    			},
    		],
    	});
    
    	await server.listen();
    });
    
    afterAll(async () => {
    	await server.close();
    	await upstream.close();
    });

## Reset the harness between tests

When reusing a server across tests, call `server.reset()` after each test. It recreates local storage and restores Workers to the options used when the current session started.
    
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc" }],
    });
    
    afterEach(async () => {
    	await server.reset();
    });
    
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc" }],
    });
    
    afterEach(async () => {
    	await server.reset();
    });

After a reset, apply any required schema migrations and seed data again. For examples, refer to [Prepare test state](https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/).

## Print debug output when tests fail

`server.debug()` prints the server timeline and captured Workers runtime logs. Call it when a test throws an exception or fails and you need more information to debug it.

The following example uses a cleanup hook from Vitest:
    
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc" }],
    });
    
    afterEach(({ task }) => {
    	if (task.result?.state === "fail") {
    		server.debug();
    	}
    });
    
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc" }],
    });
    
    afterEach(({ task }) => {
    	if (task.result?.state === "fail") {
    		server.debug();
    	}
    });

## Specify types for Worker handles

`server.getWorker()` accepts types for the Worker environment and module exports. You can define these types manually. But to keep them aligned with your Worker, you can generate the env type from the Wrangler configuration and derive the exports from its source module.

Give each Worker a distinct environment interface so the generated declarations can be used together:

npmyarnpnpm
    
    
    npx wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv
    
    
    yarn wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv
    
    
    pnpm wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv

Repeat this command for each Worker and include the generated files in the TypeScript configuration for your tests:
    
    
    {
    	"include": ["./workers/*/worker-configuration.d.ts", "./tests/**/*.ts"]
    }

Pass the generated environment interface to `server.getWorker()`. Use `typeof import()` to derive the Worker exports from its source module:
    
    
    const apiWorker = server.getWorker("api-worker");
    
    
    const apiWorker = server.getWorker<
    	ApiEnv,
    	typeof import("../workers/api/index")
    >("api-worker");

In this example, `ApiEnv` comes from `worker-configuration.d.ts`. The module type includes the default export and its RPC methods. Re-run [`wrangler types`](https://developers.cloudflare.com/workers/languages/typescript/#generate-types) when the Worker configuration changes.

[PreviousGet started](https://developers.cloudflare.com/workers/testing/test-harness/get-started/)[NextPrepare test state](https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/test-harness/configure.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
