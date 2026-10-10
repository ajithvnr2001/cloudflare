---
url: https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/
title: Reranking and API-based system prompt configuration in AI Search \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.389790+00:00
---

# Reranking and API-based system prompt configuration in AI Search · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 28, 2025

## Reranking and API-based system prompt configuration in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports reranking for improved retrieval quality and allows you to set the system prompt directly in your API requests.

#### Rerank for more relevant results

You can now enable [reranking](https://developers.cloudflare.com/ai-search/configuration/retrieval/reranking/) to reorder retrieved documents based on their semantic relevance to the user’s query. Reranking helps improve accuracy, especially for large or noisy datasets where vector similarity alone may not produce the optimal ordering.

You can enable and configure reranking in the dashboard or directly in your API requests:
    
    
    const answer = await env.AI.autorag("my-autorag").aiSearch({
    	query: "How do I train a llama to deliver coffee?",
    	model: "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    	reranking: {
    		enabled: true,
    		model: "@cf/baai/bge-reranker-base",
    	},
    });

#### Set system prompts in API

Previously, [system prompts](https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/) could only be configured in the dashboard. You can now define them directly in your API requests, giving you per-query control over behavior. For example:
    
    
    // Dynamically set query and system prompt in AI Search
    async function getAnswer(query, tone) {
    	const systemPrompt = `You are a ${tone} assistant.`;
    
    	const response = await env.AI.autorag("my-autorag").aiSearch({
    		query: query,
    		system_prompt: systemPrompt,
    	});
    
    	return response;
    }
    
    // Example usage
    const query = "What is Cloudflare?";
    const tone = "friendly";
    
    const answer = await getAnswer(query, tone);
    console.log(answer);

Learn more about [Reranking](https://developers.cloudflare.com/ai-search/configuration/retrieval/reranking/) and [System Prompt](https://developers.cloudflare.com/ai-search/configuration/retrieval/system-prompt/) in AI Search.
