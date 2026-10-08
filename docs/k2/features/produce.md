---
url: https://developers.cloudflare.com/k2/features/produce/
title: Produce records \u00b7 Cloudflare K2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:38.942301+00:00
---

# Produce records · Cloudflare K2 docs

> Source: https://developers.cloudflare.com/k2/features/produce/

  1. [Home](https://developers.cloudflare.com/)
  2. /[K2](https://developers.cloudflare.com/k2/)
  3. /Features
  4. /Produce records



# Produce records

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/k2/features/produce/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRecords and batchesProduce over HTTP Produce from a browserProduce from a Worker Configure the binding Send recordsHandle errorsNext steps

You can write records to a K2 stream in two ways:

  * Over HTTP, by sending a `POST` request to the stream's `/produce` endpoint.
  * From a Worker, by calling `send()` on a Workers binding.



Each input must be enabled on the stream. Refer to [Inputs](https://developers.cloudflare.com/k2/configuration/#inputs).

## Records and batches

A record has two fields:

Field | Type | Required | Description  
---|---|---|---  
`content` | bytes | Yes | The record payload as raw bytes.  
`headers` | object of string to string | No | Metadata about the record.  
  
Records are sent in batches. A batch must contain at least one record, and there is no limit on the number of records other than the maximum batch size. Batch writes are atomic, so either all records in the batch are recorded successfully or none are.

Timestamps are written by the server when the batch is received, and are not currently overridable by users.

For record, header, and batch size limits, refer to [Limits](https://developers.cloudflare.com/k2/platform/limits/#produce-records).

## Produce over HTTP

Send a `POST` request to `https://<STREAM_ID>.k2.cloudflarestorage.com/produce`. The request body is a JSON object with a `records` array. Record `content` must be standard base64.
    
    
    curl "https://$STREAM_ID.k2.cloudflarestorage.com/produce" \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "records": [
          {
            "content": "eyJvcmRlcl9pZCI6MTAwMSwic3RhdHVzIjoiY3JlYXRlZCJ9",
            "headers": { "event-type": "order.created" }
          },
          {
            "content": "eyJvcmRlcl9pZCI6MTAwMiwic3RhdHVzIjoiY3JlYXRlZCJ9"
          }
        ]
      }'
    
    
    { "success": true }

The request must meet the following requirements:

  * The `Content-Type` header must be `application/json`.
  * To compress the request body, gzip it and set the `Content-Encoding: gzip` header. The size limit applies both before and after decompression.
  * `content` must be standard base64 with correct padding. URL-safe base64 is not supported.
  * The request body cannot contain fields other than `records`, and records cannot contain fields other than `content` and `headers`.
  * If the HTTP input has [authentication](https://developers.cloudflare.com/k2/configuration/#authentication) enabled, include an API token in the `Authorization` header.



### Produce from a browser

To produce from a web page, add your site's origin to the stream's [CORS configuration](https://developers.cloudflare.com/k2/configuration/#cors).

Do not include an API token in code that runs in a browser, because anyone who visits the page can read it. To produce from a browser, the stream's HTTP input must have [authentication](https://developers.cloudflare.com/k2/configuration/#authentication) disabled. This makes the `/produce` endpoint public, so anyone who knows the stream ID can write records to the stream. Validate records in your consumers.
    
    
    const encoder = new TextEncoder();
    
    const records = [{ order_id: 1001, status: "created" }].map((event) => ({
    	content: encoder.encode(JSON.stringify(event)).toBase64(),
    	headers: { "event-type": "order.created" },
    }));
    
    const response = await fetch(
    	"https://<STREAM_ID>.k2.cloudflarestorage.com/produce",
    	{
    		method: "POST",
    		headers: { "Content-Type": "application/json" },
    		body: JSON.stringify({ records }),
    	},
    );
    
    const result = await response.json();
    if (!result.success) {
    	console.error(`Produce failed: ${result.error.message}`);
    }

`Uint8Array.prototype.toBase64()` is available in recent browsers. For older browsers, use `btoa()` or a base64 library.

## Produce from a Worker

A Workers binding lets a Worker produce to a stream without an API token. The binding handles authentication for you.

### Configure the binding

Add a `k2` binding to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/). Set `stream` to the ID of the stream to produce to:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "orders-producer",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "k2": [
        {
          "binding": "ORDERS",
          "stream": "<STREAM_ID>"
        }
      ]
    }
    
    
    name = "orders-producer"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[k2]]
    binding = "ORDERS"
    stream = "<STREAM_ID>"

Field | Description  
---|---  
`binding` | The name of the binding in your Worker code. In this example, the binding is `env.ORDERS`.  
`stream` | The ID of the stream, 32 lowercase hexadecimal characters. The stream must be in the same account as the Worker.  
  
To bind to more than one stream, add a `[[k2]]` entry for each stream.

When you deploy, Cloudflare checks that the stream exists in your account and that you have permission to use it. If the check fails, the deployment fails with one of the following errors:

Code | Description  
---|---  
`10399` | The binding has no `stream` field, or the value is not a 32-character lowercase hexadecimal stream ID.  
`10400` | The stream does not exist in the account you are deploying to.  
`10401` | You do not have permission to bind this stream.  
`10402` | Cloudflare could not validate the binding. Try the deployment again.  
  
### Send records

Call `send()` on the binding with an array of records. Record `content` must be an `ArrayBuffer` or a `Uint8Array`. Every record in a batch must use the same type.

This example uses the `Env` type that [`wrangler types`](https://developers.cloudflare.com/workers/languages/typescript/#generate-types) generates from your Wrangler configuration. Run `npx wrangler types` after you add the binding.

src/index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const event = { order_id: 1001, status: "created" };
    		const encoder = new TextEncoder();
    
    		const result = await env.ORDERS.send([
    			{
    				content: encoder.encode(JSON.stringify(event)),
    				headers: { "event-type": "order.created" },
    			},
    		]);
    
    		if (!result.success) {
    			console.error(`Produce failed: ${result.error.message}`);
    			return new Response("Failed to record event", {
    				status: result.error.retryable ? 503 : 500,
    			});
    		}
    
    		return new Response("Event recorded");
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const event = { order_id: 1001, status: "created" };
    		const encoder = new TextEncoder();
    
    		const result = await env.ORDERS.send([
    			{
    				content: encoder.encode(JSON.stringify(event)),
    				headers: { "event-type": "order.created" },
    			},
    		]);
    
    		if (!result.success) {
    			console.error(`Produce failed: ${result.error.message}`);
    			return new Response("Failed to record event", {
    				status: result.error.retryable ? 503 : 500,
    			});
    		}
    
    		return new Response("Event recorded");
    	},
    } satisfies ExportedHandler<Env>;

`send()` does not throw when K2 rejects a batch. Instead, it returns a result object. Check `result.success` after each call.

String content is not supported, including base64 strings. Encode text to bytes with `TextEncoder` before you send it.

## Handle errors

When a batch fails, K2 returns an error object instead of `{ "success": true }`. Over HTTP, the response also has a non-`200` status code.
    
    
    {
    	"success": false,
    	"error": {
    		"code": 10211,
    		"message": "K2 is temporarily unavailable",
    		"retryable": true
    	}
    }

If `retryable` is `true`, K2 did not store the batch. Retry the same batch with exponential backoff.

If `retryable` is `false`, do not retry the batch without changing it. Some failures, such as `10212`, have an unknown outcome: the batch may or may not have been stored. K2 does not deduplicate records, so retrying can store the batch twice. Design consumers to handle duplicate records.

Produce error codes

Code | HTTP status | Retryable | Description  
---|---|---|---  
`10200` | `404` | No | The stream does not exist, or the input is not enabled.  
`10204` | `400` | No | The request is invalid. For example, the JSON or base64 is malformed, or a header exceeds its size limit.  
`10205` | `415` | No | The `Content-Type` header is not `application/json`.  
`10206` | `413` | No | The request exceeds 5 MB.  
`10207` | `413` | No | A record exceeds 1 MB.  
`10208` | `401` | No | The stream requires authentication and the request has no `Authorization` header.  
`10209` | `401` | No | The `Authorization` header is malformed or the API token is invalid.  
`10210` | `403` | No | The API token does not have permission to produce to this stream.  
`10211` | `503` | Yes | K2 is temporarily unavailable. The batch was not stored.  
`10212` | `503` | No | K2 could not append the batch. The batch may or may not have been stored.  
`10213` | `500` | No | An internal error occurred.  
  
## Next steps

  * [Consume records](https://developers.cloudflare.com/k2/features/consume/) from the stream through a subscription.



[PreviousConcepts](https://developers.cloudflare.com/k2/concepts/)[NextConsume records](https://developers.cloudflare.com/k2/features/consume/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/k2/features/produce.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
