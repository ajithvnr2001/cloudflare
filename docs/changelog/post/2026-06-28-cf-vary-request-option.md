---
url: https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/
title: Workers fetch requests now support cf.vary \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:59.940080+00:00
---

# Workers fetch requests now support cf.vary · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 28, 2026

## Workers fetch requests now support cf.vary

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers `fetch()` requests now support the `cf.vary` request option. Use `cf.vary` to control how Cloudflare caches origin responses with a `Vary` header for a single subrequest.

src/index.jsjs
    
    
    export default {
    	async fetch(request) {
    		return fetch(request, {
    			cf: {
    				vary: {
    					default: { action: "bypass" },
    					headers: {
    						accept: {
    							action: "normalize",
    							media_types: ["text/html", "application/json"],
    						},
    						"accept-language": {
    							action: "normalize",
    							languages: ["en", "fr", "de"],
    						},
    					},
    				},
    			},
    		});
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		return fetch(request, {
    			cf: {
    				vary: {
    					default: { action: "bypass" },
    					headers: {
    						accept: {
    							action: "normalize",
    							media_types: ["text/html", "application/json"],
    						},
    						"accept-language": {
    							action: "normalize",
    							languages: ["en", "fr", "de"],
    						},
    					},
    				},
    			},
    		});
    	},
    } satisfies ExportedHandler;

For more information, refer to [`cf.vary`](https://developers.cloudflare.com/workers/runtime-apis/request/#the-cfvary-property).
