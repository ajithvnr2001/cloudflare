---
url: https://developers.cloudflare.com/magic-transit/network-health/
title: Network health \u00b7 Cloudflare Magic Transit docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:18.727946+00:00
---

# Network health · Cloudflare Magic Transit docs

> Source: https://developers.cloudflare.com/magic-transit/network-health/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Magic Transit](https://developers.cloudflare.com/magic-transit/)
  3. /Network health



# Network health

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/magic-transit/network-health/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic Transit uses health check probes to determine the status of tunnels. Cloudflare uses this information to steer traffic through the best available route and warn you about potential issues with a tunnel. Service-level indicators (SLIs) and service-level objectives (SLOs) combine to determine when Cloudflare sends you tunnel health alerts. Refer to [How Cloudflare calculates tunnel health alerts](https://developers.cloudflare.com/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/) for more information about SLIs and SLOs.

There are two types of health checks available: endpoint and tunnel health checks.

  * Endpoint health checks evaluate connectivity from Cloudflare distributed data centers to your origin network. Endpoint probes flow over available tunnels to provide a broad picture of Internet health and do not inform tunnel selection or steering logic.

Cloudflare global network servers issue endpoint health checks outside of customer network namespaces and typically target endpoints beyond the tunnel-terminating border router.

During onboarding, you specify IP addresses to configure endpoint health checks.

  * Tunnel health checks monitor the status of the tunnels that route traffic from Cloudflare to your origin network. Magic Transit relies on health checks to steer traffic to the best available routes.

During onboarding, you specify the tunnel endpoints or tunnel health check targets that the tunnel probes from Cloudflare's global network will monitor.

You can access tunnel health check results through the API. Cloudflare aggregates these results from individual health check results on Cloudflare servers.




Refer to [Tunnel health checks](https://developers.cloudflare.com/magic-transit/reference/tunnel-health-checks/) for a deep dive into the different types of health checks, what they do, and how they work.

Note

Magic Transit customers with [Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/) enabled for the European Union can access GRE, IPsec, and CNI (Cloudflare Network Interconnect) health check and traffic volume data in the Cloudflare dashboard and through the API. This ensures that customers who need to be General Data Protection Regulation (GDPR) compliant can access all Magic Transit features.

Refer to the following pages for details on how to use the various network health checks available.

  * [Run endpoint health checks (beta)](https://developers.cloudflare.com/magic-transit/network-health/run-endpoint-health-checks/)
  * [Check tunnel health in the dashboard](https://developers.cloudflare.com/magic-transit/network-health/check-tunnel-health-dashboard/)
  * [Update tunnel health checks frequency](https://developers.cloudflare.com/magic-transit/network-health/update-tunnel-health-checks-frequency/)
  * [Configure tunnel health alerts](https://developers.cloudflare.com/magic-transit/network-health/configure-tunnel-health-alerts/)
  * [How Cloudflare calculates tunnel health alerts](https://developers.cloudflare.com/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/)



[PreviousEnable Magic user roles](https://developers.cloudflare.com/magic-transit/how-to/enable-magic-roles/)[NextRun endpoint health checks](https://developers.cloudflare.com/magic-transit/network-health/run-endpoint-health-checks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/magic-transit/network-health/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
