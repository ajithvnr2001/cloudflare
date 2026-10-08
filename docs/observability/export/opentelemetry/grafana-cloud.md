---
url: https://developers.cloudflare.com/observability/export/opentelemetry/grafana-cloud/
title: Export to Grafana Cloud \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:26.226341+00:00
---

# Export to Grafana Cloud · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/export/opentelemetry/grafana-cloud/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /…

[Export](https://developers.cloudflare.com/observability/export/)

  4. /[OpenTelemetry export](https://developers.cloudflare.com/observability/export/opentelemetry/)
  5. /Export to Grafana Cloud



# Export to Grafana Cloud

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/observability/export/opentelemetry/grafana-cloud/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Get your OpenTelemetry credentials2\. Configure Cloudflare Observability destinations3\. Enable export

Grafana Cloud provides visualization, alerting, and telemetry analytics. It accepts Cloudflare telemetry through the OpenTelemetry Protocol (OTLP).

Export Cloudflare traces to Grafana Tempo and logs to Grafana Loki.

![Grafana Tempo trace view showing a distributed trace for a service with multiple spans including fetch requests, durable object subrequests, and queue operations, with timing information displayed on a timeline](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1934,height=714,format=webp/_astro/grafana-traces.CuFntNVO.png)

This guide configures Grafana Cloud to receive Cloudflare traces and logs.

## Prerequisites

Before you begin, you need an active [Grafana Cloud account ↗︎](https://grafana.com/auth/sign-up/create-user). You also need Cloudflare logs or traces to export.

## 1\. Get your OpenTelemetry credentials

  1. Log in to the [Grafana Cloud portal ↗︎](https://grafana.com/).
  2. From your organization home page, go to **Connections** > **Add new connection**.
  3. Search for `OpenTelemetry`, then select **OpenTelemetry (OTLP)**.
  4. Select **Quickstart** , then select **JavaScript**.
  5. Select **Create a new token**.
  6. Enter a token name, such as `cloudflare-otel`.
  7. Select **Create token** , then select **Close**.
  8. Copy the `OTEL_EXPORTER_OTLP_ENDPOINT` value from **Environment variables**.
  9. Copy the `OTEL_EXPORTER_OTLP_HEADERS` value from the same block.



## 2\. Configure Cloudflare Observability destinations

  1. In the Cloudflare dashboard, go to **Observability** > **Destinations**.

[ Go to **OpenTelemetry** ↗ ](https://dash.cloudflare.com/?to=/:account/observability/destinations)
  2. Select **Add destination**.

  3. Enter a descriptive destination name, such as `grafana-traces`.

  4. For **Destination type** , select _Traces_ or _Logs_. Create a separate destination for each type you export.

  5. Enter the Grafana OTLP endpoint for your telemetry type:

     * **Traces** : Append `/v1/traces` to the endpoint.
     * **Logs** : Append `/v1/logs` to the endpoint.
  6. Add the Grafana authentication header:

     * **Header name** : `Authorization`
     * **Header value** : The Basic authentication value from Grafana
  7. Select **Save**.




The endpoint resembles `https://otlp-gateway-prod-us-east-2.grafana.net/otlp`.

## 3\. Enable export

Creating a destination does not start exporting telemetry. To export [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/), [configure OpenTelemetry export for your Worker](https://developers.cloudflare.com/workers/observability/opentelemetry-export/). To export [Cloudflare Traces](https://developers.cloudflare.com/observability/traces/), [configure export for your domain](https://developers.cloudflare.com/observability/traces/configuration/#export-traces).

Data may take several minutes to appear in Grafana Cloud.

[PreviousExport to Honeycomb](https://developers.cloudflare.com/observability/export/opentelemetry/honeycomb/)[NextExport to Axiom](https://developers.cloudflare.com/observability/export/opentelemetry/axiom/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/export/opentelemetry/grafana-cloud.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
