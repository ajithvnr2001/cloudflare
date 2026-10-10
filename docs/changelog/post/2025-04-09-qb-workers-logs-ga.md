---
url: https://developers.cloudflare.com/changelog/post/2025-04-09-qb-workers-logs-ga/
title: Investigate your Workers with the Query Builder in the new Observability dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.141354+00:00
---

# Investigate your Workers with the Query Builder in the new Observability dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-09-qb-workers-logs-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 9, 2025

## Investigate your Workers with the Query Builder in the new Observability dashboard

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Workers Observability dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/) offers a single place to investigate and explore your [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs).

The **Overview** tab shows logs from all your Workers in one place. The **Invocations** view groups logs together by invocation, which refers to the specific trigger that started the execution of the Worker (i.e. fetch). The **Events** view shows logs in the order they were produced, based on timestamp. Previously, you could only view logs for a single Worker.

![Workers Observability Overview Tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1680,height=626,format=webp/_astro/2025-04-09-workers-observability-overview.BKVvdscp.png)

The **Investigate** tab presents a Query Builder, which helps you write structured queries to investigate and visualize your logs. The Query Builder can help answer questions such as:

  * Which paths are experiencing the most 5XX errors?
  * What is the wall time distribution by status code for my Worker?
  * What are the slowest requests, and where are they coming from?
  * Who are my top N users?

![Workers Observability Overview Tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2650,height=1318,format=webp/_astro/2025-04-09-query-builder.CaW9IZza.png)

The Query Builder can use any field that you store in your logs as a key to visualize, filter, and group by. Use the Query Builder to quickly access your data, build visualizations, save queries, and share them with your team.

#### Workers Logs is now Generally Available

[Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs) is now Generally Available. With a [small change](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#enable-workers-logs) to your Wrangler configuration, Workers Logs ingests, indexes, and stores all logs emitted from your Workers for up to 7 days.

We've introduced a number of changes during our beta period, including:

  * Dashboard enhancements with customizable fields as columns in the Logs view and support for invocation-based grouping
  * Performance improvements to ensure no adverse impact
  * Public [API endpoints ↗︎](https://developers.cloudflare.com/api/resources/workers/subresources/observability/) for broader consumption



The API documents three endpoints: list the keys in the telemetry dataset, run a query, and list the unique values for a key. For more, visit our [REST API documentation ↗︎](https://developers.cloudflare.com/api/resources/workers/subresources/observability/).

Visit the [docs](https://developers.cloudflare.com/workers/observability/query-builder) to learn more about the capabilities and methods exposed by the Query Builder. Start using Workers Logs and the Query Builder today by enabling observability for your Workers:
    
    
    {
    	"observability": {
    		"enabled": true,
    		"logs": {
    			"invocation_logs": true,
    			"head_sampling_rate": 1 // optional. default = 1.
    		}
    	}
    }
    
    
    [observability]
    enabled = true
    
      [observability.logs]
      invocation_logs = true
      head_sampling_rate = 1
