---
url: https://developers.cloudflare.com/r2/examples/cache-api/
title: Use the Cache API \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:46.328812+00:00
---

# Use the Cache API · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/examples/cache-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /[Examples](https://developers.cloudflare.com/r2/examples/)
  4. /Use the Cache API



# Use the Cache API

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/examples/cache-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Use the [Cache API](https://developers.cloudflare.com/workers/runtime-apis/cache/) to store R2 objects in Cloudflare's cache.

Note

You will need to [connect a custom domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) or [route](https://developers.cloudflare.com/workers/configuration/routing/routes/) to your Worker in order to use the Cache API. Cache API operations in the Cloudflare Workers dashboard editor, Playground previews, and any `*.workers.dev` deployments will have no impact.
    
    
    export default {
      async fetch(request, env, context) {
        try {
          const url = new URL(request.url);
    
          // Construct the cache key from the cache URL
          const cacheKey = new Request(url.toString(), request);
          const cache = caches.default;
    
          // Check whether the value is already available in the cache
          // if not, you will need to fetch it from R2, and store it in the cache
          // for future access
          let response = await cache.match(cacheKey);
    
          if (response) {
            console.log(`Cache hit for: ${request.url}.`);
            return response;
          }
    
          console.log(
            `Response for request url: ${request.url} not present in cache. Fetching and caching request.`
          );
    
          // If not in cache, get it from R2
          const objectKey = url.pathname.slice(1);
          const object = await env.MY_BUCKET.get(objectKey);
          if (object === null) {
            return new Response('Object Not Found', { status: 404 });
          }
    
          // Set the appropriate object headers
          const headers = new Headers();
          object.writeHttpMetadata(headers);
          headers.set('etag', object.httpEtag);
    
          // Cache API respects Cache-Control headers. Setting s-max-age to 10
          // will limit the response to be in cache for 10 seconds max
          // Any changes made to the response here will be reflected in the cached value
          headers.append('Cache-Control', 's-maxage=10');
    
          response = new Response(object.body, {
            headers,
          });
    
          // Store the fetched response as cacheKey
          // Use waitUntil so you can return the response without blocking on
          // writing to cache
          context.waitUntil(cache.put(cacheKey, response.clone()));
    
          return response;
        } catch (e) {
          return new Response('Error thrown ' + e.message);
        }
      },
    };

[PreviousUse SSE-C](https://developers.cloudflare.com/r2/examples/ssec/)[NextTutorials](https://developers.cloudflare.com/r2/tutorials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/examples/cache-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
