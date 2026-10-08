---
url: https://developers.cloudflare.com/workers-ai/configuration/bindings/
title: Workers Bindings \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:56.680281+00:00
---

# Workers Bindings · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/configuration/bindings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Configuration
  4. /Workers Bindings



# Workers Bindings

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/configuration/bindings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWorkersPages FunctionsMethods async env.AI.run()

## Workers

[Workers](https://developers.cloudflare.com/workers/) provides a serverless execution environment that allows you to create new applications or augment existing ones.

To use Workers AI with Workers, you must create a Workers AI [binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/). Bindings allow your Workers to interact with resources, like Workers AI, on the Cloudflare Developer Platform. You create bindings on the Cloudflare dashboard or by updating your [Wrangler file](https://developers.cloudflare.com/workers/wrangler/configuration/).

To bind Workers AI to your Worker, add the following to the end of your Wrangler file:
    
    
    {
    	"ai": {
    		"binding": "AI" // i.e. available in your Worker on env.AI
    	}
    }
    
    
    [ai]
    binding = "AI"

## Pages Functions

[Pages Functions](https://developers.cloudflare.com/pages/functions/) allow you to build full-stack applications with Cloudflare Pages by executing code on the Cloudflare network. Functions are Workers under the hood.

To configure a Workers AI binding in your Pages Function, you must use the Cloudflare dashboard. Refer to [Workers AI bindings](https://developers.cloudflare.com/pages/functions/bindings/#workers-ai) for instructions.

## Methods

### async env.AI.run()

`async env.AI.run()` runs a model. Takes a model as the first parameter, and an object as the second parameter.
    
    
    const answer = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
        prompt: "What is the origin of the phrase 'Hello, World'"
    });

**Parameters**

  * `model` `string` required

    * The model to run.

**Supported options**

    * `stream` `boolean` optional
      * Returns a stream of results as they are available.


    
    
    const answer = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
        prompt: "What is the origin of the phrase 'Hello, World'",
        stream: true
    });
    
    return new Response(answer, {
        headers: { "content-type": "text/event-stream" }
    });

[PreviousModels](https://developers.cloudflare.com/workers-ai/models/)[NextOpenAI compatible API endpoints](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/configuration/bindings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
