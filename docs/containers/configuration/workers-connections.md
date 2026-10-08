---
url: https://developers.cloudflare.com/containers/configuration/workers-connections/
title: Connect to Workers and Bindings \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:34.372109+00:00
---

# Connect to Workers and Bindings · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/configuration/workers-connections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Configuration
  4. /Connect to Workers and Bindings



# Connect to Workers and Bindings

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/configuration/workers-connections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse bindings in outbound handlersAccess Durable Object stateRelated resources

Containers can access [Workers bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) — KV, R2, D1, Durable Objects, and others — through [outbound handlers](https://developers.cloudflare.com/containers/configuration/outbound-traffic/#define-outbound-handlers). An outbound handler intercepts HTTP requests from the container and runs inside the Workers runtime, where all of your configured bindings are available.

The container makes a plain HTTP request to a virtual hostname (for example, `http://my.kv/some-key`), and the outbound handler resolves it using the bound resource. No SDK or client library is required inside the container.

## Use bindings in outbound handlers

Define an `outboundByHost` handler for each virtual hostname. The `env` argument gives you access to every binding declared in your Wrangler configuration.
    
    
    export class MyContainer extends Container {}
    
    MyContainer.outboundByHost = {
    	"my.kv": async (request, env, ctx) => {
    		const url = new URL(request.url);
    		const key = url.pathname.slice(1);
    		const value = await env.KV.get(key);
    		return new Response(value);
    	},
    	"my.r2": async (request, env, ctx) => {
    		const url = new URL(request.url);
    		// Scope access to this container's ID
    		const path = `${ctx.containerId}${url.pathname}`;
    		const object = await env.R2.get(path);
    		return new Response(object?.body ?? null, { status: object ? 200 : 404 });
    	},
    };

The container calls `http://my.kv/some-key` and the handler resolves it using the KV binding. A call to `http://my.r2/file.png` reads from R2, scoped to the current container instance.

Note

You can use `ctx.containerId` to apply different rules per container instance — for example, to look up per-instance configuration from KV.

## Access Durable Object state

The `ctx` argument exposes `containerId`, which lets you interact with the container's own Durable Object from an outbound handler.
    
    
    "get-state.do": async (request, env, ctx) => {
      const id = env.MY_CONTAINER.idFromString(ctx.containerId);
      const stub = env.MY_CONTAINER.get(id);
      // Assumes getStateForKey is defined on your DO
      return stub.getStateForKey(request.body);
    },

## Related resources

  * [Handle outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/) — Block, allow, and intercept outbound HTTP from a container
  * [Environment variables and secrets](https://developers.cloudflare.com/containers/configuration/environment-variables/) — Configure secrets and environment variables
  * [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/) — Full `ctx.container` API reference



[PreviousScheduling Policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/)[NextEnvironment Variables](https://developers.cloudflare.com/containers/configuration/environment-variables/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/configuration/workers-connections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
