---
url: https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/
title: Manage AI Search namespaces with Wrangler CLI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.731873+00:00
---

# Manage AI Search namespaces with Wrangler CLI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 10, 2026

## Manage AI Search namespaces with Wrangler CLI

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports namespace-level Wrangler commands, making it easier to manage [namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/) from your terminal, scripts, and agent workflows.

The following commands are available:

Command | Description  
---|---  
`wrangler ai-search namespace list` | List AI Search namespaces  
`wrangler ai-search namespace create` | Create a new AI Search namespace  
`wrangler ai-search namespace get` | Get details for a namespace  
`wrangler ai-search namespace update` | Update a namespace description  
`wrangler ai-search namespace delete` | Delete an AI Search namespace  
  
Create a namespace for a new application or tenant directly from the CLI:
    
    
    wrangler ai-search namespace create docs-production --description "Production documentation search"

List namespaces with pagination or filter by name or description:
    
    
    wrangler ai-search namespace list --search docs --page 1 --per-page 10

Use `--json` with `list`, `create`, `get`, and `update` to return structured output that automation and AI agents can parse directly.

Instance-level commands also now support a `--namespace` flag, so you can interact with instances inside a specific namespace from the CLI:
    
    
    wrangler ai-search list --namespace docs-production

For full usage details, refer to the [AI Search Wrangler commands documentation](https://developers.cloudflare.com/ai-search/wrangler-commands/).
