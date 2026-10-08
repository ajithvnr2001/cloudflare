---
url: https://developers.cloudflare.com/ai-gateway/features/guardrails/supported-model-types/
title: Supported model types \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:29.987790+00:00
---

# Supported model types · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/features/guardrails/supported-model-types/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

[Features](https://developers.cloudflare.com/ai-gateway/features/)

  4. /[Guardrails](https://developers.cloudflare.com/ai-gateway/features/guardrails/)
  5. /Supported model types



# Supported model types

Last updated Aug 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/features/guardrails/supported-model-types/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway's Guardrails detects the type of AI model being used and applies safety checks accordingly:

  * **Text generation models** : Both prompts and responses are evaluated.
  * **Embedding models** : Only the prompt is evaluated, as the response consists of numerical embeddings, which are not meaningful for moderation.
  * **Unknown models** : If AI Gateway cannot determine the model type, it evaluates only the prompt and bypasses Guardrails for the response.



Note

Guardrails does not support streaming (`stream: true`) requests. For more information, refer to [Streaming behavior](https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/#streaming-behavior).

[PreviousSet up Guardrails](https://developers.cloudflare.com/ai-gateway/features/guardrails/set-up-guardrail/)[NextUsage considerations](https://developers.cloudflare.com/ai-gateway/features/guardrails/usage-considerations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/features/guardrails/supported-model-types.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
