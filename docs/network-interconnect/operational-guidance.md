---
url: https://developers.cloudflare.com/network-interconnect/operational-guidance/
title: Operational guidance \u00b7 Cloudflare Network Interconnect docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:24.955944+00:00
---

# Operational guidance · Cloudflare Network Interconnect docs

> Source: https://developers.cloudflare.com/network-interconnect/operational-guidance/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)
  3. /Operational guidance



# Operational guidance

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-interconnect/operational-guidance/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCustomer responsibilityTroubleshooting

For maintenance expectations and notifications, refer to [Maintenance](https://developers.cloudflare.com/network-interconnect/maintenance/).

## Customer responsibility

Your CNI deployment must tolerate an unplanned outage on any single circuit at any time. This means:

  * Traffic failover between redundant circuits must be automatic.
  * If your operations require manual intervention to reroute traffic during maintenance, your configuration needs review.
  * Contact your account team to validate your failover design.



## Troubleshooting

When facing connectivity problems, your first action should be to check for broader service disruptions. Visit [Cloudflare Status ↗︎](https://www.cloudflarestatus.com/) to see if any scheduled maintenance or active incidents are impacting services. This helps determine if the issue originates outside your network. Refer to [Monitoring and alerts](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/).

If no system-wide problems are reported, gather the following information before submitting a support case. Providing comprehensive details facilitates a faster resolution:

  * **Timeline** : When the issue began and ended (if applicable), including the timezone.
  * **Identification** : The CNI IP address or point-to-point prefix for the impacted CNI. If your CNI is part of a Magic setup, please also provide the name of the Magic Transit/WAN interconnect as listed in your dashboard.
  * **Physical Layer** : Light levels of the CNI link (if applicable).
  * **Service Impact** : Confirmation whether Magic Transit / WAN traffic was affected.
  * **Problem Description** : A clear summary of the issue (for example, CNI down, Border Gateway Protocol (BGP) session down, prefixes withdrawn).



[PreviousMaintenance](https://developers.cloudflare.com/network-interconnect/maintenance/)[NextChangelog](https://developers.cloudflare.com/network-interconnect/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-interconnect/operational-guidance.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
