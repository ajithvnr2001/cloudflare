---
url: https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/
title: Media transport adapters \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:35.907424+00:00
---

# Media transport adapters · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)

  4. /[Features](https://developers.cloudflare.com/realtime/sfu/features/)
  5. /Media transport adapters



# Media transport adapters

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWebSocket adapterLearn with an example

Media transport adapters connect WebRTC tracks to services that exchange media over another transport. The WebSocket adapter supports audio ingest, audio egress, and video egress as JPEG frames.

An external service can process or generate audio without implementing a WebRTC peer. Your backend creates the adapter and manages its lifetime.

## WebSocket adapter

The WebSocket adapter is generally available. Each adapter carries one track in one direction. Choose the path your service needs:

Your service | Direction | Media  
---|---|---  
Generates audio | WebSocket → SFU → WebRTC | PCM audio published as a WebRTC audio track  
Transcribes or processes audio | WebRTC → SFU → WebSocket | Audio delivered as PCM  
Inspects frames or generates previews | WebRTC → SFU → WebSocket | Video delivered as JPEG frames  
  
**WebRTC endpoint**

Media tracks

Cloudflare**Realtime SFU**

**WebSocket adapters**

Binary media packets

**Your WebSocket service**

WebRTC endpointMedia tracks ↔Realtime SFU

Realtime SFUMedia ↔WebSocket adapters

WebSocket adaptersBinary media packets ↔Your WebSocket service

Use separate adapter instances for bidirectional audio. Video ingest over the WebSocket adapter is not supported.

[Use the WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/)

## Learn with an example

The [AI audio guide](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/) shows speech generation and transcription through separate adapter paths. For video, the [WebRTC-to-JPEG example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/video-to-jpeg) receives frames in a Durable Object and distributes them to viewers.

Both examples are experimental and require application authentication and authorization before public use. Their repository guides describe setup and integration limitations.

[PreviousSimulcast](https://developers.cloudflare.com/realtime/sfu/features/simulcast/)[NextWebSocket](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/features/media-transport-adapters/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
