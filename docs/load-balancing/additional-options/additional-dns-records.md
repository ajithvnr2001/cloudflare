---
url: https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/
title: Load balance additional DNS records \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:02.902315+00:00
---

# Load balance additional DNS records · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)
  4. /Additional DNS records



# Additional DNS records

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMX recordsSRV records

In addition to load balancing between DNS records used for IP resolution — `A`, `AAAA`, and `CNAME` records — Enterprise customers can also load balance between **MX** and **SRV** records.

## MX records

To load balance between multiple mail servers:

  1. Make sure you have the [required DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/#send-and-receive-email) for your mail servers.
  2. [Create a monitor](https://developers.cloudflare.com/load-balancing/monitors/create-monitor/) with a **Type** of _SMTP_.
  3. [Create a pool](https://developers.cloudflare.com/load-balancing/pools/create-pool/) with your mail servers and attach the newly created monitor.
  4. [Create a load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/) that includes your newly created pools. Since it will forward SMTP traffic, the load balancer should be [unproxied (DNS-only)](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing).



## SRV records

To load balance between different **SRV** records, which contain significantly more information than many other DNS records:

  1. [Create your SRV records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records).
  2. [Create a monitor](https://developers.cloudflare.com/load-balancing/monitors/create-monitor/) with a **Type** of _UDP-ICMP_ or _TCP_.
  3. [Create a pool](https://developers.cloudflare.com/load-balancing/pools/create-pool/) with your various SRV records and attach the newly created monitor.
  4. [Create a load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/) that includes your newly created pools. This load balancer should be [unproxied (DNS-only)](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing).



[PreviousIntegrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/)[NextMigrate to new GraphQL nodes](https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/additional-dns-records.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
