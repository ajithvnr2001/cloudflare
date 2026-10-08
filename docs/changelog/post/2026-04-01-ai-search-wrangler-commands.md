---
url: https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/
title: Create, manage, search AI Search instances with Wrangler CLI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:43.906836+00:00
---

# Create, manage, search AI Search instances with Wrangler CLI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 1, 2026

## Create, manage, search AI Search instances with Wrangler CLI

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) supports a `wrangler ai-search` command namespace. Use it to manage instances from the command line.

The following commands are available:

Command | Description  
---|---  
`wrangler ai-search create` | Create a new instance with an interactive wizard  
`wrangler ai-search list` | List all instances in your account  
`wrangler ai-search get` | Get details of a specific instance  
`wrangler ai-search update` | Update the configuration of an instance  
`wrangler ai-search delete` | Delete an instance  
`wrangler ai-search search` | Run a search query against an instance  
`wrangler ai-search stats` | Get usage statistics for an instance  
  
The `create` command guides you through setup, choosing a name, source type (`r2` or `web`), and data source. You can also pass all options as flags for non-interactive use:
    
    
    wrangler ai-search create my-instance --type r2 --source my-bucket

Use `wrangler ai-search search` to query an instance directly from the CLI:
    
    
    wrangler ai-search search my-instance --query "how do I configure caching?"

All commands support `--json` for structured output that scripts and AI agents can parse directly.

For full usage details, refer to the [Wrangler commands documentation](https://developers.cloudflare.com/ai-search/wrangler-commands/).
