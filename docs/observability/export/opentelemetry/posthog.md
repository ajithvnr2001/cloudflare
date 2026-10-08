---
url: https://developers.cloudflare.com/observability/export/opentelemetry/posthog/
title: Export to PostHog \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:26.605462+00:00
---

# Export to PostHog · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/export/opentelemetry/posthog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /…

[Export](https://developers.cloudflare.com/observability/export/)

  4. /[OpenTelemetry export](https://developers.cloudflare.com/observability/export/opentelemetry/)
  5. /Export to PostHog



# Export to PostHog

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/observability/export/opentelemetry/posthog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Get your PostHog project API key2\. Select your PostHog endpoint3\. Configure a Cloudflare Observability destination4\. Enable export5\. View logs in PostHogTroubleshooting Logs do not appear in PostHog Fix authentication errorsRelated resources

PostHog provides product analytics, logs, and error tracking. Export Cloudflare logs to correlate them with sessions and events.

![PostHog logs view with attributes expanded and a timeline view at the top](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2580,height=1702,format=webp/_astro/posthog-example.DhJh65s7.png)

This guide configures PostHog to receive Cloudflare logs.

## Prerequisites

Before you begin, you need:

  * An active [PostHog account ↗︎](https://app.posthog.com/signup)
  * Your PostHog project API key
  * Cloudflare logs available for export



## 1\. Get your PostHog project API key

  1. Log in to your [PostHog account ↗︎](https://app.posthog.com/).
  2. Go to [**Project settings** ↗︎](https://app.posthog.com/settings/project).
  3. Find **Project API key** in the project details.
  4. Copy the project API key.



The project API key starts with `phc_`.

## 2\. Select your PostHog endpoint

PostHog uses different endpoints for each data region:

Region | Logs endpoint  
---|---  
**US** (default) | `https://us.i.posthog.com/i/v1/logs`  
**EU** | `https://eu.i.posthog.com/i/v1/logs`  
  
Find your region in your PostHog project settings. Your PostHog URL also contains `us` or `eu`.

## 3\. Configure a Cloudflare Observability destination

Caution

PostHog accepts logs through its OpenTelemetry Protocol (OTLP) endpoint. It does not accept traces through OTLP.

  1. In the Cloudflare dashboard, go to **Observability** > **Destinations**.

[ Go to **OpenTelemetry** ↗ ](https://dash.cloudflare.com/?to=/:account/observability/destinations)
  2. Select **Add destination**.

  3. Configure the destination:

     * **Destination name** : `posthog-logs`
     * **Destination type** : _Logs_
     * **OTLP endpoint** : Your PostHog regional logs endpoint
     * **Custom header name** : `Authorization`
     * **Custom header value** : `Bearer <YOUR_PROJECT_API_KEY>`
  4. Select **Save**.




![Cloudflare destination configuration for PostHog logs with destination name, type selection, OTLP endpoint, and custom headers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1194,height=1180,format=webp/_astro/posthog-example-destination-modal.Dkn5CFBP.png)

## 4\. Enable export

Creating a destination does not start exporting logs. To export [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/), [configure OpenTelemetry export for your Worker](https://developers.cloudflare.com/workers/observability/opentelemetry-export/). PostHog does not support [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/) or [Cloudflare Traces](https://developers.cloudflare.com/observability/traces/) through OTLP.

## 5\. View logs in PostHog

  1. Log in to your [PostHog account ↗︎](https://app.posthog.com/).
  2. Go to **Logs**.
  3. Review exported severity levels, timestamps, and attributes.



You can filter logs by severity, time range, attributes, and keywords.

## Troubleshooting

### Logs do not appear in PostHog

  1. Verify that the API key starts with `phc_`.
  2. Confirm that the endpoint matches your PostHog region.
  3. Check the destination status in the Cloudflare dashboard.
  4. Check whether sampling excludes the expected logs.



### Fix authentication errors

Confirm that the `Authorization` value includes the `Bearer` prefix. Also verify that the project API key remains active.

Alternatively, add the token to the endpoint query string: `https://us.i.posthog.com/i/v1/logs?token=<YOUR_PROJECT_API_KEY>`.

## Related resources

  * [PostHog logs documentation ↗︎](https://posthog.com/docs/logs)
  * [PostHog getting started with logs ↗︎](https://posthog.com/docs/logs/start-here)
  * [OpenTelemetry logs specification ↗︎](https://opentelemetry.io/docs/specs/otel/logs/)



[PreviousExport to Sentry](https://developers.cloudflare.com/observability/export/opentelemetry/sentry/)[NextPricing](https://developers.cloudflare.com/observability/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/export/opentelemetry/posthog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
