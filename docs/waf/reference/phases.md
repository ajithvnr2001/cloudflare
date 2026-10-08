---
url: https://developers.cloudflare.com/waf/reference/phases/
title: WAF phases \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:47.353861+00:00
---

# WAF phases · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/reference/phases/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Reference
  4. /Phases



# WAF phases

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/reference/phases/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Web Application Firewall provides the following [phases](https://developers.cloudflare.com/ruleset-engine/about/phases/) where you can create rulesets and rules:

  * `http_request_firewall_custom`
  * `http_ratelimit`
  * `http_request_firewall_managed`



These phases exist both at the account level and at the zone level. Considering the available phases and the two different levels, rules will be evaluated in the following order:

Security feature | Scope | Phase | Ruleset kind | Location in the dashboard  
---|---|---|---|---  
[Custom rulesets](https://developers.cloudflare.com/waf/account/custom-rulesets/)  
| Account | `http_request_firewall_custom` | `custom` (create)  
`root` (deploy) | [ Go to **WAF** ↗ ](https://dash.cloudflare.com/?to=/:account/application-security/waf) > **Custom rulesets** tab  
[Custom rules](https://developers.cloudflare.com/waf/custom-rules/) | Zone | `http_request_firewall_custom` | `zone` | [ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)  
[Rate limiting rulesets](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/) | Account | `http_ratelimit` | `root` | [ Go to **WAF** ↗ ](https://dash.cloudflare.com/?to=/:account/application-security/waf) > **Rate limiting rulesets** tab  
[Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) | Zone | `http_ratelimit` | `zone` | [ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)  
[Managed rulesets](https://developers.cloudflare.com/waf/account/managed-rulesets/) | Account | `http_request_firewall_managed` | `root` | [ Go to **WAF** ↗ ](https://dash.cloudflare.com/?to=/:account/application-security/waf) > **Managed rulesets** tab  
[Managed rules](https://developers.cloudflare.com/waf/managed-rules/) | Zone | `http_request_firewall_managed` | `zone` | [ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)  
  
To learn more about phases, refer to [Phases](https://developers.cloudflare.com/ruleset-engine/about/phases/) in the Ruleset Engine documentation.

[PreviousAlerts](https://developers.cloudflare.com/waf/reference/alerts/)[NextOverview](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/reference/phases.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
