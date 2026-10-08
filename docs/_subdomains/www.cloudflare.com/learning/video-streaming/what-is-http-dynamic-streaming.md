---
url: https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/
title: What is HDS streaming? | HLS vs. HDS
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:02.338018+00:00
---

# What is HDS streaming? | HLS vs. HDS

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is HDS streaming? | HLS vs. HDS 

HTTP dynamic streaming (HDS) is a method for delivering video to end users over the Internet using HTTP. HDS is not as commonly used as other streaming protocols like HTTP live streaming (HLS). 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand how HTTP dynamic streaming (HDS) works 
  * Contrast HDS with HTTP live streaming (HLS) 
  * Explain why HDS has less widespread support than HLS 



Related content  [ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)[ What is MPEG-DASH? | HLS vs. DASH ](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[ What is a video CDN? ](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[ What is live streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)

On this page

  * What is HTTP dynamic streaming?

  * What was Adobe Flash Player?

  * How does HDS streaming work?

  * What is a manifest file?

  * What is adaptive bitrate streaming?

  * HLS vs. HDS: What is the difference?




## What is HTTP dynamic streaming (HDS)?

HTTP dynamic streaming, or HDS, is an [adaptive bitrate streaming](https://www.cloudflare.com/learning/video/what-is-adaptive-bitrate-streaming/) method developed by Adobe. HDS delivers MP4 video content over [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) connections. HDS can be used for on-demand [streaming](https://www.cloudflare.com/learning/video/what-is-streaming/) or [live streaming](https://www.cloudflare.com/learning/video/what-is-live-streaming/). Since they are delivered over HTTP, HDS streams can be cached — either by a content delivery network ([CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)) or another [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) server.

HDS was developed for use with Adobe Flash Player and Adobe AIR. Adobe Flash Player has been discontinued, and an outside firm now supports AIR instead of Adobe. HDS is not supported by Apple devices.

## What was Adobe Flash Player?

Adobe Flash Player was a browser plugin for playing video content. For many years, the Flash plugin was the most widespread way to embed video into webpages. However, after the release of the [HTML5 video element](https://www.cloudflare.com/learning/video/how-html5-video-works/), Flash was no longer the main option for embedded video. In addition, Flash had many security vulnerabilities that made it dangerous. (For instance, several Flash vulnerabilities allowed attackers to execute any code they wanted in someone's browser.)

Browsers and operating systems gradually dropped support for Flash over the years to avoid security incidents. Finally, Adobe stopped supporting Flash Player on December 31, 2020.

## How does HDS streaming work?

The process of creating and delivering an HDS stream is roughly:

**Server:** Before video files can be streamed via HDS, they must be converted from regular MP4 to the F4F (fragmented MP4) file format. F4F video files contain audio, video, and metadata. Because the files are "fragmented," these three elements can be stored separately from each other.

HDS videos are encoded with [H.264](https://www.cloudflare.com/learning/video/what-is-h264-avc/), which is a common [encoding](https://www.cloudflare.com/learning/video/video-encoding-formats/) standard. Like many other streaming technologies, HDS encodes versions of the video file at multiple quality levels and divides videos into shorter segments a few seconds in length. This makes adaptive bitrate streaming possible (learn more below).

**Distribution:** HDS video segments are pushed out to client devices that request the stream over the Internet. A CDN usually helps distribute the stream, along with caching the stream to [serve it more quickly.](https://www.cloudflare.com/developer-platform/solutions/live-streaming/)

**Client:** The device that requested the stream uses the video's manifest file, which is contained within the metadata, as a reference for assembling and playing the video segments in order. It also changes the picture quality as needed.

## What is a manifest file?

A manifest file can be compared to a set of directions for assembling a model airplane. The directions indicate where each piece goes, enabling someone who owns the model kit to build the airplane themselves.

Similarly, a video's manifest file tells a client device playing the video (such as a user's laptop or smartphone) how to assemble the video segments in order, how to load the audio file, where subtitles are stored, and so on. This allows the client device to construct and play the video correctly.

Manifest files are stored in video metadata. A file's "metadata" is information about the rest of the file.

## What is adaptive bitrate streaming?

Adaptive bitrate streaming is a technique that allows video players to adjust the quality level of a video in response to network conditions. If a network connection is performing slowly, the player loads lower-quality video segments, which can load more quickly. If a network connection is performing better, the player loads the video in high definition instead. These adjustments are made while the video is playing.

Adaptive bitrate streaming is possible because streamed videos are divided into segments and encoded at several different quality levels. As a result, a player can select from multiple quality levels for each segment of video. After each segment, the player can switch to a higher or lower quality level as needed.

HDS uses adaptive bitrate streaming, and the similarly named [HTTP live streaming (HLS)](https://www.cloudflare.com/learning/video/what-is-http-live-streaming/) does as well.

## HLS vs. HDS: What is the difference?

HLS is one of the most widely used streaming protocols. HLS started out as a proprietary streaming protocol developed by Apple, although it has since become an open standard. Apple devices still support only HLS.

One important difference between these two streaming methods is that HDS has less widespread support and adoption than HLS. As of 2021, Apple has close to one-fourth of the smartphone market worldwide, so using HDS cuts out a significant chunk of potential viewers. In fact, HDS was meant for use with Adobe Flash, which has been discontinued. Today, relatively few viewers are likely to have devices that can play HDS streams.

Cloudflare Stream makes it easy to upload and stream video to viewers all over the world. Learn more about the formats supported by [Cloudflare Stream](https://www.cloudflare.com/developer-platform/products/cloudflare-stream/).
