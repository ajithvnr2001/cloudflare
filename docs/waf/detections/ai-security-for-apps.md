---
url: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/
title: AI Security for Apps \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:39.760376+00:00
---

# AI Security for Apps · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Traffic detections](https://developers.cloudflare.com/waf/detections/)
  4. /AI Security for Apps



# AI Security for Apps

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityMore resources

Applications that use large language models (LLMs) are exposed to threats specific to how LLMs process input — prompt injection attacks, PII exposure in prompts, and prompts about unsafe topics.

AI Security for Apps (formerly Firewall for AI) complements your existing WAF rules with detections designed for these LLM-specific threats. It is model-agnostic — the detections work regardless of which LLM you use.

  * [PII detection](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/) — Detect personally identifiable information (PII) in incoming prompts, such as phone numbers, email addresses, social security numbers, and credit card numbers.
  * [Unsafe and custom topic detection](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/) — Detect prompts related to unsafe subjects such as violent crimes or hate speech, or custom topics specific to your organization.
  * [Prompt injection detection](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/prompt-injection/) — Detect prompts designed to subvert your LLM's intended behavior, such as attempts to make the model ignore its instructions or reveal its system prompt.



When enabled, AI Security for Apps scans incoming requests to [endpoints labeled `cf-llm`](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/) for LLM prompts that may contain threats. Currently, the detection only handles requests with a JSON content type (`application/json`).

Based on scan results, Cloudflare populates [AI detection fields](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/) — fields you can use in WAF rule expressions. You can use these fields in two ways:

  * **Monitor:** Filter by the `cf-llm` label in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) to review detection results across your traffic.
  * **Mitigate:** Use the fields in [custom rules](https://developers.cloudflare.com/waf/custom-rules/) or [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) to block or challenge requests based on detection results.



## Availability

AI Security for Apps capabilities vary by Cloudflare plan:

Capability | Free | Pro | Business | Enterprise  
---|---|---|---|---  
**LLM endpoint discovery** — Automatically identify AI-powered endpoints across your web properties | Yes | Yes | Yes | Yes  
**AI Security Log Mode Ruleset** — Pre-built ruleset that logs the full request body alongside detection results | No | No | No | Paid add-on  
**AI detection fields** — PII detection, prompt injection scoring, unsafe topic detection, custom topics | No | No | No | Paid add-on  
  
To get access to the [AI Security Log Mode Ruleset](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/#log-mode) and enable [AI detection fields](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/), contact your account team.

AI Security for Apps is built into the Cloudflare [Web Application Firewall (WAF)](https://developers.cloudflare.com/waf/) — the WAF must be enabled on your zone before detection fields can be populated and used in rule expressions.

## More resources

  * [AI Gateway](https://developers.cloudflare.com/ai-gateway/) — Monitor, control, and cache requests to LLM providers.
  * [What are the OWASP Top 10 risks for LLMs? ↗︎](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/) — Background on the most common security risks for LLM-powered applications.



[PreviousTerraform examples](https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/)[NextGet started](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/ai-security-for-apps/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
