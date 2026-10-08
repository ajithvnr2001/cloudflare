---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/
title: Use egress policies to deliver consistent egress IPs \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:55.878599+00:00
---

# Use egress policies to deliver consistent egress IPs · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Control traffic egress with source IP anchoring and allowlisting](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/)
  5. /Use egress policies to deliver consistent egress IPs



# Use egress policies to deliver consistent egress IPs

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Only available on Enterprise plans.

Egress policies allow you to determine whether your organization's traffic egresses via the default Cloudflare IP or via a [dedicated egress IP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/) assigned to your account.

To create a new egress policy:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Egress policies**.

  2. Select **Add a policy**.

  3. Name the policy.

  4. Build a logical expression that defines the traffic you want to control egress for. For example, you can add a policy to configure all traffic destined for a third-party network to use a static source IP:

Policy name | Selector | Operator | Value | Egress method  
---|---|---|---|---  
Access third-party provider | Destination IP | is | `198.51.100.158` | Dedicated Cloudflare egress IPs  
  
Primary IPv4 address | IPv6 address  
---|---  
`203.0.113.88` | `2001:db8::/32`  
  
  5. Select **Create policy**.




For more information, refer to [Egress policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/).

[PreviousEgress IP best practices](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/deploy-egress-ips/)[NextOverview](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/secure-saas-applications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
