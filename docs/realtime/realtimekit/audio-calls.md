---
url: https://developers.cloudflare.com/realtime/realtimekit/audio-calls/
title: Audio Only Calls \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:53.464729+00:00
---

# Audio Only Calls · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/audio-calls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /Audio Only Calls



# Audio Only Calls

Last updated Sep 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/audio-calls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow Audio Calls WorkPricingBuilding Audio Experiences UI Kit Core SDK

RealtimeKit supports voice calls, allowing you to build audio-only experiences such as audio rooms, support lines, or community hangouts. In these meetings, participants use their microphones and hear others, but cannot use their camera. Voice meetings reduce bandwidth requirements and focus on audio communication.

## How Audio Calls Work

A participant’s meeting experience is determined by the **Preset** applied to that participant. To run a voice meeting, ensure all participants join with a Preset that has meeting type set to `Voice`.

For details on Presets and how to configure them, refer to [Preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).

## Pricing

When a participant joins with a `Voice` meeting type Preset, they are considered an **Audio-Only Participant** for billing. This is different from the billing for Audio/Video Participants.

For detailed pricing information, refer to [Pricing](https://developers.cloudflare.com/realtime/realtimekit/pricing/).

## Building Audio Experiences

You can build voice meeting experiences using either the UI Kit or the Core SDK.

### UI Kit

UI Kit provides a pre-built meeting experience with customization options.

When participants join with a `Voice` meeting type Preset, UI Kit automatically renders a voice-only interface. You can use the default meeting UI or build your own UI using UI Kit components.

To get started, refer to [Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/).

### Core SDK

Core SDK provides full control to build custom audio-only interfaces. Video-related APIs are non-functional for participants with `Voice` type Presets.

To get started, refer to [Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/).

[PreviousSet up a webinar](https://developers.cloudflare.com/realtime/realtimekit/webinar/)[NextOverview](https://developers.cloudflare.com/realtime/realtimekit/ai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/audio-calls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
