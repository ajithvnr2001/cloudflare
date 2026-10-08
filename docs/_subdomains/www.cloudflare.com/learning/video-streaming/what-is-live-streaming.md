---
url: https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/
title: What is live streaming? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:05.160724+00:00
---

# What is live streaming? | Learning Center

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is live streaming? 

Live streaming is the real-time delivery of video content over the Internet as it is being captured. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define live streaming 
  * Understand the live streaming pipeline 
  * Know common live streaming protocols 



Related content  [ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)

On this page

  * What is live streaming?

  * How does live streaming work on a technical level?

  * Why is a CDN important for live streaming?

  * How does Cloudflare accelerate live streaming?




## What is live streaming?

[Streaming](https://www.cloudflare.com/learning/performance/what-is-streaming/) is the method of data transmission used when someone watches video on the Internet. It is a way to deliver a video file a little bit at a time, often from a remote storage location. By transmitting a few seconds of the file at a time over the internet, [client devices](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) do not have to download the entire video before starting to play it.

Live streaming is when the streamed video is sent over the Internet in real time, without first being recorded and stored. Today, TV broadcasts, video game streams, and social media video can all be live-streamed.

Think about the difference between regular streaming and live streaming as the difference between an actor reciting a memorized monologue and improvising a speech. In the former, the content is created beforehand, stored, and then relayed to the audience. In the latter, the audience receives the content in the same moment that the actor creates it – just like in live streaming.

The term live streaming usually refers to broadcast live streams: one-to-many connections that go out to multiple users at once. Videoconferencing technologies like Skype, FaceTime, and Google Hangouts Meet work on real-time communication (RTC) protocols rather than the protocols used by one-to-many live stream broadcasts.

## How does live streaming work on a technical level?

These are the main steps that take place behind the scenes in a live stream:

  * Compression
  * [Encoding](https://www.cloudflare.com/learning/video/live-stream-encoding/)
  * Segmentation
  * [Content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) distribution
  * CDN [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/)
  * Decoding
  * Video playback



#### Video capture 

Live streaming starts with raw video data: the visual information captured by a camera. Within the computing device to which the camera is attached, this visual information is represented as digital data – in other words, 1s and 0s at the deepest level.

#### Compression and encoding 

Next, the segmented video data is compressed and encoded. The data is compressed by removing redundant visual information. For example, if the first frame of the video displays a person talking against a grey background, the grey background does not need to render for any subsequent frames that have the same background.

Think of video compression as being like adding a piece of new furniture to a living room. It is not necessary to buy entirely new furniture each time a new chair or side table is added. Instead it is possible to keep the room layout roughly the same and change out just one piece at a time, occasionally making larger rearrangements as necessary. Similarly, not every frame of a video stream needs to be rendered in total – just the parts that change from frame to frame, such as the movement of a person's mouth.

"Encoding" refers to the process of converting data into a new format. Live streaming video data is encoded into an interpretable digital format that a wide variety of devices recognize. Common video encoding standards include:

  * [H.264](https://www.cloudflare.com/learning/video/what-is-h264-avc/)
  * H.265
  * VP9
  * AV1



#### Segmentation 

Video includes a lot of digital information, which is why it takes longer to download a video file than to download a short PDF or an image. Because it would not be practical to send all the video data out over the Internet at once, streaming video is divided into smaller segments a few seconds in length.

#### CDN distribution and caching 

Once the live stream has been segmented, compressed, and encoded (all of which only takes a few seconds), it needs to be made available to the dozens or millions of viewers who want to watch it. In order to maintain high quality with minimal latency while serving the stream to multiple viewers in different locations, a CDN should distribute it.

A CDN is a distributed network of servers that cache and serve content on behalf of an origin server. Using a CDN results in faster performance, because user requests no longer have to travel all the way to the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) but can instead be handled by a nearby CDN server. Handling requests and delivering content in this manner also reduces the origin server’s workload. Finally, CDNs make it possible to efficiently serve content to users around the world because their servers are located all over the world instead of clustered in a single geographic area.

A CDN will also cache – temporarily save – each segment of the live stream, so most viewers will get the live stream from the CDN cache instead of from the origin server. This actually makes the live stream closer to real-time even though the cached data is a few seconds behind, because it cuts down on [round-trip time (RTT)](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/) to and from the origin server.

#### Decoding and video playback 

The CDN sends the live stream out to all the users who are watching the stream. Each user's device receives, decodes, and decompresses the segmented video data. Finally, a media player on the user's device – either a dedicated app or a video player within the browser – interprets the data as visual information, and the video plays.

#### An example 

Suppose Alice starts a live stream on her smartphone and Bob, who lives on the other side of the country, tunes into the live stream on his smartphone, along with a few dozen more of Alice's friends. Alice starts out the live stream by turning the smartphone camera on herself and saying, "Hello, world!" What needs to happen for that "Hello, world" section of video to reach Bob on the other side of the country, along with all the other people watching the stream?

First, Alice's smartphone will encode and compress that little segment of video. If Alice is filming the live stream in her kitchen, her kitchen wall is recorded as the first frame of the video, and subsequent frames will leave it out since the background doesn't change.

Now the app Alice is using will send the encoded, compressed version of her saying "Hello, world" out to the app's CDN. Fortunately for Bob, one of the CDN servers is just a few miles away from his home, so his smartphone's request for the first segment of the live stream is answered almost immediately. Other live stream viewers may experience more or less latency than Bob depending on their geographic location.

Bob's phone decodes the video segment and reconstructs the compressed data, so that Alice's kitchen wall appears in every frame. And finally, only a few seconds after Alice said "Hello, world" in her kitchen on the other side of the country, her face appears on Bob's smartphone and Bob sees and hears her greeting.

## Why is a CDN important for live streaming?

**Bandwidth:** Any given point on a network can only have so much data pass through at a time; this measurement is known as "bandwidth." If a stream of data reaches a point on the network where the amount of data exceeds capacity, this is called a "choke point" because data delivery is choked off and slowed down. A choke point is similar to the way traffic slowdowns might occur when too many cars attempt to use a single-lane road.

If all viewers of a stream are getting the stream data from its point of origin, then the origin server and its surrounding network infrastructure becomes a choke point and the stream slows down. But if the main burden of stream delivery is moved to a CDN, then the choke point is eliminated.

**Global content delivery:** Because CDNs are distributed all around the world, they are able to deliver content to a global audience. An origin server in New York cannot effectively serve content to an audience in Milan, and this is especially the case with heavy content like video. However, a CDN can forward and serve content from any point on its network, so that a person in Milan watching a live stream from New York can get the stream from a server in Milan instead of waiting for it to load all the way from New York.

**Latency and RTT reduction:** Delivering content globally with a CDN [reduces latency for live stream](https://www.cloudflare.com/developer-platform/solutions/live-streaming/) viewers by cutting down on RTT (round-trip time). The request-response round trip is shorter both in terms of distance and in terms of time, as a viewer’s request for a live stream no longer has to travel to the original source of the stream, and the streaming data no longer has to travel from the origin, either. This reduces delays and helps keep the live stream closer to "live."

**Workload:** Replying to user requests for data costs a server some compute power. Replying to many user requests for video data can overwhelm a single server. A CDN utilizes dozens or hundreds of servers that can take much of the workload off the origin server and keep it up and running.

**Caching:** A CDN caches each video segment of a live stream. The CDN can then deliver the segments from the cache instead of getting the data from the origin server.

Serving a live stream from a cache seems like a contradiction: If the stream is live, how can saving it and delivering it a few seconds later be faster? While it's true that a cached live stream will lag behind real-time, this is still faster than going all the way to the origin server. The round trip would take so long that the stream would fall even further behind. With CDN caching, users experience minimal lag time.

## How does Cloudflare accelerate live streaming?

The [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) uses a technique called concurrent streaming acceleration to speed up live stream delivery. Some CDNs cannot serve a video segment to more than one user until the segment is completely saved in the cache. The Cloudflare CDN, however, is able to serve these segments directly to multiple viewers at once as they are loading, cutting out precious seconds of wait time for the users. [Learn more about concurrent streaming acceleration](https://blog.cloudflare.com/introducing-concurrent-streaming-acceleration/).
