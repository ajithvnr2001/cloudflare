---
url: https://developers.cloudflare.com/agents/models/
title: Models \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:16.533020+00:00
---

# Models · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/models/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Models



# Models

Last updated Oct 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/models/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow a model is chosenWhat every model getsConfigure the bindingChoose a provider

The Agents SDK includes model providers for [Workers AI](https://developers.cloudflare.com/workers-ai/) and [AI Gateway](https://developers.cloudflare.com/ai-gateway/). Each provider is one `createAI` factory over the Worker's `AI` binding. There are two, one per framework:

Import | Framework | Use it with  
---|---|---  
`agents/models/ai-sdk` | [AI SDK ↗︎](https://ai-sdk.dev/) v7 | `generateText`, `streamText`, Think, and any AI SDK consumer  
`agents/models/pi-ai` | [Pi AI ↗︎](https://github.com/earendil-works/pi/tree/main/packages/ai) | The [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/), and Pi AI's `stream`  
  
Both take the same options, route through the same gateway, and handle Workers AI the same way.

Beta

The model providers are in beta. Their APIs may change in a minor release.

## How a model is chosen

The providers keep one model catalog up to date: Workers AI. Every other vendor's models come from that vendor's own package, and the provider routes them through AI Gateway.

  * **A Workers AI model** is a `@cf/` id, such as `ai("@cf/zai-org/glm-4.7-flash")`. It runs through `env.AI.run()`. A compatibility layer turns each model's response into the standard OpenAI chat completions shape.
  * **A third-party model** is a model object built by the vendor's provider, such as `ai(anthropic("claude-opus-4-8"))`. The vendor's code builds the request and parses the response. The provider swaps the transport, so the request goes through AI Gateway with `env.AI.gateway(id).run()`.



The provider does not keep third-party model ids, wire formats, or thinking settings. When a vendor ships a new model, update the vendor's package.

## What every model gets

  * **No API tokens in your Worker.** Requests go through the `AI` binding. AI Gateway holds third-party credentials, through [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) or a key you [store on the gateway](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).
  * **Gateway options.** Caching, logging, metadata, timeouts, and retries are options on the provider, the model, or the call. The `default` gateway is created the first time you use it.
  * **Fallback.** List models to try in order if the first fails before it produces output. Mix Workers AI and third-party models freely.
  * **Gateway metadata on every result.** Each response carries the gateway log id, cache status, and the model that actually answered.



## Configure the binding

Both providers need the `AI` binding:
    
    
    {
    	"ai": {
    		"binding": "AI",
    	},
    }
    
    
    [ai]
    binding = "AI"

## Choose a provider

### [AI SDK](https://developers.cloudflare.com/agents/models/ai-sdk/)

A full AI SDK ProviderV4 for text, tools, structured output, embeddings, images, speech, transcription, and reranking.

### [Pi AI](https://developers.cloudflare.com/agents/models/pi-ai/)

Pi AI models for the Pi harness, Pi Durable, and any framework built on a Pi AI Models registry.

[PreviousCode Mode API reference](https://developers.cloudflare.com/agents/tools/codemode/api-reference/)[NextAI SDK](https://developers.cloudflare.com/agents/models/ai-sdk/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/models/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
