---
url: https://developers.cloudflare.com/durable-objects/examples/readable-stream/
title: Use ReadableStream with Durable Object and Workers \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:08.461440+00:00
---

# Use ReadableStream with Durable Object and Workers · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/examples/readable-stream/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Examples
  4. /Use ReadableStream with Durable Object and Workers



# Use ReadableStream with Durable Object and Workers

Stream ReadableStream from Durable Objects.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/examples/readable-stream/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example demonstrates:

  * A Worker receives a request, and forwards it to a Durable Object `my-id`.
  * The Durable Object streams an incrementing number every second, until it receives `AbortSignal`.
  * The Worker reads and logs the values from the stream.
  * The Worker then cancels the stream after 5 values.


    
    
    import { DurableObject } from "cloudflare:workers";
    
    // Send incremented counter value every second
    async function* dataSource(signal) {
    	let counter = 0;
    	while (!signal.aborted) {
    		yield counter++;
    		await new Promise((resolve) => setTimeout(resolve, 1_000));
    	}
    
    	console.log("Data source cancelled");
    }
    
    export class MyDurableObject extends DurableObject {
    	async fetch(request) {
    		const abortController = new AbortController();
    
    		const stream = new ReadableStream({
    			async start(controller) {
    				if (request.signal.aborted) {
    					controller.close();
    					abortController.abort();
    					return;
    				}
    
    				for await (const value of dataSource(abortController.signal)) {
    					controller.enqueue(new TextEncoder().encode(String(value)));
    				}
    			},
    			cancel() {
    				console.log("Stream cancelled");
    				abortController.abort();
    			},
    		});
    
    		const headers = new Headers({
    			"Content-Type": "application/octet-stream",
    		});
    
    		return new Response(stream, { headers });
    	}
    }
    
    export default {
    	async fetch(request, env, ctx) {
    		const stub = env.MY_DURABLE_OBJECT.getByName("foo");
    		const response = await stub.fetch(request, { ...request });
    		if (!response.ok || !response.body) {
    			return new Response("Invalid response", { status: 500 });
    		}
    
    		const reader = response.body
    			.pipeThrough(new TextDecoderStream())
    			.getReader();
    
    		let data = [];
    		let i = 0;
    		while (true) {
    			// Cancel the stream after 5 messages
    			if (i > 5) {
    				reader.cancel();
    				break;
    			}
    			const { value, done } = await reader.read();
    
    			if (value) {
    				console.log(`Got value ${value}`);
    				data = [...data, value];
    			}
    
    			if (done) {
    				break;
    			}
    			i++;
    		}
    
    		return Response.json(data);
    	},
    };
    
    
    import { DurableObject } from 'cloudflare:workers';
    
    // Send incremented counter value every second
    async function* dataSource(signal: AbortSignal) {
        let counter = 0;
        while (!signal.aborted) {
            yield counter++;
            await new Promise((resolve) => setTimeout(resolve, 1_000));
        }
    
        console.log('Data source cancelled');
    }
    
    export class MyDurableObject extends DurableObject<Env> {
        async fetch(request: Request): Promise<Response> {
            const abortController = new AbortController();
    
            const stream = new ReadableStream({
                async start(controller) {
                    if (request.signal.aborted) {
                        controller.close();
                        abortController.abort();
                        return;
                    }
    
                    for await (const value of dataSource(abortController.signal)) {
                        controller.enqueue(new TextEncoder().encode(String(value)));
                    }
                },
                cancel() {
                    console.log('Stream cancelled');
                    abortController.abort();
                },
            });
    
            const headers = new Headers({
                'Content-Type': 'application/octet-stream',
            });
    
            return new Response(stream, { headers });
        }
    
    }
    
    export default {
        async fetch(request, env, ctx): Promise<Response> {
            const stub = env.MY_DURABLE_OBJECT.getByName("foo");
            const response = await stub.fetch(request, { ...request });
            if (!response.ok || !response.body) {
                return new Response('Invalid response', { status: 500 });
            }
    
            const reader = response.body.pipeThrough(new TextDecoderStream()).getReader();
    
            let data = [] as string[];
            let i = 0;
            while (true) {
                // Cancel the stream after 5 messages
                if (i > 5) {
                    reader.cancel();
                    break;
                }
                const { value, done } = await reader.read();
    
                if (value) {
                    console.log(`Got value ${value}`);
                    data = [...data, value];
                }
    
                if (done) {
                    break;
                }
                i++;
            }
    
            return Response.json(data);
        },
    
    } satisfies ExportedHandler<Env>;

Note

In a setup where a Durable Object returns a readable stream to a Worker, if the Worker cancels the Durable Object's readable stream, the cancellation propagates to the Durable Object.

[PreviousTesting Durable Objects](https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/)[NextUse RpcTarget class to handle Durable Object metadata](https://developers.cloudflare.com/durable-objects/examples/reference-do-name-using-init/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/examples/readable-stream.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
