---
url: https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/
title: What is HLS? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:02.506205+00:00
---

# What is HLS? | Learning Center

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is HLS? 

HTTP Live Streaming (HLS) is a widely used protocol for delivering video content over the Internet using standard HTTP. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define HLS 
  * Understand how HLS works 
  * Compare HLS with other streaming protocols 



Related content  [ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)

On this page

  * What is HTTP live streaming?

  * What is streaming?

  * What is HTTP?

  * How does HLS work?

  * What is adaptive bitrate streaming in HLS?

  * Does HLS use TCP or UDP as its transport protocol?

  * What other protocols are commonly used for streaming?

  * Does Cloudflare support HTTP live streaming?




## What is HTTP live streaming (HLS)?

HTTP live streaming (HLS) is one of the most widely used video [streaming](https://www.cloudflare.com/learning/performance/what-is-streaming/) protocols. Although it is called HTTP "live" streaming, it is used for both on-demand streaming and [live streaming](https://www.cloudflare.com/learning/video/what-is-live-streaming/). HLS breaks down video files into smaller downloadable HTTP files and delivers them using the [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) protocol. [Client](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) devices load these HTTP files and then play them back as video.

One advantage of HLS is that all Internet-connected devices support HTTP, making it simpler to implement than streaming protocols that require the use of specialized servers. Another advantage is that an HLS stream can increase or decrease video quality depending on network conditions without interrupting playback. This is why video quality may get better or worse in the middle of a video as a user is watching it. This feature is known as "adaptive bitrate video delivery" or "[adaptive bitrate streaming](https://www.cloudflare.com/learning/video/what-is-adaptive-bitrate-streaming/)," and without it, slow network conditions can stop a video from playing altogether.

HLS was developed by Apple for use on Apple products, but it is now used across a wide range of devices.

## What is streaming?

Streaming is a way of delivering visual and audio media to users over the Internet. It works by continually sending the media file to a user's device a little bit at a time instead of all at once. The original media file is stored remotely, or, in the case of live streaming, created in real-time with a remote camera or microphone. This way, the video or audio can play without the user's device downloading the entire file first.

## What is HTTP?

HTTP is an [application layer](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) protocol for transferring information between devices connected to a network. Every website and application accessible by regular users runs on HTTP. Data transfer over HTTP is typically based on requests and responses. Almost all HTTP messages are either a request or a response to a request.

With streaming over HTTP, the standard request-response pattern does not apply. The connection between client and server remains open for the duration of the stream, and the server pushes video data to the client so that the client does not have to request every segment of video data.

## How does HLS work?

**Server:** An HLS stream originates from a server where (in on-demand streaming) the media file is stored, or where (in live streaming) the stream is created. Because HLS is based on HTTP, any ordinary web server can originate the stream.

Two main processes take place on the server:

  1. **Encoding:** The video data is reformatted so that any device can recognize and interpret the data. HLS must use [H.264](https://www.cloudflare.com/learning/video/what-is-h264-avc/) or H.265 encoding.
  2. **Segmenting:** The video is divided up into segments a few seconds in length. The length of the segments can vary, although the default length is 6 seconds (until 2016 it was 10 seconds). 
     * In addition to dividing the video into segments, HLS creates an index file of the video segments to record the order they belong in.
     * HLS will also create several duplicate sets of segments at different quality levels: 480p, 720p, 1080p, and so on.



**Distribution:** The encoded video segments are pushed out to client devices over the Internet when client devices request the stream. Typically, a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) will help distribute the stream to geographically diverse areas. A CDN will also cache the stream to [serve it to clients even more quickly.](https://www.cloudflare.com/developer-platform/solutions/live-streaming/)

**Client device:** The client device is the device that receives the stream and plays the video – for instance, a user smartphone or laptop. The client device uses the index file as a reference for assembling the video in order, and it switches from higher quality to lower quality picture (and vice versa) as needed.

## What is adaptive bitrate streaming in HLS?

One of the advantages HLS has over some other streaming protocols is adaptive bitrate streaming. This refers to the ability to adjust video quality in the middle of a stream as network conditions change. This ability allows videos to keep playing even if network conditions get worse; conversely, it also maximizes video quality to be as high as the network can support.

If the network slows down, the user's video player detects this, and adaptive bitrate streaming lowers the quality of the stream so that the video does not stop playing. If more network bandwidth becomes available, adaptive bitrate streaming improves the quality of the stream.

Adaptive bitrate streaming is possible because HLS creates several duplicate segmented streams at different quality levels during the segmentation process. The user's video player can switch from one of those streams to another one during video playback.

## Does HLS use TCP or UDP as its transport protocol?

[TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) and [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) are transport protocols, meaning they are responsible for delivering content over the Internet. TCP tends to deliver data more reliably than UDP, but the latter is much faster, even though some data may be lost in transit.

Because UDP is faster, some streaming protocols use UDP instead of TCP. HLS, however, uses TCP. This is for several reasons:

  1. HLS is over HTTP, and the HTTP protocol is built for use with TCP ([with some exceptions](https://blog.cloudflare.com/http3-the-past-present-and-future/)).
  2. The modern Internet is more reliable and more efficient than it was when streaming was first developed. In many parts of the world today, user connectivity has vastly improved, especially for mobile connections. As a result, users have enough bandwidth to support the delivery of every video frame.
  3. Adaptive bitrate streaming helps compensate for the potentially slower data delivery of TCP.
  4. HLS streaming does not need to be "real time," as is the case with videoconferencing connections. A few extra seconds of lag does not impact the user experience as much as missing video frames would.



## What other protocols are commonly used for streaming?

There are a number of similar protocols to HLS, like [MPEG-DASH](https://www.cloudflare.com/learning/video/what-is-mpeg-dash/) and [HDS](https://www.cloudflare.com/learning/video/what-is-http-dynamic-streaming/), that also run over HTTP and offer adaptive bitrate streaming. Adobe Flash, which ran on RTMP or HDS, used to be the main technology used for video streaming; however, many browsers no longer support Flash. RTMP is still in use, although support for it is declining.

## Does Cloudflare support HTTP live streaming?

Cloudflare supports HLS for both on-demand and live streaming. Cloudflare Stream integrates video storage, encoding, and a customizable player with the fast, secure, and reliable Cloudflare network, which spans 335+ cities in over 120+ countries. This enables users around the world to receive fast, high-quality HLS streams. [Learn more about Cloudflare Stream](https://www.cloudflare.com/developer-platform/products/cloudflare-stream/).
