---
url: https://developers.cloudflare.com/cache/cache-security/cors/
title: Cross-Origin Resource Sharing (CORS) \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:41.279080+00:00
---

# Cross-Origin Resource Sharing (CORS) · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/cache-security/cors/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Cache security
  4. /Cross-Origin Resource Sharing (CORS)



# Cross-Origin Resource Sharing (CORS)

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/cache-security/cors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd or change CORS headers at the origin serverAdd or change CORS headers on Cloudflare

A cross-origin request occurs when a webpage on one origin (for example, `a.example.com`) requests a resource from a different origin (for example, `b.secondexample.com`). Cross-Origin Resource Sharing (CORS) is a mechanism that uses HTTP headers to let the server at `b.secondexample.com` indicate whether `a.example.com` is allowed to access its resources. Browsers enforce these headers and block access to responses that are not permitted.

Cloudflare supports CORS by:

  * Identifying cached assets based on the `Host` Header, `Origin` Header, URL path, and query. This allows different resources to use the same `Host` header but different `Origin` headers.
  * Passing `Access-Control-Allow-Origin` headers from the origin server to the browser.



The `Access-Control-Allow-Origin` header lets a server specify rules for sharing its resources with external origins. A server may respond with different `Access-Control-Allow-Origin` values depending on the `Origin` header in the request. These headers are often present on [cacheable content](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/).

## Add or change CORS headers at the origin server

If you add or change CORS configuration at your origin web server, purging the Cloudflare cache by URL does not update the CORS headers. Force Cloudflare to retrieve the new CORS headers via one of the following options:

  * Change the filename or URL to bypass cache to instruct Cloudflare to retrieve the latest CORS headers.
  * Use the [single-file purge API](https://developers.cloudflare.com/api/resources/cache/methods/purge/#purge-cached-content-by-url) to specify the appropriate CORS headers along with the purge request.
  * Update the resource’s last-modified time at your origin web server. Then, complete a [full purge](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/) to retrieve the latest version of your assets including updated CORS headers.



## Add or change CORS headers on Cloudflare

You can use one of following methods to set CORS headers using Cloudflare products:

  * Use a [Worker](https://developers.cloudflare.com/workers/): Refer to [CORS header proxy](https://developers.cloudflare.com/workers/examples/cors-header-proxy/) for an example.
  * Configure a [Snippet](https://developers.cloudflare.com/rules/snippets/): Refer to [Define CORS headers](https://developers.cloudflare.com/rules/snippets/examples/define-cors-headers/) for an example.
  * Use [Transform Rules](https://developers.cloudflare.com/rules/transform/): Refer to [Add a wildcard CORS response header](https://developers.cloudflare.com/rules/transform/examples/add-cors-header/) for an example.



[PreviousCache Deception Armor](https://developers.cloudflare.com/cache/cache-security/cache-deception-armor/)[NextCDN Reference Architecture ↗︎](https://developers.cloudflare.com/reference-architecture/architectures/cdn/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/cache-security/cors.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
