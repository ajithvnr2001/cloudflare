---
url: https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/
title: OWASP evaluation example \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:45.176551+00:00
---

# OWASP evaluation example · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)Rulesets reference

  4. /[Cloudflare OWASP Core Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/)
  5. /Evaluation example



# OWASP evaluation example

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following example calculates the OWASP request threat score for an incoming request. The OWASP managed ruleset configuration is the following:

  * OWASP Anomaly Score Threshold: _High - 25 and higher_
  * OWASP Paranoia Level: _PL3_
  * OWASP Action: _Managed Challenge_



This table shows the progress of the OWASP ruleset evaluation:

Rule ID | Paranoia level | Rule matched? | Rule score | Cumulative  
threat score  
---|---|---|---|---  
– | – | – | – | 0  
`...1813a269` | PL3 | Yes | +5 | 5  
`...ccc02be6` | PL3 | No | – | 5  
`...96bfe867` | PL2 | Yes | +5 | 10  
`...48b74690` | PL1 | Yes | +5 | 15  
`...3297003f` | PL2 | Yes | +3 | 18  
`...317f28e1` | PL1 | No | – | 18  
`...682bb405` | PL2 | Yes | +5 | 23  
`...56bb8946` | PL2 | No | – | 23  
`...e5f94216` | PL3 | Yes | +3 | 26  
(...) | (...) | (...) | (...) | (...)  
`...f3b37cb1` | PL4 | (not evaluated) | – | 26  
  
Final request threat score: `26`

Since `26` >= `25` — that is, the threat score is greater than the configured score threshold — Cloudflare will apply the configured action (_Managed Challenge_). If you had configured a score threshold of _Medium - 40 and higher_ , Cloudflare would not apply the action, since the request threat score would be lower than the score threshold (`26` < `40`).

[**Sampled logs** in Security Events](https://developers.cloudflare.com/waf/analytics/security-events/#sampled-logs) would display the following details for the example incoming request handled by the OWASP Core Ruleset:

![Event log for example incoming request mitigated by the OWASP Core Ruleset](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1160,height=818,format=webp/_astro/owasp-example-event-log.B3Lc0T9C.png)

In sampled logs, the rule associated with requests mitigated by the Cloudflare OWASP Core Ruleset is the last rule in this managed ruleset: `949110: Inbound Anomaly Score Exceeded`, with rule ID ...843b323c. To get the scores of individual rules contributing to the final request threat score, expand **Additional logs** in the event details.

[PreviousConcepts](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/)[NextConfigure in the dashboard](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/reference/owasp-core-ruleset/example.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
