---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/
title: Cloudflare Advanced DNS Protection \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:45.806678+00:00
---

# Cloudflare Advanced DNS Protection · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systems

  4. /[General settings](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/)
  5. /Advanced DNS Protection



# Advanced DNS Protection

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksSetupData collectionTroubleshooting No data about Advanced DNS Protection in Network AnalyticsRelated products

Cloudflare's Advanced DNS Protection, powered by [`flowtrackd` ↗︎](https://blog.cloudflare.com/announcing-flowtrackd/), provides stateful protection against DNS-based DDoS attacks, specifically sophisticated and fully randomized DNS attacks such as [random prefix attacks](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/about/).

Note

Advanced TCP and DNS Protection systems are automatically enabled in `Monitor` mode with the default thresholds for new Magic Transit customers and their [authorized prefixes](https://developers.cloudflare.com/magic-transit/how-to/advertise-prefixes/).

Magic Transit customers can also enable the Advanced DDoS systems when the prefixes are ready, change the sensitivity level, or adjust the thresholds by contacting their account team.

## How it works

Cloudflare's Advanced DNS Protection works by first learning your traffic patterns and forming a baseline of the type of DNS queries you normally receive. Later, the system will be able to distinguish between legitimate and malicious queries, protecting your DNS infrastructure without impacting legitimate traffic.

Currently, the protection system only analyzes DNS over UDP (it does not include DNS over TCP).

The [Network Analytics dashboard](https://developers.cloudflare.com/analytics/network-analytics/) will display system-specific analytics for Advanced DNS Protection in the **DNS protection** tab, including the queried domains and record types.

* * *

## Setup

[Create a rule](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-rule/#create-an-advanced-dns-protection-rule) to enable Advanced DNS Protection.

* * *

## Data collection

Cloudflare collects DNS-related data such as query type (for example, `A` record) and the queried domains. For details, refer to [Data collection](https://developers.cloudflare.com/analytics/network-analytics/reference/data-collection/).

Caution

Currently, to disable this data collection you must remove your prefixes either in the Cloudflare dashboard or through the [Delete a prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/tcp-protection/#prefix-operations) API operation. However, this procedure will remove the prefixes from both Advanced DNS Protection and [Advanced TCP Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/).

* * *

## Troubleshooting

### No data about Advanced DNS Protection in Network Analytics

If you cannot find any data related to Advanced DNS Protection in the **DNS Protection** tab of Network Analytics, it could be because one of these reasons:

  * You did not [add your prefixes](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/) to Advanced L3/4 DDoS Protection.
  * Accounts that existed before January 2025 were not automatically provisioned. If you onboarded before January 2025, Advanced DNS Protection may not have been enabled for your account.
  * You do not have any DNS over UDP traffic.



* * *

## Related products

Advanced DNS Protection can protect you against volumetric DNS DDoS attacks. To perform DNS caching, proxying, and configuration, use the [Cloudflare DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/).

Currently, Advanced DNS Protection is not available for DNS Firewall.

[PreviousGeneral settings](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/)[NextAdvanced TCP Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
