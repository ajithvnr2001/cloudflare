---
url: https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/
title: What is adaptive bitrate streaming?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:51.563880+00:00
---

# What is adaptive bitrate streaming?

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is adaptive bitrate streaming? 

Adaptive bitrate streaming adjusts video quality based on network conditions to improve video streaming over HTTP networks. This process makes playback as smooth as possible for viewers regardless of their device, location, or Internet speed. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what adaptive bitrate streaming is and how it works 
  * Explain which protocols support adaptive bitrate streaming 
  * Understand the benefits of adaptive bitrate streaming 



Related content  [ What is MPEG-DASH? | HLS vs. DASH ](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[ What is HDS streaming? | HLS vs. HDS ](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)[ How does live stream encoding work? | Video encoding ](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)

On this page

  * What is adaptive bitrate streaming?

  * How does adaptive bitrate streaming work?

  * What are the benefits of adaptive bitrate streaming?

  * What streaming protocols support adaptive bitrate streaming?

  * Does Cloudflare support adaptive bitrate streaming?




## What is adaptive bitrate streaming?

Adaptive bitrate streaming is a method for improving streaming over HTTP networks. The term “bitrate” refers to how quickly data travels across a network and is often used to describe an Internet connection’s speed. A high-speed connection is a high-bitrate connection. [Streaming](https://www.cloudflare.com/learning/video/what-is-streaming/) — or the process that makes watching videos online possible — consists of transmitting video files hosted in a remote server to a client. In streaming, videos are segmented into smaller clips so viewers do not need to wait for an entire video to load before they can begin watching it.

First, multiple versions of video files are created and encoded to fit a variety of network conditions. Then, based on factors like bandwidth and device type, the video player selects the highest-quality file that the device can play with the smallest amount of buffering possible. This allows playback to be as smooth as possible for end users around the world, regardless of their device or Internet speed.

Adaptive bitrate streaming works similarly to how a manager might assign work to a new employee. To help the employee acclimate, the manager will likely start off with fewer and/or simpler assignments. Once the employee successfully completes their introductory projects, the manager will begin to assign more complex tasks. As the employee settles into their role, the manager will continually adjust the employee’s workload to ensure they are learning but not overwhelmed.

Similarly, in adaptive bitrate streaming, the video player learns what video quality a connection can withstand. If the connection is struggling to play a video segment, the player will switch to a smaller file with lower quality for the next segment. A viewer may experience some changes in quality, but the video will continue to play.

## How does adaptive bitrate streaming work?

Adaptive bitrate streaming starts at the video encoding stage. [Encoding](https://www.cloudflare.com/learning/video/video-encoding-formats/) is the process in which uncompressed videos are converted into a form that can be stored and used on many devices. For adaptive bitrate streaming to work, different video files that support different bitrates must be created.

After encoding, the video is [segmented](https://developer.att.com/video-optimizer/docs/best-practices/adaptive-bitrate-video-streaming) into smaller files that are a few seconds in length. In most streaming setups, videos are transmitted in a series of segments, rather than an entire video file sent all at once. The segmentation process is particularly important because without it, video players would need to download the entire video file before the content could begin playing.

Moreover, segments are important to adaptive bitrate streaming because the adjustment process is triggered at the end of a video segment. If a viewer’s connection cannot download the video fast enough to stream without buffering, the video player will switch to a smaller file once the segment finishes.

When a video first starts playing, many video players will start by requesting the lowest bitrate file available. If the player determines that the client can handle a higher bitrate file, it will select higher bitrate files until it finds the highest one the client can handle. If the selected file is the ideal match for the connection, the player will continue to request segments at that bitrate unless the conditions change. This is known as the adaptive bitrate or [encoding “ladder](https://streaminglearningcenter.com/blogs/the-evolving-encoding-ladder-what-you-need-to-know.html).” The player moves up the ladder when the connection has enough bandwidth to accommodate higher bitrate videos and down the ladder when it decreases.

## What are the benefits of adaptive bitrate streaming?

As of 2021, [viewers stream one billion hours of YouTube video a day](https://www.oberlo.com/blog/youtube-statistics). Video content is an ever-growing channel for communication, advertising, education, and more. Thus, ensuring the quality of video playback matters. Adaptive bitrate streaming offers many benefits that can improve video quality:

  * **Widening access:** Without adaptive bitrate streaming, viewers with slower connections or certain devices would never be able to see some videos.

  * **Improving the user experience:** Adaptive bitrate streaming decreases buffering, so users experience fewer frustrating loading delays.

  * **Enabling mobile viewing with fewer interruptions:** [Streaming on mobile devices](https://www.dacast.com/blog/increase-viewership-live-streams) has increased by 1,000% since 2012, so optimizing for mobile streaming is critical. When a viewer streams mobile video content while moving from place to place, bitrate can vary widely on a single device. For example, connection strength on a home WiFi network may be stronger than a connection on a train or in a shopping mall. By continuously adjusting to changing conditions, adaptive bitrate streaming can minimize disruptions for mobile viewers.




## What streaming protocols support adaptive bitrate streaming?

Adaptive bitrate streaming is possible only with certain streaming protocols. A [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) is a set of standards that dictate how data is packaged and processed across networks. Streaming has its own set of protocols.

The three most popular streaming protocols that support adaptive bitrate streaming are [HTTP live streaming (HLS)](https://www.cloudflare.com/learning/video/what-is-http-live-streaming/), [Dynamic Adaptive Streaming over HTTP (DASH)](https://www.cloudflare.com/learning/video/what-is-mpeg-dash/), and [HTTP Dynamic Streaming (HDS)](https://www.cloudflare.com/learning/video/what-is-http-dynamic-streaming/).

All three follow the same basic process of encoding and segmenting videos before streaming. However, each protocol has its own encoding or file type requirements and is compatible with different devices. For example, some protocols require specific encoding formats, which are ways of optimizing video files for different platforms, programs, and devices.

  * **HLS:** HLS works for on-demand and [live streaming](https://www.cloudflare.com/learning/video/what-is-live-streaming/) and requires the [H.264](https://www.cloudflare.com/learning/video/what-is-h264-avc/) or H.265 encoding format. Unlike some protocols, HLS does not require the use of special servers. Originally, HLS was compatible only with Apple devices, but it is now device-agnostic. However, Apple devices accept only the HLS format.

  * **DASH:** DASH does not require any specific encoding standard. Additionally, any [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) can be set up to serve DASH streams because it runs over [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/). The DASH format, like all other formats besides HLS, does not work with Apple devices.

  * **HDS:** Originally designed to work with Adobe Flash (which has been discontinued), this format can be used for on-demand or [live streaming](https://www.cloudflare.com/developer-platform/solutions/live-streaming/) and works over HTTP connections The HDS format requires videos to be converted from [MP4](https://www.cloudflare.com/learning/video/what-is-mp4/) to F4F (fragmented MP4) and the H.264 encoding standard. Apple devices are the only devices that are incompatible with the HDS protocol.




## Does Cloudflare support adaptive bitrate streaming?

Cloudflare Stream is a video platform that operates within 100 milliseconds of 99% of the Internet-connected population in the developed world. It supports adaptive bitrate streaming and automatically encodes videos at multiple screen sizes and quality levels, supporting a variety of devices and bitrates. [Learn more about improving playback with Cloudflare Stream.](https://www.cloudflare.com/developer-platform/products/cloudflare-stream/)
