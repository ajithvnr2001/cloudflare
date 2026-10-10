---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.appsec.request.failed_detections/
title: cf.appsec.request.failed_detections \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:35.864152+00:00
---

# cf.appsec.request.failed_detections · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.appsec.request.failed_detections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Appsec.Request.Failed_detections



# cf.appsec.request.failed_detections

`cf.appsec.request.failed_detections``Array<String>`

IDs of supported detections that reported failures for the request.

The field contains IDs of detections that reported failures before custom rules are evaluated, so you can act on those failures.

The default value is `[]`, which means no detection failures were reported.

Duplicate IDs are removed. Array order is not guaranteed.

The field does not alter the existing behavior of detections. Use it in rules to choose how to handle requests with reported failures.

Supported in zone and account custom rules and rate limiting rules. Also supported in zone Request Header Transform Rules.

The field is available on all plans, but using it does not grant access to detections or rule features that your plan does not include.

The possible IDs are:

ID | Detection  
---|---  
`waf_content_scan` | Content scanning  
`waf_score` | WAF attack score  
`waf_signature` | Attack signature detection  
`waf_credential_check` | Leaked credentials detection  
`llm_prompt_pii` | LLM prompt PII detection  
`llm_prompt_injection` | LLM prompt injection detection  
`llm_prompt_custom_topic` | LLM prompt custom topic detection  
`llm_prompt_unsafe_topic` | LLM prompt unsafe topic detection  
  
Example value:
    
    
    ["waf_score"]

Example usage:
    
    
    # Match any reported detection failure
    len(cf.appsec.request.failed_detections) gt 0
    
    # Match a reported WAF attack score failure
    any(cf.appsec.request.failed_detections[*] eq "waf_score")
    
    # Join IDs for a request header value
    join(cf.appsec.request.failed_detections, ",")

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
