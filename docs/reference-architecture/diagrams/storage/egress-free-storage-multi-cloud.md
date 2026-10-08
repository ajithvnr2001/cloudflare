---
url: https://developers.cloudflare.com/reference-architecture/diagrams/storage/egress-free-storage-multi-cloud/
title: Egress-free object storage in multi-cloud setups \u00b7 Cloudflare Reference Architecture docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:43.012100+00:00
---

# Egress-free object storage in multi-cloud setups · Cloudflare Reference Architecture docs

> Source: https://developers.cloudflare.com/reference-architecture/diagrams/storage/egress-free-storage-multi-cloud/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Reference Architecture](https://developers.cloudflare.com/reference-architecture/)
  3. /…

Reference Architecture Diagrams

  4. /Storage
  5. /Egress-free object storage in multi-cloud setups



# Egress-free object storage in multi-cloud setups

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/reference-architecture/diagrams/storage/egress-free-storage-multi-cloud/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntroductionR2 multi-cloud setupRelated resources

## Introduction

Object storage is a modern data storage approach that stores data as objects rather than in a hierarchical structure like traditional file systems, making object storage highly scalable and flexible for managing vast amounts of data across diverse applications and environments.

Oftentimes organizations leverage multiple cloud providers to distribute their workloads across different platforms, mitigating risks associated with vendor lock-in, enhancing resilience, and optimizing performance and cost. However, managing data across multiple clouds introduces challenges related to data mobility and interoperability, particularly when it comes to transferring data between cloud providers or on-premises environments.

Egress fees are charges incurred when data is transferred out of a cloud provider's network, either to another cloud provider, on-premises infrastructure, or external services. These fees can vary depending on factors such as the volume of data transferred, the destination of the data, and the network bandwidth utilized.

[R2](https://developers.cloudflare.com/r2/) offers an enticing value proposition by not charging the costly egress bandwidth fees associated with typical cloud storage services. This can be very advantageous in the context of multi-cloud environments, especially when you want to run compute-intensive workloads such as AI model training, query engines, and other data science tools.

## R2 multi-cloud setup

![Figure 1: R2 multi-cloud setup](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=523,format=svg/_astro/r2-multi-cloud.jB-KW29c.svg)Figure 1: R2-multi-cloud setup

  1. **Worker and R2 interaction** : Use R2's [Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/) to interact with R2 from a Worker. Alternatively, for improved portability, use R2's [S3 API](https://developers.cloudflare.com/r2/api/s3/) from a Worker. No R2 egress fees apply.
  2. **External service and R2 interaction** : Use R2's [S3 API](https://developers.cloudflare.com/r2/api/s3/) to interact with R2 from external services. No R2 egress fees apply.



## Related resources

  * [R2: Get started](https://developers.cloudflare.com/r2/get-started)
  * [R2: S3 API](https://developers.cloudflare.com/r2/api/s3/)
  * [R2: Workers API](https://developers.cloudflare.com/r2/api/workers/)
  * [R2: Configure aws4fetch for R2](https://developers.cloudflare.com/r2/examples/aws/aws4fetch/)



[PreviousControl and data plane architectural pattern for Durable Objects](https://developers.cloudflare.com/reference-architecture/diagrams/storage/durable-object-control-data-plane-pattern/)[NextEvent notifications for storage](https://developers.cloudflare.com/reference-architecture/diagrams/storage/event-notifications-for-storage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/reference-architecture/diagrams/storage/egress-free-storage-multi-cloud.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
