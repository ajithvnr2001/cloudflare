---
url: https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/
title: What Is MPEG-DASH? | HLS vs. DASH
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:06.689588+00:00
---

# What Is MPEG-DASH? | HLS vs. DASH

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is MPEG-DASH? | HLS vs. DASH 

MPEG-DASH is a technique for streaming video over the Internet. MPEG-DASH uses HTTP and can run on any web server. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn how the MPEG-DASH video streaming technique works 
  * Compare and contrast MPEG-DASH with HLS 
  * Explore the benefits of adaptive bitrate streaming 



Related content  [ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)[ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[ How does live stream encoding work? | Video encoding ](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[ What is live streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[ MOV vs. MP4 | Video file formats ](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)

On this page

  * What is MPEG-DASH?

  * What is HTTP?

  * How does MPEG-DASH work?

  * What is adaptive bitrate streaming?

  * HLS vs. DASH: What are the main differences?

  * Does Cloudflare support MPEG-DASH?




## What is MPEG-DASH?

[Streaming](https://www.cloudflare.com/learning/performance/what-is-streaming/) is a way of delivering data over the Internet so that a device can start displaying the data before it fully loads. Video is streamed over the Internet so that the [client](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) device does not have to download the entire video file before playing it.

MPEG-DASH is a streaming method. DASH stands for "Dynamic Adaptive Streaming over [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)." Because it is based on HTTP, any [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) can be set up to serve MPEG-DASH streams.

MPEG-DASH is similar to [HLS](https://www.cloudflare.com/learning/video/what-is-http-live-streaming/), another streaming protocol, in that it breaks videos down into smaller chunks and [encodes](https://www.cloudflare.com/learning/video/live-stream-encoding/) those chunks at different quality levels. This makes it possible to stream videos at different quality levels, and to switch in the middle of a video from one quality level to another one.

## What is HTTP?

HTTP is a [layer 7](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) protocol for communicating over the Internet. Web applications use HTTP to send data back and forth in a way that devices at both ends will be able to interpret; this is sort of like two people from different parts of the world using a common language to communicate.

MPEG-DASH uses HTTP, which is an advantage because most of the Internet already uses HTTP. With HTTP, the stream goes to a standard port (port 80 or 443) that is almost always open. This ensures that the stream is rarely blocked by a [firewall](https://www.cloudflare.com/learning/security/what-is-a-firewall/), which can block streaming protocols that use specialized or unusual ports.

## How does MPEG-DASH work?

The main steps in the MPEG-DASH streaming process are:

  * **Encoding and segmentation:** The origin server divides the video file into smaller segments a few seconds in length. The server also creates an index file – like a table of contents for the video segments. Then the segments are encoded, meaning formatted in a way that multiple devices can interpret. MPEG-DASH allows the use of any encoding standard.

  * **Delivery:** When users start watching the stream, the encoded video segments are pushed out to client devices over the Internet. In almost all cases, a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) helps distribute the stream more efficiently.

  * **Decoding and playback:** As a user's device receives the streamed data, it decodes the data and plays back the video. The video player automatically switches to a lower or higher quality picture in order to adjust to network conditions – for example, if the user currently has very little bandwidth, the video will play at a lower quality level that uses less bandwidth.




## What is adaptive bitrate streaming?

[Adaptive bitrate streaming](https://www.cloudflare.com/learning/video/what-is-adaptive-bitrate-streaming/) is the ability to adjust video quality in the middle of a stream as network conditions change. Several streaming protocols, including MPEG-DASH, HLS, and HDS, allow for adaptive bitrate streaming.

Adaptive bitrate streaming is possible because the origin server encodes video segments at several different quality levels. This happens during the encoding and segmentation processes. A video player can switch from one quality level to another one in the middle of the video without interrupting playback. This prevents the video from stopping altogether if network bandwidth is suddenly reduced.

## HLS vs. DASH: What are the main differences?

HLS is another streaming protocol in wide use today. MPEG-DASH and HLS are similar in a number of ways. Both protocols run over HTTP, use [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) as their transport protocol, break video into segments with an accompanying index file, and offer adaptive bitrate streaming.

However, several key differences distinguish the two protocols:

**Encoding formats:** MPEG-DASH allows the use of any encoding standard. HLS, on the other hand, requires the use of [H.264](https://www.cloudflare.com/learning/video/what-is-h264-avc/) or H.265.

**Device support:** HLS is the only format supported by Apple devices. iPhones, MacBooks, and other Apple products cannot play video delivered over MPEG-DASH.

**Segment length:** This was a larger difference between the protocols before 2016, when the default segment length for HLS was 10 seconds. Today the default length for HLS is 6 seconds, although it can be adjusted from the default. MPEG-DASH segments are usually between 2 and 10 seconds in length, although the optimum length is 2-4 seconds.

**Standardization:** MPEG-DASH is an international standard. HLS was developed by Apple and has not been published as an international standard, even though it has wide support.

## Does Cloudflare support MPEG-DASH?

Cloudflare video streaming products support MPEG-DASH, along with other streaming standards. The main Cloudflare products for video streaming are [Cloudflare Stream](https://www.cloudflare.com/products/cloudflare-stream/) and [Cloudflare Stream Delivery](https://www.cloudflare.com/products/stream-delivery/).

Cloudflare Stream is an on-demand video streaming platform that integrates video storage, encoding, and a customizable player with the [Cloudflare global network](https://www.cloudflare.com/network/). Cloudflare Stream Delivery caches and accelerates video streams that are not stored on the Cloudflare network.

[Learn more about video streaming.](https://www.cloudflare.com/learning/video/what-is-live-streaming/)
