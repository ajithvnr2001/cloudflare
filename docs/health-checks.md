---
url: https://developers.cloudflare.com/health-checks/
title: Health Checks \u00b7 Cloudflare Health Checks docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:28.427286+00:00
---

# Health Checks · Cloudflare Health Checks docs

> Source: https://developers.cloudflare.com/health-checks/

  1. [Home](https://developers.cloudflare.com/)
  2. /Health Checks



# Health Checks

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/health-checks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesRelated productsAvailability

* * *

Smart Shield

This functionality is now offered as part of Cloudflare's origin server safeguard, Smart Shield. [Learn more](https://developers.cloudflare.com/smart-shield/).

Standalone Health Checks monitors an IP address or hostname for origin servers or applications and notifies you in near real-time if there happens to be a problem.

A health check is a service that runs on Cloudflare's edge network to monitor whether an origin server is online. This allows you to view the health of your origin servers even if there is only one origin or you do not yet need to balance traffic across your infrastructure.

Health Checks support various configurations to hone in on what you can check, including response codes, protocol types, and intervals. You can specify a particular path if an origin server serves multiple applications or check a larger subset of response codes for your staging environment. All of these options allow you to properly target your Health Check, providing a precise picture of what is wrong with an origin server.

Note

Standalone Health Checks are different from health monitors associated with load balancers. For more details about health monitors, refer to the [Load Balancing documentation](https://developers.cloudflare.com/load-balancing/monitors/).

* * *

## Features

[Health Checks Analytics](https://developers.cloudflare.com/health-checks/health-checks-analytics/)

You can use Health Checks Analytics to evaluate origin uptime, latency, failure reason, and specific event logs to debug possible origin issues.

Use Health Checks Analytics

* * *

## Related products

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing distributes traffic across your [endpoints](https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-components/), which reduces endpoint strain and latency and improves the experience for end users.

* * *

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | No | Yes | Yes | Yes  
Number of checks | 0 | 10 | 50 | 1,000  
Analytics | No | Yes | Yes | Yes  
  
* * *

[NextGet started](https://developers.cloudflare.com/health-checks/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/health-checks/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
