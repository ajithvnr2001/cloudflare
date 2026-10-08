---
url: https://www.cloudflare.com/learning/video-streaming/turn-server/
title: What is a TURN server?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:41.898463+00:00
---

# What is a TURN server?

> Source: https://www.cloudflare.com/learning/video-streaming/turn-server/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is a TURN server? 

A Traversal Using Relays around NAT (TURN) server allows for reliable WebRTC connections in highly restrictive networks. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Describe what a TURN server does 
  * Understand the advantage of using a TURN server 
  * Contrast TURN vs. STUN servers 



Related content  [ How WebRTC works: What is WebRTC used for? ](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[ What is voice over Internet Protocol (VoIP)? ](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[ What is live streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

On this page

  * What is a TURN server?

    * TURN vs. STUN server

  * What is WebRTC?

  * What is network address translation?

  * What is the advantage of using a TURN server?

  * Does Cloudflare Realtime include TURN service?




## What is a TURN server?

A Traversal Using Relays around NAT (TURN) server is a type of web server that enables [WebRTC](https://www.cloudflare.com/learning/video/how-webrtc-works/) connections between computing devices when [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/) or the usage of private IP addresses break real-time communications connections, such as video or audio calls. As the acronym indicates, TURN service circumvents network address translation (NAT) to ensure the connection between clients does not break in the middle of a session.

Simply put, TURN servers help ensure that video and audio calls work well even when the network is not configured to support them.

TURN servers become necessary when one of the devices in a WebRTC connection uses a private [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). Devices that have private IP addresses use NAT to connect to other devices. NAT repackages [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) and sends them to the private IP address, but it does not work well with many [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/), including WebRTC.

Imagine Alice wants to drive to Bob's house, but there is a roadblock set up across the highway between them. Instead of taking the highway and hitting the roadblock, Alice takes side streets until she reaches Bob's house via an alternate route. A TURN server provides an alternate route for WebRTC connections when NAT might otherwise be an impassable roadblock.

#### TURN vs. STUN server

A STUN (Session Traversal Utilities for NAT) server is another type of server that supports WebRTC connections. It allows two devices to discover each other's public IP addresses and initiate a direct connection. However, STUN servers often cannot bypass stringent security measures. In such cases, a TURN server can be used instead.

## What is WebRTC?

Web Real-Time Communications (WebRTC) is an open-source technology that allows for establishing direct peer-to-peer (P2P) real-time communication via [APIs](https://www.cloudflare.com/learning/security/api/what-is-an-api/). It allows client devices to [stream](https://www.cloudflare.com/learning/video/what-is-streaming/) files to each other instead of relying on a central server (as opposed to protocols like [HLS](https://www.cloudflare.com/learning/video/what-is-http-live-streaming/) or [HDS](https://www.cloudflare.com/learning/video/what-is-http-dynamic-streaming/), which presume a [client-server model](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)). WebRTC has also come to be used for a number of communications protocols, such as [voice over Internet protocol (VoIP)](https://www.cloudflare.com/learning/video/what-is-voip/), which supports Internet-based telephone and video calls.

## What is network address translation (NAT)?

NAT (network address translation) is a technique for mapping private IP addresses to public IP addresses — or, most commonly, mapping multiple private IP addresses to one public IP address. (IP addresses are essential for setting up connections between devices.)

NAT is like using a forwarding address within a postal system. Correspondents can send mail without knowing the recipient's true mailing address, since the forwarding address will send it on to that address. Similarly, NAT matches a public IP address to a private IP address and forwards packets to the correct places.

One of the most popular applications of NAT is assigning IP addresses within [local area networks (LANs)](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/), such as home WiFi networks. There are not enough IPv4 addresses to go around, so routers assign dynamic, private IP addresses to network-connected devices. These IP addresses are likely used by other devices on the Internet as well, so to avoid confusion the router uses NAT to change them to one public-facing IP address that is not duplicated anywhere else. (The ISP may dynamically assign those public-facing IP addresses also.)

NAT is additionally used as a security measure to keep IP addresses private. A device can avoid revealing its true IP address outside the network — or even within the network — and use NAT to broadcast a public IP address and connect to other devices.

The problem is that some [application-layer](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) protocols do not work well with NAT, just as one's forwarding address may not be able to forward every type of mail (large packages, for instance).

## What is the advantage of using a TURN server?

A TURN server helps ensure connectivity even in highly restricted network environments that use NAT and firewalls to conceal IP addresses. It allows real-time communications to work when normal connections are not possible and STUN servers cannot support them. TURN servers improve reliability for Internet-based phone services or chat services.

## Does Cloudflare Realtime include TURN service?

[Cloudflare Realtime](https://www.cloudflare.com/developer-platform/products/cloudflare-calls/) is a service that allows developers to build real-time audio, video, and data applications. Cloudflare Realtime does include a global TURN server, making it easier to build real-time applications that are fast and reliable. [To learn more about Cloudflare's TURN service, see the developer docs](https://developers.cloudflare.com/realtime/).
