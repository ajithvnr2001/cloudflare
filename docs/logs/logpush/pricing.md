---
url: https://developers.cloudflare.com/logs/logpush/pricing/
title: Pricing \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:16.319732+00:00
---

# Pricing · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Logpush](https://developers.cloudflare.com/logs/logpush/)
  4. /Pricing



# Pricing

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLogpush pricingMeasure usageCalculate monthly chargesExport evolution Workers Logpush OpenTelemetry destinationsCloudflare billing policy

Logpush is available with self-service, usage-based pricing on Free, Pro, and Business plans. Enterprise customers continue to work with their account team. Cloudflare bills export and transformation usage after each monthly billing period.

The rates on this page apply to Logpush datasets other than [Workers Trace Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events/). Workers Logpush retains separate request-based pricing.

## Logpush pricing

Usage | Included monthly usage | Rate  
---|---|---  
Logs exported to internal destinations | 25 GB per Cloudflare account | $0.03 per additional GB  
Logs exported to external destinations | 25 GB per Cloudflare account | $0.10 per additional GB  
Logs transformed | 1 GB per Cloudflare account | $0.04 per additional GB  
  
R2 and Pipelines are internal destinations. All other destinations are external.

Note

Existing Enterprise contracts retain their current Logpush pricing through renewal. Contact your account team for contract-specific pricing.

Logpush rates do not include charges from destination services. For internal destinations, refer to [R2 pricing](https://developers.cloudflare.com/r2/pricing/) and [Pipelines pricing](https://developers.cloudflare.com/pipelines/platform/pricing/).

## Measure usage

Cloudflare measures export usage from uncompressed bytes successfully delivered. Transformation usage includes the uncompressed input bytes processed by [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/).

A transformed job can generate both transformation and export usage. Cloudflare applies the transformation rate to the input and the applicable export rate to the delivered output.

## Calculate monthly charges

Cloudflare calculates each usage component separately. Billable usage equals measured monthly usage minus that component's included usage, with a minimum of zero. Cloudflare then multiplies billable usage by the component's rate.

For example, consider an account with 40 GB of internal exports, 60 GB of external exports, and 5 GB of transformation input:

Usage | Calculation | Charge  
---|---|---  
Internal exports | (40 GB - 25 GB) x $0.03 | $0.45  
External exports | (60 GB - 25 GB) x $0.10 | $3.50  
Logs transformed | (5 GB - 1 GB) x $0.04 | $0.16  
**Total** | $0.45 + $3.50 + $0.16 | **$4.11**  
  
## Export evolution

The Export area in the Cloudflare Observability platform brings Logpush and OpenTelemetry destinations together. From one place, you can choose a dataset, configure where its data should go, and manage how it leaves Cloudflare.

Export destinations include R2, Pipelines, external storage and analytics providers, and OpenTelemetry endpoints. Whether you use Logpush or an OpenTelemetry-compatible destination, Cloudflare handles formatting, delivery, and retries.

Future pricing alignment

As Export evolves, Cloudflare plans to align its export methods with a similar usage-based pricing model. The Logpush pricing described on this page is one step toward that model.

### Workers Logpush

Workers Logpush exports Workers Trace Events and remains available with the Workers Paid plan. Each account includes 10 million requests per month, then pays $0.05 per additional million requests. This pricing does not change with the Logpush pricing described on this page.

For more information, refer to [Workers Trace Events Logpush pricing](https://developers.cloudflare.com/workers/platform/pricing/#workers-trace-events-logpush).

### OpenTelemetry destinations

OpenTelemetry destination usage is not included in Logpush GB-based pricing. It retains its event-based Workers Observability pricing and allowances.

For current rates, refer to [Cloudflare Observability pricing](https://developers.cloudflare.com/observability/pricing/).

## Cloudflare billing policy

For more information about usage billing, refer to the [Cloudflare Billing Policy](https://developers.cloudflare.com/billing/understand/billing-policy/).

[PreviousTransformers](https://developers.cloudflare.com/logs/logpush/transformers/)[NextLogpush Health Dashboards](https://developers.cloudflare.com/logs/logpush/logpush-health/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
