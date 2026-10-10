---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.token_count/
title: cf.llm.prompt.token_count \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:35.309275+00:00
---

# cf.llm.prompt.token_count · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.token_count/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Llm.Prompt.Token_count



# cf.llm.prompt.token_count

`cf.llm.prompt.token_count``Number`

An estimated token count for the LLM prompt in the request.

The count is calculated using a general-purpose tokenizer and may not exactly match the count reported by your LLM provider.

Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Example usage:
    
    
    # Matches requests where the estimated token count exceeds 4,000:
    (cf.llm.prompt.token_count gt 4000)

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
