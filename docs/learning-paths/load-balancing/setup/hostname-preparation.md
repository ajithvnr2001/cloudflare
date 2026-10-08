---
url: https://developers.cloudflare.com/learning-paths/load-balancing/setup/hostname-preparation/
title: Hostname preparation \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:50.599093+00:00
---

# Hostname preparation · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/setup/hostname-preparation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Setup](https://developers.cloudflare.com/learning-paths/load-balancing/setup/)
  5. /Hostname preparation



# Hostname preparation

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/setup/hostname-preparation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRouting strategy

Before setting up anything related to your load balancer, make sure you test that production hostnames meet the following criteria:

  * Based on the [priority order](https://developers.cloudflare.com/load-balancing/load-balancers/dns-records/#priority-order) of DNS records, they will receive the intended amount of traffic.
  * Each hostname is covered by an [SSL/TLS certificate](https://developers.cloudflare.com/load-balancing/load-balancers/dns-records/#ssltls-coverage).



After confirming each of these conditions are met, you can proceed with setting up your load balancer.

## Routing strategy

Depending on your preferences and infrastructure, you might route traffic to your load balancer in different ways:

  * For most customers, it's simpler to create the load balancer on the hostname directly (`www.example.com`).
  * However, you could also create the load balancer on another hostname (`lb.example.com`) and then route traffic using a `CNAME` record on `test.example.com` that points to `lb.example.com`.



[PreviousOverview](https://developers.cloudflare.com/learning-paths/load-balancing/setup/)[NextCreate monitor](https://developers.cloudflare.com/learning-paths/load-balancing/setup/create-monitor/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/setup/hostname-preparation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
