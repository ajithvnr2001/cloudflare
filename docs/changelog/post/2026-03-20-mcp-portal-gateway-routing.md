---
url: https://developers.cloudflare.com/changelog/post/2026-03-20-mcp-portal-gateway-routing/
title: Route MCP server portal traffic through Cloudflare Gateway \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.971677+00:00
---

# Route MCP server portal traffic through Cloudflare Gateway · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-20-mcp-portal-gateway-routing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 20, 2026

## Route MCP server portal traffic through Cloudflare Gateway

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now route traffic through [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) for richer HTTP request logging and data loss prevention (DLP) scanning.

When Gateway routing is turned on, portal traffic appears in your [Gateway HTTP logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/). You can create [Gateway HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) with [DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/) to detect and block sensitive data sent to upstream MCP servers.

Note

DLP [AI prompt profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#ai-prompt) do not apply to MCP server portal traffic.

To enable Gateway routing, go to **Access controls** > **AI controls** , edit the portal, and turn on **Route traffic through Cloudflare Gateway** under **Basic information**.

![Route MCP server portal traffic through Cloudflare Gateway](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1568,height=158,format=webp/_astro/portal-route-through-gateway.0KMUAXBm.png)

For more details, refer to [Route traffic through Gateway](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway).
