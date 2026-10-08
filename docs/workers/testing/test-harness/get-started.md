---
url: https://developers.cloudflare.com/workers/testing/test-harness/get-started/
title: Get started \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:57.351919+00:00
---

# Get started · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/test-harness/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)

  4. /[Integration test harness](https://developers.cloudflare.com/workers/testing/test-harness/)
  5. /Get started



# Get started

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/test-harness/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCreate a test harnessManage the test harness lifecycleWrite your first test

This guide shows how to write a basic integration test for a Worker with `createTestHarness()`. The example uses Vitest as the test runner and exercises a Worker built with Wrangler.

## Prerequisites

You need:

  * A Worker project with a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/)
  * A Node.js test runner such as [Vitest ↗︎](https://vitest.dev/)
  * `wrangler` installed as a development dependency



## Create a test harness

Import `createTestHarness()` from `wrangler`. Point the test harness at your Worker configuration file.

test/index.test.jsjs
    
    
    import { createTestHarness } from "wrangler";
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc" }],
    });

test/index.test.tsts
    
    
    import { createTestHarness } from "wrangler";
    
    const server = createTestHarness({
    	workers: [{ configPath: "./wrangler.jsonc" }],
    });

## Manage the test harness lifecycle

For simplicity, we will reuse a single server for the test suite and reset it after each test. You can also start a new server for each test if the tests do not share the same configuration.

test/index.test.jsjs
    
    
    import { afterAll, afterEach, beforeAll } from "vitest";
    
    beforeAll(async () => {
    	// Start the server before all tests
    	await server.listen();
    });
    
    afterEach(async () => {
    	// Recreates storage and restores the original Worker options after each test
    	await server.reset();
    });
    
    afterAll(async () => {
    	// Close the server after all tests
    	await server.close();
    });

test/index.test.tsts
    
    
    import { afterAll, afterEach, beforeAll } from "vitest";
    
    beforeAll(async () => {
    	// Start the server before all tests
    	await server.listen();
    });
    
    afterEach(async () => {
    	// Recreates storage and restores the original Worker options after each test
    	await server.reset();
    });
    
    afterAll(async () => {
    	// Close the server after all tests
    	await server.close();
    });

## Write your first test

Use the [helpers](https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/) provided by the test harness to interact with the Worker and assert its behavior. For example, you can call `server.fetch()` to send a request to the Worker and assert against its response.

test/index.test.jsjs
    
    
    import { test } from "vitest";
    
    test("responds", async ({ expect }) => {
    	const response = await server.fetch("/");
    	expect(await response.text()).toBe("Hello World");
    });

test/index.test.tsts
    
    
    import { test } from "vitest";
    
    test("responds", async ({ expect }) => {
    	const response = await server.fetch("/");
    	expect(await response.text()).toBe("Hello World");
    });

[PreviousOverview](https://developers.cloudflare.com/workers/testing/test-harness/)[NextConfigure the test harness](https://developers.cloudflare.com/workers/testing/test-harness/configure/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/test-harness/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
