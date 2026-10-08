---
url: https://developers.cloudflare.com/ddos-protection/about/components/
title: Main components \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:44.340521+00:00
---

# Main components · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/about/components/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /[About](https://developers.cloudflare.com/ddos-protection/about/)
  4. /Main components



# Main components

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/about/components/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAutonomous EdgeCentralized DDoS protection system

![Diagram with the main components providing protection against DDoS attacks at Cloudflare](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2495,height=1700,format=webp/_astro/ddos-diagram.DygBAs9m.png)

## Autonomous Edge

The Cloudflare Autonomous Edge is powered by the denial-of-service daemon (`dosd`), which is a home-grown software-defined system. The flow tracking daemon, `flowtrackd`, is our stateful mitigation platform alongside `dosd`. A `dosd` instance runs in every single server in every one of [Cloudflare global network's data centers ↗︎](https://www.cloudflare.com/network/) around the world. These `dosd` instances can detect and mitigate DDoS attacks autonomously without requiring centralized consensus. Cloudflare users can configure this system through [DDoS Attack Protection managed rulesets](https://developers.cloudflare.com/ddos-protection/managed-rulesets/).

Another component of Cloudflare's Autonomous Edge includes the [Advanced TCP Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/) system. This is Cloudflare's TCP state tracking machine for detecting and mitigating the most randomized and sophisticated TCP-based DDoS attacks in unidirectional routing topologies — such as the case of [Magic Transit](https://developers.cloudflare.com/magic-transit/). Advanced TCP Protection is able to identify the state of a TCP connection and then drops, challenges, or rate-limits packets that do not belong to a legitimate connection.

For more information, refer to our blog post [A deep-dive into Cloudflare's autonomous edge DDoS protection ↗︎](https://blog.cloudflare.com/deep-dive-cloudflare-autonomous-edge-ddos-protection/).

## Centralized DDoS protection system

Complementary to the Autonomous Edge, Cloudflare's entire global network is overwatched by a global version of `dosd`. This component protects Cloudflare's entire global network by detecting and mitigating globally distributed volumetric DDoS attacks.

The centralized systems run in Cloudflare's core data centers. They receive samples from every global network data center, analyze them, and automatically send mitigation instructions when detecting an attack. The system is also synchronized to each of our customers' web servers to identify their health and trigger any required mitigation actions.

[PreviousHow DDoS protection works](https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/)[NextAttack coverage](https://developers.cloudflare.com/ddos-protection/about/attack-coverage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/about/components.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
