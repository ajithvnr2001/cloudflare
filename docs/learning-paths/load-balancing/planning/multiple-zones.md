---
url: https://developers.cloudflare.com/learning-paths/load-balancing/planning/multiple-zones/
title: Account-level load balancing \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:49.894600+00:00
---

# Account-level load balancing · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/planning/multiple-zones/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Planning your load balancer](https://developers.cloudflare.com/learning-paths/load-balancing/planning/)
  5. /Account-level load balancing



# Account-level load balancing

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/planning/multiple-zones/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewShared configurationsUnique configurations

If you want to set up load balancing for multiple hostnames or domains within your account, your approach would depend on the requirements for each hostname.

## Shared configurations

If you want to share a load balancing configuration across multiple hostnames, you can use the same load balancer through `CNAME` routing.

  1. When you [set up](https://developers.cloudflare.com/learning-paths/load-balancing/setup/) the load balancer, create the load balancer on a new hostname (`lb.example.com`).
  2. When you are ready to [route production traffic](https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/), [create](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records) a `CNAME` record on a hostname that points to the load balancer created in step 1 (`lb.example.com`).
  3. Repeat steps 1 and 2 with all other hostnames.



Note

You could also achieve the same goal or create more advanced routing decisions by setting up DNS Overrides within [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/) on each hostname that override the hostname to `lb.example.com`.

## Unique configurations

If each zone needs unique load balancer configurations (failover order, routing), you should create separate load balancers. Since pools and monitors are configured at the account level, even different load balancers can share the same pools and monitors.

For simpler routing, create a load balancer on each hostname.

For more advanced routing, create multiple load balancers and then set up [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/) to route traffic to each load balancer based on specific characteristics of the request.

[PreviousCustom load balancing rules](https://developers.cloudflare.com/learning-paths/load-balancing/planning/custom-rules/)[NextOverview](https://developers.cloudflare.com/learning-paths/load-balancing/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/planning/multiple-zones.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
