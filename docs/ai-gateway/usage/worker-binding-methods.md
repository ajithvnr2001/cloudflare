---
url: https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/
title: Workers Bindings \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:36.339087+00:00
---

# Workers Bindings · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Using AI Gateway
  4. /Workers Bindings



# Workers Bindings

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigurationenv.AI.run() Gateway optionsenv.AI.aiGatewayLogIdenv.AI.gateway() patchLog() getLog() getUrl()

The AI binding (`env.AI`) lets you call AI models and access AI Gateway features directly from your Worker.

For a step-by-step setup guide, refer to [Set up Workers AI with AI Gateway](https://developers.cloudflare.com/ai-gateway/integrations/aig-workers-ai-binding/).

## Configuration

Add an AI binding to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):
    
    
    {
    	"ai": {
    		"binding": "AI",
    	},
    }
    
    
    [ai]
    binding = "AI"

The binding is accessible in your Worker code as `env.AI`.

If you're using TypeScript, run [`wrangler types`](https://developers.cloudflare.com/workers/wrangler/commands/general/#types) whenever you modify your Wrangler configuration file. This generates types for the `env` object based on your bindings, as well as [runtime types](https://developers.cloudflare.com/workers/languages/typescript/).

## `env.AI.run()`

Runs an inference request through AI Gateway. Accepts Workers AI models (`@cf/` prefix) and third-party models (`{author}/{model}` format).

**Workers AI model:**
    
    
    const resp = await env.AI.run(
    	"@cf/moonshotai/kimi-k2.5",
    	{
    		prompt: "tell me a joke",
    	},
    	{
    		gateway: {
    			id: "default", // or use a specific gateway name
    		},
    	},
    );
    
    
    const resp = await env.AI.run(
    	"@cf/moonshotai/kimi-k2.5",
    	{
    		prompt: "tell me a joke",
    	},
    	{
    		gateway: {
    			id: "default", // or use a specific gateway name
    		},
    	},
    );

To use prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), set the gateway's [Workers AI billing setting](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing) to **Unified billing** and specify that gateway in the binding request. Prepaid credits provide access to Workers AI models that otherwise require the Workers Paid plan and provide [higher rate limits for frontier models](https://developers.cloudflare.com/workers-ai/platform/limits/#paid-models).

**Third-party model:**
    
    
    const resp = await env.AI.run(
    	"openai/gpt-4.1-mini",
    	{
    		messages: [{ role: "user", content: "tell me a joke" }],
    	},
    	{
    		gateway: {
    			id: "default", // or use a specific gateway name
    		},
    	},
    );
    
    
    const resp = await env.AI.run(
    	"openai/gpt-4.1-mini",
    	{
    		messages: [{ role: "user", content: "tell me a joke" }],
    	},
    	{
    		gateway: {
    			id: "default", // or use a specific gateway name
    		},
    	},
    );

Third-party models require an AI Gateway and use [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/). Cloudflare manages the provider credentials and deducts credits from your account. You do not need to supply your own API keys.

Note

On the AI binding path, only a [BYOK (Bring Your Own Keys)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/) key stored under the `default` alias is used. Keys stored under other aliases are not consulted, and the request falls through to Unified Billing. To select a non-default alias, use the [provider-native endpoints](https://developers.cloudflare.com/ai-gateway/usage/providers/) with the `cf-aig-byok-alias` header. See [credential precedence](https://developers.cloudflare.com/ai-gateway/features/unified-billing/#credential-precedence) for details.

Browse available models in the [model catalog](https://developers.cloudflare.com/ai/models/).

**Dynamic route:**

Pass a [dynamic route](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) as the model in the form `dynamic/{route}`. Set `gateway.id` to the gateway that owns the route — routes are not shared across gateways. Dynamic routes accept the OpenAI chat completions request shape only.
    
    
    const resp = await env.AI.run(
    	"dynamic/my-route",
    	{
    		messages: [{ role: "user", content: "tell me a joke" }],
    	},
    	{
    		gateway: {
    			id: "my-gateway",
    		},
    	},
    );
    
    
    const resp = await env.AI.run(
    	"dynamic/my-route",
    	{
    		messages: [{ role: "user", content: "tell me a joke" }],
    	},
    	{
    		gateway: {
    			id: "my-gateway",
    		},
    	},
    );

### Gateway options

The third argument to `env.AI.run()` accepts a `gateway` object with the following parameters:

Parameter | Type | Default | Description  
---|---|---|---  
`id` | `string` | _required_ | Name of your [AI Gateway](https://developers.cloudflare.com/ai-gateway/get-started/). Must be in the same account as your Worker. Use `"default"` to automatically create a gateway on the first authenticated request. Refer to [Default gateway](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#default-gateway) for details.  
`skipCache` | `boolean` | `false` | Skip the [cache](https://developers.cloudflare.com/ai-gateway/features/caching/) for this request.  
`cacheTtl` | `number` | — | [Cache TTL](https://developers.cloudflare.com/ai-gateway/features/caching/) in seconds.  
`cacheKey` | `string` | — | Custom [cache key](https://developers.cloudflare.com/ai-gateway/features/caching/) for this request.  
`collectLog` | `boolean` | — | Whether to [collect logs](https://developers.cloudflare.com/ai-gateway/observability/logging/) for this request.  
`metadata` | `object` | — | [Custom metadata](https://developers.cloudflare.com/ai-gateway/observability/custom-metadata/) to attach to the log entry.  
  
## `env.AI.aiGatewayLogId`

Returns the log ID from the most recent `env.AI.run()` request.
    
    
    const myLogId = env.AI.aiGatewayLogId;

## `env.AI.gateway()`

Returns a gateway instance for accessing AI Gateway methods directly.
    
    
    const gateway = env.AI.gateway("my-gateway");

The gateway instance exposes the following methods.

### `patchLog()`

Sends feedback, score, and metadata for a specific log entry. All properties in the second argument are optional.
    
    
    await gateway.patchLog("my-log-id", {
    	feedback: 1,
    	score: 100,
    	metadata: {
    		user: "123",
    	},
    });

**Returns:** `Promise<void>`

### `getLog()`

Retrieves details of a specific log entry. If the `AiGatewayLog` type is missing, run [`wrangler types`](https://developers.cloudflare.com/workers/languages/typescript/#generate-types).
    
    
    const log = await gateway.getLog("my-log-id");

**Returns:** `Promise<AiGatewayLog>`

### `getUrl()`

Returns the base URL for your AI Gateway. Pass an optional provider name to get the provider-specific endpoint.
    
    
    const baseUrl = await gateway.getUrl();
    // https://gateway.ai.cloudflare.com/v1/my-account-id/my-gateway/
    
    const openaiUrl = await gateway.getUrl("openai");
    // https://gateway.ai.cloudflare.com/v1/my-account-id/my-gateway/openai

**Parameters:** Optional `provider` (string or `AIGatewayProviders` enum)

**Returns:** `Promise<string>`

#### SDK integration examples

**OpenAI SDK:**
    
    
    import OpenAI from "openai";
    
    const openai = new OpenAI({
    	apiKey: "my api key", // defaults to process.env["OPENAI_API_KEY"]
    	baseURL: await env.AI.gateway("my-gateway").getUrl("openai"),
    });

**Vercel AI SDK with OpenAI:**
    
    
    import { createOpenAI } from "@ai-sdk/openai";
    
    const openai = createOpenAI({
    	baseURL: await env.AI.gateway("my-gateway").getUrl("openai"),
    });

**Vercel AI SDK with Anthropic:**
    
    
    import { createAnthropic } from "@ai-sdk/anthropic";
    
    const anthropic = createAnthropic({
    	baseURL: await env.AI.gateway("my-gateway").getUrl("anthropic"),
    });

[PreviousREST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/)[NextUnified API (OpenAI compat)](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/worker-binding-methods.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
