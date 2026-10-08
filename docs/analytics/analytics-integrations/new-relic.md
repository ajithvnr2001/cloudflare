---
url: https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/
title: New Relic \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:11.322551+00:00
---

# New Relic · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[Analytics integrations](https://developers.cloudflare.com/analytics/analytics-integrations/)
  4. /New Relic



# New Relic

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesTask 1 - Install the Cloudflare Network Logs quickstartTask 2 - View the Cloudflare Dashboards Overview Security Performance Reliability

This tutorial explains how to analyze Cloudflare metrics using the [New Relic One Cloudflare Quickstart ↗︎](https://newrelic.com/instant-observability/cloudflare/fc2bb0ac-6622-43c6-8c1f-6a4c26ab5434).

## Prerequisites

Before sending your Cloudflare log data to New Relic, make sure that you:

  * Have a Cloudflare Enterprise account with Cloudflare Logs enabled.
  * Have a New Relic account.
  * Configure [Logpush to New Relic](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/new-relic/).



## Task 1 - Install the Cloudflare Network Logs quickstart

  1. Log in to New Relic.
  2. Click the Instant Observability button (top right).
  3. Search for **Cloudflare Network Logs**.

![Cloudflare Network Logs install screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1030,format=webp/_astro/cloudflare-network-logs.CYJYSb1Z.png)

  4. Click **Install this quickstart**.
  5. Follow the steps to deploy.



## Task 2 - View the Cloudflare Dashboards

You can view your dashboards on the New Relic dashboard page. The dashboards include the following information:

### Overview

Get a quick overview of the most important metrics from your websites and applications on the Cloudflare network.

![Cloudflare Network Logs install screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1407,height=817,format=webp/_astro/dash-1.CTd2mveX.png)

### Security

Get insights on threats to your websites and applications, including number of threats taken action on by the Web Application Firewall (WAF), threats over time, top threat countries, and more.

![Cloudflare Network security metrics screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1402,height=511,format=webp/_astro/dash-2.DpiyWwxC.png)

### Performance

Identify and address performance issues and caching misconfigurations. Metrics include total requests, total versus cached requests, total versus origin requests.

![Cloudflare Network Logs performance metrics screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1400,height=609,format=webp/_astro/dash-3.DMdRroU0.png)

### Reliability

Get insights on the availability of your websites and Applications. Metrics include, edge response status over time, percentage of `3xx`/`4xx`/`5xx` errors over time, and more.

![Cloudflare Network Logs reliability metrics screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=929,height=510,format=webp/_astro/dash-4.BIqk6bUl.png)

[PreviousGraylog](https://developers.cloudflare.com/analytics/analytics-integrations/graylog/)[NextOverview](https://developers.cloudflare.com/analytics/analytics-integrations/splunk/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-integrations/new-relic.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
