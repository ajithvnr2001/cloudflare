---
url: https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/
title: What is a video CDN?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:16.974156+00:00
---

# What is a video CDN?

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is a video CDN? 

A video content delivery network (CDN) helps deliver streaming video quickly and efficiently to viewers around the world. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define 'video CDN' 
  * Explain how CDN video streaming works 
  * Describe the advantages of using a CDN for streaming video 



Related content  [ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[ What is live streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[ What is MPEG-DASH? | HLS vs. DASH ](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[ How does live stream encoding work? | Video encoding ](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

On this page

  * What is a video CDN?

  * What is a CDN?

  * Why use a CDN for streaming video?

    * Minimizing distance to viewers reduces latency

    * Origin server is not overwhelmed

    * Streaming content does not exceed network bandwidth

  * How can a stream be cached?

  * How does a CDN cache a live stream?

  * Does the Cloudflare CDN work with video?




## What is a video CDN?

A video CDN is a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) that has been designed to support video stream delivery. The use of a CDN for [streaming](https://www.cloudflare.com/learning/video/what-is-streaming/) video helps a stream reach viewers around the world, minimizes [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) and [buffering](https://www.cloudflare.com/learning/video/what-is-buffering/) time, and ensures that the stream's source or [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) are not overwhelmed with requests.

While most CDNs are able to cache and deliver video content alongside HTML, images, JavaScript, CSS style sheets, and other web content, video CDNs can be constructed exclusively for streaming video. For instance, Netflix built out their own distributed network called Open Connect to more efficiently deliver their video content.

## What is a CDN?

A content delivery network (CDN) is a group of connected servers that [cache](https://www.cloudflare.com/learning/cdn/what-is-caching/) and deliver content over the Internet. CDNs are spread out all over the world, enabling them to deliver content more efficiently to a wider range of people than an origin server or a single data center can. A CDN caches content whenever a user requests the content from a website that uses that CDN; to "cache" means to temporarily store a file.

Suppose Bob [hosts](https://www.cloudflare.com/developer-platform/solutions/hosting/) a website, bobisgreat.example.com, on a server in New York City, New York. When Alice in Albany, New York (about 250 kilometers away), visits the website, it loads quickly, since the website content has to travel only 250 kilometers. However, when Carlos tries to load bobisgreat.example.com from his house in Los Angeles, California (about 4,800 kilometers away), he has to wait a lot longer for the website to load.

If Bob uses a CDN service, the CDN can cache his website's content at locations close to both Alice and Carlos. Suppose Bob's CDN caches his website at data centers in Albany and Los Angeles, in addition to New York City. Now both Alice and Carlos hardly have to wait any time at all for bobisgreat.example.com to load in their browsers.

## Why use a CDN for streaming video?

#### Minimizing distance to viewers reduces latency

The same principle described above applies for streaming video. The closer the video content is to the viewer, the [faster it will load and play](https://www.cloudflare.com/developer-platform/solutions/live-streaming/). A CDN is likely to have a server closer to any given viewer than the stream's point of origin.

#### Origin server is not overwhelmed

Using the many servers of a CDN means that the server where the stream originates will not become overwhelmed with requests for the stream. A group of 200 servers can handle streaming video to thousands of viewers far better than a single server can.

#### Streaming content does not exceed network bandwidth

A network can have only a certain amount of data pass through at once. This maximum amount is called "bandwidth." If the amount of data passing through a network exceeds its bandwidth, data delivery slows down to a huge degree, just as limiting cars to one lane slows down traffic on a highway. If a stream is delivered from the multiple distributed servers of a CDN, it is less likely that any one network will become overwhelmed with traffic in this way.

## How can a stream be cached?

Streaming continuously transmits video files from a server to a client. However, streaming video does not go to a user's device as one continuous file. Rather, streaming video is broken up into smaller segments. Each segment is loaded and put in the correct order by the user's video player.

Each individual video segment can be cached by a CDN, just as an image, an HTML page, or a snippet of JavaScript code can be cached by a CDN. When a user requests a stream, the CDN begins caching the video segments as soon as they arrive from the stream's origin. When the next user requests the same stream, the CDN can deliver those segments from the cache instead, which is much faster.

## How does a CDN cache a live stream?

For video-on-demand streaming, in which the video is delivered from storage, caching the video is fairly simple: the CDN requests the stored video from the origin server, the origin server delivers it, and the CDN then caches the video.

In live streaming, there is no stored version of the video ready to go. However, the process is similar. The only difference is that the CDN caches the video segments as they are created in real time, instead of caching a previously created video. The stream is then served to viewers from the cache instead of directly from the stream's origin.

Even though most viewers have to wait a few extra seconds for each segment to be cached, if done efficiently this can actually make the stream closer to "live" than fetching the stream directly from the origin server. Because a CDN is closer to viewers than the origin server, serving the stream from the cache can cut down on round-trip time ([RTT](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)) to and from the origin server. In addition, using a CDN reduces the possibility that bandwidth issues will slow down the live stream for viewers.

## Does the Cloudflare CDN work with video?

[Cloudflare Stream](https://www.cloudflare.com/products/cloudflare-stream/) is a streaming service for delivering video via the Cloudflare CDN. Cloudflare's global network ensures fast delivery and smooth video playback for viewers in any location; Cloudflare operates within 100 milliseconds of 99% of the developed world.
