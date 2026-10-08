---
url: https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/
title: New formats parameter for the Browser Run /snapshot endpoint \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:57.577266+00:00
---

# New formats parameter for the Browser Run /snapshot endpoint · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 11, 2026

## New formats parameter for the Browser Run /snapshot endpoint

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-11-browser-run-snapshot-formats/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/)'s [`/snapshot` endpoint](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) now supports a `formats` parameter that lets you return multiple page formats in a single API call. Previously, `/snapshot` returned only HTML content and a screenshot. You can now also include Markdown and the accessibility tree in the same response.

These formats are particularly useful for AI agent workflows:

  * Markdown provides a token-efficient representation of page content that LLMs can process directly, without parsing HTML markup.
  * The accessibility tree provides a structured representation of a page's elements, including roles, labels, and hierarchy, helping LLMs understand page structure and navigate its contents.



The following example returns a screenshot, Markdown, and the accessibility tree in one call:
    
    
    curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/snapshot' \
      -H 'Authorization: Bearer <apiToken>' \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://example.com/",
        "formats": ["screenshot", "markdown", "accessibilityTree"]
      }'
    
    
    import Cloudflare from "cloudflare";
    
    const client = new Cloudflare({
    	apiToken: process.env["CLOUDFLARE_API_TOKEN"],
    });
    
    const snapshot = await client.browserRendering.snapshot.create({
    	account_id: process.env["CLOUDFLARE_ACCOUNT_ID"],
    	url: "https://example.com/",
    	formats: ["screenshot", "markdown", "accessibilityTree"],
    });
    
    console.log(snapshot.markdown);
    console.log(snapshot.accessibilityTree);
    
    
    interface Env {
    	BROWSER: BrowserRun;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		return await env.BROWSER.quickAction("snapshot", {
    			url: "https://example.com/",
    			formats: ["screenshot", "markdown", "accessibilityTree"],
    		});
    	},
    } satisfies ExportedHandler<Env>;

You must request at least two formats. If you only need one, use the respective single-format endpoint such as [`/screenshot`](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/) or [`/markdown`](https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/).

Refer to the [`/snapshot` documentation](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) for the full list of accepted values.
