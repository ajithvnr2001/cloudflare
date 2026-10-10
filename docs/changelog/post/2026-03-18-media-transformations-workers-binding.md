---
url: https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/
title: Media Transformations binding for Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.351274+00:00
---

# Media Transformations binding for Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 18, 2026

## Media Transformations binding for Workers

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use a Workers binding to transform videos with Media Transformations. This allows you to resize, crop, extract frames, and extract audio from videos stored anywhere, even in private locations like R2 buckets.

The Media Transformations binding is useful when you want to:

  * Transform videos stored in private or protected sources
  * Optimize videos and store the output directly back to R2 for re-use
  * Extract still frames for classification or description with Workers AI
  * Extract audio tracks for transcription using Workers AI



To get started, add the Media binding to your Wrangler configuration:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "media": {
        "binding": "MEDIA"
      }
    }
    
    
    [media]
    binding = "MEDIA"

Then use the binding in your Worker to transform videos:
    
    
    export default {
    	async fetch(request, env) {
    		const video = await env.R2_BUCKET.get("input.mp4");
    
    		const result = env.MEDIA.input(video.body)
    			.transform({ width: 480, height: 270 })
    			.output({ mode: "video", duration: "5s" });
    
    		return await result.response();
    	},
    };
    
    
    export default {
    	async fetch(request, env) {
    		const video = await env.R2_BUCKET.get("input.mp4");
    
    		const result = env.MEDIA.input(video.body)
    			.transform({ width: 480, height: 270 })
    			.output({ mode: "video", duration: "5s" });
    
    		return await result.response();
    	},
    };

Output modes include `video` for optimized MP4 clips, `frame` for still images, `spritesheet` for multiple frames, and `audio` for M4A extraction.

For more information, refer to the [Media Transformations binding documentation](https://developers.cloudflare.com/stream/transform-videos/bindings/).
