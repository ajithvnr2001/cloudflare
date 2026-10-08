---
url: https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/
title: Get started with AI Gateway automatically \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:39.137369+00:00
---

# Get started with AI Gateway automatically · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 2, 2026

## Get started with AI Gateway automatically

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-02-default-gateway/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now start using AI Gateway with a single API call — no setup required. Use `default` as your gateway ID, and AI Gateway creates one for you automatically on the first request.

To try it out, [create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `AI Gateway - Read`, `AI Gateway - Edit`, and `Workers AI - Read` permissions, then run:
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/$CLOUDFLARE_ACCOUNT_ID/default/compat/chat/completions \
      --header "cf-aig-authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'

AI Gateway gives you logging, caching, rate limiting, and access to multiple AI providers through a single endpoint. For more information, refer to [Get started](https://developers.cloudflare.com/ai-gateway/get-started/).
