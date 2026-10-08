---
url: https://developers.cloudflare.com/network-flow/magic-transit-integration/
title: Magic Transit integration \u00b7 Cloudflare Network Flow docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:23.605907+00:00
---

# Magic Transit integration · Cloudflare Network Flow docs

> Source: https://developers.cloudflare.com/network-flow/magic-transit-integration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Flow](https://developers.cloudflare.com/network-flow/)
  3. /Magic Transit integration



# Magic Transit integration

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-flow/magic-transit-integration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewActivate IP auto-advertisement Dashboard API{props.productName} rules

[Magic Transit On Demand](https://developers.cloudflare.com/magic-transit/on-demand/) allows you to keep Magic Transit disabled during normal operations and activate it only when you need DDoS protection. Network Flow monitors your traffic while Magic Transit is off and detects attacks. When an attack is detected, you can enable Magic Transit automatically or manually.

You can create Network Flow rules that monitor specific IP prefixes for DDoS attacks. When an attack is detected, Cloudflare notifies you by email, [webhook](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/), or [PagerDuty](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/).

If you enable auto-advertisement on a rule, Magic Transit activates automatically to protect the targeted prefixes. You can enable auto-advertisement for individual Network Flow rules through the dashboard or API.

After Magic Transit activates and your traffic flows through Cloudflare, Cloudflare blocks malicious DDoS traffic. Your origin servers receive only clean traffic through IPsec or GRE tunnels.

The following diagrams illustrate this process:

![The diagram shows the flow of traffic when you send flow data from your network to Cloudflare for analysis.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1435,height=802,format=webp/_astro/1-flowdata.C2Oap_Pf.png)

![Cloudflare automatically notifies you when Cloudflare detects an attack	based on your flow data.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1436,height=761,format=webp/_astro/2-flowdata.DLOwyPqi.png)

![You can create rules to activate Magic Transit automatically, to protect your IP addresses from a DDoS
attack.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1436,height=761,format=webp/_astro/3-flowdata.CiegeHTC.png)

## Activate IP auto-advertisement

Before a rule can automatically activate Magic Transit, you must enable IP advertisement for the relevant prefixes. You can do this through the dashboard or the API.

### Dashboard

To activate IP advertisement through the Cloudflare dashboard, refer to [Configure dynamic advertisement](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/#configure-dynamic-advertisement).

### API

To activate IP advertisement through the API, refer to the [IP Address Management Dynamic Advertisement API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/).

## Network Flow rules

To create Network Flow rules with auto-advertisement, refer to [Rule Auto-Advertisement](https://developers.cloudflare.com/network-flow/rules/#rule-auto-advertisement).

[PreviousDDoS testing guide](https://developers.cloudflare.com/network-flow/tutorials/ddos-testing-guide/)[NextFree version](https://developers.cloudflare.com/network-flow/network-flow-free/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-flow/magic-transit-integration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
