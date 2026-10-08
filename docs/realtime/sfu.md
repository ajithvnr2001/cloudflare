---
url: https://developers.cloudflare.com/realtime/sfu/
title: Overview \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:33.881305+00:00
---

# Overview · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /Realtime SFU



# Realtime SFU

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat you can buildHow the pieces fit togetherChoose a starting point

Connect devices, applications, and AI with real-time media and data.

Cloudflare Realtime SFU (Selective Forwarding Unit) routes WebRTC audio, video, and DataChannels between your endpoints. Your application chooses who publishes, who subscribes, and who can send controls back.

WebRTC provides connections for live media and messages. Each endpoint connects to the SFU, which forwards its publications to the subscribers your application selects.

Use standard HTTPS APIs and WebRTC from browsers, embedded firmware, native applications, and servers. Your signaling backend can run on Workers, in a container, or on your existing infrastructure.

[Get started](https://developers.cloudflare.com/realtime/sfu/get-started/) [Explore examples](https://developers.cloudflare.com/realtime/sfu/examples/)

## What you can build

### [Embedded devices](https://developers.cloudflare.com/realtime/sfu/examples/embedded-devices/)

Send audio and telemetry from an ESP32 to browsers, with controls for one authorized operator. Use the same design for robot gateways.

### [Cloud gaming](https://developers.cloudflare.com/realtime/sfu/examples/cloud-gaming/)

Stream a game from a Container to browsers, then send keyboard and pointer input back over DataChannels.

### [AI audio pipelines](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/)

Transcribe microphone audio with Workers AI, then send generated speech to browsers through WebSocket media adapters.

For a video conferencing application, start with [RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/). It provides meeting SDKs, participant management, and customizable UI components. Choose Realtime SFU when you need direct control over WebRTC connections, media routing, and signaling.

For a browser-first introduction, [run a custom video room](https://developers.cloudflare.com/realtime/sfu/get-started/). You can also compose interactive broadcasts, remote inspection tools, and media-processing applications from the same primitives.

## How the pieces fit together

Your endpoints exchange media and DataChannels with Realtime SFU. A separate application backend authenticates users and devices, calls the SFU API, and shares the track identifiers that endpoints need.

**Browser, device, or native endpoint**

WebRTC media and DataChannels

**Realtime SFU**

Application signaling

HTTPS API

**Your backend**

**Application state**

Browser, device, or native endpoint↔ WebRTC media and DataChannelsRealtime SFU

Browser, device, or native endpoint↔ Application signalingYour backend

Your backend↔ HTTPS APIRealtime SFU

Your backend↔Application state

The backend holds the SFU App Secret and manages application state and permissions. Refer to [application architecture](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/) for the responsibilities and trust boundaries.

## Choose a starting point

You want to | Start with  
---|---  
Run a working application | [Get started](https://developers.cloudflare.com/realtime/sfu/get-started/)  
Understand connections, publications, and subscriptions | [Sessions and tracks](https://developers.cloudflare.com/realtime/sfu/concepts/sessions-tracks/)  
Implement your own media or messaging endpoint | [Connection patterns](https://developers.cloudflare.com/realtime/sfu/get-started/connection-patterns/)  
Add messages, video quality selection, or a media adapter | [Features](https://developers.cloudflare.com/realtime/sfu/features/)  
Look up an API operation or request body | [Connection API](https://developers.cloudflare.com/realtime/sfu/api/)  
Diagnose a connection or media problem | [Observability](https://developers.cloudflare.com/realtime/sfu/observability/)  
  
For a coding agent, start with the [SFU documentation index](https://developers.cloudflare.com/realtime/sfu/llms.txt). It links to the task guides and API reference.

The [examples collection](https://developers.cloudflare.com/realtime/sfu/examples/) identifies each application's requirements and limitations. Refer to [pricing](https://developers.cloudflare.com/realtime/sfu/platform/pricing/) and [limits](https://developers.cloudflare.com/realtime/sfu/platform/limits/) when planning your integration.

[PreviousLegal](https://developers.cloudflare.com/realtime/realtimekit/legal/)[NextOverview](https://developers.cloudflare.com/realtime/sfu/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
