---
url: https://developers.cloudflare.com/changelog/post/2025-04-11-new-models-faster-inference/
title: Workers AI for Developer Week - faster inference, new models, async batch API, expanded LoRA support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.970877+00:00
---

# Workers AI for Developer Week - faster inference, new models, async batch API, expanded LoRA support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-11-new-models-faster-inference/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 11, 2025

## Workers AI for Developer Week - faster inference, new models, async batch API, expanded LoRA support

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Happy Developer Week 2025! Workers AI is excited to announce a couple of new features and improvements available today. Check out our [blog ↗︎](https://blog.cloudflare.com/workers-ai-improvements) for all the announcement details.

#### Faster inference + New models

We’re rolling out some in-place improvements to our models that can help speed up inference by 2-4x! Users of the models below will enjoy an automatic speed boost starting today:

  * [`@cf/meta/llama-3.3-70b-instruct-fp8-fast`](https://developers.cloudflare.com/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/) gets a speed boost of 2-4x, leveraging techniques like speculative decoding, prefix caching, and an updated inference backend.
  * [`@cf/baai/bge-small-en-v1.5`](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/), [`@cf/baai/bge-base-en-v1.5`](https://developers.cloudflare.com/workers-ai/models/bge-base-en-v1.5/), [`@cf/baai/bge-large-en-v1.5`](https://developers.cloudflare.com/workers-ai/models/bge-large-en-v1.5/) get an updated back end, which should improve inference times by 2x. 
    * With the `bge` models, we’re also announcing a new parameter called `pooling` which can take `cls` or `mean` as options. We highly recommend using `pooling: cls` which will help generate more accurate embeddings. However, embeddings generated with cls pooling are not backwards compatible with mean pooling. For this to not be a breaking change, the default remains as mean pooling. Please specify `pooling: cls` to enjoy more accurate embeddings going forward.



We’re also excited to launch a few new models in our catalog to help round out your experience with Workers AI. We’ll be deprecating some older models in the future, so stay tuned for a deprecation announcement. Today’s new models include:

  * [`@cf/mistralai/mistral-small-3.1-24b-instruct`](https://developers.cloudflare.com/workers-ai/models/mistral-small-3.1-24b-instruct/): a 24B parameter model achieving state-of-the-art capabilities comparable to larger models, with support for vision and tool calling.
  * [`@cf/google/gemma-3-12b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-3-12b-it/): well-suited for a variety of text generation and image understanding tasks, including question answering, summarization and reasoning, with a 128K context window, and multilingual support in over 140 languages.
  * [`@cf/qwen/qwq-32b`](https://developers.cloudflare.com/workers-ai/models/qwq-32b/): a medium-sized reasoning model, which is capable of achieving competitive performance against state-of-the-art reasoning models, e.g., DeepSeek-R1, o1-mini.
  * [`@cf/qwen/qwen2.5-coder-32b-instruct`](https://developers.cloudflare.com/workers-ai/models/qwen2.5-coder-32b-instruct/): the current state-of-the-art open-source code LLM, with its coding abilities matching those of GPT-4o.



#### Batch Inference

Introducing a new batch inference feature that allows you to send us an array of requests, which we will fulfill as fast as possible and send them back as an array. This is really helpful for large workloads such as summarization, embeddings, etc. where you don’t have a human-in-the-loop. Using the batch API will guarantee that your requests are fulfilled eventually, rather than erroring out if we don’t have enough capacity at a given time.

Check out the [tutorial](https://developers.cloudflare.com/workers-ai/features/batch-api/) to get started! Models that support batch inference today include:

  * [`@cf/meta/llama-3.3-70b-instruct-fp8-fast`](https://developers.cloudflare.com/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/)
  * [`@cf/baai/bge-small-en-v1.5`](https://developers.cloudflare.com/workers-ai/models/bge-small-en-v1.5/)
  * [`@cf/baai/bge-base-en-v1.5`](https://developers.cloudflare.com/workers-ai/models/bge-base-en-v1.5/)
  * [`@cf/baai/bge-large-en-v1.5`](https://developers.cloudflare.com/workers-ai/models/bge-large-en-v1.5/)
  * [`@cf/baai/bge-m3`](https://developers.cloudflare.com/workers-ai/models/bge-m3/)
  * [`@cf/meta/m2m100-1.2b`](https://developers.cloudflare.com/workers-ai/models/m2m100-1.2b/)



#### Expanded LoRA support

We’ve upgraded our LoRA experience to include 8 newer models, and can support ranks of up to 32 with a 300MB safetensors file limit (previously limited to rank of 8 and 100MB safetensors) Check out our [LoRAs page](https://developers.cloudflare.com/workers-ai/features/fine-tunes/loras/) to get started. Models that support LoRAs now include:

  * [`@cf/meta/llama-3.2-11b-vision-instruct`](https://developers.cloudflare.com/workers-ai/models/llama-3.2-11b-vision-instruct/)
  * [`@cf/meta/llama-3.3-70b-instruct-fp8-fast`](https://developers.cloudflare.com/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/)
  * [`@cf/meta/llama-guard-3-8b`](https://developers.cloudflare.com/workers-ai/models/llama-guard-3-8b/)
  * [`@cf/meta/llama-3.1-8b-instruct-fast`](https://developers.cloudflare.com/workers-ai/models/llama-3.1-8b-instruct-fast/) (coming soon)
  * [`@cf/deepseek-ai/deepseek-r1-distill-qwen-32b`](https://developers.cloudflare.com/workers-ai/models/deepseek-r1-distill-qwen-32b/) (coming soon)
  * [`@cf/qwen/qwen2.5-coder-32b-instruct`](https://developers.cloudflare.com/workers-ai/models/qwen2.5-coder-32b-instruct/)
  * [`@cf/qwen/qwq-32b`](https://developers.cloudflare.com/workers-ai/models/qwq-32b/)
  * [`@cf/mistralai/mistral-small-3.1-24b-instruct`](https://developers.cloudflare.com/workers-ai/models/mistral-small-3.1-24b-instruct/)
  * [`@cf/google/gemma-3-12b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-3-12b-it/)


