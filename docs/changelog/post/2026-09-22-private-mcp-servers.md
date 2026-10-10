---
url: https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/
title: Private MCP server support for MCP server portals \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.755801+00:00
---

# Private MCP server support for MCP server portals · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 22, 2026

## Private MCP server support for MCP server portals

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to MCP servers available only on your private network. The portal uses [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) to reach [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and IP addresses without exposing the MCP server to the public Internet.

Connect the server network to Cloudflare with [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/), or another [Cloudflare One connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/). Configure a private hostname or CIDR route, then turn on **Route traffic through Cloudflare Gateway** when you add the server. OAuth authorization server endpoints, such as the authorization and token endpoints, must be accessible on the public Internet. If Cloudflare automatically registers the OAuth client through Dynamic Client Registration (DCR), the registration endpoint must also be accessible on the public Internet.

For setup instructions, refer to [Connect a private MCP server](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-a-private-mcp-server).
