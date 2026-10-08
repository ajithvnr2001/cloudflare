---
url: https://developers.cloudflare.com/learning-paths/surge-readiness/security/enable-iaum/
title: What to do when under attack \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:01.384163+00:00
---

# What to do when under attack · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/surge-readiness/security/enable-iaum/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Surge Readiness

  4. /Security
  5. /What to do when under attack



# What to do when under attack

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/surge-readiness/security/enable-iaum/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable "I'm Under Attack" mode (IAUM)Change Access Control List (ACL)Change Origin IPs and update Cloudflare DNS records

## Enable "I'm Under Attack" mode (IAUM)

If you are under attack and have this feature enabled during the attack, visitors will receive an interstitial page for about five seconds while the traffic is analyzed to make sure it is a legitimate human visitor. The vast majority of Layer 7 attack scripts are defeated by IUAM and can be honed via Page Rules.

Refer to [I'm Under Attack Mode ↗︎](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/) for more information.

## Change Access Control List (ACL)

An ACL refers to rules that are applied to port numbers or IP addresses that are available on a host permitting use of the service. When you only allow Cloudflare IPs, you eliminate threats attempting to attack your origin IP range.

Refer to [Cloudflare IP Ranges ↗︎](https://www.cloudflare.com/ips) for more information.

## Change Origin IPs and update Cloudflare DNS records

If your origin is still being attacked, consider moving your Origin IPs and updating your Cloudflare DNS records.

Refer to [Prevent DDoS attacks](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/concepts/) for detailed guidance.

Note

To learn about best practices for DDoS protection, review [Proactive DDoS defense](https://developers.cloudflare.com/ddos-protection/best-practices/proactive-defense/).

[PreviousControl domain access](https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/)[NextCaching](https://developers.cloudflare.com/learning-paths/surge-readiness/performance/caching/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/surge-readiness/security/enable-iaum.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
