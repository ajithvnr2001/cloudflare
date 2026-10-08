---
url: https://developers.cloudflare.com/changelog/product/stream/
title: Stream Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:49.824109+00:00
---

# Stream Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/stream/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Jul 31, 2026

## [Rotate Stream broadcast keys for live inputs](https://developers.cloudflare.com/changelog/post/2026-07-30-rotate-stream-broadcast-keys/)

[Stream](https://developers.cloudflare.com/stream/)

You can now rotate the broadcast credentials for a Stream live input without changing the live input identifier.

Use key rotation when live input credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys revokes the old credentials, disconnects broadcasts using stale credentials, and returns refreshed credentials in the API response.

To rotate keys for a live input, make a `POST` request to the `rotate_keys` endpoint:
    
    
    curl --request POST \
    https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/rotate_keys \
    --header "Authorization: Bearer <API_TOKEN>"

Live input responses now also include `keysRotatedAt`, which indicates when the live input keys were last rotated. This field is omitted for live inputs whose keys have never been rotated.

For endpoint details, refer to [Rotate keys for a live input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/rotate_keys/). For usage guidance, refer to [Manage live inputs](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#manage-live-inputs).

May 7, 2026

## [Introducing Stream Bindings for Workers](https://developers.cloudflare.com/changelog/post/2026-05-07-stream-workers-binding/)

[Stream](https://developers.cloudflare.com/stream/)

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

Mar 18, 2026

## [Media Transformations binding for Workers](https://developers.cloudflare.com/changelog/post/2026-03-18-media-transformations-workers-binding/)

[Stream](https://developers.cloudflare.com/stream/)

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

Feb 24, 2026

## [Stream live inputs can now be disabled and enabled](https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/)

[Stream](https://developers.cloudflare.com/stream/)

You can now disable a live input to reject incoming RTMPS and SRT connections. When a live input is disabled, any broadcast attempts will fail to connect.

This gives you more control over your live inputs:

  * Temporarily pause an input without deleting it
  * Programmatically end creator broadcasts
  * Prevent new broadcasts from starting on a specific input



To disable a live input via the API, set the `enabled` property to `false`:
    
    
    curl --request PUT \
    https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \
    --header "Authorization: Bearer <API_TOKEN>" \
    --data '{"enabled": false}'

You can also disable or enable a live input from the **Live inputs** list page or the live input detail page in the Dashboard.

All existing live inputs remain enabled by default. For more information, refer to [Start a live stream](https://developers.cloudflare.com/stream/stream-live/start-stream-live/).

Aug 8, 2025

## [Introducing observability and metrics for Stream Live Inputs](https://developers.cloudflare.com/changelog/post/2025-08-08-stream-live-observability/)

[Stream](https://developers.cloudflare.com/stream/)

New information about broadcast metrics and events is now available in [Cloudflare Stream](https://developers.cloudflare.com/stream/) in the Live Input details of the Dashboard.

![Live Input details showing metrics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1382,height=907,format=webp/_astro/2025-08-05-live-input-metrics.B31Z3RGB.png)

You can now easily understand broadcast-side health and performance with new observability, which can help when troubleshooting common issues, particularly for new customers who are just getting started, and platform customers who may have limited visibility into how their end-users configure their encoders.

To get started, start a live stream ([just getting started?](https://developers.cloudflare.com/stream/examples/obs-from-scratch/)), then visit the Live Input details page in Dash.

See our new live [Troubleshooting](https://developers.cloudflare.com/stream/stream-live/troubleshooting/) guide to learn what these metrics mean and how to use them to address common broadcast issues.

Jul 22, 2025

## [Audio mode for Media Transformations](https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/)

[Stream](https://developers.cloudflare.com/stream/)

We now support `audio` mode! Use this feature to extract audio from a source video, outputting an M4A file to use in downstream workflows like [AI inference](https://developers.cloudflare.com/workers-ai/), content moderation, or transcription.

For example,

Example URLtext
    
    
    https://example.com/cdn-cgi/media/<OPTIONS>/<SOURCE-VIDEO>
    https://example.com/cdn-cgi/media/mode=audio,time=3s,duration=60s/<input video with diction>

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

Jun 10, 2025

## [Increased limits for Media Transformations](https://developers.cloudflare.com/changelog/post/2025-06-10-media-transformations-limits-increase/)

[Stream](https://developers.cloudflare.com/stream/)

We have increased the limits for [Media Transformations](https://developers.cloudflare.com/stream/transform-videos/):

  * Input file size limit is now 100MB (was 40MB)
  * Output video duration limit is now 1 minute (was 30 seconds)



Additionally, we have improved caching of the input asset, resulting in fewer requests to origin storage even when transformation options may differ.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

May 14, 2025

## [Introducing Origin Restrictions for Media Transformations](https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/)

[Stream](https://developers.cloudflare.com/stream/)

We are adding [source origin restrictions](https://developers.cloudflare.com/stream/transform-videos/sources/) to the Media Transformations beta. This allows customers to restrict what sources can be used to fetch images and video for transformations. This feature is the same as --- and uses the same settings as --- [Image Transformations sources](https://developers.cloudflare.com/images/optimization/transformations/sources/).

When transformations is first enabled, the default setting only allows transformations on images and media from the same website or domain being used to make the transformation request. In other words, by default, requests to `example.com/cdn-cgi/media` can only reference originals on `example.com`.

![Enable allowed origins from the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1664,height=872,format=webp/_astro/allowed-origins.4hu5lHws.png)

Adding access to other sources, or allowing any source, [is easy to do](https://developers.cloudflare.com/images/optimization/transformations/sources/) in the **Transformations** tab under **Stream**. Click each domain enabled for Transformations and set its sources list to match the needs of your content. The user making this change will need permission to edit zone settings.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

Apr 11, 2025

## [Signed URLs and Infrastructure Improvements on Stream Live WebRTC Beta](https://developers.cloudflare.com/changelog/post/2025-04-14-webrtc-beta-signed-urls/)

[Stream](https://developers.cloudflare.com/stream/)

Cloudflare [Stream](https://developers.cloudflare.com/stream/) has completed an infrastructure upgrade for our [Live WebRTC beta](https://developers.cloudflare.com/stream/webrtc-beta/) support which brings increased scalability and improved playback performance to all customers. WebRTC allows broadcasting directly from a browser (or supported WHIP client) with ultra-low latency to tens of thousands of concurrent viewers across the globe.

Additionally, as part of this upgrade, the WebRTC beta now supports Signed URLs to protect playback, just like our standard live stream options (HLS/DASH).

For more information, learn about the [Stream Live WebRTC beta](https://developers.cloudflare.com/stream/webrtc-beta/).

Mar 6, 2025

## [Introducing Media Transformations from Cloudflare Stream](https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/)

[Stream](https://developers.cloudflare.com/stream/)

Today, we are thrilled to announce Media Transformations, a new service that brings the magic of [Image Transformations](https://developers.cloudflare.com/images/optimization/transformations/overview/) to _short-form video files,_ wherever they are stored!

For customers with a huge volume of short video — generative AI output, e-commerce product videos, social media clips, or short marketing content — uploading those assets to Stream is not always practical. Sometimes, the greatest friction to getting started was the thought of all that migrating. Customers want a simpler solution that retains their current storage strategy to deliver small, optimized MP4 files. Now you can do that with Media Transformations.

To transform a video or image, [enable transformations](https://developers.cloudflare.com/stream/transform-videos/#getting-started) for your zone, then make a simple request with a specially formatted URL. The result is an MP4 that can be used in an HTML video element without a player library. If your zone already has Image Transformations enabled, then it is ready to optimize videos with Media Transformations, too.

URL formattext
    
    
    https://example.com/cdn-cgi/media/<OPTIONS>/<SOURCE-VIDEO>

For example, we have a short video of the mobile in Austin's office. The original is nearly 30 megabytes and wider than necessary for this layout. Consider a simple width adjustment:

Example URLtext
    
    
    https://example.com/cdn-cgi/media/width=640/<SOURCE-VIDEO>
    https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4

The result is less than 3 megabytes, properly sized, and delivered dynamically so that customers do not have to manage the creation and storage of these transformed assets.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

Feb 14, 2025

## [Rewind, Replay, Resume: Introducing DVR for Stream Live](https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/)

[Stream](https://developers.cloudflare.com/stream/)

Previously, all viewers watched "the live edge," or the latest content of the broadcast, synchronously. If a viewer paused for more than a few seconds, the player would automatically "catch up" when playback started again. Seeking through the broadcast was only available once the recording was available after it concluded.

Starting today, customers can make a small adjustment to the player embed or manifest URL to enable the DVR experience for their viewers. By offering this feature as an opt-in adjustment, our customers are empowered to pick the best experiences for their applications.

When building a player embed code or manifest URL, just add `dvrEnabled=true` as a query parameter. There are some things to be aware of when using this option. For more information, refer to [DVR for Live](https://developers.cloudflare.com/stream/stream-live/dvr-for-live/).

Jan 30, 2025

## [Expanded language support for Stream AI Generated Captions](https://developers.cloudflare.com/changelog/post/2025-01-30-stream-generated-captions-new-languages/)

[Stream](https://developers.cloudflare.com/stream/)

Stream's [generated captions](https://developers.cloudflare.com/stream/edit-videos/adding-captions/#generate-a-caption) leverage Workers AI to automatically transcribe audio and provide captions to the player experience. We have added support for these languages:

  * `cs` \- Czech
  * `nl` \- Dutch
  * `fr` \- French
  * `de` \- German
  * `it` \- Italian
  * `ja` \- Japanese
  * `ko` \- Korean
  * `pl` \- Polish
  * `pt` \- Portuguese
  * `ru` \- Russian
  * `es` \- Spanish



For more information, learn about [adding captions to videos](https://developers.cloudflare.com/stream/edit-videos/adding-captions/).
