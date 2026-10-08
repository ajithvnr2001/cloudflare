---
url: https://developers.cloudflare.com/waf/custom-rules/skip/options/
title: Available skip options \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:37.900149+00:00
---

# Available skip options · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/skip/options/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /[Configure a rule with the Skip action](https://developers.cloudflare.com/waf/custom-rules/skip/)
  5. /Skip options



# Available skip options

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/skip/options/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSkip the remaining custom rules (current ruleset)Skip phasesSkip productsSkip the remaining custom rules (current phase)Other options Log requests matching the skip rule

The following sections cover the available skip options in custom rules.

## Skip the remaining custom rules (current ruleset)

  * Dashboard option: **All remaining custom rules**
  * API action parameter: `ruleset`



Skips the remaining rules in the current ruleset.

## Skip phases

Note

When an account-level skip rule uses the phases action parameter, Cloudflare skips the specified phases at both the account and zone levels for matching requests.

  * Dashboard options: **All rate limiting rules** , **All Super Bot Fight Mode rules** , and **All managed rules**
  * API action parameter: `phases`



Skips the execution of one or more phases. Based on the phases you can skip, this option effectively allows you to skip [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/), [Super Bot Fight Mode rules](https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/), and/or [WAF Managed Rules](https://developers.cloudflare.com/waf/managed-rules/).

The phases you can skip are the following:

  * `http_ratelimit`
  * `http_request_sbfm`
  * `http_request_firewall_managed`



Refer to [Phases](https://developers.cloudflare.com/ruleset-engine/about/phases/) for more information.

Notes

Currently, you cannot skip [Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/), only Super Bot Fight Mode.

Skipping a phase does not skip security products that run outside the Ruleset Engine, such as [Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/) or [Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/). To skip those products, use the Skip products option instead.

## Skip products

  * API action parameter: `products`



Skips specific security products that are not based on the Ruleset Engine. The products you can skip are the following:

Product name in the dashboard | API value  
---|---  
[Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/) | `zoneLockdown`  
[User Agent Blocking](https://developers.cloudflare.com/waf/tools/user-agent-blocking/) | `uaBlock`  
[Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/) | `bic`  
[Hotlink Protection](https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/) | `hot`  
[Security Level](https://developers.cloudflare.com/waf/tools/security-level/) | `securityLevel`  
[Rate limiting rules (Previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/) | `rateLimit`  
[Managed rules (Previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/) | `waf`  
  
The API values in the table are case-sensitive.

## Skip the remaining custom rules (current phase)

  * Dashboard option: N/A (currently only available via API)
  * API action parameter: `phase`



The `phase: "current"` option is supported only in zone-level custom and entry point rulesets for the `http_request_firewall_custom` phase. When matched, it skips all remaining rules in the phase, including rules in custom rulesets executed later.

## Other options

### Log requests matching the skip rule

  * Dashboard option: **Log matching requests**
  * API action parameter: `logging` > `enabled` (boolean, optional)



When disabled, Cloudflare will not log any requests matching the current skip rule, and these requests will not appear in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/).

If you do not specify this option in the API, the default value is `true` for custom rules with the skip action (logs requests matching the skip rule).

[PreviousAPI examples](https://developers.cloudflare.com/waf/custom-rules/skip/api-examples/)[NextAllow traffic from IP addresses in allowlist only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/skip/options.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
