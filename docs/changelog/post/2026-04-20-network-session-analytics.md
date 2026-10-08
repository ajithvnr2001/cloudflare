---
url: https://developers.cloudflare.com/changelog/post/2026-04-20-network-session-analytics/
title: Network session analytics dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:48.002540+00:00
---

# Network session analytics dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-20-network-session-analytics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 20, 2026

## Network session analytics dashboard

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-20-network-session-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The new [Network session analytics](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/) dashboard is now available in Cloudflare One. This dashboard provides visibility into your network traffic patterns, helping you understand how traffic flows through your Cloudflare One infrastructure.

![Cloudflare One Network Session Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2926,height=1574,format=webp/_astro/cf1-network-session-analytics.Gl90hEcp.png)

#### What you can do with Network session analytics

  * **Analyze geographic distribution** : View a world map showing where your network traffic originates, with a list of top locations by session count.
  * **Monitor key metrics** : Track session count, total bytes transferred, and unique users.
  * **Identify connection issues** : Analyze connection close reasons to troubleshoot network problems.
  * **Review protocol usage** : See which network protocols (TCP, UDP, ICMP) are most used.



#### Dashboard features

  * **Summary metrics** : Session count, bytes total, and unique users
  * **Traffic by location** : World map visualization and location list with top traffic sources
  * **Top protocols** : Breakdown of TCP, UDP, ICMP, and ICMPv6 traffic
  * **Connection close reasons** : Insights into why sessions terminated (client closed, origin closed, timeouts, errors)



#### How to access

  1. Log in to [Cloudflare One ↗︎](https://dash.cloudflare.com).
  2. Go to **Zero Trust** > **Insights** > **Dashboards**.
  3. Select **Network session analytics**.



For more information, refer to the [Network session analytics documentation](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/).
