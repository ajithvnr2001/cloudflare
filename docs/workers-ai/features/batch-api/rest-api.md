---
url: https://developers.cloudflare.com/workers-ai/features/batch-api/rest-api/
title: REST API \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:57.057971+00:00
---

# REST API · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/batch-api/rest-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features

  4. /[Asynchronous Batch API](https://developers.cloudflare.com/workers-ai/features/batch-api/)
  5. /REST API



# REST API

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/batch-api/rest-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Sending a Batch Request2\. Retrieving the Batch Response

If you prefer to work directly with the REST API instead of a [Cloudflare Worker](https://developers.cloudflare.com/workers-ai/features/batch-api/workers-binding/), below are the steps on how to do it:

## 1\. Sending a Batch Request

Make a POST request using the following pattern. You can pass `external_reference` as a unique ID per-request that will be returned in the response.

Sending a batch requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/baai/bge-m3?queueRequest=true" \
     --header "Authorization: Bearer $API_TOKEN" \
     --header 'Content-Type: application/json' \
     --json '{
        "requests": [
            {
                "query": "This is a story about Cloudflare",
                "contexts": [
                    {
                        "text": "This is a story about an orange cloud"
                    },
                    {
                        "text": "This is a story about a llama"
                    },
                    {
                        "text": "This is a story about a hugging emoji"
                    }
                ],
                "external_reference": "reference-1"
            }
        ]
      }'
    
    
    {
    	"result": {
    		"status": "queued",
    		"request_id": "768f15b7-4fd6-4498-906e-ad94ffc7f8d2",
    		"model": "@cf/baai/bge-m3"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

## 2\. Retrieving the Batch Response

After receiving a `request_id` from your initial POST, you can poll for or retrieve the results with another POST request:

Retrieving a responsebash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/baai/bge-m3?queueRequest=true" \
     --header "Authorization: Bearer $API_TOKEN" \
     --header 'Content-Type: application/json' \
     --json '{
        "request_id": "<uuid>"
      }'
    
    
    {
    	"result": {
    		"responses": [
    			{
    				"id": 0,
    				"result": {
    					"response": [
    						{ "id": 0, "score": 0.73974609375 },
    						{ "id": 1, "score": 0.642578125 },
    						{ "id": 2, "score": 0.6220703125 }
    					]
    				},
    				"success": true,
    				"external_reference": "reference-1"
    			}
    		],
    		"usage": { "prompt_tokens": 12, "completion_tokens": 0, "total_tokens": 12 }
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

[PreviousWorkers Binding](https://developers.cloudflare.com/workers-ai/features/batch-api/workers-binding/)[NextOverview](https://developers.cloudflare.com/workers-ai/features/function-calling/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/batch-api/rest-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
