---
url: https://developers.cloudflare.com/learning-paths/data-center-protection/concepts/what-is-magic-transit/
title: What is Magic Transit? \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:47.025428+00:00
---

# What is Magic Transit? · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/data-center-protection/concepts/what-is-magic-transit/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Data Center Protection

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/data-center-protection/concepts/)
  5. /What is Magic Transit?



# What is Magic Transit?

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/data-center-protection/concepts/what-is-magic-transit/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic Transit is a network security and performance solution that offers Distributed Denial-of-Service (DDoS) protection, traffic acceleration, and more for on-premise, cloud-hosted, and hybrid networks.

Magic Transit works at Layer 3 of the [OSI model ↗︎](https://www.cloudflare.com/en-gb/learning/ddos/glossary/open-systems-interconnection-model-osi/), protecting entire IP networks from DDoS attacks. Instead of relying on local infrastructure that can be overwhelmed by large DDoS attacks, Magic Transit uses the [global Cloudflare Network ↗︎](https://www.cloudflare.com/network/) to ingest and mitigate attacks close to their source.

Magic Transit delivers its connectivity, security, and performance benefits by serving as the front door to your IP network. This means it accepts IP packets destined for your network, processes them, and then forwards them to your origin infrastructure.

The Cloudflare network uses Border Gateway Protocol (BGP) to announce your company's IP address space, extending your network presence globally, and [anycast](https://developers.cloudflare.com/magic-transit/reference/gre-ipsec-tunnels/#anycast) to absorb and distribute attack traffic.

Once packets hit Cloudflare's network, traffic is inspected for attacks, filtered, steered, accelerated, and sent onward to your origin. Magic Transit users have two options for their implementation: ingress traffic or ingress and egress traffic. Users with an egress implementation will need to set up policy-based routing (PBR) or ensure default routing on their end forwards traffic to Cloudflare via tunnels.

For an in-depth explanation of Magic Transit, refer to [Magic Transit Reference Architecture](https://developers.cloudflare.com/reference-architecture/architectures/magic-transit/).

[PreviousOverview](https://developers.cloudflare.com/learning-paths/data-center-protection/concepts/)[NextBenefits of using Magic Transit](https://developers.cloudflare.com/learning-paths/data-center-protection/concepts/benefits-magic-transit/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/data-center-protection/concepts/what-is-magic-transit.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
