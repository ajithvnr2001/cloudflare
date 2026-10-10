---
url: https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/
title: Introducing Stream Bindings for Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.692564+00:00
---

# Introducing Stream Bindings for Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 7, 2026

## Introducing Stream Bindings for Workers

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now interact with your Stream video library using new bindings for Workers! This allows customers to upload content to Stream, provision direct uploads, manage videos, and generate signed URLs from a Worker without making authenticated API calls. We're excited to bring Stream and Workers closer together to empower more programmatic pipelines, tighter integrations, and support generative AI and inference workloads.

Use the Stream binding when you want to:

  * Upload videos from URLs or create basic direct upload links for end users
  * Generate signed playback tokens without managing signing keys
  * Manage video metadata, captions, downloads, and watermarks
  * Build video pipelines entirely within Workers



To get started, add the Stream binding to your Wrangler configuration:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "stream": {
        "binding": "STREAM"
      }
    }
    
    
    [stream]
    binding = "STREAM"

**Generate a video with AI and upload directly to Stream** or send a URL of a file you already have:
    
    
    const aiResponse = await env.AI.run(
    	"google/veo-3.1",
    	{
    		prompt: "A dog walking next to a river",
    		duration: "10s",
    		aspect_ratio: "16:9",
    		resolution: "1080p",
    		generate_audio: true,
    	},
    	{
    		gateway: { id: "experiments" },
    	},
    );
    
    // Veo will return a URL of the generated asset.
    const videoUrl = aiResponse.result.video;
    
    // Alternative option: a video of the Austin Office mobile
    // const videoUrl = 'https://pub-d9fcbc1abcd244c1821f38b99017347f.r2.dev/aus-mobile.mp4';
    
    // Upload to Stream by providing a URL
    const streamVideo = await env.STREAM.upload(videoUrl);
    
    // The streamVideo response will include the video ID, playback and manifest
    // URLs, and other information, just like the REST API.
    
    
    const aiResponse = await env.AI.run(
    	'google/veo-3.1',
    	{
    		prompt: 'A dog walking next to a river',
    		duration: '10s',
    		aspect_ratio: '16:9',
    		resolution: '1080p',
    		generate_audio: true,
    	},
    	{
    		gateway: { id: 'experiments' },
    	},
    );
    
    // Veo will return a URL of the generated asset.
    const videoUrl = aiResponse.result.video;
    
    // Alternative option: a video of the Austin Office mobile
    // const videoUrl = 'https://pub-d9fcbc1abcd244c1821f38b99017347f.r2.dev/aus-mobile.mp4';
    
    // Upload to Stream by providing a URL
    const streamVideo = await env.STREAM.upload(videoUrl);
    
    // The streamVideo response will include the video ID, playback and manifest
    // URLs, and other information, just like the REST API.

**Generate a signed URL without using a signing key** or an API call:
    
    
    const video_id = "ce800be43a9772f4bb02f35b860fb516";
    const token = await env.STREAM.video(video_id).generateToken();
    
    // Use the "token" in an iframe embed code, manifest URL, or thumbnail:
    const embedUrl = `https://customer-igynxd2rwhmuoxw8.cloudflarestream.com/${token}/iframe`;
    
    
    const video_id = 'ce800be43a9772f4bb02f35b860fb516';
    const token = await env.STREAM.video(video_id).generateToken();
    
    // Use the "token" in an iframe embed code, manifest URL, or thumbnail:
    const embedUrl = `https://customer-igynxd2rwhmuoxw8.cloudflarestream.com/${token}/iframe`;

**Get and set video properties** easily:
    
    
    const video_id = "46c8b7f480d410840758c1cb14a72e47";
    const result = await env.STREAM.video(video_id).details();
    
    await env.STREAM.video(video_id).update({
    	meta: { name: "sample video" },
    });
    
    
    const video_id = '46c8b7f480d410840758c1cb14a72e47';
    const result = await env.STREAM.video(video_id).details();
    
    await env.STREAM.video(video_id).update({
      meta: { name: 'sample video' }
    });

For setup instructions and the full API reference, refer to [Bind to Workers API](https://developers.cloudflare.com/stream/manage-video-library/bindings/).

#### Get started with your Agent

> Add a binding for Cloudflare Stream (env.STREAM). On the watch page, use the Stream binding to get info based on the ID, and leverage video.meta.name as the page title.
