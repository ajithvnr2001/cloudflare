---
url: https://developers.cloudflare.com/ddos-protection/reference/analytics/
title: DDoS analytics \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:54.854559+00:00
---

# DDoS analytics · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/reference/analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /Reference
  4. /Analytics



# Analytics

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/reference/analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityRemarks

You can view DDoS analytics in different dashboards, depending on your service and plan:

  * The [Security Events dashboard](https://developers.cloudflare.com/waf/analytics/security-events/) provides you with visibility into L7 security events that target your zone, including HTTP DDoS attacks and TCP attacks. The dashboard displays mitigations of HTTP DDoS attacks as HTTP DDoS events. These events are also available via [Cloudflare Logs](https://developers.cloudflare.com/logs/).

  * The [Network Analytics dashboard](https://developers.cloudflare.com/analytics/network-analytics/) provides you with visibility into L3/4 traffic and DDoS attacks that target your IP ranges or Spectrum applications.




## Availability

Service | Free | Pro | Business | Enterprise  
---|---|---|---|---  
WAF/CDN | Sampled logs only | Security Events | Security Events | Security Events  
Spectrum/BYOIP | – | – | – | Network Analytics  
Magic Transit | – | – | – | Network Analytics  
  
## Remarks

In some situations, the analytics dashboards will not show you the ID of the DDoS managed rule that handled a packet/request. This means that an internal DDoS rule, which Cloudflare does not currently expose publicly, applied an action to the packet/request. These internal DDoS rules have a very low false positive rate and should always be enabled to protect your properties against DDoS attacks. For the same reason, DDoS rule IDs may also be unavailable in Cloudflare logs and API responses.

[PreviousBotnet Threat Feed](https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/)[NextReports](https://developers.cloudflare.com/ddos-protection/reference/reports/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/reference/analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
