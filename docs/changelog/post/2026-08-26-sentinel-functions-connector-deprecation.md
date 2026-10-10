---
url: https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/
title: Azure Functions-based Microsoft Sentinel connector deprecation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.104104+00:00
---

# Azure Functions-based Microsoft Sentinel connector deprecation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 26, 2026

## Azure Functions-based Microsoft Sentinel connector deprecation

[Logpush Connectors](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/)[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Enterprise customers using the [Azure Functions-based Microsoft Sentinel connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview) must migrate to the [Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview) by 2026-09-14.

Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.

To migrate, follow the [Microsoft Sentinel integration setup guide](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/).

#### Additional resources

  * [Download Cloudflare's CCF Sentinel Solution ↗︎](https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview)
  * [Microsoft Sentinel data lake overview ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview)
  * [About the CCF platform ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector)



For more information, refer to Microsoft's [Azure Monitor HTTP Data Collector API deprecation notice ↗︎](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell).
