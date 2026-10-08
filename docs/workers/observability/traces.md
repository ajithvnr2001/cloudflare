---
url: https://developers.cloudflare.com/workers/observability/traces/
title: Traces \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:36.655656+00:00
---

# Traces · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/observability/traces/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Observability](https://developers.cloudflare.com/workers/observability/)
  4. /Traces



# Traces

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/observability/traces/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview What is Workers tracing? Automatic instrumentation Custom spans How to enable tracing Exporting OpenTelemetry traces to a 3rd party destination Sampling Limits and pricing

### What is Workers tracing?

Tracing gives you end-to-end visibility into the life of a request as it travels through your Workers application and connected services. This helps you identify performance bottlenecks, debug issues, and understand complex request flows. With tracing you can answer questions such as:

  * What is the cause of a long-running request?
  * How long do subrequests from my Worker take?
  * How long are my calls to my KV Namespace or R2 bucket taking?

![Example trace showing a POST request to a cake shop with multiple spans including fetch requests and durable object operations](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1348,height=414,format=webp/_astro/wobs_waterfall_trace_122.BveqL__z.png)

### Automatic instrumentation

Cloudflare Workers provides tracing instrumentation **out of the box** — no code changes or SDK are required. Simply enable tracing on your Worker and Cloudflare automatically captures telemetry data for:

  * **Fetch calls** — All outbound HTTP requests, capturing timing, status codes, and request metadata. This enables you to quickly identify how external dependencies affect your application's performance.
  * **Binding calls** — Interactions with various Worker bindings such as KV reads and writes, R2 object storage operations and Durable Object invocations.
  * **RPC calls** — Calls between Workers and Durable Objects, including caller-side session spans and individual method-call spans.
  * **Handler calls** — The complete lifecycle of each Worker invocation, including triggers such as [fetch handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/), [scheduled handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/), and [queue handlers](https://developers.cloudflare.com/queues/configuration/javascript-apis/#consumer).



For a full list of instrumented operations, refer to the [spans and attributes documentation](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/).

### Custom spans

You can also create your own spans to trace application-specific logic. Custom spans nest automatically with the built-in instrumentation, giving you end-to-end visibility across both platform operations and your own code.

For more information, refer to [Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).

### How to enable tracing

You can configure tracing by setting `observability.traces.enabled = true` in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/#observability).
    
    
    {
    	"observability": {
    		"traces": {
    			"enabled": true,
    			// optional sampling rate (recommended for high-traffic workloads)
    			"head_sampling_rate": 0.05
    		}
    	}
    }
    
    
    [observability.traces]
    enabled = true
    head_sampling_rate = 0.05

Note

In the future, Cloudflare plans to enable automatic tracing in addition to logs when you set `observability.enabled = true` in your Wrangler configuration.

While automatic tracing is in early beta, this setting will not enable tracing by default, and will only enable logs.

An updated [`compatibility_date`](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) will be required for this change to take effect.

### Exporting OpenTelemetry traces to a 3rd party destination

Workers tracing follows [OpenTelemetry (OTel) standards ↗︎](https://opentelemetry.io/). This makes it compatible with popular observability platforms, such as [Honeycomb](https://developers.cloudflare.com/observability/export/opentelemetry/honeycomb/), [Grafana Cloud](https://developers.cloudflare.com/observability/export/opentelemetry/grafana-cloud/), and [Axiom](https://developers.cloudflare.com/observability/export/opentelemetry/axiom/), while requiring zero development effort from you. If your observability provider has an available OpenTelemetry endpoint, you can export traces (and logs)!

You can also set `persist: false` to export traces to your destination without persisting them in the Cloudflare dashboard. This allows you to use a third-party observability provider as your sole traces destination.

To export OpenTelemetry data from Workers, refer to [OpenTelemetry export](https://developers.cloudflare.com/workers/observability/opentelemetry-export/).

### Sampling

Default Sampling Rate

The default sampling rate is `1`, meaning 100% of requests will be traced if tracing is enabled. Set `head_sampling_rate` if you want to trace fewer requests.

With sampling, you can trace a percentage of incoming requests in your Cloudflare Worker. This allows you to manage volume and costs, while still providing meaningful insights into your application.

The valid sampling range is from `0` to `1`, where `0` indicates zero out of one hundred invocations will be traced, and `1` indicates every requests will be traced, and a number such a `0.05` indicates five out of one hundred requests will be traced.

If you have not specified a sampling rate, it defaults to `1`, meaning 100% of requests will be traced.
    
    
    {
    	"observability": {
    		"traces": {
    			"enabled": true,
    			// set tracing sampling rate to 5%
    			"head_sampling_rate": 0.05
    		},
    		"logs": {
    			"enabled": true,
    			// set logging sampling rate to 60%
    			"head_sampling_rate": 0.6
    		}
    	}
    }
    
    
    [observability.traces]
    enabled = true
    head_sampling_rate = 0.05
    
    [observability.logs]
    enabled = true
    head_sampling_rate = 0.6

If you have `head_sampling_rate` configured for logs, you can also create a separate rate for traces.

Sampling is [head-based ↗︎](https://opentelemetry.io/docs/concepts/sampling/#head-sampling), meaning that non-traced requests do not incur any tracing overhead.

### Limits and pricing

Workers traces have seven-day retention. Beginning December 1, 2026, stored traces contribute to account-level ingestion and storage usage under [Cloudflare Observability pricing](https://developers.cloudflare.com/observability/pricing/).

Sampling reduces the number of spans ingested and stored, which reduces billable usage.

[PreviousWorkers Logpush](https://developers.cloudflare.com/workers/observability/logs/logpush/)[NextCustom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/observability/traces/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
