---
url: https://developers.cloudflare.com/workers-ai/features/reject-if-busy/
title: Reject busy requests \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:58.915898+00:00
---

# Reject busy requests · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/reject-if-busy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Features
  4. /Reject busy requests



# Reject busy requests

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/reject-if-busy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSend a REST requestUse the Workers bindingCall Chat CompletionsHandle capacity errors

Set `rejectIfBusy` when your application should not wait in a capacity queue. Workers AI rejects the synchronous inference request if capacity is unavailable.

## Send a REST request

For the native REST API, add `rejectIfBusy` to the request `options` object:
    
    
    curl --request POST \
      --url "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "messages": [
          {
            "role": "user",
            "content": "Explain what a capacity queue is."
          }
        ],
        "options": {
          "rejectIfBusy": true
        }
      }'

## Use the Workers binding

For the Workers AI binding, pass `rejectIfBusy` in the third argument to `env.AI.run()`:
    
    
    const response = await env.AI.run(
    	"@cf/google/gemma-4-26b-a4b-it",
    	{
    		messages: [
    			{
    				role: "user",
    				content: "Explain what a capacity queue is.",
    			},
    		],
    	},
    	{ rejectIfBusy: true },
    );
    
    
    const response = await env.AI.run(
    	"@cf/google/gemma-4-26b-a4b-it",
    	{
    		messages: [
    			{
    				role: "user",
    				content: "Explain what a capacity queue is.",
    			},
    		],
    	},
    	{ rejectIfBusy: true },
    );

Do not add `rejectIfBusy` to the model input object. The binding only applies this option from the third argument.

## Call Chat Completions

For OpenAI-compatible Chat Completions, add `options` at the top level of the request body:
    
    
    curl --request POST \
      --url "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/v1/chat/completions" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "model": "@cf/google/gemma-4-26b-a4b-it",
        "messages": [
          {
            "role": "user",
            "content": "Explain what a capacity queue is."
          }
        ],
        "options": {
          "rejectIfBusy": true
        }
      }'

OpenAI clients that preserve custom fields can send this option. Clients that remove unknown fields do not apply it, so requests proceed normally.

## Handle capacity errors

Rejected requests return HTTP status `429` and internal error code `3040`. The error message is `Capacity temporarily exceeded, please try again.`

Refer to [Workers AI errors](https://developers.cloudflare.com/workers-ai/platform/errors/) for error details.

[PreviousPrompting](https://developers.cloudflare.com/workers-ai/features/prompting/)[NextOverview](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/reject-if-busy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
