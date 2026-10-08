---
url: https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/
title: What is H.264? | Advanced Video Coding (AVC)
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:02.217629+00:00
---

# What is H.264? | Advanced Video Coding (AVC)

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is H.264? | Advanced Video Coding (AVC) 

Advanced Video Coding (AVC), which is also called H.264, is the most widely used video compression standard. It is compatible with all major streaming protocols and container formats. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand video compression 
  * Explain why AVC, also known as H.264, is so widely used 
  * List some of the streaming protocols and container formats that are compatible with AVC/H.264 



Related content  [ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)[ What is MPEG-DASH? | HLS vs. DASH ](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[ What is HDS streaming? | HLS vs. HDS ](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[ What are video encoding formats? | Video formats ](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)

On this page

  * What is Advanced Video Coding?

  * What is video compression?

  * What streaming protocols use H.264?

  * What containers use AVC/H.264?

  * What is H.265?

  * Does Cloudflare Stream use H.264?




## What is Advanced Video Coding (H.264)?

Advanced Video Coding (AVC), also called H.264, is the most common video compression standard in use today. AVC/H.264 can encode high-quality video at lower bit rates than older compression standards (the "bit rate" is the number of units of information that have to be processed for each second of video).

Blu-ray and a wide variety of [streaming](https://www.cloudflare.com/learning/video/what-is-streaming/) services, including on-demand and live TV, use H.264. Despite the fact that its use sometimes requires royalty payments to organizations that own the patents for it, over 90% of the video industry uses H.264.

## What is video compression?

Video compression, also called [video encoding](https://www.cloudflare.com/learning/video/video-encoding-formats/), is the process of reducing the size of video data so that it can be efficiently moved from one place to another. A completely uncompressed video file might take up several Blu-ray discs. It would also take a tremendous amount of time to stream from a server to a user's computer, and real-time playback would be next to impossible. By contrast, a compressed video file can fit into one Blu-ray disk, even with extremely high picture quality. And it can be streamed quickly and in near real time from a server to a user's computer.

Video compression works by removing redundant visual information and unnecessary details, and by relying on mathematical calculations to generate most of each frame of video, rather than recording every frame. By recording how the visuals change from frame to frame, video compression stores entire videos without storing every frame.

H.264 is a lossy compression standard, meaning unnecessary information is removed from the video. However, this should not impact the video's quality, since the important information for displaying the video is kept.

## What streaming protocols use H.264?

Almost all streaming protocols in use today are compatible with H.264, including the Real Time Streaming Protocol (RTSP), [HTTP live streaming (HLS)](https://www.cloudflare.com/learning/video/what-is-http-live-streaming/), [HTTP dynamic streaming (HDS)](https://www.cloudflare.com/learning/video/what-is-http-dynamic-streaming/), and dynamic adaptive streaming over HTTP ([MPEG-DASH](https://www.cloudflare.com/learning/video/what-is-mpeg-dash/)). In fact, HLS works only with H.264, while some streaming protocols can use other compression standards.

## What containers use AVC/H.264?

A video container file stores video, audio, and metadata; one of the most common types of container files is MP4. H.264 works with multiple container formats, including MP4, TS, and [MOV](https://www.cloudflare.com/learning/video/mov-vs-mp4/).

## What is H.265?

H.265 is also known as High Efficiency Video Coding (HEVC), and it is the compression standard that followed H.264. It provides even better picture quality than H.264. Many video hosting servers use H.265 in addition to H.264. However, because the older H.264 is so widely adopted and already offers good quality at manageable bit rates, it is likely to remain in use for some time.

## Does Cloudflare Stream use H.264?

Cloudflare Stream encodes all videos using H.264. Stream enables [adaptive bitrate streaming](https://www.cloudflare.com/learning/video/what-is-adaptive-bitrate-streaming/) (which adjusts the quality of the video as it plays) by encoding every video at several different quality levels. Learn more about [Cloudflare Stream](https://www.cloudflare.com/developer-platform/products/cloudflare-stream/).
