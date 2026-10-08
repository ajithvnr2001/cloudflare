---
url: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/
title: Load Balancing with the China Network \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:03.409974+00:00
---

# Load Balancing with the China Network · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)
  4. /Load Balancing with the China Network



# Load Balancing with the China Network

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesLimitations

## Prerequisites

To enable load balancers to be deployed to the [China Network](https://developers.cloudflare.com/china-network/), your zone will need to meet the following two criteria:

  1. A valid [ICP license](https://developers.cloudflare.com/china-network/concepts/icp/) for the zone in question.
  2. The zone must be provisioned with access to the China Network.



Once these two criteria are met, any newly created load balancer will be automatically deployed to the China Network. When choosing a region for a pool's health checks, `China` is now available to be selected in both the dashboard and API.

You can also create a load balancer by sending a `POST` request to the following endpoint. To deploy to the China Network with the API, the `networks` array in the API call must contain `jdcloud` as a value in addition to `cloudflare`. Refer to the [Cloudflare API documentation](https://developers.cloudflare.com/api/resources/load_balancers/methods/create/) for details on the required fields and their formats.
    
    
    https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers

## Limitations

Load balancers deployed to the China Network currently have the following limitations:

  * Only cookie-based session affinity is supported.
  * Private network off-ramps (Tunnel, GRE, IPsec) are not supported.
  * Private Network Load Balancing is not available on the China Network.



[PreviousDNS persistence](https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/)[NextOverride HTTP Host headers](https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/load-balancing-china.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
