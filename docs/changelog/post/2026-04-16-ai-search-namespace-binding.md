---
url: https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/
title: AI Search instances now include built-in storage and namespace Workers Bindings \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:47.388232+00:00
---

# AI Search instances now include built-in storage and namespace Workers Bindings · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 16, 2026

## AI Search instances now include built-in storage and namespace Workers Bindings

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

New [AI Search](https://developers.cloudflare.com/ai-search/) instances created after today will work differently. New instances come with built-in storage and a vector index, so you can upload a file, have it indexed immediately, and search it right away.

Additionally new Workers Bindings are now available to use with AI Search. The new namespace binding lets you create and manage instances at runtime, and cross-instance search API lets you query across multiple instances in one call.

#### Built-in storage and vector index

All new instances now comes with built-in storage which allows you to upload files directly to it using the [Items API](https://developers.cloudflare.com/ai-search/api/items/workers-binding/) or the dashboard. No R2 buckets to set up, no external data sources to connect first.
    
    
    const instance = env.AI_SEARCH.get("my-instance");
    
    // upload and wait for indexing to complete
    const item = await instance.items.uploadAndPoll("faq.md", content);
    
    // search immediately after indexing
    const results = await instance.search({
    	messages: [{ role: "user", content: "onboarding guide" }],
    });

#### Namespace binding

The new `ai_search_namespaces` binding replaces the previous `env.AI.autorag()` API provided through the `AI` binding. It gives your Worker access to all instances within a [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/) and lets you create, update, and delete instances at runtime without redeploying.
    
    
    // wrangler.jsonc
    {
    	"ai_search_namespaces": [
    		{
    			"binding": "AI_SEARCH",
    			"namespace": "default",
    		},
    	],
    }
    
    
    // create an instance at runtime
    const instance = await env.AI_SEARCH.create({
    	id: "my-instance",
    });

For migration details, refer to [Workers binding migration](https://developers.cloudflare.com/ai-search/api/migration/workers-binding/). For more on namespaces, refer to [Namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/).

#### Cross-instance search

Within the new AI Search binding, you now have access to a Search and Chat API on the namespace level. Pass an array of instance IDs and get one ranked list of results back.
    
    
    const results = await env.AI_SEARCH.search({
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	ai_search_options: {
    		instance_ids: ["product-docs", "customer-abc123"],
    	},
    });

Refer to [Namespace-level search](https://developers.cloudflare.com/ai-search/api/search/workers-binding/#namespace-level) for details.
