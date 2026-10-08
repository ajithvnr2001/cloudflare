---
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/
title: API Reference - Embedded function calling \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:57.472179+00:00
---

# API Reference - Embedded function calling · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features[Function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/)

  4. /[Embedded](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/)
  5. /API Reference



# API Reference

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewrunWithToolscreateToolsFromOpenAPISpec

Learn more about the API reference for [embedded function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded).

## runWithTools

This wrapper method enables you to do embedded function calling. You pass it the AI binding, model, inputs (`messages` array and `tools` array), and optional configurations.

  * `AI Binding`Ai 
    * The AI binding, such as `env.AI`.
  * `model`BaseAiTextGenerationModels 
    * The ID of the model that supports function calling. For example, `@hf/nousresearch/hermes-2-pro-mistral-7b`.
  * `input`Object 
    * `messages`RoleScopedChatInput[]
    * `tools`AiTextGenerationToolInputWithFunction[]
  * `config`Object 
    * `streamFinalResponse`boolean optional
    * `maxRecursiveToolRuns`number optional
    * `strictValidation`boolean optional
    * `verbose`boolean optional
    * `trimFunction`boolean optional - For the `trimFunction`, you can pass it `autoTrimTools`, which is another helper method we've devised to automatically choose the correct tools (using an LLM) before sending it off for inference. This means that your final inference call will have fewer input tokens.



## createToolsFromOpenAPISpec

This method lets you automatically create tool schemas based on OpenAPI specs, so you don't have to manually write or hardcode the tool schemas. You can pass the OpenAPI spec for any API in JSON or YAML format.

`createToolsFromOpenAPISpec` has a config input that allows you to perform overrides if you need to provide headers like Authentication or User-Agent.

  * `spec`string 
    * The OpenAPI specification in either JSON or YAML format, or a URL to a remote OpenAPI specification.
  * `config`Config optional - Configuration options for the createToolsFromOpenAPISpec function 
    * `overrides`ConfigRule[] optional
    * `matchPatterns`RegExp[] optional
    * `options` Object optional { `verbose` boolean optional }



[PreviousUse KV API](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/kv/)[NextTroubleshooting](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/function-calling/embedded/api-reference.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
