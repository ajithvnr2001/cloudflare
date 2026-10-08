---
url: https://developers.cloudflare.com/ai-gateway/usage/websockets-api/non-realtime-api/
title: Non-realtime WebSockets API \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:35.998538+00:00
---

# Non-realtime WebSockets API · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/websockets-api/non-realtime-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /[WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/)
  5. /Non-realtime WebSockets API



# Non-realtime WebSockets API

Last updated May 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/non-realtime-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up WebSockets APIExample requestExample responseExample streaming request

The Non-realtime WebSockets API allows you to establish persistent connections for AI requests without requiring repeated handshakes. This approach is ideal for applications that do not require real-time interactions but still benefit from reduced latency and continuous communication.

## Set up WebSockets API

  1. Generate an AI Gateway token with appropriate AI Gateway Run and opt in to using an authenticated gateway.
  2. Use the `wss://` protocol to initiate a WebSocket connection: 
         
         wss://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}

  3. Open a WebSocket connection authenticated with a Cloudflare token with the AI Gateway Run permission.



Note

Alternatively, we also support authentication via the `sec-websocket-protocol` header if you are using a browser WebSocket.

## Example request
    
    
    import WebSocket from "ws";
    
    const ws = new WebSocket(
    	"wss://gateway.ai.cloudflare.com/v1/my-account-id/my-gateway/",
    	{
    		headers: {
    			"cf-aig-authorization": "Bearer AI_GATEWAY_TOKEN",
    		},
    	},
    );
    
    ws.on("open", () => {
    	ws.send(
    		JSON.stringify({
    			type: "universal.create",
    			request: {
    				eventId: "my-request",
    				provider: "workers-ai",
    				endpoint: "@cf/meta/llama-3.1-8b-instruct",
    				headers: {
    					Authorization: "Bearer WORKERS_AI_TOKEN",
    					"Content-Type": "application/json",
    				},
    				query: {
    					prompt: "tell me a joke",
    				},
    			},
    		}),
    	);
    })
    
    ws.on("message", (message) => {
    	console.log(message.toString());
    });

## Example response
    
    
    {
    	"type": "universal.created",
    	"metadata": {
    		"cacheStatus": "MISS",
    		"eventId": "my-request",
    		"logId": "01JC3R94FRD97JBCBX3S0ZAXKW",
    		"step": "0",
    		"contentType": "application/json"
    	},
    	"response": {
    		"result": {
    			"response": "Why was the math book sad? Because it had too many problems. Would you like to hear another one?"
    		},
    		"success": true,
    		"errors": [],
    		"messages": []
    	}
    }

## Example streaming request

For streaming requests, AI Gateway sends an initial message with request metadata indicating the stream is starting:
    
    
    {
    	"type": "universal.created",
    	"metadata": {
    		"cacheStatus": "MISS",
    		"eventId": "my-request",
    		"logId": "01JC40RB3NGBE5XFRZGBN07572",
    		"step": "0",
    		"contentType": "text/event-stream"
    	}
    }

After this initial message, all streaming chunks are relayed in real-time to the WebSocket connection as they arrive from the inference provider. Only the `eventId` field is included in the metadata for these streaming chunks. The `eventId` allows AI Gateway to include a client-defined ID with each message, even in a streaming WebSocket environment.
    
    
    {
    	"type": "universal.stream",
    	"metadata": {
    		"eventId": "my-request"
    	},
    	"response": {
    		"response": "would"
    	}
    }

Once all chunks for a request have been streamed, AI Gateway sends a final message to signal the completion of the request. For added flexibility, this message includes all the metadata again, even though it was initially provided at the start of the streaming process.
    
    
    {
    	"type": "universal.done",
    	"metadata": {
    		"cacheStatus": "MISS",
    		"eventId": "my-request",
    		"logId": "01JC40RB3NGBE5XFRZGBN07572",
    		"step": "0",
    		"contentType": "text/event-stream"
    	}
    }

[PreviousRealtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/)[NextOverview](https://developers.cloudflare.com/ai-gateway/features/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/websockets-api/non-realtime-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
