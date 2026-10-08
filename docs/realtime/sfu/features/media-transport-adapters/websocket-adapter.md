---
url: https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/
title: WebSocket adapter \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:36.127413+00:00
---

# WebSocket adapter · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)[Features](https://developers.cloudflare.com/realtime/sfu/features/)

  4. /[Media transport adapters](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/)
  5. /WebSocket



# WebSocket adapter

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported media and directionsPrepare your endpointMedia formats WebSocket binary format Audio ingest packets (buffer mode) Media egress packets (stream mode)Create adapter Send audio into the SFU Send audio or video to your servicePartial batch resultsClose adapterAutomatic reconnection for streaming Media buffering during reconnectTroubleshootingUsage and pricingLearn with an example

The WebSocket adapter connects an SFU media track to your service without requiring it to implement WebRTC. Use it to send or receive audio, or receive video as JPEG frames.

The WebSocket adapter is generally available. Each adapter connects one SFU track to your service in one direction.

## Supported media and directions

Choose whether your service sends audio into the SFU or receives an existing publication:

Direction and API location | Path | Media  
---|---|---  
Audio into the SFU (`location: "local"`) | WebSocket service → SFU → WebRTC | 48 kHz stereo PCM input, published as Opus audio  
Media out of the SFU (`location: "remote"`) | WebRTC → SFU → WebSocket service | Opus audio decoded to 48 kHz stereo PCM, or video as JPEG  
  
The API uses buffer mode for audio ingest and stream mode for media egress. For bidirectional audio, create one adapter for each direction. Video ingest is not supported.

JPEG egress defaults to 1 frame per second (FPS). Customers with an Enterprise contract can contact their Cloudflare account team to discuss higher frame rates for their use case.

## Prepare your endpoint

Your service hosts the WebSocket endpoint. The SFU connects to it for both ingest and egress.

Set `endpoint` to a publicly reachable `wss://` URL that accepts WebSocket upgrades and the binary packet format. A localhost endpoint is not reachable from the SFU, and the adapter does not follow HTTP redirects.

The SFU API App Secret belongs on your backend. Authentication for your WebSocket service is a separate boundary. Adapter requests do not support custom WebSocket headers. A scoped token in the endpoint URL's path or query string is one way for your service to authenticate the connection.

Keep endpoint tokens out of browser responses and logs. For media-egress recovery (stream mode), the same endpoint URL is reused. Its credential must remain valid for the reconnect attempts; consuming it permanently at the first handshake prevents that recovery.

## Media formats

### WebSocket binary format

Each binary WebSocket message contains a Protocol Buffers packet:
    
    
    message Packet {
      uint32 sequenceNumber = 1;
      uint32 timestamp = 2;
      bytes payload = 5;
    }

PCM payloads use signed 16-bit little-endian samples at 48 kHz, stereo, with left and right samples interleaved. Video payloads contain complete JPEG images.

### Audio ingest packets (buffer mode)

Only `payload` is used for ingest. Send small, frequent audio chunks within the 32 KB serialized-message limit. Account for protobuf overhead when choosing a chunk size.

### Media egress packets (stream mode)

Audio messages contain PCM frames with timestamps and sequence numbers. Video messages contain JPEG frames with timestamps; a video sequence number may be unset. Each frame is a separate WebSocket message.

The JPEG path supports H.264, H.265, VP8, and VP9 WebRTC input. Refer to [supported SFU codecs](https://developers.cloudflare.com/realtime/sfu/platform/limits/#supported-codecs) for the broader media-track codec list.

## Create adapter

Your backend sends an authenticated JSON request to:
    
    
    POST https://rtc.live.cloudflare.com/v1/apps/{appId}/adapters/websocket/new

Include `Authorization: Bearer <APP_SECRET>` and `Content-Type: application/json`. Send one to four entries in `tracks`. The [OpenAPI schema](https://developers.cloudflare.com/realtime/static/realtime-api-2024-05-21.yaml) describes the complete contract.

Save the `adapterId` from every successful item so your backend can close it later.

### Send audio into the SFU

For audio ingest, use `location: "local"` to create a publication from your WebSocket service:
    
    
    {
    	"tracks": [
    		{
    			"location": "local",
    			"trackName": "generated-speech",
    			"endpoint": "wss://example.com/audio-source",
    			"inputCodec": "pcm"
    		}
    	]
    }

The required ingest fields are:

Field | Value  
---|---  
`location` | `"local"`  
`trackName` | Name for the new publication  
`endpoint` | WebSocket URL that supplies audio  
`inputCodec` | `"pcm"`  
  
Ingest uses buffer mode. The API selects the mode from `location`; a `mode` field does not change it. An ingest request's `sessionId` is ignored because the SFU allocates a publishing session.

A successful item includes the new session ID:
    
    
    {
    	"tracks": [
    		{
    			"trackName": "generated-speech",
    			"adapterId": "<ADAPTER_ID>",
    			"sessionId": "<PUBLISHER_SESSION_ID>",
    			"endpoint": "wss://example.com/audio-source"
    		}
    	]
    }

Your application shares the session ID and track name with authorized WebRTC subscribers. Subscribers can follow [Receive a published track](https://developers.cloudflare.com/realtime/sfu/get-started/connection-patterns/#receive-a-published-track) to play that audio. The WebSocket service sends protobuf packets containing PCM audio. Keep each serialized WebSocket message within 32 KB, including protobuf overhead.

### Send audio or video to your service

Start with an existing media publication. To create one, follow [Publish audio or video](https://developers.cloudflare.com/realtime/sfu/get-started/connection-patterns/#publish-audio-or-video).

For media egress, use `location: "remote"` to send that publication to your service:
    
    
    {
    	"tracks": [
    		{
    			"location": "remote",
    			"sessionId": "<PUBLISHER_SESSION_ID>",
    			"trackName": "microphone",
    			"endpoint": "wss://example.com/audio-consumer",
    			"outputCodec": "pcm"
    		}
    	]
    }

The required media-egress fields are:

Field | Value  
---|---  
`location` | `"remote"`  
`sessionId` | Session that owns the publication  
`trackName` | Name of the existing publication  
`endpoint` | WebSocket URL that receives media  
`outputCodec` | `"pcm"` for an Opus audio publication or `"jpeg"` for video  
  
Stream mode is selected automatically. PCM output requires an Opus source track. For JPEG output, use a video publication and set `outputCodec: "jpeg"`.

A successful media-egress item contains the adapter ID, track name, and endpoint. It does not return a new session ID:
    
    
    {
    	"tracks": [
    		{
    			"trackName": "microphone",
    			"adapterId": "<ADAPTER_ID>",
    			"endpoint": "wss://example.com/audio-consumer"
    		}
    	]
    }

## Partial batch results

Creation and closure return results for individual request entries. An HTTP `200` response means at least one entry succeeded. It can also contain failed entries:
    
    
    {
    	"tracks": [
    		{
    			"trackName": "microphone",
    			"adapterId": "<ADAPTER_ID>",
    			"endpoint": "wss://example.com/audio-consumer"
    		},
    		{
    			"trackName": "camera",
    			"errorCode": "websocket_handshake_failed",
    			"errorDescription": "The handshake with the provided endpoint failed."
    		}
    	]
    }

Inspect every item. Save successful allocations even if another item fails. Retrying an entire partially successful creation batch can allocate duplicate resources.

If every attempted item fails, the outer response is HTTP `503`. Item errors contain `errorCode` and `errorDescription`; their individual HTTP status codes are not included.

## Close adapter

Close is idempotent. You can safely repeat a close request, including for an adapter that is already closed.

Match each result to its requested `adapterId`. Retain failed or unreported items for retry with bounded backoff. The partial batch response rules apply.

Send one to four adapter IDs from your backend:
    
    
    POST https://rtc.live.cloudflare.com/v1/apps/{appId}/adapters/websocket/close
    
    
    {
    	"tracks": [
    		{ "adapterId": "<ADAPTER_ID_1>" },
    		{ "adapterId": "<ADAPTER_ID_2>" }
    	]
    }

Both closes in this HTTP `200` response succeeded. Neither item contains an `errorCode`:
    
    
    {
    	"tracks": [
    		{
    			"adapterId": "<ADAPTER_ID_1>",
    			"bytesProcessed": 83492
    		},
    		{
    			"adapterId": "<ADAPTER_ID_2>"
    		}
    	]
    }

`bytesProcessed` is omitted when unavailable, rather than reported as zero. It is an operational statistic, not the authoritative billed-usage total. Refer to usage and pricing.

## Automatic reconnection for streaming

For media egress (`location: "remote"`), the SFU retries the same endpoint for up to 15 seconds after a disconnect. No additional API setting is required.

If the reconnect window expires, the adapter closes. Create a new adapter to resume streaming.

Audio ingest (`location: "local"`) does not reconnect automatically. Recreate the adapter after a terminal disconnect. Share the returned `sessionId` and track name with authorized subscribers so they can [subscribe to the new publication](https://developers.cloudflare.com/realtime/sfu/get-started/connection-patterns/#receive-a-published-track).

### Media buffering during reconnect

Audio uses a short, bounded backlog. Older frames can be dropped when that backlog fills. Video retains only the latest available JPEG frame, replacing older buffered frames.

Recovery does not guarantee gapless or exactly-once delivery. It retries the same endpoint and does not provide failover to another URL.

## Troubleshooting

Use [Error codes](https://developers.cloudflare.com/realtime/sfu/observability/error-codes/) for request failures and [adapter errors](https://developers.cloudflare.com/realtime/sfu/observability/error-codes/#adapter-errors) for WebSocket connection and closure results. Inspect each item before deciding what to retry.

If the connection opens but media is missing, check the selected direction, source session and track, protobuf framing, PCM format, and message sizes. Record application resource IDs and connection transitions without recording endpoint tokens, SDP, or media contents.

## Usage and pricing

WebSocket adapter usage is tracked in Realtime billing. Egress to WebSocket endpoints follows Realtime pricing; audio ingested into the SFU is not charged as ingress. Refer to [pricing and the shared free tier](https://developers.cloudflare.com/realtime/sfu/platform/pricing/#websocket-adapter).

## Learn with an example

Follow the [AI audio guide](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/) for separate speech-generation and microphone-transcription paths. The [WebRTC-to-JPEG example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/video-to-jpeg) demonstrates a video publication delivered to a Worker as JPEG frames.

These examples require application authentication and authorization before public use. Their repository guides describe setup, lifecycle behavior, and limitations.

[PreviousMedia adapters](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/)[NextOverview](https://developers.cloudflare.com/realtime/sfu/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/features/media-transport-adapters/websocket-adapter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
