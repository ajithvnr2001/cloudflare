---
url: https://developers.cloudflare.com/changelog/post/2026-03-26-outbound-workers/
title: Easily connect Containers and Sandboxes to Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:43.875135+00:00
---

# Easily connect Containers and Sandboxes to Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-26-outbound-workers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 26, 2026

## Easily connect Containers and Sandboxes to Workers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-26-outbound-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) and [Sandboxes](https://developers.cloudflare.com/sandbox/) now support connecting directly to Workers over HTTP. This allows you to call Workers functions and [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/), like [KV](https://developers.cloudflare.com/kv) or [R2](https://developers.cloudflare.com/r2/), from within the container at specific hostnames.

#### Run Worker code

Define an `outbound` handler to capture any HTTP request or use `outboundByHost` to capture requests to individual hostnames and IPs.
    
    
    export class MyApp extends Sandbox {}
    
    MyApp.outbound = async (request, env, ctx) => {
    	// you can run arbitrary functions defined in your Worker on any HTTP request
    	return await someWorkersFunction(request.body);
    };
    
    MyApp.outboundByHost = {
    	"my.worker": async (request, env, ctx) => {
    		return await anotherFunction(request.body);
    	},
    };

In this example, requests from the container to `http://my.worker` will run the function defined within `outboundByHost`, and any other HTTP requests will run the `outbound` handler. These handlers run entirely inside the Workers runtime, outside of the container sandbox.

#### Access Workers bindings

Each handler has access to `env`, so it can call any binding set in [Wrangler config](https://developers.cloudflare.com/workers/wrangler/configuration/#bindings). Code inside the container makes a standard HTTP request to that hostname and the outbound Worker translates it into a binding call.
    
    
    export class MyApp extends Sandbox {}
    
    MyApp.outboundByHost = {
    	"my.kv": async (request, env, ctx) => {
    		const key = new URL(request.url).pathname.slice(1);
    		const value = await env.KV.get(key);
    		return new Response(value ?? "", { status: value ? 200 : 404 });
    	},
    	"my.r2": async (request, env, ctx) => {
    		const key = new URL(request.url).pathname.slice(1);
    		const object = await env.BUCKET.get(key);
    		return new Response(object?.body ?? "", { status: object ? 200 : 404 });
    	},
    };

Now, from inside the container sandbox, `curl http://my.kv/some-key` will access [Workers KV](https://developers.cloudflare.com/kv) and `curl http://my.r2/some-object` will access [R2](https://developers.cloudflare.com/r2/).

#### Access Durable Object state

Use `ctx.containerId` to reference the container's automatically provisioned [Durable Object](https://developers.cloudflare.com/durable-objects).
    
    
    export class MyContainer extends Container {}
    
    MyContainer.outboundByHost = {
    	"get-state.do": async (request, env, ctx) => {
    		const id = env.MY_CONTAINER.idFromString(ctx.containerId);
    		const stub = env.MY_CONTAINER.get(id);
    		return stub.getStateForKey(request.body);
    	},
    };

This provides an easy way to associate state with any container instance, and includes a [built-in SQLite database](https://developers.cloudflare.com/durable-objects/get-started/#2-write-a-durable-object-class-using-sql-api).

#### Get Started Today

Upgrade to `@cloudflare/containers` version 0.2.0 or later, or `@cloudflare/sandbox` version 0.8.0 or later to use outbound Workers.

Refer to [Containers outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/) and [Sandboxes outbound traffic](https://developers.cloudflare.com/sandbox/guides/outbound-traffic/) for more details and examples.
