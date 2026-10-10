---
url: https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/
title: Load Balancing health notifications now resolve automatically \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.421070+00:00
---

# Load Balancing health notifications now resolve automatically · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2026

## Load Balancing health notifications now resolve automatically

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/) health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.

As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.

This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by [Health Checks](https://developers.cloudflare.com/health-checks/) notifications.

Two things to keep in mind:

  * A recovery notification is matched to the earlier unhealthy notification for the **same pool or endpoint**. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.
  * If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.



Refer to [Integrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/) to learn more about routing Load Balancing health notifications to an incident management tool.
