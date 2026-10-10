---
url: https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/
title: Service token support for MCP server portals \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.963989+00:00
---

# Service token support for MCP server portals · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 26, 2026

## Service token support for MCP server portals

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now connect autonomous agents and bots to an [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) using an [Access service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/). Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow.

To set this up:

  * Add a [Service Auth policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#service-auth) that matches your service token to the portal's Access application.
  * Add a Service Auth policy that matches the same token to each linked MCP server's Access application.
  * Turn **Require user auth** off (`on_behalf: false`) for each linked server so the portal uses the admin credential instead of a per-user OAuth grant.



The bot connects with `CF-Access-Client-Id` and `CF-Access-Client-Secret` headers and sees the tools from every linked server it is authorized for. Servers that still require per-user OAuth are excluded from service token sessions because a service token cannot complete a per-user OAuth grant.

For step-by-step setup, refer to [Connect with a service token](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token).
