---
url: https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/
title: Run pre-flight checks \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:47.641058+00:00
---

# Run pre-flight checks · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /Data Center Protection
  4. /Run pre-flight checks



# Run pre-flight checks

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

After setting up your Magic Transit product, Cloudflare validates:

  * Tunnel connectivity
  * Tunnel and endpoint [health checks](https://developers.cloudflare.com/magic-transit/reference/tunnel-health-checks/#types-of-health-checks)
  * Letter of Agency (LOA)
  * Internet Routing Registry (IRR)
  * Maximum segment size (MSS) configurations.



Refer to [Get started](https://developers.cloudflare.com/learning-paths/data-center-protection/get-started/) for information about the above topics.

Configurations for Cloudflare global network are applied and take around one day to rollout.

On your side, you should do the following:

  * Confirm that your upstream ISPs do not have [uRPF](https://developers.cloudflare.com/byoip/troubleshooting/#urpf-filtering-and-packet-loss) strict-mode enabled. If they do, ask them to change this setting to uRPF loose mode. Having strict-mode uRPF will result in packet loss when you advertise your prefix from Cloudflare and withdraw your prefix advertisement from your ISP.
  * Confirm you have adjusted MSS/MTU value on any IPsec or GRE tunnels with third parties that are configured on your Magic Transit prefix.
  * If you are using BGP for Magic Transit prefix advertisement, configure your own alerts/logs for the BGP peerings with Cloudflare route reflectors. Cloudflare will not notify you if these peerings go down, so you should enable this on your equipment using syslog or other event-alerting tools.



[PreviousEnable Notifications](https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/)[NextAdvertise prefixes](https://developers.cloudflare.com/learning-paths/data-center-protection/advertise-prefixes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/data-center-protection/run-pre-flight-checks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
