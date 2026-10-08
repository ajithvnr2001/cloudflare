---
url: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/
title: AI Security for Apps fields \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:40.193528+00:00
---

# AI Security for Apps fields · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/)
  5. /Available fields



# AI Security for Apps fields

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When enabled, AI Security for Apps populates the following fields:

Field | Description  
---|---  
LLM PII detected   
[`cf.llm.prompt.pii_detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_detected/)   
`Boolean` | Indicates whether any personally identifiable information (PII) has been detected in the LLM prompt included in the request.  
LLM PII categories   
[`cf.llm.prompt.pii_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/)   
`Array<String>` | Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.  
[Category list](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/)  
LLM Content detected   
[`cf.llm.prompt.detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/)   
`Boolean ` | Indicates whether Cloudflare detected an LLM prompt in the incoming request.  
LLM Unsafe topic detected   
[`cf.llm.prompt.unsafe_topic_detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_detected/)   
`Boolean` | Indicates whether the incoming request includes any unsafe topic category in the LLM prompt.  
LLM Unsafe topic categories   
[`cf.llm.prompt.unsafe_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/)   
`Array<String>` | Array of string values with the type of unsafe topics detected in the LLM prompt.  
[Category list](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/)  
LLM Injection score   
[`cf.llm.prompt.injection_score`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/)   
`Number` | A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack. Lower scores indicate higher risk.  
LLM Token count   
[`cf.llm.prompt.token_count`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.token_count/)   
`Number` | An estimated token count for the LLM prompt in the request. Refer to [Token counting](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/token-counting/) for details.  
LLM Custom topic categories   
[`cf.llm.prompt.custom_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/)   
`Map<Number>` | A map of custom topic labels to relevance scores (1–99). Lower scores indicate the prompt is more relevant to that topic. Only populated when [custom topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics) are configured.  
  
[PreviousLog mode vs production mode](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/)[NextOverview](https://developers.cloudflare.com/waf/detections/threat-intelligence/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/ai-security-for-apps/fields.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
