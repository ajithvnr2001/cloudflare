---
url: https://developers.cloudflare.com/observability/export/opentelemetry/honeycomb/
title: Export to Honeycomb \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:26.392805+00:00
---

# Export to Honeycomb · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/export/opentelemetry/honeycomb/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /…

[Export](https://developers.cloudflare.com/observability/export/)

  4. /[OpenTelemetry export](https://developers.cloudflare.com/observability/export/opentelemetry/)
  5. /Export to Honeycomb



# Export to Honeycomb

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/observability/export/opentelemetry/honeycomb/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Get your Honeycomb API key2\. Configure Cloudflare Observability destinations Configure a traces destination Configure a logs destination3\. Enable export

Honeycomb is an observability platform for high-cardinality telemetry data. Export Cloudflare telemetry to Honeycomb to query logs, inspect traces, and create dashboards.

![Trace view including POST request, fetch operations, durable object subrequest, and queue send, with timing information displayed on a timeline](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2196,height=704,format=webp/_astro/honeycomb-example.cEkEF1c4.png)

This guide configures Honeycomb to receive Cloudflare traces and logs.

## Prerequisites

Before you begin, you need an active [Honeycomb account ↗︎](https://ui.honeycomb.io/signup). You also need Cloudflare logs or traces to export.

## 1\. Get your Honeycomb API key

  1. Log in to your [Honeycomb account ↗︎](https://ui.honeycomb.io/).
  2. From your profile menu, select **Team Settings**.
  3. Select **Environments** , then select the gear icon.
  4. Select an environment or create one.
  5. Under **API Keys** , select **Create Ingest API Key**.
  6. Enter a descriptive name, such as `cloudflare-otel`.
  7. Select **Can create services/datasets**.
  8. Select **Create**.
  9. Copy and securely store the API key.



The API key starts with `hcaik_`.

## 2\. Configure Cloudflare Observability destinations

Honeycomb provides separate OpenTelemetry Protocol (OTLP) endpoints for traces and logs:

  * **Traces** : `https://api.honeycomb.io/v1/traces`
  * **Logs** : `https://api.honeycomb.io/v1/logs`



### Configure a traces destination

  1. In the Cloudflare dashboard, go to **Observability** > **Destinations**.

[ Go to **OpenTelemetry** ↗ ](https://dash.cloudflare.com/?to=/:account/observability/destinations)
  2. Select **Add destination**.

  3. Configure the destination:

     * **Destination name** : `honeycomb-traces`
     * **Destination type** : _Traces_
     * **OTLP endpoint** : `https://api.honeycomb.io/v1/traces`
     * **Custom header name** : `x-honeycomb-team`
     * **Custom header value** : Your Honeycomb API key
  4. Select **Save**.




### Configure a logs destination

  1. Select **Add destination** again.
  2. Configure the destination: 
     * **Destination name** : `honeycomb-logs`
     * **Destination type** : _Logs_
     * **OTLP endpoint** : `https://api.honeycomb.io/v1/logs`
     * **Custom header name** : `x-honeycomb-team`
     * **Custom header value** : Your Honeycomb API key
  3. Select **Save**.



## 3\. Enable export

Creating a destination does not start exporting telemetry. To export [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/), [configure OpenTelemetry export for your Worker](https://developers.cloudflare.com/workers/observability/opentelemetry-export/). To export [Cloudflare Traces](https://developers.cloudflare.com/observability/traces/), [configure export for your domain](https://developers.cloudflare.com/observability/traces/configuration/#export-traces).

Data may take several minutes to appear in Honeycomb.

[PreviousOverview](https://developers.cloudflare.com/observability/export/opentelemetry/)[NextExport to Grafana Cloud](https://developers.cloudflare.com/observability/export/opentelemetry/grafana-cloud/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/export/opentelemetry/honeycomb.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
