---
url: https://developers.cloudflare.com/changelog/post/2026-07-30-ai-search-agent-sdks/
title: Use AI Search with the Agents SDK, AI SDK, and LangChain \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:05.485876+00:00
---

# Use AI Search with the Agents SDK, AI SDK, and LangChain · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-30-ai-search-agent-sdks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 30, 2026

## Use AI Search with the Agents SDK, AI SDK, and LangChain

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-30-ai-search-agent-sdks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use [AI Search](https://developers.cloudflare.com/ai-search/) directly from popular agent frameworks, adding grounded retrieval to an existing app instead of calling the REST API by hand. The new [Agents](https://developers.cloudflare.com/ai-search/agent-sdks/) section has guides for the [Vercel AI SDK](https://developers.cloudflare.com/ai-search/agent-sdks/ai-sdk/), [LangChain](https://developers.cloudflare.com/ai-search/agent-sdks/langchain/), and the [Cloudflare Agents SDK](https://developers.cloudflare.com/ai-search/agent-sdks/agents-sdk/). The AI SDK integration is a new package, and the LangChain integration is a new retriever in the existing `langchain-cloudflare` package.

#### Vercel AI SDK

The [`ai-search-provider` ↗︎](https://www.npmjs.com/package/ai-search-provider) package connects AI Search to the AI SDK, and targets AI SDK v6 (`ai@^6`). Pass `instance.chat()` to `generateText` or `streamText` to generate a response grounded in your indexed content, with the retrieved chunks returned as `sources`. You can also expose `instance.search()` as a tool for agent loops.
    
    
    import { createAISearchNamespace } from "ai-search-provider";
    import { generateText } from "ai";
    
    const aiSearch = createAISearchNamespace({ binding: env.AI_SEARCH });
    
    const { text, sources } = await generateText({
    	model: aiSearch.get("knowledge-base").chat(),
    	messages: [{ role: "user", content: "How does caching work?" }],
    });
    
    
    import { createAISearchNamespace } from "ai-search-provider";
    import { generateText } from "ai";
    
    const aiSearch = createAISearchNamespace({ binding: env.AI_SEARCH });
    
    const { text, sources } = await generateText({
    	model: aiSearch.get("knowledge-base").chat(),
    	messages: [{ role: "user", content: "How does caching work?" }],
    });

#### LangChain

The `langchain-cloudflare` package ([PyPI ↗︎](https://pypi.org/project/langchain-cloudflare/), [GitHub ↗︎](https://github.com/cloudflare/langchain-cloudflare)) provides `CloudflareAISearchRetriever`, a standard LangChain retriever backed by AI Search. Use it on its own, wrap it with `create_retriever_tool` to give an agent a search tool, or drop it into a RAG chain. It works with REST credentials or a Worker binding inside a Python Worker.
    
    
    from langchain_cloudflare import CloudflareAISearchRetriever
    
    retriever = CloudflareAISearchRetriever(
        account_id=ACCOUNT_ID,
        api_token=API_TOKEN,
        instance_name="knowledge-base",
        retrieval_type="hybrid",
    )
    
    docs = retriever.invoke("How do I configure Workers AI?")

#### Cloudflare Agents SDK

The [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) could already reach AI Search through the Workers binding. The new [guide](https://developers.cloudflare.com/ai-search/agent-sdks/agents-sdk/) walks through building a stateful chat agent that provisions its own instance, indexes content, and searches it from a tool.
    
    
    import { tool } from "ai";
    import { z } from "zod";
    
    const instance = env.AI_SEARCH.get("knowledge-base");
    
    // Expose AI Search to the agent's model as a tool it can call.
    const searchKnowledgeBase = tool({
    	description: "Search the knowledge base for relevant content.",
    	inputSchema: z.object({ query: z.string() }),
    	execute: ({ query }) => instance.search({ query }),
    });
    
    
    import { tool } from "ai";
    import { z } from "zod";
    
    const instance = env.AI_SEARCH.get("knowledge-base");
    
    // Expose AI Search to the agent's model as a tool it can call.
    const searchKnowledgeBase = tool({
    	description: "Search the knowledge base for relevant content.",
    	inputSchema: z.object({ query: z.string() }),
    	execute: ({ query }) => instance.search({ query }),
    });

For the full walkthroughs, including creating an instance and indexing content, refer to the [Agents](https://developers.cloudflare.com/ai-search/agent-sdks/) guides.
