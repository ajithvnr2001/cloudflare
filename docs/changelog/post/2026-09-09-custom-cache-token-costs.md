---
url: https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/
title: AI Gateway custom costs support cache tokens \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:13.000685+00:00
---

# AI Gateway custom costs support cache tokens · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 9, 2026

## AI Gateway custom costs support cache tokens

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers.

Add `per_cache_read_token` or `per_cache_write_token` to the `cf-aig-custom-cost` header:
    
    
    {
    	"per_token_in": 0.000001,
    	"per_token_out": 0.000002,
    	"per_cache_read_token": 0.0000001,
    	"per_cache_write_token": 0.0000005
    }

Cache-token pricing activates when either cache rate is present. An omitted cache rate defaults to `per_token_in`. If both cache rates are omitted, AI Gateway preserves the existing input and output calculation.

Providers can include cache tokens within input tokens or report them separately. AI Gateway automatically accounts for these differences and prevents double-counting.

For more information, refer to [Custom costs](https://developers.cloudflare.com/ai-gateway/configuration/custom-costs/).
