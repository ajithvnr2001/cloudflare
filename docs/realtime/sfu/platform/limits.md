---
url: https://developers.cloudflare.com/realtime/sfu/platform/limits/
title: Limits, timeouts, and quotas \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:37.118270+00:00
---

# Limits, timeouts, and quotas · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)

  4. /[Platform](https://developers.cloudflare.com/realtime/sfu/platform/)
  5. /Limits, timeouts, and quotas



# Limits, timeouts, and quotas

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAPI and resource limitsInactivity timeoutPeerConnection requirementsAdapter recoverySupported codecsUsage allowance

These limits apply to Realtime SFU resources. Application limits such as room admission or a device's viewer cap are separate policies.

## API and resource limits

The API limits are:

Resource or operation | Limit  
---|---  
API requests per session | 50 requests per second. The rate limit is per session rather than per app  
Tracks added in one API request | Up to 64  
Tracks in a session | No fixed upper bound. Endpoint and connection capacity impose practical limits  
WebSocket adapters created or closed in one request | One to four track entries  
Reply access to a publisher DataChannel | At most one subscriber with `canReply`  
WebSocket audio ingest message | 32 KB including serialized packet overhead  
  
Distribute larger track batches across multiple calls and serialize mutations on each session. Inspect per-item results before retrying a partially successful batch.

## Inactivity timeout

Apply each timeout to its resource and condition:

Condition | Timeout | Result  
---|---|---  
A media track receives no incoming media packets | 30 seconds | The track is garbage-collected. Restore an expired publication and rebuild its subscriptions.  
A session loses WebRTC connectivity | 30-second session/track reuse window | Reuse requires a viable connection and resources. Replace failed or closed connections immediately, or reconnect with a new session after the window.  
A remote DataChannel uses `waitForAck: true` | First subscriber message within 30 seconds of allocation | Without it, the gated channel closes. Create a new subscription. Refer to [subscriber readiness](https://developers.cloudflare.com/realtime/sfu/features/datachannels/#wait-for-subscriber-readiness-waitforack).  
  
For expiry before a session's first connection, follow [session setup guidance](https://developers.cloudflare.com/realtime/sfu/concepts/sessions-tracks/#session-setup). The media inactivity timeout does not define the lifetime of a connected session without media or a DataChannel-only connection. Close resources when finished.

Application heartbeat expiry does not mean WebRTC disconnected. Media that keeps arriving does not meet the inactivity condition. Use [close results](https://developers.cloudflare.com/realtime/sfu/observability/error-codes/#interpret-close-results) and [recovery guidance](https://developers.cloudflare.com/realtime/sfu/concepts/negotiation/#retry-and-reconnect) to decide whether cleanup is complete or a resource can be reused.

## PeerConnection requirements

Operations that require an established transport wait up to five seconds for connectivity before timing out. Complete initial transport negotiation before those operations. The [connection recipes](https://developers.cloudflare.com/realtime/sfu/get-started/connection-patterns/) show where to apply SDP and wait for connectivity.

## Adapter recovery

For WebRTC-to-WebSocket streaming, the SFU retries the same endpoint for up to 15 seconds after a temporary disconnect. An exhausted reconnect window closes the adapter. Ingest adapters do not automatically reconnect.

Refer to [WebSocket adapter reconnect](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming) for buffering, delivery behavior, and application recovery.

## Supported codecs

Realtime SFU supports these media-track codecs:

Media | Codecs  
---|---  
Video | H.264, H.265, VP8, VP9, AV1  
Audio | Opus, G.711 A-law, G.711 µ-law  
  
Endpoint support varies by WebRTC implementation. WebSocket adapters have their own [format and direction constraints](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#supported-media-and-directions), including PCM audio and JPEG video output.

## Usage allowance

Refer to [pricing](https://developers.cloudflare.com/realtime/sfu/platform/pricing/) for egress charging and the shared monthly free tier.

[PreviousPricing](https://developers.cloudflare.com/realtime/sfu/platform/pricing/)[NextChangelog](https://developers.cloudflare.com/realtime/sfu/platform/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
