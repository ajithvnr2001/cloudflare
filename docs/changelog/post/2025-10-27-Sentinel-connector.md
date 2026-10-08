---
url: https://developers.cloudflare.com/changelog/post/2025-10-27-Sentinel-connector/
title: Azure Sentinel Connector \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:27.127559+00:00
---

# Azure Sentinel Connector · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-27-Sentinel-connector/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 27, 2025

## Azure Sentinel Connector

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-27-Sentinel-connector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Logpush now supports integration with [Microsoft Sentinel ↗︎](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel).The new Azure Sentinel Connector built on Microsoft’s Codeless Connector Framework (CCF), is now available. This solution replaces the previous Azure Functions-based connector, offering significant improvements in security, data control, and ease of use for customers. Logpush customers can send logs to Azure Blob Storage and configure this new Sentinel Connector to ingest those logs directly into Microsoft Sentinel.

This upgrade significantly streamlines log ingestion, improves security, and provides greater control:

  * Simplified Implementation: Easier for engineering teams to set up and maintain.
  * Cost Control: New support for Data Collection Rules (DCRs) allows you to filter and transform logs at ingestion time, offering potential cost savings.
  * Enhanced Security: CCF provides a higher level of security compared to the older Azure Functions connector.
  * Data Lake Integration: Includes native integration with Data Lake.



Find the new solution [here ↗︎](https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview) and refer to the [Cloudflare's developer documentation ↗︎](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/#supported-logs:~:text=WorkBook%20fields,-Analytic%20rules)for more information on the connector, including setup steps, supported logs and Microsoft's resources.
