---
url: https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/
title: Set Browser Cache TTL \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:44.778533+00:00
---

# Set Browser Cache TTL · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration

  4. /[Edge and Browser Cache TTL](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/)
  5. /Set Browser Cache TTL



# Set Browser Cache TTL

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet Browser Cache TTL

Specify a time for a visitor’s Browser Cache TTL to accelerate the page load for repeat visitors to your website. To configure cache duration within Cloudflare’s data centers, refer to [Edge Cache TTL](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#edge-ttl).

By default, Cloudflare honors the cache expiration set in your `Expires` and `Cache-Control` headers. Cloudflare overrides any `Cache-Control` or `Expires` headers with values set via the **Browser Cache TTL** option under **Caching** on your dashboard if:

  * The value of the `Cache-Control` header from the origin web server is less than the **Browser Cache TTL** setting. This means that **Browser cache TTL** value needs to be higher than origin `max-age`.
  * The origin web server does not send a `Cache-Control` or an `Expires` header.



Unless specifically set in a [Cache Rule](https://developers.cloudflare.com/cache/how-to/cache-rules/), Cloudflare does not override or insert `Cache-Control` headers if you set **Browser Cache TTL** to **Respect Existing Headers**.

Nevertheless, the value you set via Cache Rule will be ignored if `Cache-Control: max-age` is higher. In other words, you can override to make browsers cache longer than Cloudflare's edge but not less.

## Set Browser Cache TTL

Note

If you modify cached assets, the new asset is not displayed to repeat visitors before the Browser Cache TTL duration. [Purging Cloudflare’s cache](https://developers.cloudflare.com/cache/how-to/purge-cache/) does not affect assets cached in a visitor’s browser.

  1. In the Cloudflare dashboard, go to the **Caching** page.

[ Go to **Configuration** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/caching/configuration)
  2. Under **Browser Cache TTL** , select the desired cache expiration time from the drop-down menu.




The **Respect Existing Headers** option tells Cloudflare to honor the settings in the `Cache-Control` headers from your origin web server.

[PreviousOverview](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/)[NextAlways Online](https://developers.cloudflare.com/cache/how-to/always-online/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/edge-browser-cache-ttl/set-browser-ttl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
