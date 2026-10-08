---
url: https://developers.cloudflare.com/analytics/network-analytics/get-started/
title: Get started with Network Analytics \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:15.947542+00:00
---

# Get started with Network Analytics · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/network-analytics/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[Network analytics](https://developers.cloudflare.com/analytics/network-analytics/)
  4. /Get started



# Get started

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/network-analytics/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView the Network Analytics dashboardGet Network Analytics data via APISend Network Analytics logs to a third-party serviceLimitations

Requirements

Network Analytics requires the following:

  * A Cloudflare Enterprise plan.
  * Cloudflare Magic Transit or Spectrum.
  * Cloudflare WAN.



## View the Network Analytics dashboard

  1. In the Cloudflare dashboard, go to the **Network Analytics** page.

[ Go to **Network analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/networking-insights/analytics/network-analytics/transport-analytics)
  2. Select an account that has access to Magic Transit or Spectrum.

  3. Configure the displayed data. You can [adjust the time range](https://developers.cloudflare.com/analytics/network-analytics/configure/time-range/), [select the main metric](https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/#select-high-level-metric) (total packets or total bytes), [apply filters](https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/#apply-filters), and more.




## Get Network Analytics data via API

Use the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) to query data using the available [Network Analytics nodes](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/).

## Send Network Analytics logs to a third-party service

[Create a Logpush job](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) that sends Network analytics logs to your storage service, SIEM solution, or log management provider.

## Limitations

Users with the `Analytics` role will have visibility to IDs but will not see the following on the Network Analytics dashboard:

  * Tunnel names
  * Prefix names
  * [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) rules
  * [DDoS managed rulesets](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)
  * Override names



[PreviousOverview](https://developers.cloudflare.com/analytics/network-analytics/)[NextConcepts](https://developers.cloudflare.com/analytics/network-analytics/understand/concepts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/network-analytics/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
