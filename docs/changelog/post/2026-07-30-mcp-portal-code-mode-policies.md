---
url: https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/
title: Admins can turn on Code Mode by default for MCP portal users \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:05.377571+00:00
---

# Admins can turn on Code Mode by default for MCP portal users · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 30, 2026

## Admins can turn on Code Mode by default for MCP portal users

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) now support four Code Mode policies: _Off_ , _Opt-in_ , _On by default_ , and _Enforced_. Admins can choose whether Code Mode is unavailable, optional, enabled by default, or required for every session.

Existing portals retain their current behavior. Portals that previously allowed Code Mode use _Opt-in_ , while portals that did not allow Code Mode use _Off_. New portals also use _Opt-in_ by default.

Clients turn on Code Mode for an _Opt-in_ portal with `?codemode=search_and_execute`. The _On by default_ policy lets clients opt out with `?codemode=off`, which avoids nested code execution when a client runs its own Code Mode implementation. The _Off_ and _Enforced_ policies ignore client overrides.

The Cloudflare API exposes these policies through the `code_mode` field:
    
    
    {
    	"code_mode": "default_on"
    }

The supported values are `off`, `opt_in`, `default_on`, and `enforced`. The previous `allow_code_mode` boolean is deprecated.

For configuration details and client behavior, refer to [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies).
