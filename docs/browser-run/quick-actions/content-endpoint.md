---
url: https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/
title: /content - Fetch HTML \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:37.935541+00:00
---

# /content - Fetch HTML · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /[Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/)
  4. //content - Fetch HTML



# /content - Fetch HTML

Last updated Sep 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointRequired fieldsCommon use casesBasic usage Fetch rendered HTML from a URLAdvanced usage Block specific resource types Handling JavaScript-heavy pages Set a custom user agentTroubleshooting

The `/content` endpoint instructs the browser to navigate to a website and capture the fully rendered HTML of a page, including the `head` section, after JavaScript execution. This is ideal for capturing content from JavaScript-heavy or interactive websites.

You can use this endpoint in two ways:

  * **REST API** : [Create a custom API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `Browser Rendering - Edit` permission.
  * **Workers Bindings** : Call the endpoint directly from a [Cloudflare Worker](https://developers.cloudflare.com/workers/) using the [Workers Bindings](https://developers.cloudflare.com/browser-run/reference/wrangler/#bindings). No API token is needed.



For more information, refer to [Quick Actions: Before you begin](https://developers.cloudflare.com/browser-run/quick-actions/#before-you-begin).

## Endpoint
    
    
    https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-run/content

## Required fields

You must provide either `url` or `html`:

  * `url` (string)
  * `html` (string)



## Common use cases

  * Capture the fully rendered HTML of a dynamic page
  * Extract HTML for parsing, scraping, or downstream processing



## Basic usage

### Fetch rendered HTML from a URL

Go to `https://developers.cloudflare.com/` and return the rendered HTML.
    
    
    curl -X 'POST' 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-run/content' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer <apiToken>' \
      -d '{"url": "https://developers.cloudflare.com/"}'
    
    
    import Cloudflare from "cloudflare";
    
    const client = new Cloudflare({
    	apiToken: process.env["CLOUDFLARE_API_TOKEN"],
    });
    
    const content = await client.browserRendering.content.create({
    	account_id: process.env["CLOUDFLARE_ACCOUNT_ID"],
    	url: "https://developers.cloudflare.com/",
    });
    
    console.log(content);
    
    
    interface Env {
    	BROWSER: BrowserRun;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		return await env.BROWSER.quickAction("content", {
    			url: "https://developers.cloudflare.com/",
    		});
    	},
    } satisfies ExportedHandler<Env>;

## Advanced usage

Looking for more parameters?

Visit the [Browser Run API reference](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/content/methods/create/) for all available parameters, such as setting HTTP credentials using `authenticate`, setting `cookies`, and customizing load behavior using `gotoOptions`.

### Block specific resource types

Navigate to `https://cloudflare.com/` but block images and stylesheets from loading. Undesired requests can be blocked by resource type (`rejectResourceTypes`) or by using a regex pattern (`rejectRequestPattern`). The opposite can also be done, only allow requests that match `allowRequestPattern` or `allowResourceTypes`.
    
    
    curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-run/content' \
      -H 'Authorization: Bearer <apiToken>' \
      -H 'Content-Type: application/json' \
      -d '{
          "url": "https://cloudflare.com/",
          "rejectResourceTypes": ["image"],
          "rejectRequestPattern": ["/^.*\\.(css)"]
    		}'

Many more options exist, like setting HTTP headers using `setExtraHTTPHeaders`, setting `cookies`, and using `gotoOptions` to control page load behaviour - check the endpoint [reference](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/content/methods/create/) for all available parameters.

### Handling JavaScript-heavy pages

For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.

The simplest solution is to use the `gotoOptions.waitUntil` parameter set to `networkidle0` or `networkidle2`:
    
    
    {
    	"url": "https://example.com",
    	"gotoOptions": {
    		"waitUntil": "networkidle0"
    	}
    }

For faster responses, advanced users can use `waitForSelector` to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to [Quick Actions timeouts](https://developers.cloudflare.com/browser-run/reference/timeouts/).

### Set a custom user agent

You can change the user agent at the page level by passing `userAgent` as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.

Note

The `userAgent` parameter does not bypass bot protection. Requests from Browser Run will always be identified as a bot. Because the User-Agent is configurable, destination servers looking to identify or block Browser Run requests should use the [non-configurable headers](https://developers.cloudflare.com/browser-run/reference/automatic-request-headers/#non-configurable-headers) rather than relying on the User-Agent string.

## Troubleshooting

If you have questions or encounter an error, see the [Browser Run FAQ and troubleshooting guide](https://developers.cloudflare.com/browser-run/faq/).

[PreviousOverview](https://developers.cloudflare.com/browser-run/quick-actions/)[Next/screenshot - Capture screenshot](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/quick-actions/content-endpoint.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
