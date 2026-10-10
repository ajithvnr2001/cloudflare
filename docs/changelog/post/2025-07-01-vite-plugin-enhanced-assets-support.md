---
url: https://developers.cloudflare.com/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/
title: Enhanced support for static assets with the Cloudflare Vite plugin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.136393+00:00
---

# Enhanced support for static assets with the Cloudflare Vite plugin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2025

## Enhanced support for static assets with the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use any of Vite's [static asset handling ↗︎](https://vite.dev/guide/assets) features in your Worker as well as in your frontend. These include importing assets as URLs, importing as strings and importing from the `public` directory as well as inlining assets.

Additionally, assets imported as URLs in your Worker are now automatically moved to the client build output.

Here is an example that fetches an imported asset using the [assets binding](https://developers.cloudflare.com/workers/static-assets/binding/#binding) and modifies the response.
    
    
    // Import the asset URL
    // This returns the resolved path in development and production
    import myImage from "./my-image.png";
    
    export default {
    	async fetch(request, env) {
    		// Fetch the asset using the binding
    		const response = await env.ASSETS.fetch(new URL(myImage, request.url));
    		// Create a new `Response` object that can be modified
    		const modifiedResponse = new Response(response.body, response);
    		// Add an additional header
    		modifiedResponse.headers.append("my-header", "imported-asset");
    
    		// Return the modified response
    		return modifiedResponse;
    	},
    };

Refer to [Static Assets](https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/) in the Cloudflare Vite plugin docs for more info.
