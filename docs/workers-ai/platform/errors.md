---
url: https://developers.cloudflare.com/workers-ai/platform/errors/
title: Errors \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:06.982705+00:00
---

# Errors · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/platform/errors/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Platform
  4. /Errors



# Errors

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/platform/errors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Below is a list of Workers AI errors.

**Name** | **Internal Code** | **HTTP Code** | **Description**  
---|---|---|---  
No such model | `5007` | `400` | No such model `${model}` or task  
Invalid data | `5004` | `400` | Invalid data type for base64 input: `${type}`  
Finetune missing required files | `3039` | `400` | Finetune is missing required files `(model.safetensors and config.json) `  
Incomplete request | `3003` | `400` | Request is missing headers or body: `{what}`  
Account not allowed for private model | `5018` | `403` | The account is not allowed to access this model  
Model agreement | `5016` | `403` | User has not agreed to Llama3.2 model terms  
Account blocked | `3023` | `403` | Service unavailable for account  
Account not allowed for private model | `3041` | `403` | The account is not allowed to access this model  
Model requires Workers Paid plan | `5035` | `403` | This model requires a Workers Paid plan. See [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) for details.  
Deprecated SDK version | `5019` | `405` | Request trying to use deprecated SDK version  
LoRa unsupported | `5005` | `405` | The model `${this.model}` does not support LoRa inference  
Invalid model ID | `3042` | `404` | The model name is invalid  
Request too large | `3006` | `413` | Request is too large  
Timeout | `3007` | `408` | Request timeout  
Aborted | `3008` | `408` | Request was aborted  
Account limited | `3036` | `429` | You have used up your daily free allocation of 10,000 neurons. Please upgrade to Cloudflare's Workers Paid plan if you would like to continue usage.  
Out of capacity | `3040` | `429` | `Capacity temporarily exceeded, please try again.` Also returned when `rejectIfBusy` rejects a request because capacity is unavailable.  
  
[PreviousAI Gateway ↗︎](https://developers.cloudflare.com/ai-gateway/)[NextChoose a data or storage product ↗︎](https://developers.cloudflare.com/workers/platform/storage-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/platform/errors.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
