---
url: https://developers.cloudflare.com/workers/runtime-apis/scheduler/
title: Scheduler \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:49.112373+00:00
---

# Scheduler · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/scheduler/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)
  4. /Scheduler



# Scheduler

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/scheduler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundSyntaxParametersReturn valueExamples Basic delay Retry with exponential backoff Cancel with AbortSignalRelated resources

## Background

The `scheduler` global provides task scheduling APIs based on the [WICG Scheduling APIs proposal ↗︎](https://github.com/WICG/scheduling-apis). Workers currently implement the `scheduler.wait()` method.

`scheduler.wait()` returns a Promise that resolves after a given number of milliseconds. It is an `await`-able alternative to `setTimeout()` that does not require a callback.

Like other [timers in Workers](https://developers.cloudflare.com/workers/runtime-apis/web-standards/#timers), `scheduler.wait()` does not advance during CPU execution when deployed to Cloudflare. This is a [security measure to mitigate against Spectre attacks](https://developers.cloudflare.com/workers/reference/security-model/#step-1-disallow-timers-and-multi-threading). In local development, timers advance regardless of whether I/O occurs.

## Syntax
    
    
    await scheduler.wait(delay);
    await scheduler.wait(delay, options);

## Parameters

  * `delay` number

    * The number of milliseconds to wait before the returned Promise resolves.
  * `options` object optional

    * Optional configuration for the wait operation.

    * `signal` AbortSignal optional

      * An [`AbortSignal`](https://developers.cloudflare.com/workers/runtime-apis/web-standards/#abortcontroller-and-abortsignal) that cancels the wait. When the signal is aborted, the returned Promise rejects with an `AbortError`.



## Return value

A `Promise<void>` that resolves after `delay` milliseconds. If an `AbortSignal` is provided and aborted before the delay elapses, the Promise rejects with an `AbortError`.

## Examples

### Basic delay

Use `scheduler.wait()` to pause execution for a specified duration.
    
    
    export default {
    	async fetch(request) {
    		// Wait for 1 second
    		await scheduler.wait(1000);
    		return new Response("Delayed response");
    	},
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		// Wait for 1 second
    		await scheduler.wait(1000);
    		return new Response("Delayed response");
    	},
    } satisfies ExportedHandler;

### Retry with exponential backoff

Use `scheduler.wait()` to implement a delay between retry attempts. This example uses exponential backoff with jitter.
    
    
    async function fetchWithRetry(url, maxAttempts = 3) {
    	const baseBackoffMs = 100;
    	const maxBackoffMs = 10000;
    
    	for (let attempt = 0; attempt < maxAttempts; attempt++) {
    		try {
    			return await fetch(url);
    		} catch (err) {
    			if (attempt + 1 >= maxAttempts) {
    				throw err;
    			}
    			const backoffMs = Math.min(
    				maxBackoffMs,
    				baseBackoffMs * Math.random() * Math.pow(2, attempt),
    			);
    			await scheduler.wait(backoffMs);
    		}
    	}
    	throw new Error("unreachable");
    }
    
    export default {
    	async fetch(request) {
    		const response = await fetchWithRetry("https://example.com/api");
    		return new Response(response.body, response);
    	},
    };
    
    
    async function fetchWithRetry(url: string, maxAttempts = 3): Promise<Response> {
    	const baseBackoffMs = 100;
    	const maxBackoffMs = 10000;
    
    	for (let attempt = 0; attempt < maxAttempts; attempt++) {
    		try {
    			return await fetch(url);
    		} catch (err) {
    			if (attempt + 1 >= maxAttempts) {
    				throw err;
    			}
    			const backoffMs = Math.min(
    				maxBackoffMs,
    				baseBackoffMs * Math.random() * Math.pow(2, attempt),
    			);
    			await scheduler.wait(backoffMs);
    		}
    	}
    	throw new Error("unreachable");
    }
    
    export default {
    	async fetch(request): Promise<Response> {
    		const response = await fetchWithRetry("https://example.com/api");
    		return new Response(response.body, response);
    	},
    } satisfies ExportedHandler;

### Cancel with AbortSignal

Use an [`AbortController`](https://developers.cloudflare.com/workers/runtime-apis/web-standards/#abortcontroller-and-abortsignal) to cancel a pending wait.
    
    
    export default {
    	async fetch(request) {
    		const controller = new AbortController();
    
    		// Cancel the wait after 500ms
    		setTimeout(() => controller.abort(), 500);
    
    		try {
    			await scheduler.wait(5000, { signal: controller.signal });
    			return new Response("Wait completed");
    		} catch (err) {
    			if (err instanceof DOMException && err.name === "AbortError") {
    				return new Response("Wait was cancelled", { status: 408 });
    			}
    			throw err;
    		}
    	},
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		const controller = new AbortController();
    
    		// Cancel the wait after 500ms
    		setTimeout(() => controller.abort(), 500);
    
    		try {
    			await scheduler.wait(5000, { signal: controller.signal });
    			return new Response("Wait completed");
    		} catch (err) {
    			if (err instanceof DOMException && err.name === "AbortError") {
    				return new Response("Wait was cancelled", { status: 408 });
    			}
    			throw err;
    		}
    	},
    } satisfies ExportedHandler;

## Related resources

  * [Timers](https://developers.cloudflare.com/workers/runtime-apis/web-standards/#timers) — `setTimeout()` and `setInterval()` APIs
  * [Performance and timers](https://developers.cloudflare.com/workers/runtime-apis/performance/) — `performance.now()` and timer security behavior
  * [AbortController and AbortSignal](https://developers.cloudflare.com/workers/runtime-apis/web-standards/#abortcontroller-and-abortsignal) — cancel asynchronous operations
  * [WICG Scheduling APIs proposal ↗︎](https://github.com/WICG/scheduling-apis) — the specification this API is based on



[PreviousResponse](https://developers.cloudflare.com/workers/runtime-apis/response/)[NextOverview](https://developers.cloudflare.com/workers/runtime-apis/streams/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/scheduler.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
