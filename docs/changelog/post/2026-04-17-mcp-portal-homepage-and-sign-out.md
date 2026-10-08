---
url: https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/
title: Homepage and sign-out for MCP server portals \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:47.651472+00:00
---

# Homepage and sign-out for MCP server portals · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 17, 2026

## Homepage and sign-out for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) display a homepage when users visit the portal domain in a browser.

![MCP server portal homepage showing connection status and setup instructions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1037,height=631,format=webp/_astro/portals-homepage-disconnected.BHbOwayQ.png)

The homepage shows:

  * The portal name and organization branding
  * The MCP endpoint URL with a copy button
  * Per-client connection instructions for Claude Desktop, Workers AI Playground, OpenCode, Windsurf, and other MCP clients



Authenticated users see their email address and a **Sign out** button. Selecting **Sign out** revokes all portal-level OAuth grants, deletes upstream server OAuth states, and redirects through Cloudflare Access logout. A confirmation page shows a summary of the revoked sessions.

For more information, refer to [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#portal-homepage).
