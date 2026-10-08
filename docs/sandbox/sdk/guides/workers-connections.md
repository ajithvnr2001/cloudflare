---
url: https://developers.cloudflare.com/sandbox/sdk/guides/workers-connections/
title: Connect to Workers bindings (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:27.530059+00:00
---

# Connect to Workers bindings (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/guides/workers-connections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)
  5. /Connect to Workers bindings



# Connect to Workers bindings

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/workers-connections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse bindings in outbound handlersAccess Durable Object stateRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Sandboxes can access [Workers bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) — KV, R2, D1, Durable Objects, and others — through [outbound handlers](https://developers.cloudflare.com/sandbox/sdk/guides/outbound-traffic/#define-outbound-handlers). An outbound handler intercepts HTTP requests from the sandbox and runs inside the Workers runtime, where all of your configured bindings are available.

The sandbox makes a plain HTTP request to a virtual hostname (for example, `http://my.kv/some-key`), and the outbound handler resolves it using the bound resource. No SDK or client library is required inside the sandbox.

## Use bindings in outbound handlers

Define an `outboundByHost` handler for each virtual hostname. The `env` argument gives you access to every binding declared in your Wrangler configuration.
    
    
    export class MySandbox extends Sandbox {}
    
    MySandbox.outboundByHost = {
    	"my.kv": async (request, env, ctx) => {
    		const url = new URL(request.url);
    		const key = url.pathname.slice(1);
    		const value = await env.KV.get(key);
    		return new Response(value ?? "", { status: value ? 200 : 404 });
    	},
    	"my.r2": async (request, env, ctx) => {
    		const url = new URL(request.url);
    		// Scope access to this sandbox's ID
    		const path = `${ctx.containerId}${url.pathname}`;
    		const object = await env.R2.get(path);
    		return new Response(object?.body ?? null, { status: object ? 200 : 404 });
    	},
    };
    
    
    export class MySandbox extends Sandbox {}
    
    MySandbox.outboundByHost = {
    	"my.kv": async (request: Request, env: Env, ctx: OutboundHandlerContext) => {
    		const url = new URL(request.url);
    		const key = url.pathname.slice(1);
    		const value = await env.KV.get(key);
    		return new Response(value ?? "", { status: value ? 200 : 404 });
    	},
    	"my.r2": async (request: Request, env: Env, ctx: OutboundHandlerContext) => {
    		const url = new URL(request.url);
    		// Scope access to this sandbox's ID
    		const path = `${ctx.containerId}${url.pathname}`;
    		const object = await env.R2.get(path);
    		return new Response(object?.body ?? null, { status: object ? 200 : 404 });
    	},
    };

The sandbox calls `http://my.kv/some-key` and the handler resolves it using the KV binding. A call to `http://my.r2/file.png` reads from R2, scoped to the current sandbox instance.

Note

You can use `ctx.containerId` to apply different rules per sandbox instance — for example, to look up per-instance configuration from KV.

## Access Durable Object state

The `ctx` argument exposes `containerId`, which lets you interact with the sandbox's own Durable Object from an outbound handler.
    
    
    export class MySandbox extends Sandbox {}
    
    MySandbox.outboundByHost = {
    	"get-state.do": async (request, env, ctx) => {
    		const id = env.MY_SANDBOX.idFromString(ctx.containerId);
    		const stub = env.MY_SANDBOX.get(id);
    		// Assumes getStateForKey is defined on your DO
    		return stub.getStateForKey(request.body);
    	},
    };
    
    
    export class MySandbox extends Sandbox {}
    
    MySandbox.outboundByHost = {
    	"get-state.do": async (
    		request: Request,
    		env: Env,
    		ctx: { containerId: string },
    	) => {
    		const id = env.MY_SANDBOX.idFromString(ctx.containerId);
    		const stub = env.MY_SANDBOX.get(id);
    		// Assumes getStateForKey is defined on your DO
    		return stub.getStateForKey(request.body);
    	},
    };

## Related resources

  * [Handle outbound traffic](https://developers.cloudflare.com/sandbox/sdk/guides/outbound-traffic/) — Block, allow, and intercept all outbound HTTP from a sandbox
  * [Sandbox options](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/) — Configure sandbox behavior
  * [Environment variables](https://developers.cloudflare.com/sandbox/sdk/configuration/environment-variables/) — Configure secrets and environment variables



[PreviousHandle outbound traffic](https://developers.cloudflare.com/sandbox/sdk/guides/outbound-traffic/)[NextOverview](https://developers.cloudflare.com/sandbox/sdk/api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/guides/workers-connections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
