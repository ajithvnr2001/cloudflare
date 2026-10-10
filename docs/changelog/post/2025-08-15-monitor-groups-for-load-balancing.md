---
url: https://developers.cloudflare.com/changelog/post/2025-08-15-monitor-groups-for-load-balancing/
title: Monitor Groups for Advanced Health Checking With Load Balancing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.017059+00:00
---

# Monitor Groups for Advanced Health Checking With Load Balancing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-15-monitor-groups-for-load-balancing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 16, 2025

## Monitor Groups for Advanced Health Checking With Load Balancing

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Load Balancing now supports Monitor Groups, a powerful new way to combine multiple health monitors into a single, logical group. This allows you to create sophisticated health checks that more accurately reflect the true availability of your applications by assessing multiple services at once.

With Monitor Groups, you can ensure that all critical components of an application are healthy before sending traffic to an origin pool, enabling smarter failover decisions and greater resilience. This feature is now available via the API for customers with an Enterprise Load Balancing subscription.

#### What you can do:

  * **Combine Multiple Monitors** : Group different health monitors (for example, HTTP, TCP) that check various application components, like a primary API gateway and a specific `/login` service.
  * **Isolate Monitors for Observation** : Mark a monitor as "monitoring only" to receive alerts and data without it affecting a pool's health status or traffic steering. This is perfect for testing new checks or observing non-critical dependencies.
  * **Improve Steering Intelligence** : Latency for Dynamic Steering is automatically averaged across all active monitors in a group, providing a more holistic view of an origin's performance.



This enhancement is ideal for complex, multi-service applications where the health of one component depends on another. By aggregating health signals, Monitor Groups provide a more accurate and comprehensive assessment of your application's true status.

For detailed information and API configuration guides, please visit our [developer documentation](https://developers.cloudflare.com/load-balancing/monitors/monitor-groups) for Monitor Groups.
