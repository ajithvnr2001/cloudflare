---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/
title: cf.llm.prompt.unsafe_topic_categories \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:35.245716+00:00
---

# cf.llm.prompt.unsafe_topic_categories · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Llm.Prompt.Unsafe_topic_categories



# cf.llm.prompt.unsafe_topic_categories

`cf.llm.prompt.unsafe_topic_categories``Array<String>`

Array of string values with the type of unsafe topics detected in the LLM prompt.

The possible values are the following:

Value | Category name | Description  
---|---|---  
`VIOLENCE_AND_WEAPONS` | Violence and weapons | Content that promotes, glorifies, threatens, or provides instructions for physical violence or the acquisition, creation, or use of weapons.  
`NON_VIOLENT_CRIME` | Non-violent crime | Content that encourages or facilitates nonviolent crimes, including fraud, theft, hacking, and the illegal drug trade.  
`SEXUAL_CONTENT` | Sexual content | Sexually explicit or suggestive content, including sexual exploitation, trafficking, assault, harassment, and other non-consensual sexual acts involving adults.  
`CHILD_SAFETY` | Child safety | Content that sexualizes, exploits, abuses, grooms, or otherwise endangers minors.  
`HATE_AND_DISCRIMINATION` | Hate and discrimination | Content that attacks, demeans, discriminates against, or incites hatred toward people based on protected characteristics. This category also includes content that promotes dishonesty, manipulation, or professional misconduct.  
`SELF_HARM_AND_SUICIDE` | Self-harm and suicide | Content that encourages, glorifies, or provides instructions for self-harm or suicide.  
  
Requires a Cloudflare Enterprise plan. You must also enable [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/).

Example usage:
    
    
    # Matches requests where an unsafe topic categorized as "NON_VIOLENT_CRIME" or "HATE_AND_DISCRIMINATION" was detected in the LLM prompt:
    (cf.llm.prompt.unsafe_topic_detected and any(cf.llm.prompt.unsafe_topic_categories[*] in {"NON_VIOLENT_CRIME" "HATE_AND_DISCRIMINATION"}))

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
