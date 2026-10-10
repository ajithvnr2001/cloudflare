---
url: https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/
title: Workers tracing \u2014 write custom spans with new startActiveSpan() and span.end() runtime APIs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.170335+00:00
---

# Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 28, 2026

## Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Workers runtime now provides built-in `tracing.startActiveSpan()` and `span.end()` APIs, allowing you to write custom spans for operations that last beyond a single callback — for example, instrumenting a stream pipeline where the span should stay open until the stream is fully consumed.

This augments the [existing API for writing custom spans](https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/), `tracing.enterSpan()`, which automatically ends a span when its callback is returned. With `startActiveSpan()`, the span remains open after the callback returns, and you call `span.end()` when the work is complete:

src/index.jsjs
    
    
    import { tracing } from "cloudflare:workers";
    
    const encoder = new TextEncoder();
    
    export default {
    	fetch() {
    		return tracing.startActiveSpan("stream-response", (span) => {
    			let timer;
    
    			const body = new ReadableStream({
    				start(controller) {
    					controller.enqueue(encoder.encode("Starting...\n"));
    
    					timer = setTimeout(() => {
    						controller.enqueue(encoder.encode("Complete.\n"));
    						controller.close();
    
    						span.setAttribute("stream.status", "complete");
    						span.end();
    					}, 1000);
    				},
    
    				cancel() {
    					if (timer !== undefined) clearTimeout(timer);
    
    					span.setAttribute("stream.status", "cancelled");
    					span.end();
    				},
    			});
    
    			return new Response(body, {
    				headers: { "content-type": "text/plain" },
    			});
    		});
    	},
    };

src/index.tsts
    
    
    import { tracing } from "cloudflare:workers";
    
    const encoder = new TextEncoder();
    
    export default {
    	fetch(): Response {
    		return tracing.startActiveSpan("stream-response", (span) => {
    			let timer: ReturnType<typeof setTimeout> | undefined;
    
    			const body = new ReadableStream<Uint8Array>({
    				start(controller) {
    					controller.enqueue(encoder.encode("Starting...\n"));
    
    					timer = setTimeout(() => {
    						controller.enqueue(encoder.encode("Complete.\n"));
    						controller.close();
    
    						span.setAttribute("stream.status", "complete");
    						span.end();
    					}, 1000);
    				},
    
    				cancel() {
    					if (timer !== undefined) clearTimeout(timer);
    
    					span.setAttribute("stream.status", "cancelled");
    					span.end();
    				},
    			});
    
    			return new Response(body, {
    				headers: { "content-type": "text/plain" },
    			});
    		});
    	},
    };

For more details, refer to the [custom spans documentation](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).
