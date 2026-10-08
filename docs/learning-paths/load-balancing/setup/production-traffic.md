---
url: https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/
title: Route production traffic \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:50.882689+00:00
---

# Route production traffic · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Setup](https://developers.cloudflare.com/learning-paths/load-balancing/setup/)
  5. /Route production traffic



# Route production traffic

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Now that you have set up your load balancer and verified everything is working correctly, you can put the load balancer on a live domain or subdomain:

  1. If you update your pools and monitors, review the pool health again to make sure everything is working as expected.
  2. Confirm that your production hostname has the correct [priority order](https://developers.cloudflare.com/load-balancing/load-balancers/dns-records/#priority-order) of DNS records and is covered by an [SSL/TLS certificate](https://developers.cloudflare.com/load-balancing/load-balancers/dns-records/#ssltls-coverage).
  3. Configure your load balancer to receive production traffic, which could involve either: 
     * Editing the **Hostname** of your existing load balancer.
     * Updating the `CNAME` record sending traffic to your load balancer.



Note

If you have an Enterprise account, also evaluate your application for any excluded paths. For example, you might not want the load balancer to distribute requests directed at your `/admin` path. For any exceptions, set up an [origin rule](https://developers.cloudflare.com/rules/origin-rules/features/#dns-record).

[PreviousSend traffic and review analytics](https://developers.cloudflare.com/learning-paths/load-balancing/setup/traffic-analytics/)[NextNext steps](https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/setup/production-traffic.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
