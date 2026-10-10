---
url: https://developers.cloudflare.com/changelog/post/2026-07-07-workflows-billing-updates/
title: Workflows pricing adds per-step billing. Step and storage billing to start no earlier than August 10, 2026. \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.316771+00:00
---

# Workflows pricing adds per-step billing. Step and storage billing to start no earlier than August 10, 2026. · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-07-workflows-billing-updates/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2026

## Workflows pricing adds per-step billing. Step and storage billing to start no earlier than August 10, 2026.

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) pricing now includes per-step billing. Requests and CPU time billing have been enabled since the initial public beta and is not changing.

#### Workflows adds step billing

A step is each unit of work executed by a Workflow, including step operations such as [sleeping](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/) or [waiting for events](https://developers.cloudflare.com/workflows/build/events-and-parameters/).

You can query Workflows analytics, including `stepCount` for a Workflow instance, with the [GraphQL Analytics API](https://developers.cloudflare.com/workflows/observability/metrics-analytics/#query-via-the-graphql-api).

#### Steps and storage billing to take effect August 10th, 2026

Starting no earlier than August 10th, 2026, Cloudflare will begin billing for step and storage usage on Workers Paid plans.

Storage pricing has been published since Workflows became generally available and is not changing. Storage is measured as persisted Workflow state in GB-months.

Dimension | Workers Free | Workers Paid  
---|---|---  
Steps | 3,000 included per day | 500,000 included per month, then $0.80 per additional 100,000 steps  
Storage | 1 GB-month included | 1 GB-month included, then $0.20 per additional GB-month  
  
Developers on the Workers Free plan will not be charged for steps or storage beyond the included amounts.

Cloudflare will not bill step and storage usage before August 10, 2026.

You can review Workflows usage in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) before this change takes effect. To reduce costs, consider reducing the number of steps per Workflow or improving the memory efficiency of your stored state.

Refer to the [Workflows pricing](https://developers.cloudflare.com/workflows/reference/pricing/) page for full details.
