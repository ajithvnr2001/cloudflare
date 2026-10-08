---
url: https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/
title: Automatic tracing across Durable Object and Worker subrequests \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:51.955280+00:00
---

# Automatic tracing across Durable Object and Worker subrequests · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 7, 2026

## Automatic tracing across Durable Object and Worker subrequests

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now get a single unified trace across Worker-to-Worker subrequests, with trace context propagating automatically. Previously, [automatic tracing](https://developers.cloudflare.com/workers/observability/traces/) produced disconnected traces when a Worker called another Worker through a [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) or [Durable Object](https://developers.cloudflare.com/durable-objects/).

![Unified trace showing nested spans across a Durable Object subrequest and a service binding call](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1824,height=1156,format=webp/_astro/2026-04-28-worker-to-worker-context-prop.Db1qNQJL.png)

This means you can:

  * Follow a request through your entire Worker architecture in one trace view
  * See service binding and Durable Object calls as nested child spans instead of separate traces
  * Debug cross-Worker request flows in the Cloudflare dashboard or in an external observability platform via [OpenTelemetry](https://developers.cloudflare.com/workers/observability/opentelemetry-export/)



[Tracing must be enabled](https://developers.cloudflare.com/workers/observability/traces/#how-to-enable-tracing) in your Wrangler configuration for traces to be recorded. Checkout [Workers tracing](https://developers.cloudflare.com/workers/observability/traces/) to get started.

Up next, we are working on external trace context propagation using [W3C Trace Context standards ↗︎](https://www.w3.org/TR/trace-context/), which will allow traces from your Workers to link with traces from services outside of Cloudflare.
