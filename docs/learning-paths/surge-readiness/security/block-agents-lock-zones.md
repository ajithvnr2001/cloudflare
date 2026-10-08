---
url: https://developers.cloudflare.com/learning-paths/surge-readiness/security/block-agents-lock-zones/
title: Block user agents and lock zones \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:01.125694+00:00
---

# Block user agents and lock zones · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/surge-readiness/security/block-agents-lock-zones/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Surge Readiness

  4. /Security
  5. /Block user agents and lock zones



# Block user agents and lock zones

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/surge-readiness/security/block-agents-lock-zones/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewZone Lockdown

[User Agent (UA) Blocking](https://developers.cloudflare.com/waf/tools/user-agent-blocking/) rules match against specific User-Agent request headers sent by the browser or application accessing your site. UA rules are applied against the entire domain, and after a rule is triggered, you can decide which action to take against the visitor.

Actions:

  * Block: Ensures that an IP address will never be allowed to access your site
  * Interactive Challenge: Visitors will be shown an interactive challenge before allowed access
  * Non-Interactive Challenge: Visitors will be shown a non-interactive challenge before allowed access



## Zone Lockdown

[Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/) rules allow you to define paths and only allow specific, trusted IPs to those paths. Any requests to those paths from non-whitelisted IPs will be automatically blocked with an 1106 HTTP code. This ability is particularly useful for locking down administrative or staging portions of your application.

[PreviousSecure against attacks](https://developers.cloudflare.com/learning-paths/surge-readiness/security/secure-against-attacks/)[NextDefend content with Scrape Shield](https://developers.cloudflare.com/learning-paths/surge-readiness/security/defend-content/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/surge-readiness/security/block-agents-lock-zones.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
