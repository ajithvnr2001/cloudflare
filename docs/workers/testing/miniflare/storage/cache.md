---
url: https://developers.cloudflare.com/workers/testing/miniflare/storage/cache/
title: Cache \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:56.118652+00:00
---

# Cache · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/storage/cache/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Storage
  5. /Cache



# Cache

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/storage/cache/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDefault CacheNamed CachesPersistenceManipulating Outside WorkersPurgingDisabling

  * [Cache Reference](https://developers.cloudflare.com/workers/runtime-apis/cache)
  * [How the Cache works](https://developers.cloudflare.com/workers/reference/how-the-cache-works/#cache-api) (note that cache using `fetch` is unsupported)



## Default Cache

Access to the default cache is enabled by default:
    
    
    addEventListener("fetch", (e) => {
    	e.respondWith(caches.default.match("http://miniflare.dev"));
    });

## Named Caches

You can access a namespaced cache using `open`. Note that you cannot name your cache `default`, trying to do so will throw an error:
    
    
    await caches.open("cache_name");

## Persistence

By default, cached data is stored in memory. It will persist between reloads, but not different `Miniflare` instances. To enable persistence to the file system, specify the cache persistence option:
    
    
    const mf = new Miniflare({
    	cachePersist: true, // Defaults to ./.mf/cache
    	cachePersist: "./data", // Custom path
    });

## Manipulating Outside Workers

For testing, it can be useful to put/match data from cache outside a Worker. You can do this with the `getCaches` method:
    
    
    import { Miniflare, Response } from "miniflare";
    
    const mf = new Miniflare({
    	modules: true,
    	script: `
      export default {
        async fetch(request) {
          const url = new URL(request.url);
          const cache = caches.default;
          if(url.pathname === "/put") {
            await cache.put("https://miniflare.dev/", new Response("1", {
              headers: { "Cache-Control": "max-age=3600" },
            }));
          }
          return cache.match("https://miniflare.dev/");
        }
      }
      `,
    });
    let res = await mf.dispatchFetch("http://localhost:8787/put");
    console.log(await res.text()); // 1
    
    const caches = await mf.getCaches(); // Gets the global caches object
    const cachedRes = await caches.default.match("https://miniflare.dev/");
    console.log(await cachedRes.text()); // 1
    
    await caches.default.put(
    	"https://miniflare.dev",
    	new Response("2", {
    		headers: { "Cache-Control": "max-age=3600" },
    	}),
    );
    res = await mf.dispatchFetch("http://localhost:8787");
    console.log(await res.text()); // 2

## Purging

You can programmatically purge all entries from a cache using the `purgeCache` method on the `Miniflare` instance. This is useful during development when cached assets need to be cleared without restarting the instance:
    
    
    const mf = new Miniflare({ /* options */ });
    
    // Purge the default cache and get the number of entries purged
    const count = await mf.purgeCache();
    console.log(`Purged ${count} entries`);
    
    // Purge a specific named cache
    await mf.purgeCache("my-named-cache");

## Disabling

Both default and named caches can be disabled with the `disableCache` option. When disabled, the caches will still be available in the sandbox, they just won't cache anything. This may be useful during development:
    
    
    const mf = new Miniflare({
    	cache: false,
    });

[PreviousMigrating from Version 2](https://developers.cloudflare.com/workers/testing/miniflare/migrations/from-v2/)[NextD1](https://developers.cloudflare.com/workers/testing/miniflare/storage/d1/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/storage/cache.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
