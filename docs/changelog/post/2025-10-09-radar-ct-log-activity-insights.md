---
url: https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/
title: Expanded CT log activity insights on Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.956759+00:00
---

# Expanded CT log activity insights on Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 9, 2025

## Expanded CT log activity insights on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its Certificate Transparency (CT) log insights with new stats that provide greater visibility into log activity:

  * **Log growth rate** : The average throughput of the CT log over the past 7 days, measured in certificates per hour.
  * **Included certificate count** : The total number of certificates already included in this CT log.
  * **Eligible-for-inclusion certificate count** : The number of certificates eligible for inclusion in this log but not yet included. This metric is based on certificates signed by trusted root CAs within the log’s accepted date range.
  * **Last update** : The timestamp of the most recent update to the CT log.



These new statistics have been added to the response of the [Get Certificate Log Details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/get/) API endpoint, and are displayed on the [CT log information page ↗︎](https://radar.cloudflare.com/certificate-transparency/log/nimbus2025#log-activity).

![Screenshot of the CT log activity card on the CT log information page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1598,height=441,format=webp/_astro/ct-log-activity.GHD-K7Mk.png)
