---
url: https://developers.cloudflare.com/workers/observability/
title: Observability \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:34.051636+00:00
---

# Observability · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/observability/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Observability



# Observability

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/observability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLogsTracesIssuesMetrics and analyticsQuery BuilderExporting dataDebuggingAdditional resources

Cloudflare Workers provides comprehensive observability tools to help you understand how your applications are performing, diagnose issues, and gain insights into request flows. Whether you want to use Cloudflare's native observability platform or export telemetry data to your existing monitoring stack, Workers has you covered.

## Logs

Logs are essential for troubleshooting and understanding your application's behavior. Cloudflare offers several ways to access and manage your Worker logs.

### [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)

Automatically collect, store, filter, and analyze logs in the Cloudflare dashboard.

### [Real-time logs](https://developers.cloudflare.com/workers/observability/logs/real-time-logs/)

Access log events in near real-time for immediate feedback during development and deployments.

### [Tail Workers](https://developers.cloudflare.com/workers/observability/logs/tail-workers/)

Apply custom filtering, sampling, and transformation logic to your telemetry data.

### [Workers Logpush](https://developers.cloudflare.com/workers/observability/logs/logpush/)

Send Workers Trace Event Logs to supported destinations like R2, S3, or logging providers.

## Traces

[Tracing](https://developers.cloudflare.com/workers/observability/traces/) gives you end-to-end visibility into the life of a request as it travels through your Workers application and connected services. With automatic instrumentation, Cloudflare captures telemetry data for fetch calls, binding operations (KV, R2, Durable Objects), and handler invocations - no code changes required.

## Issues

[Issues](https://developers.cloudflare.com/workers/observability/issues/) detects and groups recurring Worker failures. Investigate each occurrence and route issues to coding agents, webhooks, chat services, or incident-management tools.

## Metrics and analytics

[Metrics and analytics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/) let you monitor your Worker's health with built-in metrics including request counts, error rates, CPU time, wall time, and execution duration. View metrics per Worker or aggregated across all Workers on a zone.

## Query Builder

The [Query Builder](https://developers.cloudflare.com/workers/observability/query-builder/) helps you write structured queries to investigate and visualize your telemetry data. Build queries with filters, aggregations, and groupings to analyze logs and identify patterns.

## Exporting data

[Configure OpenTelemetry export](https://developers.cloudflare.com/workers/observability/opentelemetry-export/) for Workers logs and traces. Workers can export to any [supported OpenTelemetry destination](https://developers.cloudflare.com/observability/export/opentelemetry/).

## Debugging

### [Errors and exceptions](https://developers.cloudflare.com/workers/observability/errors/)

Understand Workers error codes and debug common issues.

### [Source maps and stack traces](https://developers.cloudflare.com/workers/observability/source-maps/)

Get readable stack traces that map back to your original source code.

### [DevTools](https://developers.cloudflare.com/workers/observability/dev-tools/)

Use Chrome DevTools for breakpoints, CPU profiling, and memory debugging during local development.

### [Local observability](https://developers.cloudflare.com/workers/local-development/local-explorer/)

Capture traces, spans, and logs from your Workers locally.

## Additional resources

### [MCP server](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/workers-observability)

Query Workers observability data using the Model Context Protocol.

### [Third-party integrations](https://developers.cloudflare.com/workers/observability/third-party-integrations/)

Integrate Workers with third-party observability platforms.

[PreviousXata](https://developers.cloudflare.com/workers/databases/third-party-integrations/xata/)[NextMetrics and analytics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/observability/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
