---
url: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/
title: PII detection \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:40.147980+00:00
---

# PII detection · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/)
  5. /PII detection



# PII detection

Last updated Aug 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAI-based PII detection Be specific to reduce false positives Example rules — AI-based detectionExact PII detection (regex) Example: Detect employee IDs More regex examples Considerations for regex rulesCombine both approaches

AI Security for Apps (formerly Firewall for AI) can detect personally identifiable information (PII) in incoming LLM prompts. There are two approaches to PII detection, and you can use them together for layered protection:

  * AI-based detection — AI Security for Apps uses an AI model to identify common PII types in the prompt content. This approach catches PII even when it appears in natural language or unexpected formats.
  * Exact detection (regex) — You write a WAF custom rule with a regular expression on the raw request body. This approach is ideal for organization-specific identifiers with a known, predictable format.



## AI-based PII detection

When AI Security for Apps is enabled and a request arrives at a `cf-llm` labeled endpoint, it scans the prompt for PII and populates two fields:

  * **LLM PII detected** ([`cf.llm.prompt.pii_detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_detected/)) — `true` if any PII was found.
  * **LLM PII categories** ([`cf.llm.prompt.pii_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/)) — An array of the specific PII types found.



The detection is powered by an AI-based Named Entity Recognition (NER) model. Refer to the [`cf.llm.prompt.pii_categories` field reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/) for the full list of recognized categories.

Detecting PII in responses

AI Security for Apps PII detection runs on incoming requests (prompts) only. If you also need to detect PII in LLM responses, you can use [Sensitive Data Detection](https://developers.cloudflare.com/waf/managed-rules/reference/sensitive-data-detection/) to scan response bodies for patterns like credit card numbers, Social Security numbers, and API keys. Sensitive Data Detection logs matches, but does not block responses. Use it alongside request-side rules for layered visibility.

Supported PII categories

Category | Description  
---|---  
`BANK_ACCOUNT` | Bank account number  
`CREDIT_CARD` | Credit card number  
`DATE_TIME` | Date or time expression  
`DRIVER_LICENSE` | Driver license number  
`EMAIL_ADDRESS` | Email address  
`IP_ADDRESS` | IPv4 address  
`LOCATION` | Physical location or address  
`PASSPORT` | Passport number  
`PERSON` | Full or partial name of an individual  
`PHONE_NUMBER` | Phone number  
`TAX_ID` | Tax identification number  
`US_SSN` | US Social Security Number  
`URL` | URL  
  
### Be specific to reduce false positives

The `cf.llm.prompt.pii_detected` field returns `true` when any PII category is detected — including broad categories like `PERSON`, `DATE_TIME`, and `LOCATION` that frequently appear in normal conversation. Blocking based on this field alone will produce a high false-positive rate for most applications.

Instead, build rules against `cf.llm.prompt.pii_categories` and list only the categories that matter for your use case. For example, a customer support chatbot may need to block credit card numbers and SSNs but can safely ignore person names and dates. Start with the narrowest set of categories, monitor matches in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/), and expand only as needed.

### Example rules — AI-based detection

#### Block any request containing PII

  * **When incoming requests match** :

Field | Operator | Value  
---|---|---  
LLM PII Detected | equals | True  
  
Expression when using the editor:  
`(cf.llm.prompt.pii_detected)`

  * **Action** : _Block_




#### Block only specific PII categories

  * **When incoming requests match** :

Field | Operator | Value  
---|---|---  
LLM PII Categories | is in | `Credit Card`  
  
Expression when using the editor:  
`(any(cf.llm.prompt.pii_categories[*] in {"CREDIT_CARD"}))`

  * **Action** : _Block_




#### Log email addresses but block credit cards and SSNs

Create two [custom rules](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/):

  1. A rule with action _Block_ and the following expression:  
`(any(cf.llm.prompt.pii_categories[*] in {"CREDIT_CARD" "US_SSN"}))`

  2. A rule with action _Log_ and the following expression:  
`(any(cf.llm.prompt.pii_categories[*] in {"EMAIL_ADDRESS"}))`




## Exact PII detection (regex)

If you need to detect **custom PII formats** specific to your organization — such as internal employee IDs, patient record numbers, or proprietary account identifiers — you can create a WAF [custom rule](https://developers.cloudflare.com/waf/custom-rules/) using a regex match on the raw body ([`http.request.body.raw`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.raw/) field).

This approach complements AI-based detection by matching predefined patterns, including organization-specific identifiers.

### Example: Detect employee IDs

In the following example, an organization uses employee IDs in the format `EMP-` followed by exactly six digits (for example, `EMP-482910`).

[Create a custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) with the following configuration:

  * **When incoming requests match** :

Field | Operator | Value  
---|---|---  
Raw request body | matches regex | `EMP-[0-9]{6}`  
  
Expression when using the editor:  
`(http.request.body.raw matches "EMP-[0-9]{6}")`

  * **Action** : _Block_

  * **With response type** : Custom JSON

  * **Response body** : `{ "error": "Request blocked: employee ID detected in prompt." }`




Scope to a specific endpoint

To limit this rule to only your LLM endpoint, combine it with a path condition:

Field | Operator | Value | Logic  
---|---|---|---  
URI Path | equals | `/api/chat` | And  
Raw request body | matches regex | `EMP-[0-9]{6}` |   
  
Expression when using the editor:  
`(http.request.uri.path eq "/api/chat" and http.request.body.raw matches "EMP-[0-9]{6}")`

### More regex examples

Custom PII type | Example format | Regex pattern  
---|---|---  
Employee ID | `EMP-482910` | `EMP-[0-9]{6}`  
Patient record number | `PAT/2024/00391` | `PAT/[0-9]{4}/[0-9]{5}`  
Internal account ID | `ACCT-XX-99999` | `ACCT-[A-Z]{2}-[0-9]{5}`  
Custom API key prefix | `sk_live_abc123...` | `sk_live_[a-zA-Z0-9]{20,}`  
  
### Considerations for regex rules

  * **Cloudflare Plan requirement.** Regex operators (`matches` and `~`) require a Business or Enterprise plan.
  * **Body size limit.** The `http.request.body.raw` field inspects a limited portion of the request body. The exact limit [varies by plan](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.raw/).
  * **JSON payloads.** The raw body includes the full JSON structure. Your regex should account for the fact that the prompt text is nested inside a JSON string.
  * **Performance.** Complex regex patterns can impact rule evaluation time. Keep patterns as specific as possible.



## Combine both approaches

You can use AI-based and exact detection together for layered protection:

`(cf.llm.prompt.pii_detected or http.request.body.raw matches "EMP-[0-9]{6}")`

This rule blocks requests where either the AI model detects any built-in PII category or the regex matches your custom identifier format.

[PreviousGet started](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/get-started/)[NextUnsafe and custom topic detection](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/ai-security-for-apps/pii-detection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
