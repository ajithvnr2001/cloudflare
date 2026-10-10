---
url: https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/
title: Tool and prompt aliases for MCP server portals \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.680501+00:00
---

# Tool and prompt aliases for MCP server portals · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## Tool and prompt aliases for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you connect third-party MCP servers through [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/), you have no control over how the server author named tools or wrote descriptions. Unclear names make it harder for AI agents to select the right tool and harder for users to understand what is available.

You can now [rename tools and prompts](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases) and rewrite their descriptions directly on the portal, without modifying the upstream server. For example, a tool named `super_cool_tool` can become `search_customer_records` with a description tailored to your organization.

![Edit tool modal showing name and description fields for an MCP server tool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1640,height=1144,format=webp/_astro/portal-edit-tool-modal.DrxORhBl.png)

Modified tools display a **Modified** label in the tools list so administrators can see which tools have been customized at a glance.

![Tools authorized list showing a modified label on a renamed tool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1862,height=700,format=webp/_astro/portal-tools-authorized-modified.B674Xvip.png)

Aliases override the metadata that MCP clients receive. You can set them at two levels:

  * **Per portal** : Applies only within a specific portal. Takes precedence over server-level aliases.
  * **Per server** : Applies across all portals that use the server.



You can reset an alias at any time to restore the original upstream name.

For more information, refer to [Tool and prompt aliases](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases).
