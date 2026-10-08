---
url: https://developers.cloudflare.com/use-cases/saas/data-isolation/
title: Store and isolate customer data \u00b7 Cloudflare use cases
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:11.749013+00:00
---

# Store and isolate customer data · Cloudflare use cases

> Source: https://developers.cloudflare.com/use-cases/saas/data-isolation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Use cases](https://developers.cloudflare.com/use-cases/)
  3. /[SaaS platforms](https://developers.cloudflare.com/use-cases/saas/)
  4. /Store and isolate customer data



# Store and isolate customer data

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/use-cases/saas/data-isolation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSolutions D1 R2 Durable Objects KVGet started

Multi-tenant platforms need to store customer data with appropriate isolation — per-tenant databases, separate object storage, or row-level separation. Cloudflare provides serverless storage options that support tenant isolation at the database, bucket, or key-prefix level.

## Solutions

### D1

Serverless SQL database built on SQLite, with global read replication. [Learn more about D1](https://developers.cloudflare.com/d1/).

  * **Database per tenant** \- Create isolated D1 databases per customer for complete data separation, or use row-level isolation in a shared database



### R2

S3-compatible object storage with zero egress fees. [Learn more about R2](https://developers.cloudflare.com/r2/).

  * **Object storage** \- Store customer files and assets per tenant using prefix or bucket-level isolation, with no egress fees



### Durable Objects

Stateful objects with strongly consistent storage and coordination. [Learn more about Durable Objects](https://developers.cloudflare.com/durable-objects/).

  * **Real-time coordination** \- Manage stateful workflows and provide strong consistency for multi-tenant operations



### KV

Globally distributed key-value storage for low-latency reads. [Learn more about KV](https://developers.cloudflare.com/kv/).

  * **Edge configuration** \- Store per-tenant settings, feature flags, and session data at the edge for low-latency reads



## Get started

  1. [D1 get started](https://developers.cloudflare.com/d1/get-started/)
  2. [R2 get started](https://developers.cloudflare.com/r2/get-started/)
  3. [Durable Objects get started](https://developers.cloudflare.com/durable-objects/get-started/)



[PreviousEnable customer code deployment](https://developers.cloudflare.com/use-cases/saas/code-deployment/)[NextProtect your platform](https://developers.cloudflare.com/use-cases/saas/protect-platform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/use-cases/saas/data-isolation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
