---
url: https://developers.cloudflare.com/observability/traces/
title: Traces \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:26.834604+00:00
---

# Traces · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/traces/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /Traces



# Traces

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/observability/traces/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable tracingInspect a trace

Cloudflare Traces show how production requests move through Cloudflare and record traces from actual traffic on your domain. Each trace contains [spans](https://developers.cloudflare.com/observability/traces/spans/) for supported steps in the request path, such as [Rules](https://developers.cloudflare.com/rules/), request routing, [Cache](https://developers.cloudflare.com/cache/), [Workers](https://developers.cloudflare.com/workers/), and origin connections. A span records how long an operation took, its outcome, and related attributes, which helps you see where a request slowed down or failed.

![A Cloudflare trace showing request processing spans, Worker and origin operations, timing, and details for a selected span.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2638,height=1124,format=webp/_astro/full-cloudflare-trace.BdBuHOv5.png)

Use Cloudflare Traces to answer questions such as:

  * Why was a request blocked or challenged, and which [security rule](https://developers.cloudflare.com/waf/custom-rules/) took action?
  * Was the URL rewritten by a [Transform Rule](https://developers.cloudflare.com/rules/transform/) before it reached the application?
  * Which [Page Rules](https://developers.cloudflare.com/rules/page-rules/), [Snippets](https://developers.cloudflare.com/rules/snippets/), or [Workers](https://developers.cloudflare.com/workers/) handled or changed the request?
  * Was the response served from [cache](https://developers.cloudflare.com/cache/), and where was time spent between Cloudflare, the origin connection, and the application?
  * Was the behavior isolated to a particular [Cloudflare location or region](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/)?



## Enable tracing

Enable tracing separately for each domain in your account. To manage sampling, context, export destinations, and trace rules, refer to [Configuration](https://developers.cloudflare.com/observability/traces/configuration/).

## Inspect a trace

Use **Add filter** or enter a query to search across traces for the selected time range. To find the trace for one request, filter on its Ray ID.

Open a trace to see the full request path as a hierarchy of spans. Each row represents one operation, and its bar shows when the operation ran and how long it took. Expand a span to inspect its child operations, or search for a span by name.

Select a span to open its details. The detail panel shows the span status, service, trigger, span and trace IDs, duration compared to similar spans, and recorded attributes. You can search or copy the attributes while investigating the operation.

Cloudflare Trace

[Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/) simulates how Cloudflare configurations would handle a request. It does not show actual production traffic.

[PreviousDatasets](https://developers.cloudflare.com/observability/logs/datasets/)[NextConfiguration](https://developers.cloudflare.com/observability/traces/configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/traces/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
