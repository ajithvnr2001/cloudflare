---
url: https://developers.cloudflare.com/health-checks/concepts/health-checks-regions/
title: Health Checks regions \u00b7 Cloudflare Health Checks docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:28.466163+00:00
---

# Health Checks regions · Cloudflare Health Checks docs

> Source: https://developers.cloudflare.com/health-checks/concepts/health-checks-regions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Health Checks](https://developers.cloudflare.com/health-checks/)
  3. /Concepts
  4. /Health Checks regions



# Health Checks regions

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/health-checks/concepts/health-checks-regions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has data centers in [hundreds of cities worldwide ↗︎](https://www.cloudflare.com/network/). Health checks do not run from every single of these data centers as this would result in numerous requests to your servers. Instead, you are able to choose between one and thirteen regions from which to run health checks. Cloudflare will run Health Checks from three data centers in each region that you select.

Note

The exact location of these data centers are subject to change at any moment.

The Internet is not the same everywhere around the world and your users may not have the same experience on your application according to where they are. Running Health Checks from different regions lets you know the health of your application from the point of view of the Cloudflare network in each of these regions.

Analytics are presented at two levels:

  * Regional Aggregates: Combined results from the three data centers within a specific region.
  * Global Aggregates: Total results across all configured regions and data centers.



In the event log, entries are labeled by region or as **Global**. We do not provide granular data for individual data centers.

If you select multiple regions or choose **All Regions** (Business and Enterprise Only), you may increase traffic to your servers. Each region sends individual health checks from three data centers.

[PreviousHealth Checks Analytics](https://developers.cloudflare.com/health-checks/health-checks-analytics/)[NextZone Lockdown](https://developers.cloudflare.com/health-checks/how-to/zone-lockdown/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/health-checks/concepts/health-checks-regions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
