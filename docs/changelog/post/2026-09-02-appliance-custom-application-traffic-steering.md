---
url: https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/
title: Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:12.128198+00:00
---

# Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 2, 2026

## Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now define [custom applications](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application) for [breakout](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) and [prioritized](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/) traffic on the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard, without calling the API.

![Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-custom-application-traffic-steering.D25Ga9-d.gif)

  * In **Traffic Steering** > **Breakout traffic** or **Prioritized traffic** , select **Assign application traffic** > **Add** to create a custom application matched by **Hostnames** , **IP subnets** , and/or the new **Source subnets** field, alongside Cloudflare-managed applications.
  * Edit or delete an existing custom application from the same panel, no API round-trip required.
  * **Source subnets** lets you match traffic by its source IP range, complementing the existing [source LAN interface breakout criteria](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source).



This complements the existing API and Terraform workflow for managing applications.

For details, refer to [Breakout traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) and [Prioritized traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/).
