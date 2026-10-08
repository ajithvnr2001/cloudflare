---
url: https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/
title: Run integration tests against your Worker's production build \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:04.143458+00:00
---

# Run integration tests against your Worker's production build · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 27, 2026

## Run integration tests against your Worker's production build

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now provides `createTestHarness()`, an API for running integration tests against Workers built with [Wrangler or the Cloudflare Vite plugin](https://developers.cloudflare.com/workers/testing/test-harness/configure/#configure-worker-projects) from any Node.js test runner.

The test harness starts a local Worker server with [helpers for dispatching requests, resetting storage, and inspecting runtime logs](https://developers.cloudflare.com/workers/wrangler/api/#createtestharness).

This is useful for tests that need to:

  * [Route requests across multiple Workers](https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/#test-route-dispatch-across-workers)
  * [Mock outbound `fetch()` requests](https://developers.cloudflare.com/workers/testing/test-harness/integrations/#mock-service-worker) with Node.js request mocking libraries such as [MSW ↗︎](https://mswjs.io/)
  * [Run Playwright tests against a Worker](https://developers.cloudflare.com/workers/testing/test-harness/integrations/#playwright)



For example, this test starts two Workers and mocks an upstream API:

tests/vitest.test.jsjs
    
    
    import { afterAll, afterEach, beforeAll, test } from "vitest";
    import { http, HttpResponse } from "msw";
    import { setupServer } from "msw/node";
    import { createTestHarness } from "wrangler";
    
    const network = setupServer();
    const server = createTestHarness({
    	workers: [
    		/** Includes `"routes": ["example.com/*"]` */
    		{ configPath: "./workers/web/wrangler.jsonc" },
    		/** Includes `"routes": ["api.example.com/v1/*"]` */
    		{ configPath: "./workers/api/wrangler.jsonc" },
    	],
    });
    
    beforeAll(async () => {
    	network.listen({ onUnhandledRequest: "error" });
    	await server.listen();
    });
    
    afterEach(async () => {
    	network.resetHandlers();
    	await server.reset();
    });
    
    afterAll(async () => {
    	network.close();
    	await server.close();
    });
    
    test("routes requests to each Worker", async ({ expect }) => {
    	// Mock the outbound fetch used to load user profiles.
    	network.use(
    		http.get("http://identity.example.com/profile/123", ({ params }) => {
    			return HttpResponse.json({ id: 123, name: "Ada" });
    		}),
    	);
    
    	const apiWorkerResponse = await server.fetch(
    		"http://api.example.com/v1/users/123",
    	);
    	expect(await apiWorkerResponse.json()).toEqual({
    		id: 123,
    		name: "Ada",
    	});
    
    	const webWorkerResponse = await server.fetch("http://example.com/users/123");
    	expect(await webWorkerResponse.text()).toBe("Profile: Ada");
    });

tests/vitest.test.tsts
    
    
    import { afterAll, afterEach, beforeAll, test } from "vitest";
    import { http, HttpResponse } from "msw";
    import { setupServer } from "msw/node";
    import { createTestHarness } from "wrangler";
    
    const network = setupServer();
    const server = createTestHarness({
    	workers: [
    		/** Includes `"routes": ["example.com/*"]` */
    		{ configPath: "./workers/web/wrangler.jsonc" },
    		/** Includes `"routes": ["api.example.com/v1/*"]` */
    		{ configPath: "./workers/api/wrangler.jsonc" },
    	],
    });
    
    beforeAll(async () => {
    	network.listen({ onUnhandledRequest: "error" });
    	await server.listen();
    });
    
    afterEach(async () => {
    	network.resetHandlers();
    	await server.reset();
    });
    
    afterAll(async () => {
    	network.close();
    	await server.close();
    });
    
    test("routes requests to each Worker", async ({ expect }) => {
    	// Mock the outbound fetch used to load user profiles.
    	network.use(
    		http.get("http://identity.example.com/profile/123", ({ params }) => {
    			return HttpResponse.json({ id: 123, name: "Ada" });
    		}),
    	);
    
    	const apiWorkerResponse = await server.fetch(
    		"http://api.example.com/v1/users/123",
    	);
    	expect(await apiWorkerResponse.json()).toEqual({
    		id: 123,
    		name: "Ada",
    	});
    
    	const webWorkerResponse = await server.fetch("http://example.com/users/123");
    	expect(await webWorkerResponse.text()).toBe("Profile: Ada");
    });

Cloudflare now recommends `createTestHarness()` for integration tests instead of [`unstable_startWorker()`](https://developers.cloudflare.com/workers/testing/unstable_startworker/) or [`unstable_dev()`](https://developers.cloudflare.com/workers/wrangler/api/#unstable_dev). To start a development server programmatically, use the Vite [`createServer()` ↗︎](https://vite.dev/guide/api-javascript.html#createserver) API with the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

For more information about `createTestHarness()`, refer to the [Integration test harness guide](https://developers.cloudflare.com/workers/testing/test-harness/).
