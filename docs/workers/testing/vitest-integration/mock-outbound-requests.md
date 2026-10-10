---
url: https://developers.cloudflare.com/workers/testing/vitest-integration/mock-outbound-requests/
title: Mock outbound requests \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:28.003499+00:00
---

# Mock outbound requests · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/vitest-integration/mock-outbound-requests/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)

  4. /[Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/)
  5. /Mock outbound requests



# Mock outbound requests

Last updated Oct 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstall dependenciesCreate a network mockMock an HTTP requestMock an outbound WebSocket

Use [`@msw/cloudflare` ↗︎](https://github.com/mswjs/cloudflare) to mock outbound HTTP and WebSocket requests with `@cloudflare/vitest-plugin`. The integration supports unit tests that call your Worker's exported handler and integration tests that call `exports.default.fetch()`.

## Install dependencies

Install Mock Service Worker (MSW) version 3 or later and the Cloudflare integration:

npmyarnpnpmbun
    
    
    npm i -D msw@^3.0.0 @msw/cloudflare
    
    
    yarn add -D msw@^3.0.0 @msw/cloudflare
    
    
    pnpm add -D msw@^3.0.0 @msw/cloudflare
    
    
    bun add -d msw@^3.0.0 @msw/cloudflare

## Create a network mock

Create a shared network mock for your tests:

test/network.jsjs
    
    
    import { setupNetwork } from "@msw/cloudflare";
    
    export const network = setupNetwork();

test/network.tsts
    
    
    import { setupNetwork } from "@msw/cloudflare";
    
    export const network = setupNetwork();

In a Vitest setup file, start the mock before tests, reset handlers after each test, and stop it after tests finish:

test/setup.jsjs
    
    
    import { afterAll, afterEach, beforeAll } from "vitest";
    import { network } from "./network";
    
    beforeAll(() => network.enable());
    afterEach(() => network.resetHandlers());
    afterAll(() => network.disable());

test/setup.tsts
    
    
    import { afterAll, afterEach, beforeAll } from "vitest";
    import { network } from "./network";
    
    beforeAll(() => network.enable());
    afterEach(() => network.resetHandlers());
    afterAll(() => network.disable());

Add the setup file to the `setupFiles` array in your Vitest configuration.

## Mock an HTTP request

Use `network.use()` and MSW request handlers to return a response for an outbound request. This example tests a Worker that requests a greeting from an external API:

src/index.jsjs
    
    
    export default {
    	async fetch() {
    		return fetch("https://api.example.com/greeting");
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(): Promise<Response> {
    		return fetch("https://api.example.com/greeting");
    	},
    } satisfies ExportedHandler;

test/worker.test.jsjs
    
    
    import {
    	createExecutionContext,
    	waitOnExecutionContext,
    } from "cloudflare:test";
    import { env } from "cloudflare:workers";
    import { http, HttpResponse } from "msw";
    import { expect, it } from "vitest";
    import worker from "../src";
    import { network } from "./network";
    
    it("mocks an outbound request", async () => {
    	network.use(
    		http.get("https://api.example.com/greeting", () => {
    			return HttpResponse.json({ message: "Hello" });
    		}),
    	);
    
    	const ctx = createExecutionContext();
    	const response = await worker.fetch(
    		new Request("https://example.com"),
    		env,
    		ctx,
    	);
    	await waitOnExecutionContext(ctx);
    	expect(await response.json()).toEqual({ message: "Hello" });
    });

test/worker.test.tsts
    
    
    import {
    	createExecutionContext,
    	waitOnExecutionContext,
    } from "cloudflare:test";
    import { env } from "cloudflare:workers";
    import { http, HttpResponse } from "msw";
    import { expect, it } from "vitest";
    import worker from "../src";
    import { network } from "./network";
    
    it("mocks an outbound request", async () => {
    	network.use(
    		http.get("https://api.example.com/greeting", () => {
    			return HttpResponse.json({ message: "Hello" });
    		}),
    	);
    
    	const ctx = createExecutionContext();
    	const response = await worker.fetch(
    		new Request("https://example.com"),
    		env,
    		ctx,
    	);
    	await waitOnExecutionContext(ctx);
    	expect(await response.json()).toEqual({ message: "Hello" });
    });

## Mock an outbound WebSocket

Use MSW's `ws.link()` API to mock a WebSocket connection created by your Worker. The [request-mocking fixture ↗︎](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/request-mocking) includes HTTP, `exports.default.fetch()`, and WebSocket examples.

[PreviousConfiguration](https://developers.cloudflare.com/workers/testing/vitest-integration/configuration/)[NextTest APIs](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/vitest-integration/mock-outbound-requests.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
