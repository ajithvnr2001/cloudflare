---
url: https://developers.cloudflare.com/analytics/analytics-integrations/datadog/
title: Datadog \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:10.683861+00:00
---

# Datadog · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-integrations/datadog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[Analytics integrations](https://developers.cloudflare.com/analytics/analytics-integrations/)
  4. /Datadog



# Datadog

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-integrations/datadog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOverviewTask 1 - Install the Cloudflare AppTask 2 - View the dashboard

This tutorial explains how to analyze Cloudflare metrics using the [Cloudflare Integration tile for Datadog ↗︎](https://docs.datadoghq.com/integrations/cloudflare/).

## Overview

Before viewing the Cloudflare dashboard in Datadog, note that this integration:

  * Is available to all Cloudflare customer plans (Free, Pro, Business and Enterprise)
  * Is based on the Cloudflare Analytics API
  * Provides Cloudflare web traffic and DNS metrics only
  * Does not feature data coming from request logs stored in Cloudflare Logs



## Task 1 - Install the Cloudflare App

To install the Cloudflare App for Datadog:

  1. Log in to **Datadog**.

  2. Click the **Integrations** tab.

  3. In the **search box** , start typing _Cloudflare_. The app tile should appear below the search box. ![Searching for Cloudflare App in the Datadog Integrations tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1210,height=738,format=webp/_astro/datadog-integrations.BJs60jr6.png)

  4. Click the **Cloudflare** tile to begin the installation.

  5. Next, click **Configuration** and then complete the following:

     * **Account name** : (Optional) This can be any value. It has not impact on the site data pulled from Cloudflare.

     * **Email** : This value helps keep your account safe. We recommend creating a dedicated Cloudflare user for analytics with the [_Analytics_ role](https://developers.cloudflare.com/fundamentals/manage-members/roles/) (read-only). Note that the _Analytics_ role is available to Enterprise customers only.

     * **API Key** : Enter your Cloudflare Global API key. For details refer to [API Keys](https://developers.cloudflare.com/fundamentals/api/get-started/keys/).

  6. Click **Install Integration**. ![Configuring and installing the Datadog integration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1324,height=656,format=webp/_astro/cloudflare-tile-datadog-fill-details.Bd14uPIs.png)




The Cloudflare App for Datadog should be installed now and you can view the dashboard.

## Task 2 - View the dashboard

By default, the dashboard displays metrics for all sites in your Cloudflare account. Use the dashboard filters see metrics for a specific domain.

The dashboard displays the following metrics:

  * **Threats** (threats by type, threats by country)
  * **Requests** (total requests, cached requests, uncached requests, top countries by request, requests by IP class, top content types)
  * **Bandwidth** (total bandwidth, encrypted and unencrypted traffic cached bandwidth, uncached bandwidth)
  * **Caching** (Cache hit rate, request caching rate over time)
  * **HTTP response status errors**
  * **Page views**
  * **Search Engine Bot Traffic**
  * **DNS** (DNS queries, response time, top hostnames, queries by type, stale vs. uncached queries)

![Dashboard displaying metrics for a site on a Cloudflare account](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3476,height=1732,format=webp/_astro/cloudflare-dashboard-datadog.BETjd10H.png)

[PreviousOverview](https://developers.cloudflare.com/analytics/analytics-integrations/)[NextPrometheus](https://developers.cloudflare.com/analytics/analytics-integrations/prometheus/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-integrations/datadog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
