---
url: https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/
title: Customize cache behavior with Workers \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:45.525074+00:00
---

# Customize cache behavior with Workers · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Interaction with Cloudflare products
  4. /Customize cache behavior with Workers



# Customize cache behavior with Workers

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCache features in Workers

You can use [Workers](https://developers.cloudflare.com/workers/) to customize cache behavior on Cloudflare's network. Workers run as middleware in the request lifecycle — a single Worker handles both the request and response phases. When a request arrives, it hits the Worker before the cache is checked. The Worker can modify the incoming request (for example, rewrite the URL or add headers), then call `fetch()` to continue the request through the cache. When the response comes back — whether from cache or from the origin server — the Worker can also modify the response before it is sent to the visitor.

Note

This page describes how Workers interact with a zone's Cloudflare Cache. You can also enable **[Workers Cache](https://developers.cloudflare.com/workers/cache/)** for your Worker — a cache that sits in front of the Worker itself, so that Cloudflare returns a cached response without running the Worker. Use Workers Caching to cache the output of a Worker's logic directly, independent of any zone configuration.

The diagram below illustrates a common interaction flow between Workers and Cache.

![Workers and cache flow example flow diagram.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=15151,height=3234,format=webp/_astro/workers-cache-flow.DBEQRofC.png)

  1. A visitor (a) requests a URL, and this request is directed to a Worker. The Worker can then interact with the request, either requesting the content from the origin server using (b) `fetch()` or sending a (f) response back to the visitor.
  2. If the content is cached, the cache sends a (e) response back to the Worker, which can modify the response before sending a (f) response back to the visitor.
  3. When using [cache rules](https://developers.cloudflare.com/cache/how-to/cache-rules/) with Workers, the cache rule must match the properties of the URL in the `fetch()` (b) request — such as headers, hostname, or URL path — not the original visitor URL/host (a). Otherwise, the rule will not be applied.



Here are a few examples of how Workers can be used to customize cache behavior:

  * **Modify Response** : Adjust or enhance content after it is retrieved from the cache, ensuring that responses are up-to-date or tailored to specific needs.

  * **Signed URLs** : Generate time-limited signed URLs to control access and enhance security.

  * **Personalized Response** : Deliver personalized content based on user data while using cached resources to reduce the load on the origin server.

  * **Reduce Latency** : Serve content from a data center close to the visitor, decreasing load times and improving the user experience.




You can also use [Snippets](https://developers.cloudflare.com/rules/snippets/) for lightweight modifications like header changes, redirects, and JWT validation without deploying a full Worker script. Snippets are included at no additional cost on all paid plans but have stricter resource limits (5 ms execution time, 32 KB package size).

Note

When using Workers and [O2O](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/) (a traffic routing configuration where requests pass through two Cloudflare zones), some caveats and limitations may apply.

## Cache features in Workers

Workers offer two ways to interact with the cache. Use `fetch()` when your Worker makes subrequests to an origin. Use the Cache API when your Worker generates responses without a backend origin.

  * **fetch()** : When a Worker calls `fetch()`, the request passes through Cloudflare's cache and [Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) (if enabled). You can control caching behavior by setting properties on the request's [`cf` object](https://developers.cloudflare.com/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties) — including time-to-live (TTL) values, custom cache keys, and cache headers. For more details, refer to [Cache using fetch](https://developers.cloudflare.com/workers/examples/cache-using-fetch/).

  * **Cache API** : Allows you to programmatically store, retrieve, and delete responses in Cloudflare's cache using `caches.default` or `caches.open()`. Unlike `fetch()`, the Cache API only operates on the cache in the data center handling the current request — it does not interact with Tiered Cache. Use the Cache API when you need to cache responses that did not come from an origin. For more details, refer to [Using the Cache API](https://developers.cloudflare.com/workers/examples/cache-api/).




To understand more about how Cache and Workers interact, refer to [Cache in Workers](https://developers.cloudflare.com/workers/reference/how-the-cache-works/).

[PreviousUsing ETag Headers with Cloudflare](https://developers.cloudflare.com/cache/reference/etag-headers/)[NextHow Workers interact with Cache Rules](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers-cache-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/interaction-cloudflare-products/workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
