---
url: https://developers.cloudflare.com/changelog/product-group/media/
title: Media Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:36.989798+00:00
---

# Media Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/media/

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

Sep 23, 2026

## [View transformation analytics in Images](https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can now view account-level analytics for your Images transformation usage.

Go to **Images & Stream** > **Transformations** > **Analytics** to view sampled estimates of image transformation request traffic, including:

  * Requests by source, split between URL-based transformations and Images binding transformations
  * Top zones, transformation configurations, and origin hosts for URL-based requests
  * Top Worker scripts for Images binding requests



Use these analytics to identify the zones, configurations, origins, and Workers generating the most image transformation requests.

Sep 2, 2026

## [New in Images: text rasterization and updates to the binding](https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

We've added more ways to manage and manipulate images with the [Images binding](https://developers.cloudflare.com/images/optimization/binding/). Here's what's new:

**Render text into an image.** Output a string of text into its own image or draw it over another image.

  * Use the [`.text()`](https://developers.cloudflare.com/images/optimization/binding/#textcontent-options) method to rasterize text with the Images binding.
  * Style content using the `font`, `size`, and `color` options.
  * The [`draw`](https://developers.cloudflare.com/images/optimization/draw-overlays/#draw-with-cfimage) array in `cf.image` now accepts a `text` key.



**Manage hosted images without an API token.**

  * **Metadata filtering:** Pass `filter.metadata` to [`.list()`](https://developers.cloudflare.com/images/storage/binding/#listoptions) to return images by custom metadata. Match a bounded range by setting two operators in one condition, for example, `priority: { gte: 2, lte: 5 }`.
  * **Server-side signing:** Get a signed URL for a private image with [`.signedUrl()`](https://developers.cloudflare.com/images/storage/binding/#imageimageidsignedurloptions).
  * **User uploads:** Create a Direct Creator Upload link with [`.createDirectUpload()`](https://developers.cloudflare.com/images/storage/binding/#createdirectuploadoptions) so that a client can upload an image to your storage.



**Set headers in a single call.**

  * Pass a `headers` option to [`.response()`](https://developers.cloudflare.com/images/optimization/binding/#responseoptions) to set headers without rebuilding the `Response`.
  * `Content-Type` is always taken from the optimized image and can't be overridden by a specified header.
  * Set `Cache-Control` with [Workers Cache](https://developers.cloudflare.com/workers/cache/) to cache your optimized image at the edge.



For more information, refer to [Optimize with Workers](https://developers.cloudflare.com/images/optimization/binding/), [Draw overlays and watermarks](https://developers.cloudflare.com/images/optimization/draw-overlays/), and [Manage hosted images with Workers](https://developers.cloudflare.com/images/storage/binding/).

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

Jul 1, 2026

## [Images binding is now billed per unique transformation](https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

The [Images binding](https://developers.cloudflare.com/images/optimization/binding/) is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.

Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.

Calls to [`.info()`](https://developers.cloudflare.com/images/optimization/binding/#infostream) are no longer billed.

For more information, refer to [Images pricing](https://developers.cloudflare.com/images/pricing/#images-transformed) and the [Images binding documentation](https://developers.cloudflare.com/images/optimization/binding/).

Jun 16, 2026

## [New optimization features in Images](https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

These updates introduce new features for optimizing and manipulating with Images:

  * **New`composite` option:** Control how [overlays are blended](https://developers.cloudflare.com/images/optimization/draw-overlays/#composite) with the base image.
  * **Percentage widths:** Set the dimensions of an overlay as [a fraction of the dimensions](https://developers.cloudflare.com/images/optimization/draw-overlays/#width-and-height) of the base image.
  * **New`fit` modes:** Use [`aspect-crop`](https://developers.cloudflare.com/images/optimization/features/#aspect-crop) to always preserve the target aspect ratio or [`scale-up`](https://developers.cloudflare.com/images/optimization/features/#scale-up) to always enlarge images.
  * **New`upscale` parameter:** Apply [AI upscaling](https://developers.cloudflare.com/images/optimization/features/#upscale) to produce sharper, more detailed results when enlarging images.



Jun 10, 2026

## [Manage hosted images with the Images binding](https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.

The `env.IMAGES.hosted` namespace supports the following storage and management operations:

  * [`.upload(image, options)`](https://developers.cloudflare.com/images/storage/binding/#uploadimage-options) — Upload a new image to your account.
  * [`.list(options)`](https://developers.cloudflare.com/images/storage/binding/#listoptions) — List images with pagination.
  * [`.image(imageId).details()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddetails) — Get image metadata.
  * [`.image(imageId).bytes()`](https://developers.cloudflare.com/images/storage/binding/#imageimageidbytes) — Stream the original image bytes.
  * [`.image(imageId).update(options)`](https://developers.cloudflare.com/images/storage/binding/#imageimageidupdateoptions) — Update metadata or access controls.
  * [`.image(imageId).delete()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddelete) — Delete an image.



For example, you can upload an image from a request body and return its metadata:
    
    
    const image = await env.IMAGES.hosted.upload(request.body, {
    	filename: "upload.jpg",
    	metadata: { source: "worker" },
    });
    
    return Response.json(image);

Or retrieve and serve the original bytes of a hosted image:
    
    
    const bytes = await env.IMAGES.hosted.image("IMAGE_ID").bytes();
    return new Response(bytes);

For more information, refer to the [Images binding](https://developers.cloudflare.com/images/storage/binding/).

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

May 27, 2026

## [Transformation flows in Images](https://developers.cloudflare.com/changelog/post/2026-05-27-transformation-flows/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

![Custom flow configuration panel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1654,height=1398,format=webp/_astro/custom-flow.DeAGR8BY.png)

Flows are automated rules that pair conditions (such as file extension, URL path, or query parameter) with parameters. Set up a flow to automatically apply image optimization to matching requests on your zone without writing code or changing URLs.

There are two modes for transformation flows:

  * **[Provider flows](https://developers.cloudflare.com/images/optimization/transformations/flows/#set-up-a-provider-flow)** — Migrate from another image optimization service. Your existing URLs continue to work while Cloudflare rewrites provider-specific parameters to their Cloudflare equivalents. Currently, Cloudflare supports provider flows for Fastly Image Optimizer.
  * **[Custom flows](https://developers.cloudflare.com/images/optimization/transformations/flows/#set-up-a-custom-flow)** — Define your own conditions and actions for use cases like automatic format conversion, [responsive sizing](https://developers.cloudflare.com/images/optimization/make-responsive-images/#using-widthauto) with `width=auto`, or directory-based optimization.



To get started, go to **Images** > **Transformations** > **Automation** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/images/transformations).

Learn more about [transformation flows](https://developers.cloudflare.com/images/optimization/transformations/flows/).

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

Jul 8, 2025

## [HEIC support in Cloudflare Images](https://developers.cloudflare.com/changelog/post/heic-support/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can use Images to ingest HEIC images and serve them in supported output formats like AVIF, WebP, JPEG, and PNG.

When inputting a HEIC image, dimension and sizing limits may still apply. Refer to our documentation to see limits for [uploading to Images](https://developers.cloudflare.com/images/storage/upload-images/methods/) or [transforming a remote image](https://developers.cloudflare.com/images/optimization/transformations/overview/).

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

Feb 24, 2025

## [Bind the Images API to your Worker](https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can now [interact with the Images API](https://developers.cloudflare.com/images/optimization/binding/) directly in your Worker.

This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.

The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:
    
    
    {
    	"images": {
    		"binding": "IMAGES", // i.e. available in your Worker on env.IMAGES
    	},
    }
    
    
    [images]
    binding = "IMAGES"

Within your Worker code, you can interact with this binding by using `env.IMAGES`.

Here's how you can rotate, resize, and blur an image, then output the image as AVIF:
    
    
    const info = await env.IMAGES.info(stream);
    // stream contains a valid image, and width/height is available on the info object
    
    const response = (
    	await env.IMAGES.input(stream)
    		.transform({ rotate: 90 })
    		.transform({ width: 128 })
    		.transform({ blur: 20 })
    		.output({ format: "image/avif" })
    ).response();
    
    return response;

For more information, refer to [Images Bindings](https://developers.cloudflare.com/images/optimization/binding/).

Feb 14, 2025

## [Rewind, Replay, Resume: Introducing DVR for Stream Live](https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/)

[Stream](https://developers.cloudflare.com/stream/)

Previously, all viewers watched "the live edge," or the latest content of the broadcast, synchronously. If a viewer paused for more than a few seconds, the player would automatically "catch up" when playback started again. Seeking through the broadcast was only available once the recording was available after it concluded.

Starting today, customers can make a small adjustment to the player embed or manifest URL to enable the DVR experience for their viewers. By offering this feature as an opt-in adjustment, our customers are empowered to pick the best experiences for their applications.

When building a player embed code or manifest URL, just add `dvrEnabled=true` as a query parameter. There are some things to be aware of when using this option. For more information, refer to [DVR for Live](https://developers.cloudflare.com/stream/stream-live/dvr-for-live/).

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/media/2/)

[Next →](https://developers.cloudflare.com/changelog/product-group/media/2/)
