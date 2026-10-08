---
url: https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/
title: How does live stream encoding work? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:14.292893+00:00
---

# How does live stream encoding work? | Learning Center

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  How does live stream encoding work? 

Encoding compresses raw video into a smaller, streamable format using codecs like H.264 and H.265. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand video encoding 
  * Know common video codecs 
  * Learn about adaptive bitrate streaming 



Related content  [ What is live streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)

On this page

  * What is live streaming?

  * What is video encoding?

  * How does live stream encoding work?

  * How are newer technologies making live streaming faster?

  * How are CDNs getting better at accelerating live streaming?




## What is live streaming?

Streaming is a method of delivering data over the Internet without making end users fully download the data. Live streaming is a type of streaming in which the stream is sent over the Internet in real time, without first being recorded and stored.

Video game streaming, social media streams like Periscope and Facebook Live, and professional sports broadcasts over the Internet are all examples of live streaming. Although both audio and video can be live streamed, this article will focus on live video streaming.

## What is video encoding?

Video encoding is the process of compressing video data so it can be efficiently sent to another location. The device on the receiving end of a stream – say, a tablet on which a user is watching their favorite TV show – decodes the encoded data. Video encoding follows publicly known standards so that a variety of devices can interpret the encoded stream.

Video encoding is necessary for two main reasons:

  1. Uncompressed video files take far too long to send over the Internet for streaming to be practical.
  2. Video has to be in a format that any user device – smartphones, laptops, PCs, etc. – can interpret.



In a video live stream, a device takes audiovisual inputs, encodes them, and sends them out to the audience all at the same time. The encoding part of this process is essential for allowing a variety of user devices to receive and play the video.

## How does live stream encoding work?

A live stream from a source that captures video – e.g., a webcam – is sent to a server, where a streaming protocol such as HLS or MPEG-DASH will break the video feed into smaller segments, each a few seconds in length.

The video content is then encoded using an encoding standard. The encoding standard in wide use today is called [H.264](https://www.cloudflare.com/learning/video/what-is-h264-avc/), but standards like H.265, VP9, and AV1 are also in use. This encoding process compresses the video by removing redundant visual information. For example, in a stream of someone talking against the background of a blue sky, the blue sky does not need to be rendered again for every second of video, since it does not change a lot. Therefore, the blue sky can be stripped out from most frames of the video.

The compressed, segmented video data is then distributed using a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/). Without a CDN, very few viewers will actually be able to load the live stream – the final section of this article explains why.

Most mobile devices have a built-in encoder, making it easy for regular users to live stream on social media platforms and via messaging apps. Brands and companies that want a higher quality stream use their own encoding software, hardware, or both.

## How are newer technologies making live streaming faster?

With many live streams, viewers still experience 20 to 30 seconds of [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) – in other words, the content they view is 20 to 30 seconds behind real time. This is partially because each segment of video has to fully load before it can play, and each segment of video can take several seconds to load.

One solution to this delay is a process called chunked encoding. This process works by "chunking,” that is, breaking up the video segments into even smaller pieces. Then those smaller pieces are encoded, and the devices receiving the stream can play these smaller chunks before the entire segment loads.

## How are CDNs getting better at accelerating live streaming?

CDNs are essential for live streaming because they make it possible to distribute the stream to users in vastly different locations. Also, CDNs have much more bandwidth for distributing the stream than a single [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). Without a CDN, the live stream can easily run into bandwidth issues.

However, most CDNs still have to load a full segment of video before they can serve the segment to multiple users at once. This [reintroduces](https://www.cloudflare.com/learning/cdn/common-cdn-issues/) the latency problem that chunked encoding is supposed to solve.

To speed up live streaming, Cloudflare offers a feature called [concurrent streaming acceleration](https://blog.cloudflare.com/introducing-concurrent-streaming-acceleration/). The [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) can deliver a segment of video to multiple end users at once while it is still loading, eliminating the wait time while the entire segment loads. The [Cloudflare global network](https://www.cloudflare.com/network/) spans 335+ cities in more than 120+ countries, enabling users around the world to tune into a [ high-quality, real-time live stream.](https://www.cloudflare.com/developer-platform/solutions/live-streaming/)
