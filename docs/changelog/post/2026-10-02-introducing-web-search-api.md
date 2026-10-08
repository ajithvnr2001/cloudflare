---
url: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/
title: Introducing Web Search API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:18.522287+00:00
---

# Introducing Web Search API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 2, 2026

## Introducing Web Search API

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Web Search API](https://developers.cloudflare.com/web-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Web Search API](https://developers.cloudflare.com/web-search/) is now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff.

At launch, you can choose between three search providers: [Ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/). All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare's [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) crawling standards.

Web Search API runs through [AI Gateway](https://developers.cloudflare.com/ai-gateway/), so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Call Web Search API with the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/websearch/ \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "What are some fun things to do in Salt Lake City as fall approaches?",
        "provider": "ceramic",
        "limit": 5,
        "options": { "gateway": { "id": "default" } }
      }'

Or from a Worker with the AI binding:
    
    
    const response = await env.AI.websearch({
    	gatewayId: "default",
    	query: "What are some fun things to do in Salt Lake City as fall approaches?",
    	provider: "exa",
    	limit: 5,
    });
    
    const results = await response.json();

To get started, refer to [How to use Web Search API](https://developers.cloudflare.com/web-search/how-to-use/).
