---
url: https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/
title: Control domain access \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:01.215363+00:00
---

# Control domain access · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Surge Readiness

  4. /Security
  5. /Control domain access



# Control domain access

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-domain-access/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[IP Access Rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/) specify an action based on the origin of your user across a single domain or all of the domains in your account.

IP Access Rules can be applied based on:

  * IPv4 address or range: Specified in CIDR notation as `/16` or `/24`
  * IPv6 address or range: Specified in CIDR notation as `/32`, `/48`, `/64`
  * ASN
  * Country or the Tor network



Note

We recommend locking down your origin with an Access Control List (ACL) which only allows [Cloudflare IPs ↗︎](http://www.cloudflare.com/ips).

Actions:

  * Block: Ensures that an IP address will never be allowed to access your site.
  * Non-Interactive Challenge: Visitors will be shown a non-interactive challenge before allowed access.
  * Interactive Challenge: Visitors will be shown an interactive challenge before allowed access.
  * Allowlist: Ensures that an IP address will never be blocked from accessing your site. This supersedes any Cloudflare security profile.



[PreviousDefend content with Scrape Shield](https://developers.cloudflare.com/learning-paths/surge-readiness/security/defend-content/)[NextWhat to do when under attack](https://developers.cloudflare.com/learning-paths/surge-readiness/security/enable-iaum/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/surge-readiness/security/control-domain-access.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
