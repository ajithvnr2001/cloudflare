---
url: https://developers.cloudflare.com/workers-ai/features/fine-tunes/
title: Fine-tunes \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:57.202069+00:00
---

# Fine-tunes · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/fine-tunes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Features
  4. /Fine-tunes



# Fine-tunes

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/fine-tunes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is fine-tuning?

Learn how to use Workers AI to get fine-tuned inference.

[Fine-tuned inference with LoRAs](https://developers.cloudflare.com/workers-ai/features/fine-tunes/loras/)

Upload a LoRA adapter and run fine-tuned inference with one of our base models.

Run inference with LoRAs

* * *

## What is fine-tuning?

Fine-tuning is a general term for modifying an AI model by continuing to train it with additional data. The goal of fine-tuning is to increase the probability that a generation is similar to your dataset. Training a model from scratch is not practical for many use cases given how expensive and time consuming they can be to train. By fine-tuning an existing pre-trained model, you benefit from its capabilities while also accomplishing your desired task.

[Low-Rank Adaptation ↗︎](https://arxiv.org/abs/2106.09685) (LoRA) is a specific fine-tuning method that can be applied to various model architectures, not just LLMs. It is common that the pre-trained model weights are directly modified or fused with additional fine-tune weights in traditional fine-tuning methods. LoRA, on the other hand, allows for the fine-tune weights and pre-trained model to remain separate, and for the pre-trained model to remain unchanged. The end result is that you can train models to be more accurate at specific tasks, such as generating code, having a specific personality, or generating images in a specific style.

[PreviousJSON Mode](https://developers.cloudflare.com/workers-ai/features/json-mode/)[NextUsing LoRA adapters](https://developers.cloudflare.com/workers-ai/features/fine-tunes/loras/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/fine-tunes/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
