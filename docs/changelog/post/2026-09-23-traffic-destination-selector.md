---
url: https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/
title: Traffic Destination selector in Gateway policies \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:15.620142+00:00
---

# Traffic Destination selector in Gateway policies · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 23, 2026

## Traffic Destination selector in Gateway policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Destination** selector that identifies how traffic exits Cloudflare. This allows administrators to write policies that target specific off-ramp methods - for example, applying different rules to traffic destined for the public Internet compared to traffic routed through Cloudflare Tunnel or Cloudflare WAN.

#### Available traffic destination values

UI name | API value | Description  
---|---|---  
Internet | `internet` | Traffic to the public Internet  
Cloudflare WAN | `cloudflare_wan` | Traffic through a [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/) connection  
Cloudflare Tunnel | `cloudflare_tunnel` | Traffic to a private origin through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)  
Cloudflare One Client | `device_client` | Traffic to another device running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)  
Mesh | `mesh` | Traffic through a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node  
  
The selector uses the `net.offramp.type` API field in both HTTP and Network policies.

UI name | API example  
---|---  
Traffic Destination | `net.offramp.type == "internet"`  
  
For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).
