---
url: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-cache-key/
title: Purge cache key resources \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:45.026630+00:00
---

# Purge cache key resources · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-cache-key/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration

  4. /[Purge cache](https://developers.cloudflare.com/cache/how-to/purge-cache/)
  5. /Purge cache key resources



# Purge cache key resources

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-cache-key/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPurge by device typePurge by geoPurge by language

Instantly purge resources that use Cache Keys via the [Cloudflare API](https://developers.cloudflare.com/api/resources/cache/methods/purge/). If you use [Cloudflare's Purge by URL](https://developers.cloudflare.com/api/resources/cache/methods/purge/#purge-cached-content-by-url), include the headers and query strings that are in your custom Cache Key.

Currently, it is not possible to purge a URL stored through Cache API that uses a custom cache key set by a Worker. Instead, use a [custom key created by Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#cache-key). Alternatively, purge your assets using purge everything, purge by tag, purge by host or purge by prefix.

To instantly purge by `device_type`, `geo`, or `lang` use `CF-Device-Type`, `CF-IPCountry` or `accept-language`, respectively. [Purge by Tag / Host](https://developers.cloudflare.com/api/resources/cache/methods/purge/#purge-cached-content-by-tag-host-or-prefix) and [Purge Everything](https://developers.cloudflare.com/api/resources/cache/methods/purge/#purge-all-cached-content) are not impacted by the use of custom Cache Keys.

## Purge by device type

For a Cache Key based on device type, purge the asset by passing the `CF-Device-Type` header with the API purge request (valid headers include mobile, desktop, and tablet).

Refer to the example API request below to instantly purge all mobile assets on the root webpage.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Cache Purge`

Purge Cached Contentbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"files": [
    				{
    						"url": "http://my.website.com/",
    						"headers": {
    								"CF-Device-Type": "mobile"
    						}
    				}
    		]
    	}'

## Purge by geo

Instantly purge resources for a location-based Cache Key by specifying the two-letter country code. Spain is used in the example below.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Cache Purge`

Purge Cached Contentbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"files": [
    				{
    						"url": "http://my.website.com/",
    						"headers": {
    								"CF-IPCountry": "ES"
    						}
    				}
    		]
    	}'

## Purge by language

For a Cache Key based on language, purge the asset by passing the `accept-language` header. Refer to the example API request below to instantly purge all assets in Chinese (PRC).

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Cache Purge`

Purge Cached Contentbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"files": [
    				{
    						"url": "http://my.website.com/",
    						"headers": {
    								"accept-language": "zh-CN"
    						}
    				}
    		]
    	}'

[Previous​Purge cache by prefix (URL)](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/)[NextP​urge varied images](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-varied-images/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/purge-cache/purge-cache-key.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
