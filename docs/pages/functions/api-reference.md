---
url: https://developers.cloudflare.com/pages/functions/api-reference/
title: API reference \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:31.914672+00:00
---

# API reference · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/api-reference/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /[Functions](https://developers.cloudflare.com/pages/functions/)
  4. /API reference



# API reference

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/api-reference/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethods onRequests env.ASSETS.fetch()Types EventContext EnvWithFetch

The following methods can be used to configure your Pages Function.

## Methods

### `onRequests`

The `onRequest` method will be called unless a more specific `onRequestVerb` method is exported. For example, if both `onRequest` and `onRequestGet` are exported, only `onRequestGet` will be called for `GET` requests.

  * `onRequest(contextEventContext)` Response | Promise<Response>

    * This function will be invoked on all requests no matter what the request method is, as long as no specific request verb (like one of the methods below) is exported.
  * `onRequestGet(contextEventContext)` Response | Promise<Response>

    * This function will be invoked on all `GET` requests.
  * `onRequestPost(contextEventContext)` Response | Promise<Response>

    * This function will be invoked on all `POST` requests.
  * `onRequestPatch(contextEventContext)` Response | Promise<Response>

    * This function will be invoked on all `PATCH` requests.
  * `onRequestPut(contextEventContext)` Response | Promise<Response>

    * This function will be invoked on all `PUT` requests.
  * `onRequestDelete(contextEventContext)` Response | Promise<Response>

    * This function will be invoked on all `DELETE` requests.
  * `onRequestHead(contextEventContext)` Response | Promise<Response>

    * This function will be invoked on all `HEAD` requests.
  * `onRequestOptions(contextEventContext)` Response | Promise<Response>

    * This function will be invoked on all `OPTIONS` requests.



### `env.ASSETS.fetch()`

The `env.ASSETS.fetch()` function allows you to fetch a static asset from your Pages project.

You can pass a [Request object](https://developers.cloudflare.com/workers/runtime-apis/request/), URL string, or URL object to `env.ASSETS.fetch()` function. The URL must be to the pretty path, not directly to the asset. For example, if you had the path `/users/index.html`, you will request `/users/` instead of `/users/index.html`. This method call will run the header and redirect rules, modifying the response that is returned.

## Types

### `EventContext`

The following are the properties on the `context` object which are passed through on the `onRequest` methods:

  * `request` [Request](https://developers.cloudflare.com/workers/runtime-apis/request/)

This is the incoming [Request](https://developers.cloudflare.com/workers/runtime-apis/request/).

  * `functionPath` string

This is the path of the request.

  * `waitUntil(promisePromise<any>)` void

Refer to [`waitUntil` documentation](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil) for more information.

  * `passThroughOnException()` void

Refer to [`passThroughOnException` documentation](https://developers.cloudflare.com/workers/runtime-apis/context/#passthroughonexception) for more information. Note that this will not work on an [advanced mode project](https://developers.cloudflare.com/pages/functions/advanced-mode/).

  * `next(input?Request | string, init?RequestInit)` Promise<Response>

Passes the request through to the next Function or to the asset server if no other Function is available.

  * `env` EnvWithFetch

  * `params` Params<P>

Holds the values from [dynamic routing](https://developers.cloudflare.com/pages/functions/routing/#dynamic-routes).

In the following example, you have a dynamic path that is `/users/[user].js`. When you visit the site on `/users/nevi` the `params` object would look like:
        
        {
        	user: "nevi";
        }

This allows you fetch the dynamic value from the path:
        
        export function onRequest(context) {
        	return new Response(`Hello ${context.params.user}`);
        }

Which would return `"Hello nevi"`.

  * `data` Data




### `EnvWithFetch`

Holds the environment variables, secrets, and bindings for a Function. This also holds the `ASSETS` binding which is how you can fallback to the asset-serving behavior.

[PreviousRouting](https://developers.cloudflare.com/pages/functions/routing/)[NextA/B testing with middleware](https://developers.cloudflare.com/pages/functions/examples/ab-testing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/api-reference.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
