---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/
title: cf.llm.prompt.pii_categories \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:03.786829+00:00
---

# cf.llm.prompt.pii_categories · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Llm.Prompt.Pii_categories



# cf.llm.prompt.pii_categories

`cf.llm.prompt.pii_categories``Array<String>`

Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.

The possible values are the following:

Category | Description  
---|---  
`BANK_ACCOUNT` | Bank account number  
`CREDIT_CARD` | Credit card number  
`DATE_TIME` | Date or time expression  
`DRIVER_LICENSE` | Driver license number  
`EMAIL_ADDRESS` | Email address  
`IP_ADDRESS` | Internet Protocol (IPv4) address  
`LOCATION` | Physical location or address  
`PASSPORT` | Passport number  
`PERSON` | Full or partial name of an individual  
`PHONE_NUMBER` | Telephone number  
`TAX_ID` | Tax identification number  
`US_SSN` | US Social Security Number (SSN)  
`URL` | Uniform Resource Locator (URL), used to locate a resource on the Internet  
  
The categories are detected by an AI-based Named Entity Recognition (NER) model.

Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Example usage:
    
    
    # Matches requests where PII categorized as "EMAIL_ADDRESS" or "BANK_ACCOUNT" was detected:
    (cf.llm.prompt.pii_detected and any(cf.llm.prompt.pii_categories[*] in {"EMAIL_ADDRESS" "BANK_ACCOUNT"}))

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
