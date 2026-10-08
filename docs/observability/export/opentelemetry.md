---
url: https://developers.cloudflare.com/observability/export/opentelemetry/
title: OpenTelemetry export \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:26.141493+00:00
---

# OpenTelemetry export · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/export/opentelemetry/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /[Export](https://developers.cloudflare.com/observability/export/)
  4. /OpenTelemetry export



# OpenTelemetry export

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/observability/export/opentelemetry/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported telemetryAvailable destinationsCreate a destinationEnable export for Cloudflare TracesEnable OpenTelemetry export for your WorkerCheck destination statusKnown limitations

Cloudflare exports telemetry to destinations that support the OpenTelemetry Protocol (OTLP). Use these destinations with Cloudflare telemetry and your existing observability tools.

## Supported telemetry

You can export these telemetry types:

  * [**Cloudflare Traces**](https://developers.cloudflare.com/observability/traces/) \- Traces showing production request paths through Cloudflare
  * [**Workers Traces**](https://developers.cloudflare.com/workers/observability/traces/) \- Traces showing requests through Workers and connected services
  * [**Workers Logs**](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) \- Application and system logs, including `console.log()` output



## Available destinations

These endpoint formats cover common observability providers. Check your provider documentation for current authentication requirements.

Provider | Traces endpoint | Logs endpoint  
---|---|---  
[**Honeycomb**](https://developers.cloudflare.com/observability/export/opentelemetry/honeycomb/) | `https://api.honeycomb.io/v1/traces` | `https://api.honeycomb.io/v1/logs`  
[**Grafana Cloud**](https://developers.cloudflare.com/observability/export/opentelemetry/grafana-cloud/) | `https://otlp-gateway-<REGION>.grafana.net/otlp/v1/traces` | `https://otlp-gateway-<REGION>.grafana.net/otlp/v1/logs`  
[**Firetiger** ↗︎](https://docs.firetiger.com/ingest/cloudflare-workers.html) | `https://ingest.cloud.firetiger.com/v1/traces` | `https://ingest.cloud.firetiger.com/v1/logs`  
[**Axiom**](https://developers.cloudflare.com/observability/export/opentelemetry/axiom/) | `https://api.axiom.co/v1/traces` | `https://api.axiom.co/v1/logs`  
[**Sentry**](https://developers.cloudflare.com/observability/export/opentelemetry/sentry/) | `https://<HOST>/api/<PROJECT_ID>/integration/otlp/v1/traces` | `https://<HOST>/api/<PROJECT_ID>/integration/otlp/v1/logs`  
[**Sematext** ↗︎](https://sematext.com/docs/guide/managed-otlp-endpoint/) | `https://otlp-receiver.sematext.com` (US), `https://otlp-receiver.eu.sematext.com` (EU) | `https://otlp-receiver.sematext.com` (US), `https://otlp-receiver.eu.sematext.com` (EU)  
[**PostHog**](https://developers.cloudflare.com/observability/export/opentelemetry/posthog/) | Not supported | `https://<REGION>.i.posthog.com/i/v1/logs`  
[**Datadog** ↗︎](https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest/managed_platforms/) | `https://cloudflare.integrations.otlp.<DD_SITE>/v1/traces` | `https://cloudflare.integrations.otlp.<DD_SITE>/v1/logs`  
[**New Relic** ↗︎](https://docs.newrelic.com/docs/opentelemetry/best-practices/opentelemetry-otlp/) | `https://otlp.nr-data.net/v1/traces` | `https://otlp.nr-data.net/v1/logs`  
[**Splunk Observability** ↗︎](https://dev.splunk.com/observability/reference/api/ingest_data/latest) | `https://ingest.<REALM>.signalfx.com/v2/trace/otlp` | N/A  
[**Splunk Platform** ↗︎](https://github.com/splunk/splunk-connect-for-otlp) | `http://splunk.internal:4318/v1/traces` | `http://splunk.internal:4318/v1/logs`  
[**SigNoz** ↗︎](https://signoz.io/docs/integrations/outposts/cloudflare-workers/) | `https://ingest.<region>.signoz.cloud:443/v1/traces` | `https://ingest.<region>.signoz.cloud:443/v1/logs`  
  
Authentication

Most providers require authentication headers. Check your provider documentation for specific requirements.

## Create a destination

Create an account-level Cloudflare Observability destination first.

Protocol

Cloudflare does not support the [binary format ↗︎](https://opentelemetry.io/docs/specs/otlp/#binary-protobuf-encoding) for OTLP ingestion.

![Observability Destinations dashboard showing configured destinations for Grafana and Honeycomb with their respective endpoints and status](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1794,height=750,format=webp/_astro/destinations.B-CW_OSI.png)

  1. In the Cloudflare dashboard, go to **Observability** > **Destinations**.

[ Go to **OpenTelemetry** ↗ ](https://dash.cloudflare.com/?to=/:account/observability/destinations)
  2. Select **Add destination**.

  3. Configure the destination:

     * **Destination name** \- Enter a descriptive name, such as `grafana-traces`.
     * **Destination type** \- Select _Traces_ or _Logs_.
     * **OTLP endpoint** \- Enter the provider endpoint for your telemetry type.
     * **Custom headers** \- Add any provider authentication headers.
  4. Select **Save**.




![Edit Destination dialog showing configuration for Honeycomb tracing with destination name, type selection, OTLP endpoint, and custom headers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1942,height=974,format=webp/_astro/destination-setup.B8cxx8yd.png)

## Enable export for Cloudflare Traces

Add the destination under **Export destinations** in your domain settings. Refer to [Cloudflare Traces configuration](https://developers.cloudflare.com/observability/traces/configuration/#export-traces).

## Enable OpenTelemetry export for your Worker

Configure and redeploy your Worker after creating a destination. Refer to [Workers OpenTelemetry export](https://developers.cloudflare.com/workers/observability/opentelemetry-export/).

## Check destination status

The dashboard shows each destination delivery status. The status reflects the most recent delivery attempt.

Status | Description | Troubleshooting  
---|---|---  
**Last: n minutes ago** | Cloudflare delivered data recently. | No action required  
**Never run** | Cloudflare has not delivered data. | Check source traffic, export settings, and sampling rates  
**Error** | Cloudflare could not deliver data. | Check the OTLP endpoint and authentication headers  
  
## Known limitations

Some providers do not support every OTLP telemetry type. Check the available destinations and your provider documentation.

[PreviousLogpush ↗︎](https://developers.cloudflare.com/logs/logpush/)[NextExport to Honeycomb](https://developers.cloudflare.com/observability/export/opentelemetry/honeycomb/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/export/opentelemetry/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
