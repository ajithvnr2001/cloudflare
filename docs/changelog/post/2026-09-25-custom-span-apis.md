---
url: https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/
title: Workers tracing \u2014 new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:16.245371+00:00
---

# Workers tracing — new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2026

## Workers tracing — new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/) in Workers now support more of the OpenTelemetry span API, so you can instrument more of your code and record errors directly on your spans.

  * **`tracing.startSpan(name)`** creates a span without making it the active span, and returns it. Other spans do not nest under it. Call `span.end()` when the operation is complete.
  * **`tracing.getActiveSpan()`** returns the currently active span. Use it to annotate the current span from helper functions and libraries without passing the span object through your code. Outside any custom span, it returns the invocation's root span.
  * **`span.recordException(exception)`** records an exception event on a span. It accepts an `Error`, a string, or an object with a `code`, `name`, or `message`.
  * **`span.setAttributes(attributes)`** sets multiple attributes at once. `setAttribute()` and `setAttributes()` now return the span, so you can chain calls.



src/index.jsjs
    
    
    import { tracing } from "cloudflare:workers";
    
    export default {
    	async fetch(request, env) {
    		const user = await authenticate(request, env);
    
    		// Annotate the invocation's root span
    		tracing.getActiveSpan()?.setAttributes({
    			"user.id": user.id,
    			"user.plan": user.plan,
    		});
    
    		const span = tracing.startSpan("load-profile");
    		try {
    			return Response.json(await loadProfile(env, user.id));
    		} catch (err) {
    			span.recordException(err);
    			throw err;
    		} finally {
    			span.end();
    		}
    	},
    };

src/index.tsts
    
    
    import { tracing } from "cloudflare:workers";
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const user = await authenticate(request, env);
    
    		// Annotate the invocation's root span
    		tracing.getActiveSpan()?.setAttributes({
    			"user.id": user.id,
    			"user.plan": user.plan,
    		});
    
    		const span = tracing.startSpan("load-profile");
    		try {
    			return Response.json(await loadProfile(env, user.id));
    		} catch (err) {
    			span.recordException(err as Error);
    			throw err;
    		} finally {
    			span.end();
    		}
    	},
    };

For more details, refer to the [custom spans documentation](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).
