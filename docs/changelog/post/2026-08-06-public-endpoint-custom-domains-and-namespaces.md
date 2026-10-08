---
url: https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/
title: AI Search makes it easier to build a search engine for your data \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.935389+00:00
---

# AI Search makes it easier to build a search engine for your data · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 6, 2026

## AI Search makes it easier to build a search engine for your data

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) gets you from a data source to a working search endpoint quickly. This release adds what you need to put that endpoint in front of real users: your own domain, authentication, and one endpoint across several instances. It also adds crawling for sites without a complete sitemap, so your index covers everything you want it to find.

Each of the following is a new option. The previous behavior is still the default, so nothing changes until you change it.

#### Serve search from your own domain

A [public endpoint](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/) is a URL that a site or app can query directly, with no authentication in front of it. By default that URL is a generated hostname on `search.ai.cloudflare.com`. You can now serve the same endpoint from a [custom domain](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/), a hostname in a zone that you own:
    
    
    https://search.example.com/search

#### Restrict who can query your content

Once your endpoint is on your own domain, you can put [Cloudflare Access](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/) in front of it. For example, you usually want to give `/mcp` to specific agents rather than to anyone who finds the URL. Agents authenticate with an Access service token, and people who open the endpoint in a browser sign in through your identity provider.

#### Search several instances from one URL

A namespace can expose its own [public endpoint](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/namespace/) with `/search`, `/chat/completions`, and `/mcp` paths that fan out across the instances you choose:
    
    
    curl https://ns-<NAMESPACE_ENDPOINT_ID>.search.ai.cloudflare.com/search \
      --header "Content-Type: application/json" \
      --data '{
        "messages": [{ "content": "How do I configure AI Search?", "role": "user" }],
        "ai_search_options": { "instance_ids": ["docs", "support"] }
      }'

#### Index your sites without a sitemap

Website data sources support a new `discover` [parse type](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/). It starts at the source URL and collects pages from both your sitemaps and the links it finds while crawling:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/instances" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "id": "my-ai-search",
        "type": "web-crawler",
        "source": "example.com",
        "source_params": {
          "web_crawler": {
            "parse_type": "discover",
            "discover_options": { "source": "links", "limit": 5000, "depth": 3 }
          }
        }
      }'

To learn more, refer to the [AI Search documentation](https://developers.cloudflare.com/ai-search/).
