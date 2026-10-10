---
url: https://developers.cloudflare.com/changelog/post/2025-12-18-wrangler-auth-token/
title: Retrieve your authentication token with `wrangler auth token` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.582640+00:00
---

# Retrieve your authentication token with `wrangler auth token` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-18-wrangler-auth-token/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 18, 2025

## Retrieve your authentication token with `wrangler auth token`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now includes a new [`wrangler auth token`](https://developers.cloudflare.com/workers/wrangler/commands/general/#auth-token) command that retrieves your current authentication token or credentials for use with other tools and scripts.
    
    
    wrangler auth token

The command returns whichever authentication method is currently configured, in priority order: API token from `CLOUDFLARE_API_TOKEN`, or OAuth token from `wrangler login` (automatically refreshed if expired).

Use the `--json` flag to get structured output including the token type:
    
    
    wrangler auth token --json

The JSON output includes the authentication type:
    
    
    // API token
    { "type": "api_token", "token": "..." }
    
    // OAuth token
    { "type": "oauth", "token": "..." }
    
    // API key/email (only available with --json)
    { "type": "api_key", "key": "...", "email": "..." }

API key/email credentials from `CLOUDFLARE_API_KEY` and `CLOUDFLARE_EMAIL` require the `--json` flag since this method uses two values instead of a single token.
