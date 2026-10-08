---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-websocket-adapter-ga/
title: Realtime SFU WebSocket adapter is generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:17.790365+00:00
---

# Realtime SFU WebSocket adapter is generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-websocket-adapter-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## Realtime SFU WebSocket adapter is generally available

[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-websocket-adapter-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/) for [Cloudflare's Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) is now generally available. The SFU (selective forwarding unit) is managed WebRTC infrastructure for live audio, video, and data across [Cloudflare's global network in 330+ cities ↗︎](https://www.cloudflare.com/products/turn-sfu/).

The adapter connects live calls to any server that accepts WebSockets, such as a [Durable Object](https://developers.cloudflare.com/durable-objects/). It delivers uncompressed pulse-code modulation (PCM) audio and JPEG video frames. Your backend can process this media without implementing a WebRTC client.

#### What you can build

  * Transcribe or record call audio, or let a voice agent hear and respond to participants. The [AI audio example](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/) uses Durable Objects and Workers AI for transcription and speech generation. Separate adapters receive PCM audio and send generated speech back to participants.
  * Analyze images or build previews from live video. The [WebRTC-to-JPEG example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/video-to-jpeg) sends a browser's camera stream to a Durable Object as JPEG frames at one frame per second by default.



#### What changes for existing integrations

Existing adapter creation requests and media formats stay the same.

For WebRTC-to-WebSocket streaming, the SFU now automatically retries the same endpoint for up to 15 seconds instead of 5, with no additional API setting.

The [close API](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#close-adapter) is now idempotent and returns success even if the adapter has already closed:
    
    
    {
    	"tracks": [{ "adapterId": "<ADAPTER_ID>" }]
    }

Refer to the [WebSocket adapter guide](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/) for setup, media formats, and API requests.
