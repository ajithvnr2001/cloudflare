---
url: https://developers.cloudflare.com/realtime/sfu/examples/
title: Examples \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:34.894585+00:00
---

# Examples · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/examples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)
  4. /Examples



# Examples

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/examples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBuild an applicationLearn a specific featureSource and status

Choose an application, run its example, and follow the SFU operations behind it. Each guide explains the topology, setup, adaptation points, and current limitations.

## Build an application

### [Embedded devices and remote control](https://developers.cloudflare.com/realtime/sfu/examples/embedded-devices/)

Stream audio and telemetry from an ESP32, with one browser controlling the device.

### [Cloud gaming](https://developers.cloudflare.com/realtime/sfu/examples/cloud-gaming/)

Publish a Container's audio and video, and return browser input through DataChannels.

### [AI audio pipelines](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/)

Connect speech-to-text and text-to-speech services through WebSocket adapters.

### [Custom video room](https://developers.cloudflare.com/realtime/sfu/examples/video-room/)

Start with two browser participants, then inspect presence, discovery, and media lifecycle.

The [video-room quickstart](https://developers.cloudflare.com/realtime/sfu/get-started/) is the default introduction to publishing and receiving media. The application examples are experimental; their guides identify integration work and known limitations.

## Learn a specific feature

Example | What to try  
---|---  
[DataChannels ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/echo-datachannels) | Establish two endpoints, acknowledge readiness, send replies, and compare delivery settings  
[WebRTC video to JPEG ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/video-to-jpeg) | Send a camera track through an adapter and receive JPEG frames over WebSocket  
[SFU network visualization ↗︎](https://realtime-sfu.dev-demos.workers.dev) | Explore an illustration of endpoint connections and media routing  
  
The DataChannel example is intended for localhost. The JPEG example requires application authentication and authorization before public use.

## Source and status

Browse the [Realtime examples repository ↗︎](https://github.com/cloudflare/realtime-examples) for complete source, component guides, and declared checks. The catalog distinguishes maintained, experimental, and legacy examples. Legacy entries are historical or educational references with documented limitations.

[PreviousWebSocket](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/)[NextEmbedded devices](https://developers.cloudflare.com/realtime/sfu/examples/embedded-devices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/examples/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
