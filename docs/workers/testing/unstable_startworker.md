---
url: https://developers.cloudflare.com/workers/testing/unstable_startworker/
title: Wrangler's unstable_startWorker() \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:58.081571+00:00
---

# Wrangler's unstable_startWorker() · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/unstable_startworker/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Testing](https://developers.cloudflare.com/workers/testing/)
  4. /Wrangler's unstable_startWorker()



# Wrangler's unstable_startWorker()

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/unstable_startworker/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Caution

`unstable_startWorker()` is deprecated. Cloudflare recommends using the [`createTestHarness()`](https://developers.cloudflare.com/workers/testing/test-harness/) API, which provides a harness specifically designed for integration testing.

The [`unstable_startWorker()`](https://developers.cloudflare.com/workers/wrangler/api/#unstable_startworker) API exposes the internals of the Wrangler dev server, and allows you to customize how it runs. Compared to using [Miniflare directly for testing](https://developers.cloudflare.com/workers/testing/miniflare/writing-tests/), you can pass in a Wrangler configuration file, and it will automatically load the configuration for you.

This example uses `node:test`, but should apply to any testing framework:
    
    
    import assert from "node:assert";
    import test, { after, before, describe } from "node:test";
    import { unstable_startWorker } from "wrangler";
    
    describe("worker", () => {
    	let worker;
    
    	before(async () => {
    		worker = await unstable_startWorker({ config: "wrangler.json" });
    	});
    
    	test("hello world", async () => {
    		assert.strictEqual(
    			await (await worker.fetch("http://example.com")).text(),
    			"Hello world",
    		);
    	});
    
    	after(async () => {
    		await worker.dispose();
    	});
    });

[PreviousR2](https://developers.cloudflare.com/workers/testing/miniflare/storage/r2/)[NextOverview](https://developers.cloudflare.com/workers/wrangler/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/unstable_startworker.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
