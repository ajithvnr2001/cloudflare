---
url: https://developers.cloudflare.com/changelog/product/realtime/
title: Realtime Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:48.934303+00:00
---

# Realtime Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/realtime/

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

Sep 30, 2026

## [Realtime SFU WebSocket adapter is generally available](https://developers.cloudflare.com/changelog/post/2026-09-30-websocket-adapter-ga/)

[Realtime](https://developers.cloudflare.com/realtime/)

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

Aug 13, 2026

## [Control Realtime SFU DataChannel delivery](https://developers.cloudflare.com/changelog/post/2026-08-13-datachannels-reliability-ordering/)

[Realtime](https://developers.cloudflare.com/realtime/)

[Cloudflare Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) is a [WebRTC selective forwarding unit](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/) that runs on Cloudflare's global network. It forwards audio, video, and application data between WebRTC clients without requiring you to manage SFU infrastructure or regions.

[DataChannels](https://developers.cloudflare.com/realtime/sfu/features/datachannels/) are WebRTC channels for application messages. A client publishes a named DataChannel to Realtime SFU, and the SFU forwards its messages to every client that subscribes to that channel. Use DataChannels for low-latency payloads such as chat messages, game state, sensor updates, and control events.

#### What changed

Realtime SFU DataChannels now support unordered and partially reliable delivery. DataChannels remain reliable and ordered by default, so existing channels keep their current behavior.

With ordered delivery, a delayed message can block later messages. For game state or sensor updates, recent data may be more useful than recovering an older message. Unordered delivery lets later messages proceed, while partial reliability limits retransmission attempts or the transport's retry window.

#### Choose delivery behavior

Delivery settings answer two questions: whether newer messages can bypass a delayed message, and when the transport should stop retrying delivery.

The publisher chooses one policy for each named channel. Every subscriber mirrors it. Use separate named channels for different policies, such as reliable commands and unreliable pointer updates:

Goal | Settings | Use when  
---|---|---  
Reliable, ordered delivery (default) | Omit `ordered`, `maxRetransmits`, and `maxPacketLifeTime` | Messages remain useful and must arrive in order  
Reliable, unordered delivery | Set `ordered: false`; omit both retry fields | Messages remain useful, but later messages should not wait for earlier messages  
No retries or ordering | Set `ordered: false` and `maxRetransmits: 0` | The application tolerates message loss and discards out-of-date updates  
Limited retries | Set `maxRetransmits: <COUNT>` | Brief recovery is useful, but repeated retries are not  
Time-limited transport retries | Set `maxPacketLifeTime: <MILLISECONDS>` | Limit how long the transport attempts transmission and retransmission  
  
Omitted `ordered` means `true`; ordering is independent of retries. Set at most one of `maxRetransmits` and `maxPacketLifeTime`. Omit both for reliable delivery, whether ordered or unordered. Setting `maxRetransmits: 0` explicitly requests no retransmissions.

`maxPacketLifeTime` does not impose an end-to-end message-age deadline. Use application timestamps or sequence numbers to discard stale updates. Reliable delivery does not provide durable storage or confirm command execution.

#### Apply the policy end to end

Your application must supply the publisher's policy in every subscriber request and browser `createDataChannel()` call. Negotiated DataChannels do not communicate these settings to the browser automatically. Each endpoint uses its own allocated channel ID; `waitForAck` and `canReply` remain subscription-specific.

The shared policy applies to one named publication, so other channels in the same session or application can use different policies. Asymmetric reliability is outside the supported contract.

The following example configures unordered delivery with no retransmissions. It begins after you [establish a DataChannel transport on both sessions and complete any required SDP exchange](https://developers.cloudflare.com/realtime/sfu/features/datachannels/#set-up-a-datachannel). Run the API requests from your backend with `APP_ID`, `APP_TOKEN`, `PUBLISHER_SESSION_ID`, and `SUBSCRIBER_SESSION_ID` set in your environment.

  1. On the publisher session, create the local DataChannel:


    
    
    curl --request POST \
      --url "https://rtc.live.cloudflare.com/v1/apps/$APP_ID/sessions/$PUBLISHER_SESSION_ID/datachannels/new" \
      --header "Authorization: Bearer $APP_TOKEN" \
      --header "Content-Type: application/json" \
      --data @- <<EOF
    {
      "dataChannels": [
        {
          "location": "local",
          "dataChannelName": "player-state",
          "ordered": false,
          "maxRetransmits": 0
        }
      ]
    }
    EOF

  2. On each subscriber session, pull the remote DataChannel with the same delivery settings:


    
    
    curl --request POST \
      --url "https://rtc.live.cloudflare.com/v1/apps/$APP_ID/sessions/$SUBSCRIBER_SESSION_ID/datachannels/new" \
      --header "Authorization: Bearer $APP_TOKEN" \
      --header "Content-Type: application/json" \
      --data @- <<EOF
    {
      "dataChannels": [
        {
          "location": "remote",
          "sessionId": "$PUBLISHER_SESSION_ID",
          "dataChannelName": "player-state",
          "ordered": false,
          "maxRetransmits": 0
        }
      ]
    }
    EOF

  3. In the publisher and subscriber clients, create the negotiated browser DataChannel with the same settings. In this example, `pc` is the active `RTCPeerConnection`, and `channelId` is the ID returned by the corresponding API request:


    
    
    const channel = pc.createDataChannel("player-state", {
      negotiated: true,
      id: channelId,
      ordered: false,
      maxRetransmits: 0,
    });

#### Related documentation

  * [Realtime SFU overview](https://developers.cloudflare.com/realtime/sfu/)
  * [DataChannels](https://developers.cloudflare.com/realtime/sfu/features/datachannels/)
  * [Connection API](https://developers.cloudflare.com/realtime/sfu/api/)



Jun 8, 2026

## [Post-meeting transcriptions are now Generally Available in RealtimeKit](https://developers.cloudflare.com/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/)

[Realtime](https://developers.cloudflare.com/realtime/)

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/) lets you build products where people meet over live audio and video — such as HealthTech, EdTech, proctoring, and other real-time platforms — on Cloudflare's [global WebRTC infrastructure](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/).

[Post-meeting transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#post-meeting-transcription) is now Generally Available, so completed RealtimeKit meetings can automatically produce full transcript files after they end. Those transcripts can also power [AI-generated summaries](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/) for meeting notes, review workflows, and follow-up tasks after the transcript is available.

Post-meeting transcription is a managed service powered by [Workers AI](https://developers.cloudflare.com/workers-ai/) using [Whisper Large v3 Turbo](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/). RealtimeKit handles transcription processing and can return transcript and summary files through [webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/) or the REST API, so you do not need to run your own transcription infrastructure.

#### Generate transcripts and summaries

To generate a transcript after a meeting ends, set `transcribe_on_end: true` when [creating a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/). To also generate an AI summary automatically after the transcript is available, set `summarize_on_end: true`:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "title": "Weekly product review",
        "transcribe_on_end": true,
        "summarize_on_end": true,
        "ai_config": {
          "transcription": {
            "language": "en"
          },
          "summarization": {
            "word_limit": 500,
            "text_format": "markdown",
            "summary_type": "team_meeting"
          }
        }
      }'

#### Consume results

When RealtimeKit finishes processing a meeting, it creates download URLs for the transcript and, if `summarize_on_end` is set, the summary. You can receive those URLs automatically with [webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/), or fetch them later for a specific session with the [REST API](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/#rest-api).

To receive results as soon as they are ready, configure the `meeting.transcript` and `meeting.summary` webhook events:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "AI results webhook",
        "url": "https://example.com/webhook",
        "events": ["meeting.transcript", "meeting.summary"],
        "enabled": true
      }'

To fetch results later, call the [transcript](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/) or [summary](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/) endpoint for the session:
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Use the [Generate summary of transcripts for the session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/) API only if `summarize_on_end` was not set and you want to generate a summary manually after the transcript is available:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Post-meeting transcription supports [CSV, JSON, SRT, and VTT transcript outputs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#output-formats), [automatic language detection and Whisper language codes](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#post-meeting-supported-languages). RealtimeKit also supports [real-time transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#real-time-transcription) with [Deepgram Nova-3](https://developers.cloudflare.com/workers-ai/models/nova-3/) for live captions, in-meeting accessibility, and real-time note-taking.

Learn more in the [RealtimeKit transcription docs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) and [summary docs](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/).

May 29, 2026

## [Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media](https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/)

[Realtime](https://developers.cloudflare.com/realtime/)

[Cloudflare Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) is a [WebRTC Selective Forwarding Unit that runs on Cloudflare's global network](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/), so you can route live audio, video, and data between WebRTC clients around the world without managing SFU infrastructure or regions.

When you use the [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/) to stream WebRTC media to a WebSocket endpoint, the adapter now auto-reconnects and buffers audio and video after brief endpoint disconnects or restarts.

#### Streaming WebRTC media to WebSocket endpoints

Many teams also use Realtime SFU as the media layer for backend applications, such as transcription, recording, note-taking, and agentic media-processing services. These systems often need to consume live WebRTC audio or video from the SFU in backend infrastructure, including [Durable Objects](https://developers.cloudflare.com/durable-objects/), [Workers](https://developers.cloudflare.com/workers/), [Containers](https://developers.cloudflare.com/containers/), or external services, without running a WebRTC client themselves.

The [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/) bridges that gap by streaming WebRTC media from the SFU to a standard WebSocket endpoint as application-consumable payloads: [PCM audio frames and JPEG video frames](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#media-formats).

#### What changed

When you use the WebSocket adapter in [Stream mode (egress)](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#stream-mode-egress) to send live audio or video from the SFU to your own WebSocket endpoint, the SFU now [automatically reconnects](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming) after brief endpoint disconnects or restarts. This is especially helpful for long-running media pipelines where the WebSocket endpoint may briefly restart while a recording, transcription, or live analysis job is still in progress.

Previously, a brief disconnect from your WebSocket endpoint could close the adapter and require your application to recreate it before media could resume. Now, the SFU retries the same endpoint for up to 5 seconds with no API change required. If the endpoint comes back within that window, audio and video delivery resumes automatically.

The reconnect behavior also includes [live-first media buffering](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#media-buffering-during-reconnect), so brief interruptions reduce media loss without replaying stale video.

#### Reconnect behavior

During reconnect:

  * Audio uses a short bounded backlog to reduce audible loss. If the interruption lasts longer than the backlog can cover, older audio may be dropped.
  * Video resumes from the [latest available JPEG frame](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#video-jpeg) instead of replaying stale frames.
  * Recovery is best effort and does not guarantee gapless or exactly-once delivery.



If the endpoint remains unavailable after the 5-second reconnect window, the adapter closes and must be recreated.

#### Learn more

  * [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/)
  * [Automatic reconnection for streaming](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming)
  * [Get started with Realtime SFU](https://developers.cloudflare.com/realtime/sfu/get-started/)
  * [Realtime SFU example architecture](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/)
  * [Realtime vs Regular SFUs](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/)
  * [Global SFU Network Visualization ↗︎](https://realtime-sfu.dev-demos.workers.dev/)



May 28, 2026

## [Record specific participant audio tracks in RealtimeKit](https://developers.cloudflare.com/changelog/post/2026-05-28-realtimekit-track-recording/)

[Realtime](https://developers.cloudflare.com/realtime/)

You can now record specific participant audio tracks in RealtimeKit with [track recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/). Track recording creates separate WebM files for each participant instead of a single composite recording, which is useful for post-processing, transcription, and regulated or content-sensitive workflows.

To record specific participants, pass `user_ids` when starting a track recording:
    
    
    curl --request POST \
      --url https://api.cloudflare.com/client/v4/accounts/<account_id>/realtime/kit/<app_id>/recordings/track \
      --header 'Authorization: Bearer <api_token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "meeting_id": "97440c6a-140b-40a9-9499-b23fd7a3868a",
      "user_ids": ["user-123", "user-456"]
    }'

To pass `user_ids` for selective track recording, use the following minimum SDK versions:

  * Web Core: `@cloudflare/realtimekit` version `1.4.0` or later
  * Web UI Kit: `@cloudflare/realtimekit-ui`, `@cloudflare/realtimekit-react-ui`, or `@cloudflare/realtimekit-angular-ui` version `1.1.2` or later
  * Android Core or iOS Core: version `2.0.0` or later
  * Android UI Kit or iOS UI Kit: version `1.1.0` or later



[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/) provides SDKs and UI components so that you can build your own meeting experience on Cloudflare's [global WebRTC infrastructure](https://developers.cloudflare.com/realtime/#realtime-sfu). Teams today build products ranging from telehealth to education on RealtimeKit for global audiences. You can get started today with our [Quickstart](https://developers.cloudflare.com/realtime/realtimekit/quickstart/) or take a look at our [Cloudflare Meet repo ↗︎](https://github.com/cloudflare/meet) as a reference.

Mar 6, 2026

## [Real-time transcription in RealtimeKit now supports 10 languages with regional variants](https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)[Realtime](https://developers.cloudflare.com/realtime/)

[Real-time transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) in RealtimeKit now supports 10 languages with regional variants, powered by [Deepgram Nova-3](https://developers.cloudflare.com/workers-ai/models/nova-3/) running on [Workers AI](https://developers.cloudflare.com/workers-ai/).

During a meeting, participant audio is routed through [AI Gateway](https://developers.cloudflare.com/ai-gateway/) to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.

Set the language when [creating a meeting](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/) via `ai_config.transcription.language`:
    
    
    {
    	"ai_config": {
    		"transcription": {
    			"language": "fr"
    		}
    	}
    }

Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like `en-AU`, `en-GB`, `en-IN`, `en-NZ`, `es-419`, `fr-CA`, `de-CH`, `pt-BR`, and `pt-PT`. Use `multi` for automatic multilingual detection.

If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.

  * [Transcription docs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)
  * [Nova-3 model page](https://developers.cloudflare.com/workers-ai/models/nova-3/)
  * [Workers AI](https://developers.cloudflare.com/workers-ai/)
  * [AI Gateway](https://developers.cloudflare.com/ai-gateway/)


