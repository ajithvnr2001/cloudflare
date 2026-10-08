---
url: https://developers.cloudflare.com/realtime/
title: Overview \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:51.804641+00:00
---

# Overview · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/

  1. [Home](https://developers.cloudflare.com/)
  2. /Realtime



# Cloudflare Realtime

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat you can buildRealtime primitivesFrequently asked questions Should I use RealtimeKit or Realtime SFU? How does TURN fit into WebRTC? For webinars, should I use RealtimeKit or Stream Live?Next steps

Build live applications where people, AI systems, and devices communicate in real time over [Cloudflare's global network ↗︎](https://www.cloudflare.com/network/).

![](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1400,height=799,format=webp/_astro/global-web-rtc-network.vo5ylKmC.png)![](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1400,height=799,format=webp/_astro/global-web-rtc-network-dark.DktEEERJ.png)

[RealtimeKitAdd audio or video calls to your appUse prebuilt meeting UI and SDKs for web and mobile. Add managed recording or transcription if your app needs it.Explore RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Realtime SFUBuild custom WebRTC applicationsUse the Realtime SFU API to control which endpoints publish or receive audio, video, and data. Your application handles signaling and permissions.Explore Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)

## What you can build

[RealtimeKitIn-app meetingsAdd audio or video calls to your web or mobile app with prebuilt screens and controls.View guide](https://developers.cloudflare.com/realtime/realtimekit/quickstart/)[RealtimeKitVirtual classroomsSet instructor and student permissions, then split a class into breakout rooms. Record or transcribe sessions when needed.View guide](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/)[RealtimeKitLive eventsAdd reactions, chat, and polls to a live event.View guide](https://developers.cloudflare.com/realtime/realtimekit/webinar/)[Realtime SFUEmbedded devicesSend audio and telemetry from an ESP32 to browsers, with controls for one authorized operator. Use the same design for robot gateways.View guide](https://developers.cloudflare.com/realtime/sfu/examples/embedded-devices/)[Realtime SFUCloud gamingStream a game from a Container to browsers, then send keyboard and pointer input back over DataChannels.View guide](https://developers.cloudflare.com/realtime/sfu/examples/cloud-gaming/)[Realtime SFUAI audio pipelinesTranscribe microphone audio with Workers AI, then send generated speech to browsers through WebSocket media adapters.View guide](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/)

## Realtime primitives

### [Cloudflare TURN](https://developers.cloudflare.com/realtime/turn/)

Relay WebRTC traffic through Cloudflare when a NAT or firewall prevents a direct connection.

### [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/)

Send PCM audio in either direction between Realtime SFU and a WebSocket service, or receive video as JPEG frames.

### [DataChannels](https://developers.cloudflare.com/realtime/sfu/features/datachannels/)

Exchange chat, sensor updates, and control events between WebRTC endpoints.

## Frequently asked questions

### Should I use RealtimeKit or Realtime SFU?

If you are new to [WebRTC ↗︎](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/) and want to add audio or video meetings to your app, use [RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/). It includes [web and mobile SDKs](https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/) with [prebuilt UI](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/). Cloudflare handles signaling and media routing, and you can add managed [recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/) or [transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/).

If you have WebRTC experience and need control over [what each endpoint publishes or receives](https://developers.cloudflare.com/realtime/sfu/concepts/sessions-tracks/), use [Realtime SFU](https://developers.cloudflare.com/realtime/sfu/). Your application handles [signaling, permissions, session state, and track discovery](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/). Cloudflare runs the SFU and forwards media to subscribers.

### How does TURN fit into WebRTC?

A [TURN server](https://developers.cloudflare.com/realtime/turn/what-is-turn/) relays traffic when a NAT or firewall prevents two WebRTC endpoints from connecting directly. If a direct connection works, TURN stays out of the path.

RealtimeKit configures [Cloudflare TURN](https://developers.cloudflare.com/realtime/turn/) for you. Realtime SFU includes access to the same service. You can also use Cloudflare TURN with your own SFU or peer-to-peer application by [generating TURN credentials](https://developers.cloudflare.com/realtime/turn/generate-credentials/).

Cloudflare TURN uses [Anycast ↗︎](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/), so you do not have to deploy regional TURN servers or load balancers.

### For webinars, should I use RealtimeKit or Stream Live?

Use [RealtimeKit webinars](https://developers.cloudflare.com/realtime/realtimekit/webinar/) when attendees join as participants. They might speak, appear on camera, or move into [breakout rooms](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/).

Use [Stream Live](https://developers.cloudflare.com/stream/stream-live/) when a small group of presenters broadcasts and the audience mainly watches. For example, a webinar with a few presenters and a large watch-only audience should use Stream Live.

## Next steps

### [Get started with RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/quickstart/)

Create your first meeting and add RealtimeKit to your app.

### [Get started with Realtime SFU](https://developers.cloudflare.com/realtime/sfu/get-started/)

Create an application, open an SFU session, and publish a media track.

[NextOverview](https://developers.cloudflare.com/realtime/realtimekit/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
