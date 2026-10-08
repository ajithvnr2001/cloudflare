---
url: https://developers.cloudflare.com/use-cases/saas/code-deployment/
title: Enable customer code deployment \u00b7 Cloudflare use cases
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:11.629577+00:00
---

# Enable customer code deployment · Cloudflare use cases

> Source: https://developers.cloudflare.com/use-cases/saas/code-deployment/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Use cases](https://developers.cloudflare.com/use-cases/)
  3. /[SaaS platforms](https://developers.cloudflare.com/use-cases/saas/)
  4. /Enable customer code deployment



# Enable customer code deployment

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/use-cases/saas/code-deployment/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSolutions Workers for PlatformsGet started

SaaS platforms often need to let customers run their own code — custom logic, integrations, webhooks — without compromising tenant isolation or platform stability. Cloudflare Workers for Platforms runs each customer's code in a separate V8 isolate with dispatch routing based on hostname, path, or header.

## Solutions

### Workers for Platforms

Deploy isolated Workers execution environments for your customers. [Learn more about Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/).

  * **Tenant isolation** \- Each customer's code runs in a separate V8 isolate with no shared memory between tenants
  * **Custom logic** \- Customers can deploy their own Workers to extend or customize your platform's behavior
  * **Dispatch routing** \- Route incoming requests to the correct customer Worker based on hostname, path, or header
  * **Observability** \- Tail Workers capture logs and errors across all tenant code from a single integration



## Get started

  1. [Workers for Platforms get started](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/get-started/)
  2. [Configure Dispatch Namespaces](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/)



[PreviousCustomer domains with SSL for SaaS](https://developers.cloudflare.com/use-cases/saas/custom-domains/)[NextStore and isolate customer data](https://developers.cloudflare.com/use-cases/saas/data-isolation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/use-cases/saas/code-deployment.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
