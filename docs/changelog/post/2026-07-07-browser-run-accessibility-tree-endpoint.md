---
url: https://developers.cloudflare.com/changelog/post/2026-07-07-browser-run-accessibility-tree-endpoint/
title: New Browser Run endpoint for accessibility trees \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.378612+00:00
---

# New Browser Run endpoint for accessibility trees · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-07-browser-run-accessibility-tree-endpoint/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2026

## New Browser Run endpoint for accessibility trees

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) now supports a standalone `/accessibilityTree` endpoint, giving agent and automation workflows direct access to the browser's accessibility tree for a rendered webpage.

An accessibility tree is the browser's structured view of a rendered page: roles, names, states, values, and hierarchy. It is useful for accessibility tooling, but also for AI agents and automation workflows that need page structure without the noise of raw HTML or the cost of screenshots.

For AI agents, this means less inference from pixels and less parsing HTML. You can provide the page structure directly, helping agents identify available elements and determine which actions they can take.

With the new `/accessibilityTree` endpoint, you can request the accessibility tree directly when you only need the semantic structure of a page. If you need multiple page formats in a single API call, you can use the [`/snapshot`](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) endpoint, which also returns Markdown, HTML, and screenshots.
    
    
    curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-run/accessibilityTree' \
      -H 'Authorization: Bearer <apiToken>' \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://example.com/"
    }'
    
    
    {
    	"success": true,
    	"result": {
    		"accessibilityTree": {
    			"role": "RootWebArea",
    			"name": "Example Domain",
    			"children": [
    				{
    					"role": "heading",
    					"name": "Example Domain",
    					"level": 1
    				},
    				{
    					"role": "link",
    					"name": "Learn more"
    				}
    			]
    		}
    	}
    }

Use `interestingOnly` to return only semantically meaningful nodes, or `root` to capture the accessibility tree for a specific subtree.

Refer to the [`/accessibilityTree` documentation](https://developers.cloudflare.com/browser-run/quick-actions/accessibility-tree-endpoint/) for usage examples and supported parameters.
