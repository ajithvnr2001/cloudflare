---
url: https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/
title: AI Search (formerly AutoRAG) now with More Models To Choose From \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.620228+00:00
---

# AI Search (formerly AutoRAG) now with More Models To Choose From · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2025

## AI Search (formerly AutoRAG) now with More Models To Choose From

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AutoRAG is now AI Search! The new name marks a new and bigger mission: to make world-class search infrastructure available to every developer and business.

With AI Search you can now use models from different providers like OpenAI and Anthropic. By attaching your provider keys to the AI Gateway linked to your AI Search instance, you can use many more models for both embedding and inference.

To use AI Search with other [model providers](https://developers.cloudflare.com/ai-search/configuration/models/):

  1. **Add provider keys to AI Gateway**
     1. Go to AI > AI Gateway in the dashboard.
     2. Select or create an AI gateway.
     3. In Provider Keys, choose your provider, click Add, and enter the key.
  2. **Connect a gateway to AI Search** : When creating a new AI Search, select the AI Gateway with your provider keys. For an existing AI Search, go to Settings and switch to a gateway that has your keys under Resources.
  3. **Select models** : Embedding models are only available to be changed when creating a new AI Search. Generation model can be selected when creating a new AI Search and can be changed at any time in Settings.



Once configured, your AI Search instance will be able to reference models available through your AI Gateway when making a `/ai-search` request:
    
    
    export default {
      async fetch(request, env) {
        
        // Query your AI Search instance with a natural language question to an OpenAI model
        const result = await env.AI.autorag("my-ai-search").aiSearch({
          query: "What's new for Cloudflare Birthday Week?",
          model: "openai/gpt-5"
        });
    
        // Return only the generated answer as plain text
        return new Response(result.response, {
          headers: { "Content-Type": "text/plain" },
        });
      },
    };

In the coming weeks we will also roll out updates to align the APIs with the new name. The existing APIs will continue to be supported for the time being. Stay tuned to the [AI Search Changelog](https://developers.cloudflare.com/changelog/product/ai-search/) and [Discord ↗︎](https://discord.cloudflare.com/) for more updates!
