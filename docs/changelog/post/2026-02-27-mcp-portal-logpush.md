---
url: https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/
title: Export MCP server portal logs with Logpush \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.115320+00:00
---

# Export MCP server portal logs with Logpush · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-27-mcp-portal-logpush/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 27, 2026

## Export MCP server portal logs with Logpush

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Availability

Only available on Enterprise plans.

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) now supports [Logpush](https://developers.cloudflare.com/logs/logpush/) integration. You can automatically export MCP server portal activity logs to third-party storage destinations or security information and event management (SIEM) tools for analysis and auditing.

#### Available log fields

The MCP server portal logs dataset includes fields such as:

  * `Datetime` — Timestamp of the request
  * `PortalID` / `PortalAUD` — Portal identifiers
  * `ServerID` / `ServerURL` — Upstream MCP server details
  * `Method` — JSON-RPC method (for example, `tools/call`, `prompts/get`, `resources/read`)
  * `ToolCallName` / `PromptGetName` / `ResourceReadURI` — Method-specific identifiers
  * `UserID` / `UserEmail` — Authenticated user information
  * `Success` / `Error` — Request outcome
  * `ServerResponseDurationMs` — Response time from upstream server



For the complete field reference, refer to [MCP portal logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/).

#### Set up Logpush

To configure Logpush for MCP server portal logs, refer to [Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

Note

MCP server portals is currently in beta.
