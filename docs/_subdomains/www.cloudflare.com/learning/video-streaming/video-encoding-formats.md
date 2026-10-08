---
url: https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/
title: What are video encoding formats? | Video formats
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:42.359220+00:00
---

# What are video encoding formats? | Video formats

> Source: https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What are video encoding formats? | Video formats 

Video encoding formats are schematics for digital video files that have been optimized for different platforms and devices. Each video format is comprised of an audio codec, a video codec, and a container. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what video encoding formats are 
  * Learn how lossy and lossless compression affect video delivery 
  * Compare common video encoding formats 



Related content  [ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)[ How does live stream encoding work? | Video encoding ](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[ What is live streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[ What is MPEG-DASH? | HLS vs. DASH ](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[ MOV vs. MP4 | Video file formats ](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)

On this page

  * What are video encoding formats?

  * How does video encoding work?

  * What is a codec?

  * What is a container?

  * What are the most common types of video encoding formats?

  * How does Cloudflare support different video formats?




## What are video encoding formats?

Video encoding formats, also called video file formats, are methods of optimizing digital video files for different platforms, programs, and devices. There are many different kinds of video encoding formats, but each is composed of two main parts: a codec and a container. The codec and container specify the way in which uncompressed video input is stored, transmitted, and viewed. In [streaming](https://www.cloudflare.com/learning/performance/what-is-streaming/), it is important that the encoding format is compatible with the widest range of devices possible so that the stream is available to all users.

Selecting the proper video format depends on three main factors: storage availability, quality of video output, and compatibility with different video players or programs.

For example, say that Bob wants to upload a professional video portfolio to his website. He needs to consider upload bandwidth constraints as well as the overall quality of the video itself. He might choose WebM, a royalty-free file format that is supported by Android devices, most web browsers, and [HTML5 video](https://www.cloudflare.com/learning/video/how-html5-video-works/) streaming sites (e.g. YouTube). WebM allows him to compress his video file so that it plays back smoothly without losing significant video quality.

Alice, on the other hand, has hours and hours of home videos that she wants to convert into a widely-used digital video format for safekeeping. She intends to store most of the video files on her hard drive. She might select MPEG-4 Part 14 (MP4), which preserves the quality of the video after compression and is likely to remain compatible with most programs and devices for years to come.

## How does video encoding work?

Video encoding is the process of turning uncompressed video input into a form that can be stored and played by a variety of devices. Video encoding involves two main processes: compression and transcoding.

Compression, or the discarding of superfluous data, significantly decreases the size of a video file so that it is more manageable. Without proper compression, most files would be far too large to upload easily, load quickly, or play smoothly on users’ devices.

Transcoding refers to the total audio and video conversion process from one video format to another. It ensures that a video file is compatible with the video player and/or platform it is using. Without transcoding, users would not be able to watch the video file at all.

On-demand streaming video is encoded so that it can be sent over the Internet and played on a variety of user devices. During [live streaming](https://www.cloudflare.com/learning/video/what-is-live-streaming/), the video stream is segmented, compressed, and encoded in real time.

Users may receive the [encoded live stream](https://www.cloudflare.com/developer-platform/solutions/live-streaming/) on different devices using different video players. The devices decode and decompress the segmented video before playing the video.

## What is a codec?

A codec (coder/decoder) is a method for compressing and decompressing data so that it can be easily transported and received by different applications. Separate codecs are used to compress audio and video files, but they generally work in the same way.

Codecs encode files using either lossy compression or lossless compression. Lossy compression simplifies the data in a video file and only keeps the essential parts. This is why a video using lossy compression may look pixelated or “fuzzy.” Imagine that Frank decides to send his sister a video of his rose garden: lossy compression will accurately show every rose, but may choose a single shade of pink for the flowers instead of depicting the subtle variations of pink in each petal.

Lossless compression preserves the high quality of the original video file by copying every piece of data exactly. Frank may prefer to send his sister a high-definition video of his garden — one that captures every shade of pink on every rosebud — but the resulting file size would likely be far too large to send via text or email.

Both lossy and lossless compression have their advantages and drawbacks. Lossy compression offers smaller file sizes and lower video quality, while lossless compression offers higher-quality file duplication that comes with larger file sizes.

## What is a container?

A container combines an encoded audio stream (audio codec), encoded video stream (video codec), and metadata in a single video file. The metadata tells the video player how to coordinate different audio and video codecs and may also provide additional elements, such as subtitles or alternate audio streams.

Each container supports a different range of video codecs. Some containers only work with a single type of codec and video player, which drastically limits playback options. Other containers are compatible with many types of video codecs and players.

Often, video file extensions are named for the containers they use, rather than the audio and video codecs they contain. (For example, an MP4 video file is really an MP4 container.) A video file can only play properly if both the codec and container are compatible with the video player.

## What are the most common types of video encoding formats?

There are over a dozen types of video encoding formats, and they are not all compatible with the same platforms, browsers, and devices. Here are five of the most common video formats:

**MP4:** [MPEG-4 Part 14 (MP4)](https://www.cloudflare.com/learning/video/what-is-mpeg-dash/) is a video file format created by the Motion Picture Expert Group. It compresses audio and video separately, which allows MP4 files to retain relatively high video quality after compression. Most browsers and iOS/Android devices are compatible with MP4 files.

**MOV:** QuickTime Movie (MOV) is a video file format created by Apple. Although it can run on both Mac OS and Windows OS, it is only compatible with QuickTime video players. It preserves video quality, but does not offer as much file compression as other common video formats, such as MP4.

**AVI:** Audio Video Interleave (AVI) is a video file format created by Microsoft. It is one of the oldest video file container specifications. AVI works with a number of different codecs, which can affect how well it is supported by different operating systems and browsers. It prioritizes video quality over compression, meaning that video files are larger and better quality overall.

**FLV:** Flash Video Format (FLV) is a video file format created by Adobe Flash. A clear advantage of FLV is its ability to compress video files without severe loss of video quality. However, it is far less compatible across devices and OSes than other file formats: Though it is supported by most browsers and Android devices, it cannot be used to play any video files on iOS devices like iPhones or iPads. Browsers have dropped support for Adobe Flash because it is considered to be insecure, and Adobe no longer supports Flash as of December 31, 2020.

**WebM:** WebM is a video file format developed by Google. It is a subset of the open-standard Matroska Video Container (MKV) format, which is highly adaptive to most video and audio codecs and compatible with a wide range of platforms and devices. WebM is a web-friendly, open-source alternative to MP4 that maintains high video quality after compression. Both MP4 and WebM are supported by HTML5.

## How does Cloudflare support different video formats?

Cloudflare Stream supports many [video encoding formats](https://developers.cloudflare.com/stream/faq/), including MP4, MKV, MOV, AVI, FLV, MPEG-2 TS, MPEG-2 PS, MXF, LXF, GXF, 3GP, WebM, MPG, and QuickTime. Backed by a network of data centers in 335+ cities around the world, [Cloudflare Stream](https://www.cloudflare.com/developer-platform/products/cloudflare-stream/) offers fast, high-quality video playback bundled with video storage, encoding, and a customizable video player.
