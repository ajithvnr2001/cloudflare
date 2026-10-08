---
url: https://developers.cloudflare.com/learning-paths/load-balancing/setup/check-pool-health/
title: Check pool health \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:50.516658+00:00
---

# Check pool health · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/setup/check-pool-health/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Setup](https://developers.cloudflare.com/learning-paths/load-balancing/setup/)
  5. /Check pool health



# Check pool health

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/setup/check-pool-health/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUnexpected health status

Before directing any traffic to your pools, make sure that your pools and monitors are set up correctly. The status of your health check will be _unknown_ until the results of the first check are available.

To confirm pool health using the dashboard:

  1. Go to **Load Balancing**.
  2. Select the **Pools** tab.
  3. For pools and individual endpoints, review the values in the **Health** and **Endpoint Health** columns.



For more information on pool and endpoint health statuses, refer to [How a pool becomes unhealthy](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#how-a-pool-becomes-unhealthy).

To fetch the latest health status of all pools, use the [List Pools](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/list/) command, paying attention to the `healthy` value for pools and origins (endpoints).

For troubleshooting a specific pool's health, use the [Pool Health Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/health/methods/get/) command.

## Unexpected health status

If you notice that healthy pools are being marked unhealthy:

  * Review [how endpoints and pools become unhealthy](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/).
  * Refer to the [Troubleshooting section](https://developers.cloudflare.com/load-balancing/troubleshooting/).



[PreviousCreate pools](https://developers.cloudflare.com/learning-paths/load-balancing/setup/create-pools/)[NextCreate load balancer on test domain](https://developers.cloudflare.com/learning-paths/load-balancing/setup/test-load-balancer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/setup/check-pool-health.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
