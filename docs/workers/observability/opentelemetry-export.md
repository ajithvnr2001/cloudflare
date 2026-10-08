---
url: https://developers.cloudflare.com/workers/observability/opentelemetry-export/
title: OpenTelemetry export \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:36.268683+00:00
---

# OpenTelemetry export · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/observability/opentelemetry-export/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Observability](https://developers.cloudflare.com/workers/observability/)
  4. /OpenTelemetry export



# OpenTelemetry export

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/observability/opentelemetry-export/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported telemetryConfigure exportKnown limitations

Workers can export OpenTelemetry-compliant logs and traces to external destinations. First, [create a destination and configure your provider](https://developers.cloudflare.com/observability/export/opentelemetry/).

## Supported telemetry

You can export these Workers telemetry types:

  * **Traces** \- Request flows through your Worker and connected services
  * **Logs** \- Application and system logs, including `console.log()` output



## Configure export

Add your destination names to your Wrangler configuration. Each name must match a destination configured in the dashboard.
    
    
    {
    	"observability": {
    		"traces": {
    			"enabled": true,
    			"destinations": ["tracing-destination-name"],
    
    			// traces sample rate of 5%
    			"head_sampling_rate": 0.05,
    
    			// optional: export without storing traces in Cloudflare
    			"persist": false
    		},
    		"logs": {
    			"enabled": true,
    			"destinations": ["logs-destination-name"],
    
    			// logs sample rate of 60%
    			"head_sampling_rate": 0.6,
    
    			// optional: export without storing logs in Cloudflare
    			"persist": false
    		}
    	}
    }
    
    
    [observability.traces]
    enabled = true
    destinations = [ "tracing-destination-name" ]
    head_sampling_rate = 0.05
    persist = false
    
    [observability.logs]
    enabled = true
    destinations = [ "logs-destination-name" ]
    head_sampling_rate = 0.6
    persist = false

`persist` and pricing

By default, `persist` is `true`. Logs and traces are exported and stored in Cloudflare. Beginning December 1, 2026, persisted data contributes to [Cloudflare Observability ingestion and storage usage](https://developers.cloudflare.com/observability/pricing/). Set `persist` to `false` if you only need data in your external destination.

Redeploy your Worker after updating its Wrangler configuration. Events may take several minutes to reach your destination.

## Known limitations

Workers infrastructure metrics and custom metrics cannot be exported through OpenTelemetry.

[PreviousSet up an automation](https://developers.cloudflare.com/workers/observability/issues/automations/)[NextErrors and exceptions](https://developers.cloudflare.com/workers/observability/errors/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/observability/opentelemetry-export.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
