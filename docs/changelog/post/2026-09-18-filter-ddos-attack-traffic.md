---
url: https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/
title: Filter DDoS attack traffic from Logpush jobs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:14.939904+00:00
---

# Filter DDoS attack traffic from Logpush jobs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 18, 2026

## Filter DDoS attack traffic from Logpush jobs

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Logpush jobs can now exclude identified distributed denial-of-service (DDoS) attack traffic. This option reduces attack traffic in delivered logs.

It supports the `http_requests`, `firewall_events`, and `network_analytics_logs` datasets.

In the dashboard, select **Exclude DDoS attack traffic** under **Advanced Options**. With the API, add this field to a job request:
    
    
    {
    	"filter_attack_traffic": true
    }

For more information, refer to [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#ddos-attack-traffic).
