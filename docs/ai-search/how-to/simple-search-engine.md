---
url: https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/
title: Create a simple search engine \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:42.825624+00:00
---

# Create a simple search engine · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /How to
  4. /Create a simple search engine



# Create a simple search engine

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create a Worker project2\. Bind your Worker to AI Search3\. Add the search code4\. Run and deployNext steps

This guide builds a search engine that returns the file names matching a query, using the `search()` method on the [Workers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/). You can adapt it to use the [REST API](https://developers.cloudflare.com/ai-search/api/search/rest-api/) instead.

For the best results with this pattern:

  * Disable query rewriting so the original user query is matched directly.
  * Configure your AI Search instance with small chunk sizes (256 tokens is usually enough).



## Prerequisites

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

You also need an AI Search instance that already contains indexed content. To create one and add content, refer to [Get started](https://developers.cloudflare.com/ai-search/get-started/).

## 1\. Create a Worker project

Create a new Worker project using the `create-cloudflare` CLI (C3). [C3 ↗︎](https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare) is a command-line tool designed to help you set up and deploy new applications to Cloudflare.

Create a new project named `search-engine` by running:

npmyarnpnpm
    
    
    npm create cloudflare@latest -- search-engine
    
    
    yarn create cloudflare search-engine
    
    
    pnpm create cloudflare@latest search-engine

For setup, select the following options:

  * For _What would you like to start with?_ , choose `Hello World example`.
  * For _Which template would you like to use?_ , choose `Worker only`.
  * For _Which language do you want to use?_ , choose `TypeScript`.
  * For _Do you want to use git for version control?_ , choose `Yes`.
  * For _Do you want to deploy your application?_ , choose `No` (we will be making some changes before deploying).



Go to your application directory:
    
    
    cd search-engine

## 2\. Bind your Worker to AI Search

Add the following to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "ai_search_namespaces": [
        {
          "binding": "AI_SEARCH",
          "namespace": "default",
          "remote": true
        }
      ]
    }
    
    
    [[ai_search_namespaces]]
    binding = "AI_SEARCH"
    namespace = "default"
    remote = true

This binds the `default` [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/) to `env.AI_SEARCH`. The `remote` option lets `wrangler dev` proxy requests to your deployed instance, since AI Search does not run locally.

## 3\. Add the search code

Update `src/index.ts`. This Worker reads a query from the URL, searches your instance, and returns the file name of each matching chunk. Replace `my-instance` with the name of your instance.

src/index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const url = new URL(request.url);
    		const userQuery = url.searchParams.get("query") ?? "What is Cloudflare?";
    
    		const searchResult = await env.AI_SEARCH.get("my-instance").search({
    			messages: [{ role: "user", content: userQuery }],
    		});
    
    		return Response.json({
    			files: searchResult.chunks.map((chunk) => chunk.item.key),
    		});
    	},
    };

src/index.tsts
    
    
    export interface Env {
    	AI_SEARCH: AiSearchNamespace;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const url = new URL(request.url);
    		const userQuery = url.searchParams.get("query") ?? "What is Cloudflare?";
    
    		const searchResult = await env.AI_SEARCH.get("my-instance").search({
    			messages: [{ role: "user", content: userQuery }],
    		});
    
    		return Response.json({
    			files: searchResult.chunks.map((chunk) => chunk.item.key),
    		});
    	},
    } satisfies ExportedHandler<Env>;

## 4\. Run and deploy

Start a local development server, then query it at `/?query=your+search+terms`:
    
    
    npx wrangler dev

Log in with your Cloudflare account, then deploy your Worker to make it accessible on the Internet:
    
    
    npx wrangler login
    npx wrangler deploy

## Next steps

### [Search Workers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/)

Full reference for searching and chatting from a Worker.

### [Query rewriting](https://developers.cloudflare.com/ai-search/configuration/retrieval/query-rewriting/)

Control whether AI Search rewrites the query before searching.

[PreviousShow source citations in responses](https://developers.cloudflare.com/ai-search/how-to/chunk-citations/)[NextFetch and index single web pages](https://developers.cloudflare.com/ai-search/how-to/fetch-and-index-web-pages/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/how-to/simple-search-engine.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
