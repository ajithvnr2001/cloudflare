---
url: https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/
title: Leaked Credentials Insights in Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:06.841642+00:00
---

# Leaked Credentials Insights in Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 18, 2025

## Leaked Credentials Insights in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its security insights, providing visibility into aggregate trends in authentication requests, including the detection of leaked credentials through [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) scans.

We have now introduced the following endpoints:

  * [`/leaked_credential_checks/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/summary/): Retrieves summaries of HTTP authentication requests distribution across two different dimensions.
  * [`/leaked_credential_checks/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/): Retrieves timeseries data for HTTP authentication requests distribution across two different dimensions.



The following dimensions are available, displaying the distribution of HTTP authentication requests based on:

  * `compromised`: Credential status (clean vs. compromised).
  * `bot_class`: [Bot class](https://developers.cloudflare.com/radar/concepts/bot-classes) (human vs. bot).



Dive deeper into leaked credential detection in this [blog post ↗︎](https://blog.cloudflare.com/password-reuse-rampant-half-user-logins-compromised/) and learn more about the expanded Radar security insights in our [blog post ↗︎](https://blog.cloudflare.com/cloudflare-radar-ddos-leaked-credentials-bots).
