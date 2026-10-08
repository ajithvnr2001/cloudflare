---
url: https://developers.cloudflare.com/reference-architecture/diagrams/serverless/serverless-global-apis/
title: Serverless global APIs \u00b7 Cloudflare Reference Architecture docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:42.694260+00:00
---

# Serverless global APIs · Cloudflare Reference Architecture docs

> Source: https://developers.cloudflare.com/reference-architecture/diagrams/serverless/serverless-global-apis/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Reference Architecture](https://developers.cloudflare.com/reference-architecture/)
  3. /…

Reference Architecture Diagrams

  4. /Serverless
  5. /Serverless global APIs



# Serverless global APIs

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/reference-architecture/diagrams/serverless/serverless-global-apis/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntroductionServerless global APIsRelated resources

## Introduction

Serverless APIs represent a modern approach to building and deploying scalable and reliable application programming interfaces (APIs) without the need to manage traditional server infrastructure. These APIs are designed to handle incoming requests from users or other systems, execute the necessary logic or operations, and return a response, all without the need for developers to provision or manage underlying servers.

At the heart of serverless APIs is the concept of serverless computing, where developers focus solely on writing code to implement business logic, without concerning themselves with server provisioning, scaling, or maintenance. This allows for greater agility and faster time-to-market for API-based applications.

Developers define the API endpoints and the corresponding logic or functionality using functions or microservices, which are then deployed to the serverless platform. The platform handles the execution of these functions in response to incoming requests.

Additionally, serverless APIs often integrate seamlessly with other cloud services, such as authentication and authorization services, databases, and event-driven architectures, enabling developers to build complex, scalable, and resilient applications with minimal operational overhead.

Most cloud serverless implementations have a single region where your code is executed. This means any request, from anywhere in the world, must traverse the Internet to get to this single location. All responses to the API request must also be sent back over the same Internet route to the user.

![Figure 1: Traditional single-region architecture](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1125,format=webp/_astro/single-region.DcjMitxL.png)Figure 1: Traditional single-region architecture

Cloudflare follows a different, global-first approach. Globally-deployed architectures enable lower latency and high availability for users accessing the API from different parts of the world. In order to realize performance gains, not only the compute needs to be distributed, but ideally the data as well. Different solutions such as a caching as well as global replication can enable this.

![Figure 2: Region Earth](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1126,format=webp/_astro/region-earth.DPRpgTD0.png)Figure 2: Region Earth

Overall, serverless globally-deployed APIs offer a cost-effective, scalable, and agile approach to building modern applications and services, allowing organizations to focus on delivering value to their users without being encumbered by the complexities of managing infrastructure.

## Serverless global APIs

![Figure 3: Serverless global APIs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=466,format=svg/_astro/serverless-global-apis.BnHHhP-u.svg)Figure 3: Serverless global APIs

This is an example architecture of a serverless API on Cloudflare and aims to illustrate how different compute and data products could interact with each other.

  1. **Client request** : Send request to API endpoint.
  2. **API Shield/Router** : Process incoming request using [Workers](https://developers.cloudflare.com/workers/), check for validity, and perform authentication logic, if needed. Then, forward the (potentially transformed and/or enriched) API call to individual [Workers](https://developers.cloudflare.com/workers) using [Service Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/). This allows for a separation of concerns.
  3. **Read-heavy data** : Read from [KV](https://developers.cloudflare.com/kv/) to serve read-heavy, non-dynamic data. This could include configuration data or product information. Perform writes as needed keeping [limits](https://developers.cloudflare.com/kv/platform/limits/) in mind.
  4. **Relational data** : Query [D1](https://developers.cloudflare.com/d1/) to handle relational-data. This could include user data, product data or other data.
  5. **External data** : Query external databases using [Hyperdrive](https://developers.cloudflare.com/hyperdrive/). Leverage caching to improve performance where applicable. This can be especially helpful when a data migration is out of scope of the implementation.



## Related resources

  * [Workers: Get started](https://developers.cloudflare.com/workers/get-started/guide/)
  * [Queues: Get started](https://developers.cloudflare.com/queues/get-started/)
  * [R2: Get started](https://developers.cloudflare.com/r2/get-started/)



[PreviousServerless ETL pipelines](https://developers.cloudflare.com/reference-architecture/diagrams/serverless/serverless-etl/)[NextServerless image content management](https://developers.cloudflare.com/reference-architecture/diagrams/serverless/serverless-image-content-management/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/reference-architecture/diagrams/serverless/serverless-global-apis.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
