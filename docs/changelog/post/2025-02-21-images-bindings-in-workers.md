---
url: https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/
title: Bind the Images API to your Worker \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.641416+00:00
---

# Bind the Images API to your Worker · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 24, 2025

## Bind the Images API to your Worker

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now [interact with the Images API](https://developers.cloudflare.com/images/optimization/binding/) directly in your Worker.

This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.

The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:
    
    
    {
    	"images": {
    		"binding": "IMAGES", // i.e. available in your Worker on env.IMAGES
    	},
    }
    
    
    [images]
    binding = "IMAGES"

Within your Worker code, you can interact with this binding by using `env.IMAGES`.

Here's how you can rotate, resize, and blur an image, then output the image as AVIF:
    
    
    const info = await env.IMAGES.info(stream);
    // stream contains a valid image, and width/height is available on the info object
    
    const response = (
    	await env.IMAGES.input(stream)
    		.transform({ rotate: 90 })
    		.transform({ width: 128 })
    		.transform({ blur: 20 })
    		.output({ format: "image/avif" })
    ).response();
    
    return response;

For more information, refer to [Images Bindings](https://developers.cloudflare.com/images/optimization/binding/).
