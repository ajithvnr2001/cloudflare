---
url: https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/
title: Session management for MCP server portals \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:44.592751+00:00
---

# Session management for MCP server portals · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 2, 2026

## Session management for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-02-mcp-portal-session-management/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support in-session management of upstream MCP server connections. Users can return to the server selection page at any time to enable or disable servers, reauthenticate, or change which data a server has access to — all without leaving their MCP client.

To return to the server selection page, ask your AI agent with a prompt like "take me back to the server selection page." The portal responds with an authorization URL via [MCP elicitation ↗︎](https://modelcontextprotocol.io/specification/2025-03-26/server/elicitation) that you open in your browser:
    
    
    https://<subdomain>.<domain>/authorize?elicitationId=<ELICITATION_ID>

From the server selection page you can:

  * **Enable or disable servers** — Toggle individual upstream MCP servers on or off. Disabling a server removes its tools from the active session, which reduces context window usage.
  * **Log out and reauthenticate** — Log out of a server and log back in to change which data the server has access to, or to reauthenticate with different permissions.



Users can also enable or disable a server inline by asking their AI agent directly, for example "enable the wiki server" or "disable my Jira server."

The portal also automatically prompts connected users to authorize new servers when an admin adds them to the portal. This requires the use of [managed OAuth](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#enable-managed-oauth-on-an-mcp-server-portal).

For more information, refer to [Manage portal sessions](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions).
