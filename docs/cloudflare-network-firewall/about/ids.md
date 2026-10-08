---
url: https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/
title: IDS \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:06.433866+00:00
---

# IDS · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /[About](https://developers.cloudflare.com/cloudflare-network-firewall/about/)
  4. /IDS



# IDS

Last updated Sep 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Unified Routing availability

IDS is beta for Cloudflare WAN accounts using Unified Routing and is not available for Magic Transit accounts using Unified Routing. Review feature availability for [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading) and [Magic Transit](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/#check-feature-availability-before-upgrading).

Cloudflare's Intrusion Detection System (IDS) is a Cloudflare Advanced Network Firewall (formerly Magic Firewall) feature you can use to actively monitor for a wide range of known threat signatures in your traffic. An IDS expands the security coverage of a firewall to analyze traffic against a broader threat database, detecting a variety of sophisticated attacks such as ransomware, data exfiltration, and network scanning based on signatures or “fingerprints” in network traffic.

With Cloudflare's global anycast network, you get:

  * Cloudflare's entire global network capacity is now the capacity of your IDS.
  * Built in redundancy and failover. Every server runs Cloudflare's IDS software, and traffic is automatically attracted to the closest network location to its source.
  * Continuous deployment for improvements to Cloudflare's IDS capabilities.



Refer to [Enable IDS](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-ids/) for more information on enabling IDS and creating new rulesets. After IDS is enabled, your traffic will be scanned to find malicious traffic. The detections are logged to destinations that can be configured from the dashboard. Refer to [Use Logpush with IDS](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/) for instructions on configuring a destination to receive the detections. Additionally, all traffic that is analyzed can be accessed via [network analytics](https://developers.cloudflare.com/analytics/network-analytics/). Refer to [GraphQL Analytics](https://developers.cloudflare.com/cloudflare-network-firewall/tutorials/graphql-analytics/) to query the analytics data.

[PreviousAnalytics](https://developers.cloudflare.com/cloudflare-network-firewall/about/analytics/)[NextList types](https://developers.cloudflare.com/cloudflare-network-firewall/about/list-types/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/about/ids.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
