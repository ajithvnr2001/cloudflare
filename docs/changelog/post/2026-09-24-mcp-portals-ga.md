---
url: https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/
title: MCP server portals are now generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.574199+00:00
---

# MCP server portals are now generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 24, 2026

## MCP server portals are now generally available

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) are now generally available to all Cloudflare customers. A portal gives users one endpoint for approved Model Context Protocol (MCP) servers. Cloudflare Access logs tool, prompt, and resource activity.

Since the open beta, MCP server portals have added:

  * [Gateway routing](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway) for HTTP logging and data loss prevention (DLP) scanning
  * [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies) that control how portals reduce tool definitions and token use
  * [Static OAuth client credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials) for providers that do not support Dynamic Client Registration
  * [Session management](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions) for reconnecting servers and changing authorizations from the portal
  * [Service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token) for autonomous agents and machine-to-machine access
  * [Logpush support](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) for exporting portal activity to external storage or a security information and event management (SIEM) system



To create a portal and connect an MCP client, refer to [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).
