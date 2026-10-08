---
url: https://developers.cloudflare.com/ai-gateway/features/guardrails/
title: Guardrails \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:29.545355+00:00
---

# Guardrails · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/features/guardrails/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /[Features](https://developers.cloudflare.com/ai-gateway/features/)
  4. /Guardrails



# Guardrails

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/features/guardrails/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewVideo demoHow Guardrails workRelated resource

Guardrails help you deploy AI applications safely by intercepting and evaluating both user prompts and model responses for harmful content. Acting as a proxy between your application and [model providers](https://developers.cloudflare.com/ai-gateway/usage/providers/) (such as OpenAI, Anthropic, DeepSeek, and others), AI Gateway's Guardrails ensure a consistent and secure experience across your entire AI ecosystem.

Guardrails proactively monitor interactions between users and AI models, giving you:

  * **Consistent moderation** : Uniform moderation layer that works across models and providers.
  * **Enhanced safety and user trust** : Proactively protect users from harmful or inappropriate interactions.
  * **Flexibility and control over allowed content** : Specify which categories to monitor and choose between flagging or outright blocking.
  * **Auditing and compliance capabilities** : Receive updates on evolving regulatory requirements with logs of user prompts, model responses, and enforced guardrails.



## Video demo

## How Guardrails work

AI Gateway inspects all interactions in real time by evaluating content against predefined safety parameters. Guardrails work by:

  1. Intercepting interactions: AI Gateway proxies requests and responses, sitting between the user and the AI model.

  2. Inspecting content:

     * User prompts: AI Gateway checks prompts against safety parameters (for example, violence, hate, or sexual content). Based on your settings, prompts can be flagged or blocked before reaching the model.
     * Model responses: Once processed, the AI model response is inspected. If hazardous content is detected, it can be flagged or blocked before being delivered to the user.
  3. Applying actions: Depending on your configuration, flagged content is logged for review, while blocked content is prevented from proceeding.




## Related resource

  * [Cloudflare Blog: Keep AI interactions secure and risk-free with Guardrails in AI Gateway ↗︎](https://blog.cloudflare.com/guardrails-in-ai-gateway/)



[PreviousAuto Router](https://developers.cloudflare.com/ai-gateway/features/auto-router/)[NextSet up Guardrails](https://developers.cloudflare.com/ai-gateway/features/guardrails/set-up-guardrail/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/features/guardrails/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
