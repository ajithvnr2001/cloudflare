---
url: https://developers.cloudflare.com/ai-search/get-started/wrangler/
title: CLI \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:41.204057+00:00
---

# CLI · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/get-started/wrangler/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /Get started
  4. /CLI



# CLI

Last updated Jul 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/get-started/wrangler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Install Wrangler2\. Create an AI Search instance Connect a data source (optional)3\. Check indexing status4\. Test your instanceAdd to your application

This guide walks you through creating an AI Search instance using the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/).

## 1\. Install Wrangler

Install [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the command-line tool for Cloudflare Workers and developer platform products.

npmyarnpnpmbun
    
    
    npm install wrangler
    
    
    yarn install wrangler
    
    
    pnpm install wrangler
    
    
    bun install wrangler

## 2\. Create an AI Search instance

Create a new instance.
    
    
    wrangler ai-search create my-instance

You can upload files to the instance using the [dashboard](https://developers.cloudflare.com/ai-search/get-started/dashboard/#upload-content) or the [REST API](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload/).

### Connect a data source (optional)

You can optionally connect a website or R2 bucket when creating the instance.

**Website:**

Automatically crawl and index a [website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/) that you own.
    
    
    wrangler ai-search create my-instance --type web-crawler --source developers.cloudflare.com

**R2 bucket:**

Index documents stored in an [R2 bucket](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/).
    
    
    wrangler ai-search create my-instance --type r2 --source my-bucket

## 3\. Check indexing status

Check if your content has finished indexing by running the `stats` command.
    
    
    wrangler ai-search stats my-instance

## 4\. Test your instance

Once indexing is complete, run a search query against your instance.
    
    
    wrangler ai-search search my-instance --query "What is Cloudflare?"

For the full list of available commands, refer to [Wrangler commands](https://developers.cloudflare.com/ai-search/wrangler-commands/).

## Add to your application

### [Workers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/)

Query AI Search directly from your Workers code.

### [REST API](https://developers.cloudflare.com/ai-search/api/search/rest-api/)

Query AI Search using HTTP requests.

[PreviousWorkers binding](https://developers.cloudflare.com/ai-search/get-started/workers/)[NextDashboard](https://developers.cloudflare.com/ai-search/get-started/dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/get-started/wrangler.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
