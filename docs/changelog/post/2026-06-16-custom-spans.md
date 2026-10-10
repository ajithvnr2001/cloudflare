---
url: https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/
title: Workers tracing now supports custom spans \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.497284+00:00
---

# Workers tracing now supports custom spans · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 16, 2026

## Workers tracing now supports custom spans

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create custom trace spans in your Workers code using `tracing.enterSpan()`. Custom spans appear alongside the automatic platform instrumentation (fetch calls, KV reads, D1 queries, and other platform operations) in your traces and OpenTelemetry exports, with correct parent-child nesting.

The API is available via `import { tracing } from "cloudflare:workers"` or through the handler context as `ctx.tracing`:
    
    
    import { tracing } from "cloudflare:workers";
    
    export default {
      async fetch(request, env, ctx) {
        return tracing.enterSpan("handleRequest", async (span) => {
          span.setAttribute("url.path", new URL(request.url).pathname);
          const data = await env.MY_KV.get("key");
          return new Response(data);
        });
      },
    };

Spans nest automatically based on the JavaScript async context, and are auto-ended when the callback returns or its returned promise settles. The `Span` object provides `setAttribute(key, value)` for attaching metadata and an `isTraced` property to check whether the current request is being sampled.

![Trace waterfall showing custom spans nested alongside automatic KV and fetch instrumentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1988,height=670,format=webp/_astro/wobs_custom_spans_screenshot.B-hsHjyv.png)

[Tracing must be enabled](https://developers.cloudflare.com/workers/observability/traces/#how-to-enable-tracing) in your Wrangler configuration for spans to be recorded.

For full API details and examples, refer to [Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).
