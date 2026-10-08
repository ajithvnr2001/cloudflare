---
url: https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/
title: How WebRTC works: What is WebRTC used for?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:28.556602+00:00
---

# How WebRTC works: What is WebRTC used for?

> Source: https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  How WebRTC works: What is WebRTC used for? 

WebRTC is a protocol for peer-to-peer data exchange. Because it has very little latency by design, it is often used for live video streaming. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how WebRTC works 
  * Understand what WebRTC is used for 
  * Know how to start using WebRTC 



Related content  [ What is a TURN server? ](https://www.cloudflare.com/learning/video-streaming/turn-server/)[ What is voice over Internet Protocol (VoIP)? ](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[ What is live streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

On this page

  * What is WebRTC?

  * How does WebRTC work?

    * WebRTC protocols: ICE, STUN, TURN

    * WebRTC signaling servers

    * WebRTC media servers

  * What is peer-to-peer and how does it distinguish WebRTC from other streaming protocols?

  * WebRTC vs. WebSocket: Why use WebRTC?

  * How to get started with WebRTC

  * How to set up a TURN server

  * FAQs

    * What makes WebRTC different from traditional streaming methods?

    * Why is WebRTC preferred over HLS or MPEG-DASH for live content?

    * Do users need to install special software to join a WebRTC stream?

    * What role does a signaling server play in a WebRTC connection?

    * How can Cloudflare help developers implement these real-time features?




## What is WebRTC?

Web Real-Time Communications (WebRTC) is an open-source technology that allows browsers to exchange data directly with only minimal use of an intermediary server or third-party software. Often WebRTC is used specifically for exchanging audio and video data.

WebRTC uses a set of [APIs](https://www.cloudflare.com/learning/security/api/what-is-an-api/) and [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) to set up peer-to-peer (P2P) connections directly between devices. It can support [telephone connections](https://www.cloudflare.com/learning/video/what-is-voip/), teleconferencing, [audio and video streaming](https://www.cloudflare.com/learning/video/what-is-streaming/), file transfers, and screen sharing, among other types of communication.

Most technologies for exchanging and streaming data between devices rely on the use of servers in the middle to receive data from clients, store or cache the data, and forward the data to the other client. If Alice wants to talk to Bob using a chat app, her words travel first to a web server before they reach Bob's device. WebRTC, for the most part, allows Alice and Bob to send their communications directly to each other.

As a result, from the app developer's perspective, WebRTC-based apps require a little less backend infrastructure and can have less [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) compared to apps that use client-server protocols. The other advantage of WebRTC is that users do not have to install anything: no plugins or additional software are necessary beyond a web browser.

## How does WebRTC work?

WebRTC streams directly between browsers. Almost all browsers support WebRTC natively so users do not have to install a plugin or additional software, which makes WebRTC a logical choice for building real-time communications features into a web app.

While WebRTC is primarily P2P, in reality end user devices tend to be behind [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/), they require network address translation (NAT) for connections, or they connect to the Internet via [routers](https://www.cloudflare.com/learning/network-layer/what-is-a-router/) that do not support P2P. Therefore, WebRTC connections do require intermediary servers to enable devices to find each other or to forward data from one to the other. WebRTC relies on a set of specialized protocols and servers to accomplish this.

#### WebRTC protocols: ICE, STUN, TURN

**Session Traversal Utilities for NAT (STUN)** is a protocol for finding out the public [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of the other peer in the connection. The peers ask the STUN server for the other one's public IP address and whether or not the peer can be reached behind their router's NAT. If a public IP address is available for both parties, the WebRTC connection can then proceed directly between the peers.

**Traversal Using Relays around NAT (TURN)** is used in some cases when the other peer in a connection has no public IP address due to the use of firewalls or private IP addresses. Peers connect to a [TURN server](https://www.cloudflare.com/learning/video/turn-server/) rather than directly to each other, and the server forwards their [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/).

**Interactive Connectivity Establishment (ICE)** is the framework that allows browsers to connect to STUN and TURN servers.

Learn more about WebRTC protocols [here](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols).

#### WebRTC signaling servers

For P2P media exchange between two devices, such as in a video call, they need to negotiate how they will send information to each other. This requires the use of a signaling server. The signaling server facilitates a back-and-forth between the devices as they decide on communication protocols, media resolution, video codecs, and other requirements for exchanging media streams, as well as exchanging [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) information.

#### WebRTC media servers

While WebRTC is designed to work P2P, it can also work with an intermediary media server. A media server can receive and forward media while taking into account device bandwidth limitations and other constraints. This is especially necessary when more than two devices are streaming to each other — say, when a dozen people wish to participate in a video call, instead of just two.

## What is peer-to-peer (P2P) and how does it distinguish WebRTC from other streaming protocols?

The Internet was built on the client-server model.

  * Clients: End-user devices such as desktop computers, laptop computers, and smartphones, along with [IoT](https://www.cloudflare.com/learning/ddos/glossary/internet-of-things-iot/) and smart devices

  * Servers: Large computers optimized for efficiency and hosted in [data centers](https://www.cloudflare.com/learning/cdn/glossary/data-center/)




Typically, clients load websites, apps, and data from servers, rather than communicating directly with each other. Servers are more reliable and powerful than client devices, and they are configured specifically to serve client requests. They store data and execute code on the backend so that clients do not have to store all the data they need or run compute-heavy functions. This enables users of client devices to easily browse the web and get whatever resources they need (code, video, images, etc.) from servers without having to permanently download all the web content they display.

In contrast, P2P is a networking architecture in which any connected device communicates directly with any other connected device. P2P reduces or eliminates the need for servers, allowing client devices to connect and exchange data with each other. Because all connected devices in a P2P architecture can fill the same function of sending or receiving data, they are called "peers" instead of clients.

Streaming protocols like [HLS](https://www.cloudflare.com/learning/video/what-is-http-live-streaming/), [HDS](https://www.cloudflare.com/learning/video/what-is-http-dynamic-streaming/), and [MPEG-DASH](https://www.cloudflare.com/learning/video/what-is-mpeg-dash/) presume a client-server model, with a server storing or [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) audiovisual content and then streaming it to clients. WebRTC, however, mainly uses a P2P model, in which clients stream directly to each other.

WebRTC is often better suited for [live streaming](https://www.cloudflare.com/learning/video/what-is-live-streaming/) for this reason. HLS and MPEG-DASH typically have a minimum of ten seconds of latency between the source of the stream and any stream viewers, while WebRTC is much closer to being instant. [Set up low-latency live streaming](https://www.cloudflare.com/developer-platform/solutions/live-streaming/).

(In actual production, WebRTC does incorporate servers in order to work properly, as described above.)

## WebRTC vs. WebSocket: Why use WebRTC?

WebSocket is another commonly used protocol for real-time data exchange. There are a couple of key differences between WebRTC and WebSocket that lead many app developers to prefer WebRTC for low-latency live streaming:

  * **WebSocket is client-server, while WebRTC is P2P:**As explained above, this gives WebRTC a speed advantage in many cases.

  * **WebSocket is over TCP, while WebRTC is usually over UDP:**[TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) and [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) are two different transport protocols that can underlie application-layer protocols like WebRTC, WebSocket, or [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/). To briefly summarize, TCP is more reliable but slightly slower since all packets must be delivered, while UDP is less reliable but faster since UDP does not care about packet loss. For real-time communication use cases like video chat, speed is often more important than a little bit of missing information, making UDP (and therefore WebRTC) the better choice.




## How to get started with WebRTC

[Cloudflare Stream](https://www.cloudflare.com/developer-platform/products/cloudflare-stream/) allows developers to easily build WebRTC streams into their apps, and [Cloudflare Realtime](https://www.cloudflare.com/developer-platform/products/cloudflare-realtime/) includes prebuilt components for developers to build video, audio, and chat features into their apps. Both products serve streams from the Cloudflare global network, which, with over 335+ global locations, is within milliseconds of almost every Internet user in the world.

[See these instructions to set up a WebRTC stream](https://developers.cloudflare.com/stream/webrtc-beta/) with Cloudflare Stream.

[View this reference architecture to start building](https://developers.cloudflare.com/realtime/sfu/example-architecture/) with Cloudflare Realtime.

## How to set up a TURN server

Cloudflare Realtime also includes a managed TURN server to ensure that WebRTC streams can reach end users, even if they are behind a firewall or lack a public IP address. This service helps developers and streamers make sure their content can reach as many viewers as possible, without the overhead of configuring and maintaining their own TURN servers. [Read about the Cloudflare TURN service](https://developers.cloudflare.com/realtime/turn/).

## FAQs

#### What makes WebRTC different from traditional streaming methods?

Most streaming technologies rely on a client-server model where data must first pass through a middleman server to be stored or processed before reaching the recipient. WebRTC primarily uses a peer-to-peer (P2P) architecture, allowing devices to exchange audio, video, and data directly with one another. This direct connection typically reduces the need for extensive backend infrastructure and significantly lowers latency.

#### Why is WebRTC preferred over HLS or MPEG-DASH for live content?

The main advantage is speed. Standard protocols like HLS often have a delay of several seconds between the source and the viewer. Because WebRTC is designed for real-time interaction, it is closer to being truly live, making it a better fit for use cases like video conferencing or interactive live streams.

#### Do users need to install special software to join a WebRTC stream?

One of the primary benefits of WebRTC is that it is natively supported by almost all modern web browsers. Users can participate in high-quality communications without downloading additional plugins or third-party applications.

#### What role does a signaling server play in a WebRTC connection?

Before two devices can share media, they must agree on how to communicate. A signaling server facilitates this negotiation by helping the devices exchange information about their respective routing requirements, video codecs, and media resolutions.

#### How can Cloudflare help developers implement these real-time features?

Cloudflare provides tools like Stream and Realtime that allow developers to integrate WebRTC-based video, audio, and chat into their applications without managing their own infrastructure. These services utilize a global network to ensure streams stay within milliseconds of users worldwide and include managed TURN services to help stream to devices behind firewalls.
