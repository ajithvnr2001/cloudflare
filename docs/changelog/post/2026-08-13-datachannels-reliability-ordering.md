---
url: https://developers.cloudflare.com/changelog/post/2026-08-13-datachannels-reliability-ordering/
title: Control Realtime SFU DataChannel delivery \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.084777+00:00
---

# Control Realtime SFU DataChannel delivery · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-13-datachannels-reliability-ordering/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 13, 2026

## Control Realtime SFU DataChannel delivery

[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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


