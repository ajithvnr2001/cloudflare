---
url: https://developers.cloudflare.com/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/
title: Choose OAuth scopes for Wrangler and the Cloudflare API MCP server \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.405228+00:00
---

# Choose OAuth scopes for Wrangler and the Cloudflare API MCP server · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 22, 2026

## Choose OAuth scopes for Wrangler and the Cloudflare API MCP server

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler and the [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) now use optional OAuth scopes. During authorization, you can choose which optional scopes to grant instead of approving every scope requested by each client.

The consent dialog now includes the option to edit the permissions you grant to Wrangler or the Cloudflare API MCP server:

![OAuth consent dialog with an Edit Permissions button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1368,height=1008,format=webp/_astro/oauth-optional-scopes-review.BMp1De1d.png)

You can then choose which specific permissions to grant:

![OAuth permission editor with controls for individual scopes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1366,height=1312,format=webp/_astro/oauth-optional-scopes-edit.BXIdjwS7.png)

Required scopes remain selected. Choosing fewer optional scopes limits each tool's access to the permissions needed for your workflow.

If a command or tool call needs a scope that you declined, reauthorize the client and grant that scope.

For more information, refer to [`wrangler login`](https://developers.cloudflare.com/workers/wrangler/commands/general/#login) and [Edit optional permissions](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions).
