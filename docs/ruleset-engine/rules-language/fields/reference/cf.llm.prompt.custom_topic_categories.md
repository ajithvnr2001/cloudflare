---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/
title: cf.llm.prompt.custom_topic_categories \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:35.568873+00:00
---

# cf.llm.prompt.custom_topic_categories · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Llm.Prompt.Custom_topic_categories



# cf.llm.prompt.custom_topic_categories

`cf.llm.prompt.custom_topic_categories``Map<Number>`

A map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request.

Lower scores indicate the prompt is more relevant to that topic. Only populated when [custom topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics) are configured.

Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Example usage:
    
    
    # Matches requests where the prompt is highly relevant to the "competitors" custom topic:
    (cf.llm.prompt.custom_topic_categories["competitors"] lt 30)

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
