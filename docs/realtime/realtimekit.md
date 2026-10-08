---
url: https://developers.cloudflare.com/realtime/realtimekit/
title: Overview \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:52.032510+00:00
---

# Overview · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /RealtimeKit



# RealtimeKit

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat you can buildHow RealtimeKit fits into your appKey featuresChoose how to build RealtimeKit UI Kit RealtimeKit Core SDK

Cloudflare RealtimeKit lets you build your own audio and video experiences inside web and mobile apps. It routes media on [Cloudflare's global WebRTC infrastructure](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/), so you can deliver low-latency experiences to a global audience without scaling media servers or choosing regions.

Your application controls who can join and what they can do. RealtimeKit provides the SDKs and infrastructure that connect participants inside your web or mobile app.

[Get started](https://developers.cloudflare.com/realtime/realtimekit/quickstart/) [Try a demo meeting](https://examples.realtime.cloudflare.com/meeting?demo=Default) [View code examples](https://github.com/cloudflare/realtimekit-web-examples) [Run a pre-call test](https://test.realtime.cloudflare.com/)

## What you can build

### [Group video calls](https://developers.cloudflare.com/realtime/realtimekit/quickstart/)

Add multiparty calls to collaboration tools, customer portals, and online communities.

### [Virtual classrooms](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/)

Split a class into smaller discussion rooms and assign participants automatically or manually.

### [Webinars and live events](https://developers.cloudflare.com/realtime/realtimekit/webinar/)

Keep attendees view-only until a host grants them access to the stage.

### [Audio rooms and support calls](https://developers.cloudflare.com/realtime/realtimekit/audio-calls/)

Build voice-only sessions for support lines and community discussions.

## How RealtimeKit fits into your app

Your application owns users and workflows, while RealtimeKit manages sessions and media.

Your application

server

**Application backend** Owns users, scheduling, and business logic.

Participant auth token

client

**Web or mobile app** Uses prebuilt UI Kit components or integrates the Core SDK into a custom interface.

REST APICloudflare API token

SDK connectionRealtime media

RealtimeKit

management

**REST API** Creates Meetings, adds Participants, and returns participant auth tokens.

sessions + media

**Managed realtime network** Routes realtime media between participants.

Your backend creates Meetings and adds Participants through the RealtimeKit REST API, then passes participant auth tokens to the client SDK. RealtimeKit manages session state and routes realtime media between participants.

## Key features

[Participant roles and permissions](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/)

Give hosts, speakers, and attendees different permissions for media, moderation, and in-meeting features. Reuse the same presets across meetings.

Configure presets

[Recording and custom layouts](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)

Capture composite video or separate participant audio tracks. Store recordings in [your own Cloudflare R2 bucket](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/#cloudflare-r2), or deploy a [custom recording app](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/create-record-app-using-sdks/) on [Cloudflare Workers](https://developers.cloudflare.com/workers/) when you need a different layout.

Explore recording

[Transcription and summaries](https://developers.cloudflare.com/realtime/realtimekit/ai/)

RealtimeKit uses [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) for real-time and post-meeting transcription. Generate an AI summary when a meeting ends.

Add meeting AI

[In-meeting apps](https://developers.cloudflare.com/realtime/realtimekit/custom-plugins/)

Add your own browser-based, interactive apps such as whiteboard, document viewer into the meeting layout. Use [collaborative stores](https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/) to synchronize plugin state across participants.

Build a plugin

[Backend automation](https://developers.cloudflare.com/realtime/realtimekit/webhooks/)

Receive signed meeting, participant, and recording events in your backend. A [Cloudflare Worker](https://developers.cloudflare.com/workers/) can verify each callback and start post-meeting processing.

Handle lifecycle events

## Choose how to build

RealtimeKit gives you two ways to build the client experience. Choose based on how much of the interface you want to build yourself.

### RealtimeKit UI Kit

Use [RealtimeKit UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/) when you want prebuilt screens and controls for joining and running a call. It includes the setup screen, participant grid, media controls, chat, and polls. Use the default layout or customize individual components and branding.

RealtimeKit UI Kit includes RealtimeKit Core SDK, so you can use its APIs when prebuilt components don't cover your workflow.

### RealtimeKit Core SDK

Use [RealtimeKit Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) to build every screen and interaction yourself. It provides direct access to session, participant, and media state while RealtimeKit manages signaling and media routing.

Compare supported platforms and packages in [SDK selection](https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/).

[PreviousOverview](https://developers.cloudflare.com/realtime/)[NextQuickstart](https://developers.cloudflare.com/realtime/realtimekit/quickstart/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
