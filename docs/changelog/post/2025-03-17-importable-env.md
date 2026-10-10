---
url: https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/
title: Import `env` to access bindings in your Worker's global scope \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.020290+00:00
---

# Import `env` to access bindings in your Worker's global scope · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 17, 2025

## Import `env` to access bindings in your Worker's global scope

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now access [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) from anywhere in your Worker by importing the `env` object from `cloudflare:workers`.

Previously, `env` could only be accessed during a request. This meant that bindings could not be used in the top-level context of a Worker.

Now, you can import `env` and access bindings such as [secrets](https://developers.cloudflare.com/workers/configuration/secrets/) or [environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/) in the initial setup for your Worker:
    
    
    import { env } from "cloudflare:workers";
    import ApiClient from "example-api-client";
    
    // API_KEY and LOG_LEVEL now usable in top-level scope
    const apiClient = ApiClient.new({ apiKey: env.API_KEY });
    const LOG_LEVEL = env.LOG_LEVEL || "info";
    
    export default {
    	fetch(req) {
    		// you can use apiClient or LOG_LEVEL, configured before any request is handled
    	},
    };

Note

Workers do not allow I/O from outside a request context. This means that even though `env` is accessible from the top-level scope, you will not be able to access every binding's methods.

For instance, environment variables and secrets are accessible, and you are able to call `env.NAMESPACE.get` to get a [Durable Object stub](https://developers.cloudflare.com/durable-objects/api/stub/) in the top-level context. However, calling methods on the Durable Object stub, making [calls to a KV store](https://developers.cloudflare.com/kv/api/), and [calling to other Workers](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings) will not work.

Additionally, `env` was normally accessed as a argument to a Worker's entrypoint handler, such as [`fetch`](https://developers.cloudflare.com/workers/runtime-apis/fetch/). This meant that if you needed to access a binding from a deeply nested function, you had to pass `env` as an argument through many functions to get it to the right spot. This could be cumbersome in complex codebases.

Now, you can access the bindings from anywhere in your codebase without passing `env` as an argument:
    
    
    // helpers.js
    import { env } from "cloudflare:workers";
    
    // env is *not* an argument to this function
    export async function getValue(key) {
    	let prefix = env.KV_PREFIX;
    	return await env.KV.get(`${prefix}-${key}`);
    }

For more information, see [documentation on accessing `env`](https://developers.cloudflare.com/workers/runtime-apis/bindings#how-to-access-env).
