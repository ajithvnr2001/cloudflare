---
url: https://developers.cloudflare.com/observability/export/opentelemetry/sentry/
title: Export to Sentry \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:26.645757+00:00
---

# Export to Sentry · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/export/opentelemetry/sentry/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /…

[Export](https://developers.cloudflare.com/observability/export/)

  4. /[OpenTelemetry export](https://developers.cloudflare.com/observability/export/opentelemetry/)
  5. /Export to Sentry



# Export to Sentry

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/observability/export/opentelemetry/sentry/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create a Sentry project2\. Get your Sentry OTLP endpoints3\. Configure Cloudflare Observability destinations Configure a traces destination Configure a logs destination4\. Enable export

Sentry provides distributed tracing, logs, and application monitoring. Export Cloudflare telemetry to query data and create alerts or dashboards.

![Sentry trace view with timing information displayed on a timeline](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2474,height=862,format=webp/_astro/sentry-example.DU-HO2rh.png)

This guide configures Sentry to receive Cloudflare traces and logs.

## Prerequisites

Before you begin, you need an active [Sentry account ↗︎](https://sentry.io/signup/). You also need Cloudflare logs or traces to export.

## 1\. Create a Sentry project

Skip this step if you already have a project.

  1. Log in to your [Sentry account ↗︎](https://sentry.io/).
  2. Go to **Insights** > **Projects**.
  3. Select [**New Project** ↗︎](https://sentry.io/orgredirect/organizations/:orgslug/insights/projects/new/).
  4. Complete the project form, then select **Create Project**.



## 2\. Get your Sentry OTLP endpoints

Sentry provides separate OpenTelemetry Protocol (OTLP) endpoints for traces and logs:

  * **Traces** : `https://<HOST>/api/<PROJECT_ID>/integration/otlp/v1/traces`
  * **Logs** : `https://<HOST>/api/<PROJECT_ID>/integration/otlp/v1/logs`



  1. In Sentry, go to [**Settings** > **Projects** ↗︎](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/).
  2. Select your project.
  3. Under **SDK Setup** , select **Client Keys (DSN)**.
  4. Copy the OTLP endpoints and authentication header.



For endpoint details, refer to [Sentry OTLP documentation ↗︎](https://docs.sentry.io/concepts/otlp/).

## 3\. Configure Cloudflare Observability destinations

In the Cloudflare dashboard, go to **Observability** > **Destinations**.

[ Go to **OpenTelemetry** ↗ ](https://dash.cloudflare.com/?to=/:account/observability/destinations)

### Configure a traces destination

  1. Select **Add destination**.
  2. Configure the destination: 
     * **Destination name** : `sentry-traces`
     * **Destination type** : _Traces_
     * **OTLP endpoint** : Your Sentry OTLP traces endpoint
     * **Custom header name** : `x-sentry-auth`
     * **Custom header value** : `sentry sentry_key=<SENTRY_PUBLIC_KEY>`
  3. Select **Save**.



### Configure a logs destination

  1. Select **Add destination**.
  2. Configure the destination: 
     * **Destination name** : `sentry-logs`
     * **Destination type** : _Logs_
     * **OTLP endpoint** : Your Sentry OTLP logs endpoint
     * **Custom header name** : `x-sentry-auth`
     * **Custom header value** : `sentry sentry_key=<SENTRY_PUBLIC_KEY>`
  3. Select **Save**.



## 4\. Enable export

Creating a destination does not start exporting telemetry. To export [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/), [configure OpenTelemetry export for your Worker](https://developers.cloudflare.com/workers/observability/opentelemetry-export/). To export [Cloudflare Traces](https://developers.cloudflare.com/observability/traces/), [configure export for your domain](https://developers.cloudflare.com/observability/traces/configuration/#export-traces).

Data may take several minutes to appear in Sentry.

[PreviousExport to Axiom](https://developers.cloudflare.com/observability/export/opentelemetry/axiom/)[NextExport to PostHog](https://developers.cloudflare.com/observability/export/opentelemetry/posthog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/export/opentelemetry/sentry.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
