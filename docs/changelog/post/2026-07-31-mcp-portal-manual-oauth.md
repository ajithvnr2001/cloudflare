---
url: https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/
title: Static OAuth client credentials for MCP server portals \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.975441+00:00
---

# Static OAuth client credentials for MCP server portals · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 31, 2026

## Static OAuth client credentials for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.

When adding an MCP server, administrators can enter the client ID and client secret from an OAuth application registered with the upstream provider. The configuration also supports custom OAuth endpoints, scopes, and the `client_secret_post` and `client_secret_basic` token endpoint authentication methods.

Cloudflare stores the client secret encrypted. Users still authenticate to the upstream server with their own accounts when they connect through a portal.

For setup instructions, refer to [Configure manual OAuth credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials).
