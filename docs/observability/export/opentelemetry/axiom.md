---
url: https://developers.cloudflare.com/observability/export/opentelemetry/axiom/
title: Export to Axiom \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:26.265546+00:00
---

# Export to Axiom · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/export/opentelemetry/axiom/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /…

[Export](https://developers.cloudflare.com/observability/export/)

  4. /[OpenTelemetry export](https://developers.cloudflare.com/observability/export/opentelemetry/)
  5. /Export to Axiom



# Export to Axiom

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/observability/export/opentelemetry/axiom/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create a dataset2\. Get an Axiom API token3\. Configure a Cloudflare Observability destination4\. Enable export

Axiom stores, searches, and analyzes telemetry data. Export Cloudflare traces and logs to query data and create dashboards.

![Trace view with timing information displayed on a timeline](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3773,height=1235,format=webp/_astro/axiom-example.BRPbEoGh.png)

This guide configures Axiom to receive Cloudflare traces and logs.

## Prerequisites

Before you begin, you need an active [Axiom account ↗︎](https://app.axiom.co/register). You also need Cloudflare logs or traces to export.

## 1\. Create a dataset

Skip this step if you already have a dataset.

  1. Log in to your [Axiom account ↗︎](https://app.axiom.co/).
  2. Go to **Datasets**.
  3. Select **New Dataset**.
  4. Enter a name, such as `cloudflare-otel`.
  5. Select **Create Dataset**.



## 2\. Get an Axiom API token

  1. Go to **Settings** > **API Tokens**.
  2. Select **Create API Token**.
  3. Enter a descriptive name, such as `cloudflare-otel`.
  4. Select the **Ingest** permission.
  5. Select datasets for the token, or select **All Datasets**.
  6. Select **Create**.
  7. Copy and securely store the API token.



The API token starts with `xaat-`.

## 3\. Configure a Cloudflare Observability destination

Axiom provides separate OpenTelemetry Protocol (OTLP) endpoints for traces and logs:

  * **Traces** : `https://api.axiom.co/v1/traces`
  * **Logs** : `https://api.axiom.co/v1/logs`



  1. In the Cloudflare dashboard, go to **Observability** > **Destinations**.

[ Go to **OpenTelemetry** ↗ ](https://dash.cloudflare.com/?to=/:account/observability/destinations)
  2. Select **Add destination**.

  3. Configure the destination:

     * **Destination name** : Enter `axiom-traces` or `axiom-logs`.
     * **Destination type** : Select _Traces_ or _Logs_.
     * **OTLP endpoint** : Enter the matching Axiom endpoint.
  4. Add an authentication header:

     * **Header name** : `Authorization`
     * **Header value** : `Bearer <YOUR_API_TOKEN>`
  5. Add the dataset header:

     * **Header name** : `X-Axiom-Dataset`
     * **Header value** : Your dataset name
  6. Select **Save**.




## 4\. Enable export

Creating a destination does not start exporting telemetry. To export [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/), [configure OpenTelemetry export for your Worker](https://developers.cloudflare.com/workers/observability/opentelemetry-export/). To export [Cloudflare Traces](https://developers.cloudflare.com/observability/traces/), [configure export for your domain](https://developers.cloudflare.com/observability/traces/configuration/#export-traces).

Data may take several minutes to appear in Axiom.

[PreviousExport to Grafana Cloud](https://developers.cloudflare.com/observability/export/opentelemetry/grafana-cloud/)[NextExport to Sentry](https://developers.cloudflare.com/observability/export/opentelemetry/sentry/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/export/opentelemetry/axiom.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
