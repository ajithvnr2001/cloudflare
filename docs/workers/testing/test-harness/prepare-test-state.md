---
url: https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/
title: Prepare test state \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:58.393566+00:00
---

# Prepare test state · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)

  4. /[Integration test harness](https://developers.cloudflare.com/workers/testing/test-harness/)
  5. /Prepare test state



# Prepare test state

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccess configured bindingsApply D1 migrationsPrepare Durable Object storageMock outbound requestsMock bindings with test Workers

An integration test may need data in local storage before it runs. It may also depend on external services that you do not want to call during the test. Use the test harness to prepare this state and replace those dependencies.

## Access configured bindings

`worker.getEnv()` returns the variables, secrets, and bindings configured for a Worker. You can [specify types](https://developers.cloudflare.com/workers/testing/test-harness/configure/#specify-types-for-worker-handles) for `server.getWorker()` so these values are typed. Then use the returned storage bindings to seed data directly from a test:
    
    
    const apiWorker = server.getWorker("api-worker");
    const env = await apiWorker.getEnv();
    
    await env.USERS.put("123", JSON.stringify({ name: "Ada" }));
    
    
    const apiWorker = server.getWorker<ApiEnv>("api-worker");
    const env = await apiWorker.getEnv();
    
    await env.USERS.put("123", JSON.stringify({ name: "Ada" }));

## Apply D1 migrations

Use `worker.applyD1Migrations(bindingName)` to read the migration settings for a D1 binding from the Wrangler configuration. It uses the configured `migrations_dir` and `migrations_pattern`. Without these options, it reads `.sql` files from the `migrations` directory relative to the configuration file.

Call it after storage is reset to apply migrations that have not already run. Then access the database with `worker.getEnv()` and seed the required rows.
    
    
    const apiWorker = server.getWorker("api-worker");
    
    beforeEach(async () => {
    	await apiWorker.applyD1Migrations("DATABASE");
    
    	const env = await apiWorker.getEnv();
    	await env.DATABASE.prepare(
    		"INSERT INTO daily_reports (date, user_ids) VALUES (?, ?)",
    	)
    		.bind("2026-05-29", JSON.stringify(["123", "456"]))
    		.run();
    });
    
    
    const apiWorker = server.getWorker<ApiEnv>("api-worker");
    
    beforeEach(async () => {
    	await apiWorker.applyD1Migrations("DATABASE");
    
    	const env = await apiWorker.getEnv();
    	await env.DATABASE.prepare(
    		"INSERT INTO daily_reports (date, user_ids) VALUES (?, ?)",
    	)
    		.bind("2026-05-29", JSON.stringify(["123", "456"]))
    		.run();
    });

## Prepare Durable Object storage

`worker.getDurableObjectStorage()` gives you access to the storage of a SQLite-backed Durable Object instance. Pass its binding name or exported class name. Then select the instance by name or ID.

The returned handle executes SQL inside the Durable Object. Use it to seed an instance before a test or inspect its state after the Worker runs.
    
    
    const worker = server.getWorker("api-worker");
    const storage = await worker.getDurableObjectStorage("COUNTER", {
    	name: "user-123",
    });
    
    await storage.exec(
    	"INSERT INTO counters (id, value) VALUES (?, ?)",
    	"user-123",
    	0,
    );
    
    await worker.fetch("/counter/user-123");
    
    const rows = await storage.exec(
    	"SELECT value FROM counters WHERE id = ?",
    	"user-123",
    );
    expect(rows).toEqual([{ value: 1 }]);
    
    
    const worker = server.getWorker<ApiEnv>("api-worker");
    const storage = await worker.getDurableObjectStorage("COUNTER", {
    	name: "user-123",
    });
    
    await storage.exec(
    	"INSERT INTO counters (id, value) VALUES (?, ?)",
    	"user-123",
    	0,
    );
    
    await worker.fetch("/counter/user-123");
    
    const rows = await storage.exec<{ value: number }>(
    	"SELECT value FROM counters WHERE id = ?",
    	"user-123",
    );
    expect(rows).toEqual([{ value: 1 }]);

## Mock outbound requests

The test harness proxies outbound `fetch()` requests from your Workers through the `globalThis.fetch()` function in your Node environment. This allows you to intercept these requests and return a predictable response in your tests.

Here is an example using `vi.spyOn()` to mock a single request. But you can also use [Mock Service Worker (MSW)](https://developers.cloudflare.com/workers/testing/test-harness/integrations/#mock-service-worker) to intercept these requests based on your preferences.
    
    
    import { afterEach, test, vi } from "vitest";
    
    afterEach(() => {
    	vi.restoreAllMocks();
    });
    
    test("loads a user profile", async ({ expect }) => {
    	vi.spyOn(globalThis, "fetch").mockImplementation(async (input, init) => {
    		const request = new Request(input, init);
    
    		if (request.url === "http://identity.example.com/profile/123") {
    			return Response.json({ id: "123", name: "Ada" });
    		}
    
    		throw new Error(`Unexpected request: ${request.method} ${request.url}`);
    	});
    
    	const worker = server.getWorker();
    	const response = await worker.fetch("/users/123");
    	expect(await response.json()).toEqual({ id: "123", name: "Ada" });
    });
    
    
    import { afterEach, test, vi } from "vitest";
    
    afterEach(() => {
    	vi.restoreAllMocks();
    });
    
    test("loads a user profile", async ({ expect }) => {
    	vi.spyOn(globalThis, "fetch").mockImplementation(async (input, init) => {
    		const request = new Request(input, init);
    
    		if (request.url === "http://identity.example.com/profile/123") {
    			return Response.json({ id: "123", name: "Ada" });
    		}
    
    		throw new Error(`Unexpected request: ${request.method} ${request.url}`);
    	});
    
    	const worker = server.getWorker();
    	const response = await worker.fetch("/users/123");
    	expect(await response.json()).toEqual({ id: "123", name: "Ada" });
    });

## Mock bindings with test Workers

Use `bindingOverrides` when you want to control the behavior of a binding. It routes the binding to a test Worker running inside the harness. For example, a test Worker can replace the Browser Rendering binding and return a known screenshot without starting a browser.

The test Worker can also expose JSRPC methods that configure its behavior. Use `worker.getExport()` to access the default export from your test.
    
    
    const server = createTestHarness({
    	workers: [
    		{
    			configPath: "./workers/web/wrangler.jsonc",
    			bindingOverrides: { BROWSER: "mock-browser" },
    		},
    		// The test Worker (mock-browser) that replaces the Browser Rendering binding
    		{ configPath: "./workers/mock-browser/wrangler.jsonc" },
    	],
    });
    
    // Access the test Worker to configure its behavior or assert its state.
    const mockBrowser = await server.getWorker("mock-browser").getExport();
    
    // Configure the screenshot to be returned through the overridden binding.
    await mockBrowser.setScreenshot([137, 80, 78, 71]);
    
    const response = await server.fetch("/reports/2026-05-29.png");
    expect(await response.bytes()).toEqual(Uint8Array.from([137, 80, 78, 71]));
    
    
    const server = createTestHarness({
    	workers: [
    		{
    			configPath: "./workers/web/wrangler.jsonc",
    			bindingOverrides: { BROWSER: "mock-browser" },
    		},
    		// The test Worker (mock-browser) that replaces the Browser Rendering binding
    		{ configPath: "./workers/mock-browser/wrangler.jsonc" },
    	],
    });
    
    // Access the test Worker to configure its behavior or assert its state.
    const mockBrowser = await server
    	.getWorker<unknown, typeof import("../workers/mock-browser")>("mock-browser")
    	.getExport();
    
    // Configure the screenshot to be returned through the overridden binding.
    await mockBrowser.setScreenshot([137, 80, 78, 71]);
    
    const response = await server.fetch("/reports/2026-05-29.png");
    expect(await response.bytes()).toEqual(Uint8Array.from([137, 80, 78, 71]));

[PreviousConfigure the test harness](https://developers.cloudflare.com/workers/testing/test-harness/configure/)[NextInteract with Workers](https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/test-harness/prepare-test-state.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
