---
url: https://developers.cloudflare.com/load-balancing/pools/
title: Pools \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:05.616421+00:00
---

# Pools · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/pools/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /Pools



# Pools

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/pools/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesCreate poolsPer-endpoint Host header overrideAPI commands

Within Cloudflare, pools represent your endpoints and how they are organized. As such, a pool can be a group of several endpoints, or you could also have only one endpoint (an origin server, for example) per pool.

If you are familiar with DNS terminology, think of a pool as a “record set,” except Cloudflare only returns addresses that are considered healthy. You can attach health monitors to individual pools for customized monitoring. A pool can have either a single monitor or a monitor group attached — but not both.

For more details about how endpoints and pools become unhealthy, refer to [Endpoint and pool health](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/).

Caution

Since load balancing targets are not limited to origin web servers, the term `endpoints` has been introduced. Refer to [Service-Specific Terms ↗︎](https://www.cloudflare.com/service-specific-terms-other-terms/) for its use in the context of Cloudflare offerings, and to [load balancing concepts](https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-components/) or [Reference Architecture](https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/) for use case examples.

On the [Load Balancing API](https://developers.cloudflare.com/api/resources/load_balancers/methods/get/), `origin` has been maintained.

* * *

## Properties

For an up-to-date list of pool properties, refer to [Pool properties](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/list/) in our API documentation.

* * *

## Create pools

For step-by-step guidance, refer to [Create pools](https://developers.cloudflare.com/load-balancing/pools/create-pool/).

* * *

## Per-endpoint Host header override

When your application needs specialized routing (`CNAME` setup or custom hosts like Heroku), change the `Host` header used in health monitor requests. For more details, refer to [Override HTTP Host headers](https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/).

* * *

## API commands

The Cloudflare API supports the following commands for pools. Examples are given for user-level endpoint but apply to the account-level endpoint as well.

Command | Method | Endpoint  
---|---|---  
[Create Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/create/) | `POST` | `accounts/:account_id/load_balancers/pools`  
[Delete Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/delete/) | `DELETE` | `accounts/:account_id/load_balancers/pools/:id`  
[List Pools](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/list/) | `GET` | `accounts/:account_id/load_balancers/pools`  
[Pool Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/get/) | `GET` | `accounts/:account_id/load_balancers/pools/:id`  
[Pool Health Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/health/methods/get/) | `GET` | `account/:account_id/load_balancers/pools/:id/health`  
[Overwrite specific properties](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/edit/) | `PATCH` | `accounts/:account_id/load_balancers/pools/:id`  
[Overwrite existing pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/update/) | `PUT` | `accounts/:account_id/load_balancers/pools/:id`  
[Preview Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/health/methods/create/) | `POST` | `account/:account_id/load_balancers/pools/:id/preview`  
[List Pool References](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/references/methods/get/) | `GET` | `accounts/:account_id/load_balancers/pools/:id/references`  
  
[PreviousCommon configurations](https://developers.cloudflare.com/load-balancing/load-balancers/common-configurations/)[NextManage pools](https://developers.cloudflare.com/load-balancing/pools/create-pool/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/pools/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
