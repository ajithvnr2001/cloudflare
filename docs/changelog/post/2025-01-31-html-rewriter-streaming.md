---
url: https://developers.cloudflare.com/changelog/post/2025-01-31-html-rewriter-streaming/
title: Transform HTML quickly with streaming content \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.171222+00:00
---

# Transform HTML quickly with streaming content · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-31-html-rewriter-streaming/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 31, 2025

## Transform HTML quickly with streaming content

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now transform HTML elements with streamed content using [`HTMLRewriter`](https://developers.cloudflare.com/workers/runtime-apis/html-rewriter).

Methods like `replace`, `append`, and `prepend` now accept [`Response`](https://developers.cloudflare.com/workers/runtime-apis/response/) and [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/) values as [`Content`](https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/#global-types).

This can be helpful in a variety of situations. For instance, you may have a Worker in front of an origin, and want to replace an element with content from a different source. Prior to this change, you would have to load all of the content from the upstream URL and convert it into a string before replacing the element. This slowed down overall response times.

Now, you can pass the `Response` object directly into the `replace` method, and HTMLRewriter will immediately start replacing the content as it is streamed in. This makes responses faster.

index.jsjs
    
    
    class ElementRewriter {
    	async element(element) {
    		// able to replace elements while streaming content
    		// the fetched body is not buffered into memory as part
    		// of the replace
    		let res = await fetch("https://upstream-content-provider.example");
    		element.replace(res);
    	}
    }
    
    export default {
    	async fetch(request, env, ctx) {
    		let response = await fetch("https://site-to-replace.com");
    		return new HTMLRewriter()
    			.on("[data-to-replace]", new ElementRewriter())
    			.transform(response);
    	},
    };

index.tsts
    
    
    class ElementRewriter {
    	async element(element: any) {
    		// able to replace elements while streaming content
    		// the fetched body is not buffered into memory as part
    		// of the replace
    		let res = await fetch('https://upstream-content-provider.example');
    		element.replace(res);
    	}
    }
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		let response = await fetch('https://site-to-replace.com');
    		return new HTMLRewriter().on('[data-to-replace]', new ElementRewriter()).transform(response);
    	},
    } satisfies ExportedHandler<Env>;

For more information, see the [`HTMLRewriter` documentation](https://developers.cloudflare.com/workers/runtime-apis/html-rewriter).
