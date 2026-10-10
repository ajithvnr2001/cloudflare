---
url: https://developers.cloudflare.com/changelog/product/ai-search/
title: AI Search Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:12.129851+00:00
---

# AI Search Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/ai-search/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 1, 2026

## [AI Search is generally available](https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/)

[AI Search](https://developers.cloudflare.com/ai-search/)

AI Search is now generally available. Usage-based billing begins on November 1, 2026, with included monthly ingestion, storage, semantic query, and full-text query usage. Cloudflare will send a reminder email the week before billing begins.

Refer to [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for rates and included usage.

#### Hybrid search is on by default

New AI Search instances use hybrid search by default. Hybrid search combines semantic vector retrieval with full-text matching. You can choose a different index method when you create an instance.

Refer to [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for details.

#### Workers AI embeddings and reranking are included

Workers AI embedding and reranking calls made by AI Search are included in AI Search pricing. These calls no longer appear on your Workers AI bill or in your AI Gateway logs. Generation, query rewriting, and external providers continue to use your account and gateway.

Refer to [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for details.

#### Multimodal model and image support

AI Search supports the `@cf/qwen/qwen3-vl-embedding-2b` and `google-ai-studio/gemini-embedding-2` multimodal embedding models. Search and chat requests can include images through the REST API and public endpoint.

Refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/) for the full list of embedding models.

#### OCR availability and increased file limits

Optical character recognition (OCR) is available on every account for scanned PDFs. Plain-text or code files and PDFs with OCR enabled can be up to 10 MiB. PDFs without OCR and other supported formats remain limited to 4 MiB.

Refer to [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/#file-limits) for file limits and [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for OCR pricing.

#### Source type inference

When you create an AI Search instance, the `type` field is optional. AI Search infers a website source from an HTTP or HTTPS URL, or an R2 source from an existing bucket name.

Refer to [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) for details.

Sep 11, 2026

## [AI Search supports extensionless R2 objects with Content-Type metadata](https://developers.cloudflare.com/changelog/post/2026-09-11-extensionless-r2-content-type/)

[AI Search](https://developers.cloudflare.com/ai-search/)

AI Search can index R2 objects without filename extensions when they include supported `Content-Type` metadata. This supports object keys that do not include file extensions while preserving file-type validation during indexing.

For supported file types and Content-Type requirements, refer to [R2 data sources](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/).

Aug 30, 2026

## [AI Search now supports GLM-5.3 Flash](https://developers.cloudflare.com/changelog/post/2026-08-30-glm-5.3-flash/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports [`@cf/zai-org/glm-5.3-flash`](https://developers.cloudflare.com/workers-ai/models/glm-5.3-flash/) for text generation. The model has a 1,048,576-token context window and runs on Workers AI.

To configure the model for an AI Search instance, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).

Aug 26, 2026

## [New Workers AI text generation models in AI Search](https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports six additional [Workers AI](https://developers.cloudflare.com/workers-ai/) models for text generation:

Model | Context window (tokens)  
---|---  
`@cf/deepseek-ai/deepseek-v4-flash-0731` | 1,048,576  
`@cf/deepseek-ai/deepseek-v4-pro-0813` | 1,048,576  
`@cf/openai/gpt-oss-120b` | 128,000  
`@cf/openai/gpt-oss-20b` | 128,000  
`@cf/qwen/qwen3.8-27b` | 262,144  
`@cf/moonshotai/kimi-k2.7-code` | 262,144  
  
These models run on Workers AI, so they do not require an additional provider key. Select a model when creating or updating an AI Search instance in the dashboard or through the API.

For the full list of supported models, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).

Aug 25, 2026

## [Store larger custom metadata values in AI Search](https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/)

[AI Search](https://developers.cloudflare.com/ai-search/)

AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.

For details, refer to [Metadata attributes](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

Aug 6, 2026

## [AI Search makes it easier to build a search engine for your data](https://developers.cloudflare.com/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/)

[AI Search](https://developers.cloudflare.com/ai-search/)

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

Jul 30, 2026

## [Use AI Search with the Agents SDK, AI SDK, and LangChain](https://developers.cloudflare.com/changelog/post/2026-07-30-ai-search-agent-sdks/)

[AI Search](https://developers.cloudflare.com/ai-search/)

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

Jul 8, 2026

## [Filter AI Search list items by exact object key](https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/)

[AI Search](https://developers.cloudflare.com/ai-search/)

In [AI Search](https://developers.cloudflare.com/ai-search/), you can upload files to an instance, or connect a [data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) such as an R2 bucket, to make your content searchable with natural language. Each file becomes an **item** identified by an object **key** (its filename or path). The [list items endpoint](https://developers.cloudflare.com/ai-search/api/items/rest-api/) returns the items in an instance.

That endpoint now accepts a `key` query parameter, so you can look up a single item by its exact object key without paging through the full list. This complements the existing `item_id` filter for when you know the key but not the ID.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/instances/<INSTANCE_NAME>/items?key=docs/readme.md" \
      -H "Authorization: Bearer <API_TOKEN>"

Keys are unique per data source, so combine `key` with `source` (for example, `source=builtin`) to disambiguate when the same key exists across multiple sources.

For more information, refer to [managing items](https://developers.cloudflare.com/ai-search/api/items/rest-api/).

Jul 8, 2026

## [Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion](https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)[AI Search](https://developers.cloudflare.com/ai-search/)

Workers AI [Markdown conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) (`toMarkdown`) now supports `.gif` and `.bmp` image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.

GIF and BMP files run through the same [image pipeline](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/#images) as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.

[AI Search](https://developers.cloudflare.com/ai-search/) uses `toMarkdown` automatically to process the files it ingests, so any `.gif` and `.bmp` files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.

Learn more about [Markdown conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) and the full list of [AI Search's supported file types](https://developers.cloudflare.com/ai-search/configuration/data-source/#supported-file-types).

Jul 2, 2026

## [Manage AI Search sync jobs with Wrangler CLI](https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/)

[AI Search](https://developers.cloudflare.com/ai-search/)

When you connect a [data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) to your [AI Search](https://developers.cloudflare.com/ai-search/) instance, AI Search runs sync jobs to keep your index up to date with your content. You can now manage those jobs directly from [Wrangler](https://developers.cloudflare.com/ai-search/wrangler-commands/).

For example, you can trigger a sync job from your CI/CD or automated pipelines with the `jobs create` command so your index refreshes when you push a change:
    
    
    wrangler ai-search jobs create my-instance

This creates an asynchronous sync job that checks for changes in your data source, and sends new, modified, or deleted files to be indexed. The following commands are available:

Command | Description  
---|---  
`wrangler ai-search jobs create` | Trigger a new sync job  
`wrangler ai-search jobs list` | List sync jobs for an instance  
`wrangler ai-search jobs get` | Get details for a job  
`wrangler ai-search jobs cancel` | Cancel a running job  
`wrangler ai-search jobs logs` | View log entries for a job  
  
All commands accept `--namespace`/`-n` (defaults to `default`) and `--json` for structured output that automation and AI agents can parse directly. The `list` and `logs` commands also support `--page` and `--per-page` for pagination, and `cancel` prompts for confirmation unless you pass `-y`/`--force`.

For full usage details, refer to the [AI Search Wrangler commands documentation](https://developers.cloudflare.com/ai-search/wrangler-commands/).

Jun 24, 2026

## [Control AI Search similarity cache freshness](https://developers.cloudflare.com/changelog/post/2026-06-24-ai-search-similarity-cache-controls/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now gives you more control over [similarity cache](https://developers.cloudflare.com/ai-search/configuration/retrieval/cache/) freshness. Similarity cache helps reduce latency and inference cost by reusing responses for semantically similar queries.

With these updates, you can choose how long responses are eligible for reuse and clear cached responses when they may be stale.

#### Cache duration now defaults to 48 hours

Previously, AI Search cached responses for a fixed duration of 30 days. Cached responses now use the instance's `cache_ttl` setting, and the default is **48 hours**.

You can set `cache_ttl` when creating or updating an instance to choose a cache duration from 10 minutes to 6 days.

Use a shorter TTL when your source content changes frequently and freshness is more important. Use a longer TTL when your content is stable and you want more cache reuse.

For example, set `cache_ttl` to `518400` to retain cached responses for 6 days:
    
    
    {
    	"cache_ttl": 518400
    }

#### Purge cached responses

You can also purge all cached responses for an instance on demand. Purging cached responses does not delete indexed content or source files.

It prevents AI Search from reusing previous cached responses, so subsequent similar queries generate fresh answers and repopulate the cache.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances/$INSTANCE_NAME/purge_cache" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

You can also purge cached responses from the instance settings page in the Cloudflare dashboard.

Refer to [similarity cache](https://developers.cloudflare.com/ai-search/configuration/retrieval/cache/) for the full list of supported `cache_ttl` values and more details about cache behavior.

Jun 10, 2026

## [Manage AI Search namespaces with Wrangler CLI](https://developers.cloudflare.com/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/)

[AI Search](https://developers.cloudflare.com/ai-search/)

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

Apr 16, 2026

## [AI Search instances now include built-in storage and namespace Workers Bindings](https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/)

[AI Search](https://developers.cloudflare.com/ai-search/)

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

Apr 16, 2026

## [AI Search now has hybrid search and relevance boosting](https://developers.cloudflare.com/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports hybrid search and relevance boosting, giving you more control over how results are found and ranked.

#### Hybrid search

Hybrid search combines vector (semantic) search with BM25 keyword search in a single query. Vector search finds chunks with similar meaning, even when the exact words differ. Keyword search matches chunks that contain your query terms exactly. When you enable hybrid search, both run in parallel and the results are fused into a single ranked list.

You can configure the tokenizer (`porter` for natural language, `trigram` for code), keyword match mode (`and` for precision, `or` for recall), and fusion method (`rrf` or `max`) per instance:
    
    
    const instance = await env.AI_SEARCH.create({
    	id: "my-instance",
    	index_method: { vector: true, keyword: true },
    	fusion_method: "rrf",
    	indexing_options: { keyword_tokenizer: "porter" },
    	retrieval_options: { keyword_match_mode: "and" },
    });

Refer to [Search modes](https://developers.cloudflare.com/ai-search/concepts/search-modes/) for an overview and [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for configuration details.

#### Relevance boosting

Relevance boosting lets you nudge search rankings based on document metadata. For example, you can prioritize recent documents by boosting on `timestamp`, or surface high-priority content by boosting on a custom metadata field like `priority`.

Configure up to 3 boost fields per instance or override them per request:
    
    
    const results = await env.AI_SEARCH.get("my-instance").search({
    	messages: [{ role: "user", content: "deployment guide" }],
    	ai_search_options: {
    		retrieval: {
    			boost_by: [
    				{ field: "timestamp", direction: "desc" },
    				{ field: "priority", direction: "desc" },
    			],
    		},
    	},
    });

Refer to [Relevance boosting](https://developers.cloudflare.com/ai-search/configuration/retrieval/boosting/) for configuration details.

Apr 8, 2026

## [Website Source CSS content selectors for precise content extraction in AI Search](https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports [CSS content selectors](https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/) for website data sources. You can now define which parts of a crawled page are extracted and indexed by specifying CSS selectors paired with URL glob patterns.

Content selectors solve the problem of indexing only relevant content while ignoring navigation, sidebars, footers, and other boilerplate. When a page URL matches a glob pattern, only elements matching the corresponding CSS selector are extracted and converted to Markdown for indexing.

Configure content selectors via the dashboard or API:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-search/instances" \
      -H "Authorization: Bearer {api_token}" \
      -H "Content-Type: application/json" \
      -d '{
        "id": "my-ai-search",
        "source": "https://example.com",
        "type": "web-crawler",
        "source_params": {
          "web_crawler": {
            "parse_options": {
              "content_selector": [
                {
                  "path": "**/blog/**",
                  "selector": "article .post-body"
                }
              ]
            }
          }
        }
      }'

Selectors are evaluated in order, and the first matching pattern wins. You can define up to 10 content selector entries per instance.

For configuration details and examples, refer to the [content selectors documentation](https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/).

Apr 8, 2026

## [New Workers AI models for text generation and embedding in AI Search](https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports four additional [Workers AI](https://developers.cloudflare.com/workers-ai/) models across text generation and embedding.

#### Text generation

Model | Context window (tokens)  
---|---  
`@cf/zai-org/glm-4.7-flash` | 131,072  
`@cf/qwen/qwen3-30b-a3b-fp8` | 32,000  
  
GLM-4.7-Flash is a lightweight model from Zhipu AI with a 131,072 token context window, suitable for long-document summarization and retrieval tasks. Qwen3-30B-A3B is a mixture-of-experts model from Alibaba that activates only 3 billion parameters per forward pass, keeping inference fast while maintaining strong response quality.

#### Embedding

Model | Vector dims | Input tokens | Metric  
---|---|---|---  
`@cf/qwen/qwen3-embedding-0.6b` | 1,024 | 4,096 | cosine  
`@cf/google/embeddinggemma-300m` | 768 | 512 | cosine  
  
Qwen3-Embedding-0.6B supports up to 4,096 input tokens, making it a good fit for indexing longer text chunks. EmbeddingGemma-300M from Google produces 768-dimension vectors and is optimized for low-latency embedding workloads.

All four models are available without additional provider keys since they run on Workers AI. Select them when creating or updating an AI Search instance in the dashboard or through the API.

For the full list of supported models, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).

Apr 1, 2026

## [Create, manage, search AI Search instances with Wrangler CLI](https://developers.cloudflare.com/changelog/post/2026-04-01-ai-search-wrangler-commands/)

[AI Search](https://developers.cloudflare.com/ai-search/)

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

Mar 23, 2026

## [New AI Search REST API endpoints for /search and /chat/completions](https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now offers new [REST API](https://developers.cloudflare.com/ai-search/api/search/rest-api/) endpoints for search and chat that use an OpenAI compatible format. This means you can use the familiar `messages` array structure that works with existing OpenAI SDKs and tools. The messages array also lets you pass previous messages within a session, so the model can maintain context across multiple turns.

Endpoint | Path  
---|---  
Chat Completions | `POST /accounts/{account_id}/ai-search/instances/{name}/chat/completions`  
Search | `POST /accounts/{account_id}/ai-search/instances/{name}/search`  
  
Here is an example request to the Chat Completions endpoint using the new `messages` array format:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer {API_TOKEN}" \
      -d '{
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful documentation assistant."
          },
          {
            "role": "user",
            "content": "How do I get started?"
          }
        ]
      }'

For more details, refer to the [AI Search REST API guide](https://developers.cloudflare.com/ai-search/api/search/rest-api/).

#### Migration from existing AutoRAG API (recommended)

If you are using the previous AutoRAG API endpoints (`/autorag/rags/`), we recommend migrating to the new endpoints. The previous AutoRAG API endpoints will continue to be fully supported.

Refer to the [migration guide](https://developers.cloudflare.com/ai-search/api/migration/rest-api/) for step-by-step instructions.

Mar 23, 2026

## [AI Search UI snippets and MCP support](https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports public endpoints, UI snippets, and MCP, making it easy to add search to your website or connect AI agents.

Public endpoints allow you to expose AI Search capabilities without requiring API authentication. To enable public endpoints:

  1. Go to **AI Search** in the Cloudflare dashboard. [ Go to **AI Search** ↗ ](https://dash.cloudflare.com/?to=/:account/ai/ai-search)
  2. Select your instance, and turn on **Public Endpoint** in **Settings**. For more details, refer to [Public endpoint configuration](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/).



#### UI snippets

UI snippets are pre-built search and chat components you can embed in your website. Visit [search.ai.cloudflare.com ↗︎](https://search.ai.cloudflare.com/) to configure and preview components for your AI Search instance.

![Example of the search-modal-snippet component](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1842,height=806,format=webp/_astro/ui-snippet-search-modal.nSXbvcsi.png)

To add a search modal to your page:
    
    
    <script
    	type="module"
    	src="https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js"
    ></script>
    
    <search-modal-snippet
    	api-url="https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/"
    	placeholder="Search..."
    >
    </search-modal-snippet>

For more details, refer to the [UI snippets documentation](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/).

#### MCP

The MCP endpoint allows AI agents to search your content via the Model Context Protocol. Connect your MCP client to:
    
    
    https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/mcp

For more details, refer to the [MCP documentation](https://developers.cloudflare.com/ai-search/api/search/mcp/).

Mar 23, 2026

## [Custom metadata filtering for AI Search](https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports custom metadata filtering, allowing you to define your own metadata fields and filter search results based on attributes like category, version, or any custom field you define.

#### Define a custom metadata schema

You can define up to 5 custom metadata fields per AI Search instance. Each field has a name and data type (`text`, `number`, or `boolean`):
    
    
    curl -X POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer {API_TOKEN}" \
      -d '{
        "id": "my-instance",
        "type": "r2",
        "source": "my-bucket",
        "custom_metadata": [
          { "field_name": "category", "data_type": "text" },
          { "field_name": "version", "data_type": "number" },
          { "field_name": "is_public", "data_type": "boolean" }
        ]
      }'

#### Add metadata to your documents

How you attach metadata depends on your data source:

  * **R2 bucket** : Set metadata using S3-compatible custom headers (`x-amz-meta-*`) when uploading objects. Refer to [R2 custom metadata](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/#custom-metadata) for examples.
  * **Website** : Add `<meta>` tags to your HTML pages. Refer to [Website custom metadata](https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/) for details.



#### Filter search results

Use custom metadata fields in your search queries alongside built-in attributes like `folder` and `timestamp`:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/search \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer {API_TOKEN}" \
      -d '{
        "messages": [
          {
            "content": "How do I configure authentication?",
            "role": "user"
          }
        ],
        "ai_search_options": {
          "retrieval": {
            "filters": {
              "category": "documentation",
              "version": { "$gte": 2.0 }
            }
          }
        }
      }'

Learn more in the [metadata filtering documentation](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

Feb 9, 2026

## [AI Search now with more granular controls over indexing](https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/)

[AI Search](https://developers.cloudflare.com/ai-search/)

Get your content updates into [AI Search](https://developers.cloudflare.com/ai-search/) faster and avoid a full rescan when you do not need it.

#### Reindex individual files without a full sync

Updated a file or need to retry one that errored? When you know exactly which file changed, you can now [reindex it directly](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/#controls) instead of rescanning your entire data source.

Go to **Overview** > **Indexed Items** and select the sync icon next to any file to reindex it immediately.

![Sync individual files from Indexed Items](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2118,height=782,format=webp/_astro/individual-file-indexing.CQgoIj85.png)

#### Crawl only the sitemap you need

By default, AI Search crawls all sitemaps listed in your `robots.txt`, up to the [maximum files per index limit](https://developers.cloudflare.com/ai-search/platform/limits-pricing/#limits). If your site has multiple sitemaps but you only want to index a specific set, you can now [specify a single sitemap URL](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#specific-sitemap) to limit what the crawler visits.

For example, if your `robots.txt` lists both `blog-sitemap.xml` and `docs-sitemap.xml`, you can specify just `https://example.com/docs-sitemap.xml` to index only your documentation.

Configure your selection anytime in **Settings** > **Parsing options** > **Specific sitemaps** , then trigger a sync to apply the changes.

![Specify a sitemap in Parsinh options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1973,height=387,format=webp/_astro/specify-sitemap.pLCkwmJ-.png)

Learn more about [indexing controls](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/#controls) and [website crawling configuration](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#specific-sitemap).

Jan 20, 2026

## [AI Search path filtering for website and R2 data sources](https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now includes [path filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/path-filtering/) for both [website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/#path-filtering) and [R2](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/#path-filtering) data sources. You can now control which content gets indexed by defining include and exclude rules for paths.

By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.

![Path filtering configuration in AI Search](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2346,height=1360,format=webp/_astro/path-filtering.BCH7HN-Q.png)

Path filtering uses [micromatch ↗︎](https://github.com/micromatch/micromatch) patterns, so you can use `*` to match within a directory and `**` to match across directories.

Use case | Include | Exclude  
---|---|---  
Index docs but skip drafts | `**/docs/**` | `**/docs/drafts/**`  
Keep admin pages out of results | — | `**/admin/**`  
Index only English content | `**/en/**` | —  
  
Configure path filters when creating a new instance or update them anytime from **Settings**. Check out [path filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/path-filtering/) to learn more.

Jan 20, 2026

## [Create AI Search instances programmatically via REST API](https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-simplified-api/)

[AI Search](https://developers.cloudflare.com/ai-search/)

You can now create [AI Search](https://developers.cloudflare.com/ai-search/) instances programmatically using the [API](https://developers.cloudflare.com/ai-search/get-started/api/). For example, use the API to create instances for each customer in a multi-tenant application or manage AI Search alongside your other infrastructure.

If you have created an AI Search instance via the [dashboard](https://developers.cloudflare.com/ai-search/get-started/dashboard/) before, you already have a [service API token](https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/) registered and can start creating instances programmatically right away. If not, follow the [API guide](https://developers.cloudflare.com/ai-search/get-started/api/) to set up your first instance.

For example, you can now create separate search instances for each language on your website:
    
    
    for lang in en fr es de; do
      curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances" \
        -H "Authorization: Bearer $API_TOKEN" \
        -H "Content-Type: application/json" \
        --data '{
          "id": "docs-'"$lang"'",
          "type": "web-crawler",
          "source": "example.com",
          "source_params": {
            "path_include": ["**/'"$lang"'/**"]
          }
        }'
    done

Refer to the [REST API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/create/) for additional configuration options.

Nov 19, 2025

## [AI Search support for crawling login protected website content](https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports [custom HTTP headers](https://developers.cloudflare.com/ai-search/configuration/data-source/website/authentication-headers/) for website crawling, solving a common problem where valuable content behind authentication or access controls could not be indexed.

Previously, AI Search could only crawl publicly accessible pages, leaving knowledge bases, documentation, and other protected content out of your search results. With custom headers support, you can now include authentication credentials that allow the crawler to access this protected content.

This is particularly useful for indexing content like:

  * **Internal documentation** behind corporate login systems
  * **Premium content** that requires users to provide access to unlock
  * **Sites protected by Cloudflare Access** using service tokens



To add custom headers when creating an AI Search instance, select **Parse options**. In the **Extra headers** section, you can add up to five custom headers per Website data source.

![Custom headers configuration in AI Search](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1098,height=287,format=webp/_astro/ai-search-extra-headers.B7A2spby.png)

For example, to crawl a site protected by [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/), you can add service token credentials as custom headers:
    
    
    CF-Access-Client-Id: your-token-id.access
    CF-Access-Client-Secret: your-token-secret

The crawler will automatically include these headers in all requests, allowing it to access protected pages that would otherwise be blocked.

Learn more about [configuring custom headers for website crawling](https://developers.cloudflare.com/ai-search/configuration/data-source/website/authentication-headers/) in AI Search.

Oct 28, 2025

## [Reranking and API-based system prompt configuration in AI Search](https://developers.cloudflare.com/changelog/post/2025-10-27-ai-search-reranking-system-prompt/)

[AI Search](https://developers.cloudflare.com/ai-search/)

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

← Prev

1[2](https://developers.cloudflare.com/changelog/product/ai-search/2/)

[Next →](https://developers.cloudflare.com/changelog/product/ai-search/2/)
