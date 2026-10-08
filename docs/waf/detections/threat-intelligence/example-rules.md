---
url: https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/
title: Example rules using threat intelligence \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:42.568140+00:00
---

# Example rules using threat intelligence · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Threat intelligence](https://developers.cloudflare.com/waf/detections/threat-intelligence/)
  5. /Example rules



# Example rules

Last updated Jun 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLog matches before blockingBlock DDoS participants targeting your regionChallenge a threat actor targeting the finance sectorFilter by attacker countryCombine with attack scoreRate limit threat actors on API paths

[Custom rule](https://developers.cloudflare.com/waf/custom-rules/) and [rate limiting rule](https://developers.cloudflare.com/waf/rate-limiting-rules/) examples using [threat intelligence fields](https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/). All fields are arrays — use [`any()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#any) with `[*]`.

Caution

Test rules with _Log_ before enforcing. IP-based threat intelligence is a seven-day lookback over shared infrastructure — combine with other signals such as [attack score](https://developers.cloudflare.com/waf/detections/attack-score/) before you block.

## Log matches before blocking

Deploy with _Log_ (Enterprise plans) to review matches before enforcing:

  * **Expression:**  
`any(cf.intel.ip.attacker_names[*] != "")`
  * **Action:** _Log_



Review matches in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/), then change the action to _Block_ or _Managed Challenge_.

## Block DDoS participants targeting your region

  * **Expression:**  
`any(cf.intel.ip.target_countries[*] == "FR") and any(cf.intel.ip.datasets[*] == "ddos")`
  * **Action:** _Block_



## Challenge a threat actor targeting the finance sector

  * **Expression:**  
`any(cf.intel.ip.target_industries[*] == "Banking & Financial Services") and any(cf.intel.ip.attacker_names[*] == "BLACKBASTA")`
  * **Action:** _Managed Challenge_



## Filter by attacker country

  * **Expression:**  
`any(cf.intel.ip.attacker_countries[*] == "CN")`
  * **Action:** _Block_



## Combine with attack score

Block requests flagged by the WAF threat intelligence dataset that also have a low [attack score](https://developers.cloudflare.com/waf/detections/attack-score/):

  * **Expression:**  
`any(cf.intel.ip.datasets[*] == "waf") and cf.waf.score lt 20`
  * **Action:** _Block_



## Rate limit threat actors on API paths

[Rate limiting rule](https://developers.cloudflare.com/waf/rate-limiting-rules/) applying a stricter rate to flagged IPs on your API:

  * **Expression:**  
`any(cf.intel.ip.datasets[*] == "ddos") and starts_with(http.request.uri.path, "/api/")`
  * **Action:** _Block_ when the rate is exceeded.



[PreviousGet started](https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/)[NextAvailable fields](https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/threat-intelligence/example-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
