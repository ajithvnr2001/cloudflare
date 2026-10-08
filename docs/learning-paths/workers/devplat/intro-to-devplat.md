---
url: https://developers.cloudflare.com/learning-paths/workers/devplat/intro-to-devplat/
title: Cloudflare Developer Platform \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:02.317760+00:00
---

# Cloudflare Developer Platform · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/workers/devplat/intro-to-devplat/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Workers

  4. /[Learn about Cloudflare's Developer Platform](https://developers.cloudflare.com/learning-paths/workers/devplat/)
  5. /Cloudflare Developer Platform



# Cloudflare Developer Platform

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/workers/devplat/intro-to-devplat/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWeb developmentComputeStorageImage optimization and video streamingAISummaryFeedbackCommunity

The [Cloudflare Developer Platform ↗︎](https://www.cloudflare.com/developer-platform/products/) offers various services to empower developers to build full-stack applications, including: [compute ↗︎](https://www.cloudflare.com/developer-platform/products/#compute), [storage ↗︎](https://www.cloudflare.com/developer-platform/products/#storage), [web development, image optimization, video streaming ↗︎](https://www.cloudflare.com/developer-platform/products/#webdev) and [AI ↗︎](https://ai.cloudflare.com/).

It is important to note that the developer platform product offering is growing with new releases and features updates. To review a list of product documentation related to Cloudflare Developer Platform:

  1. Go to [Cloudflare Docs ↗︎](https://developers.cloudflare.com).
  2. Select **Product directory** in the top menu.
  3. Select the **Developer platform** filter to view [product documentation for Cloudflare Developer Platform products](https://developers.cloudflare.com/directory/?product-group=Developer+platform).



## Web development

[Cloudflare Pages](https://developers.cloudflare.com/pages/) allows you to build full-stack applications at scale.

With Pages, you can deploy front-end applications using [C3, Git integration or Direct Upload](https://developers.cloudflare.com/pages/get-started/). Pages supports a large set of frameworks including [Astro](https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/), [Gatsby](https://developers.cloudflare.com/pages/framework-guides/deploy-a-gatsby-site/), [Hugo](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/), [Next.js](https://developers.cloudflare.com/pages/framework-guides/nextjs/), [Nuxt](https://developers.cloudflare.com/pages/framework-guides/deploy-a-nuxt-site/), [React](https://developers.cloudflare.com/pages/framework-guides/deploy-a-react-site/), [Remix](https://developers.cloudflare.com/pages/framework-guides/deploy-a-remix-site/), and [more](https://developers.cloudflare.com/pages/framework-guides/).

## Compute

**Cloudflare Workers**

As you have learned in previous sections, [Cloudflare Workers](https://developers.cloudflare.com/workers/) allow you to build and deploy serverless applications instantly across the globe. To explore what you can build with Workers, refer to [Examples](https://developers.cloudflare.com/workers/examples/) and [Tutorials](https://developers.cloudflare.com/workers/tutorials/).

**Email Routing**

[Cloudflare Email Routing](https://developers.cloudflare.com/email-service/) allows you to create custom email addresses for your domain and route incoming emails to your preferred mailbox. If you already have a website, refer to [Enable Email Routing](https://developers.cloudflare.com/email-service/get-started/route-emails/) to set up a custom email address for your site.

## Storage

Cloudflare storage offerings differ per use case.

Use-case | Product | Ideal for  
---|---|---  
Key-value storage | [Workers KV](https://developers.cloudflare.com/kv/) | Configuration data, service routing metadata, personalization (A/B testing)  
Object storage / blob storage | [R2](https://developers.cloudflare.com/r2/) | User-facing web assets, images, machine learning and training datasets, analytics datasets, log and event data.  
Accelerate a Postgres or MySQL database | [Hyperdrive](https://developers.cloudflare.com/hyperdrive/) | Connecting to an existing database in a cloud or on-premises using your existing database drivers & ORMs.  
Global coordination & stateful serverless | [Durable Objects](https://developers.cloudflare.com/durable-objects/) | Building collaborative applications; global coordination across clients; real-time WebSocket applications; strongly consistent, transactional storage.  
Lightweight SQL database | [D1](https://developers.cloudflare.com/d1/) | Relational data, including user profiles, product listings and orders, and/or customer data.  
Task processing, batching and messaging | [Queues](https://developers.cloudflare.com/queues/) | Background job processing (emails, notifications, APIs), message queuing, and deferred tasks.  
Event streaming | [K2](https://developers.cloudflare.com/k2/) | High-volume event data read by multiple independent consumers, such as alerting, archiving, and building machine learning features; replaying retained events.  
Vector search & embeddings queries | [Vectorize](https://developers.cloudflare.com/vectorize/) | Storing [embeddings](https://developers.cloudflare.com/workers-ai/models/?tasks=Text+Embeddings) from AI models for semantic search and classification tasks.  
Streaming ingestion | [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) | Streaming data ingestion and processing, including clickstream analytics, telemetry/log data, and structured data for querying  
Time-series metrics | [Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) | Write and query high-cardinality time-series data, usage metrics, and service-level telemetry using Workers and/or SQL.  
  
For a detailed guide to choosing the correct storage option, refer to [Choose a data or storage product](https://developers.cloudflare.com/workers/platform/storage-options/).

## Image optimization and video streaming

[Cloudflare Stream](https://developers.cloudflare.com/stream/) and [Cloudflare Images](https://developers.cloudflare.com/images/) deliver videos and pictures to your end-users without configuring or maintaining infrastructure.

## AI

[Workers AI](https://developers.cloudflare.com/workers-ai/) allow you to build and deploy AI applications that run machine learning models powered by serverless GPUs.

## Summary

You have learned:

  * More about what the Cloudflare Developer Platform offers.
  * The difference between compute, storage, application development, and AI products.



## Feedback

To improve this learning path, [file an issue on GitHub ↗︎](https://github.com/cloudflare/cloudflare-docs/issues/new/choose).

## Community

Connect with the [Cloudflare Developer Platform community on Discord ↗︎](https://discord.cloudflare.com) to ask questions, share what you are building, and discuss the platform with other developers.

[PreviousOverview](https://developers.cloudflare.com/learning-paths/workers/devplat/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/workers/devplat/intro-to-devplat.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
