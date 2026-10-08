---
url: https://developers.cloudflare.com/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/
title: Shared dictionaries passthrough now in open beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:51.092209+00:00
---

# Shared dictionaries passthrough now in open beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 30, 2026

## Shared dictionaries passthrough now in open beta

[Speed](https://developers.cloudflare.com/speed/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Shared dictionaries](https://developers.cloudflare.com/speed/optimization/content/shared-dictionaries/) ([RFC 9842 ↗︎](https://www.rfc-editor.org/rfc/rfc9842.html)) let an origin compress a response against a previous version of the same resource that the browser already has cached, so only the difference between versions travels over the wire. Shared dictionaries passthrough is now in open beta on all plans.

#### What changed

In passthrough mode, Cloudflare:

  * Forwards the `Use-As-Dictionary` and `Available-Dictionary` headers between client and origin without modification.
  * Treats `dcb` (Dictionary-Compressed Brotli) and `dcz` (Dictionary-Compressed Zstandard) as valid `Content-Encoding` values end to end, without recompressing them.
  * Extends the cache key to vary on `Available-Dictionary` and `Accept-Encoding` so each delta-compressed variant is cached correctly.



Your origin manages the dictionary lifecycle: deciding which assets are dictionaries, attaching `Use-As-Dictionary` headers, and producing deltas in response to `Available-Dictionary` requests. Cloudflare handles the transport and the cache.

In internal testing on a 272 KB JavaScript bundle, the asset shrinks from 92.1 KB with Gzip to 2.6 KB with delta Zstandard against the previous version — a 97% reduction over standard compression — with download times improving by 81–89% versus Gzip.

Shared dictionaries work with browsers that advertise `dcb` or `dcz` in `Accept-Encoding`. Today, this includes Chrome 130 or later and Edge 130 or later.

#### Get started

Turn on passthrough for your zone with a single API call:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/shared_dictionary_mode" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"value": "passthrough"
    	}'

You can also turn it on under **Speed** > **Settings** > **Content Optimization** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/speed/optimization). For full origin setup instructions and a working test recipe, refer to [Shared dictionaries](https://developers.cloudflare.com/speed/optimization/content/shared-dictionaries/), or try the live demo at [canicompress.com ↗︎](https://canicompress.com/).
