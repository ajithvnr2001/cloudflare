---
url: https://developers.cloudflare.com/learning-paths/data-center-protection/advertise-prefixes/
title: Advertise prefixes \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:46.833150+00:00
---

# Advertise prefixes · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/data-center-protection/advertise-prefixes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /Data Center Protection
  4. /Advertise prefixes



# Advertise prefixes

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/data-center-protection/advertise-prefixes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Once pre-flight checks are completed, Cloudflare unlocks your prefixes for you to [advertise via the dashboard, API or BGP](https://developers.cloudflare.com/magic-transit/how-to/advertise-prefixes/) at a time of your choosing. Refer to [Dynamic advertisement best practices](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/) to learn more about advertising prefixes.

If you are using a Cloudflare IP, you do not need to advertise your prefixes.

Caution

You must put the appropriate MSS clamps in place before [routing ↗︎](https://www.cloudflare.com/learning/network-layer/what-is-routing/) changes are made. Failure to apply an MSS clamp can result in dropped packets and hard-to-debug connectivity issues.

Also, when using [Cloudflare Network Interconnect](https://developers.cloudflare.com/magic-transit/network-interconnect/) with Magic Transit you must set the following MSS clamp sizes to accommodate additional overhead:

  * GRE tunnels over CNI with Dataplane v1: 1476 bytes
  * CNI with Dataplane v2 / CNI with Dataplane v1 with a maximum transmission unit (MTU) size of 1500 bytes handoff does not require an MSS clamp.



MSS clamps are used to backhaul data from the data center where traffic is ingested (close to the end user) to the facility with the CNI link.

[PreviousRun pre-flight checks](https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/)[NextTroubleshooting connectivity issues after prefix advertisement](https://developers.cloudflare.com/learning-paths/data-center-protection/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/data-center-protection/advertise-prefixes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
