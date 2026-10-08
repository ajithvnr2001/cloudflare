---
url: https://www.cloudflare.com/learning/video-streaming/what-is-voip/
title: What is voice over Internet Protocol (VoIP)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:17.080371+00:00
---

# What is voice over Internet Protocol (VoIP)?

> Source: https://www.cloudflare.com/learning/video-streaming/what-is-voip/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  What is voice over Internet Protocol (VoIP)? 

Voice over Internet Protocol (VoIP) is an alternative to landline-based telephone systems. VoIP uses the Internet to carry phone calls instead of the public switched telephone network. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how voice over Internet Protocol (VoIP) works 
  * Describe the technical details of VoIP 
  * Understand the causes of VoIP service disruptions and cyber attacks 



On this page

  * What is voice over Internet Protocol?

  * How does audio travel via VoIP?

  * What does the &#39

  * What protocols does VoIP use on top of IP?

  * What causes VoIP service disruptions?

  * Why is VoIP vulnerable to distributed denial-of-service attacks?

    * SIP floods in VoIP




## What is voice over Internet Protocol (VoIP)?

Voice over Internet Protocol (VoIP) is a method for making telephone calls over the Internet. Unlike the old landline telephone system, the Internet was not designed to carry audio signals in real time between connected persons. Specialized technologies and protocols had to be constructed to make this possible — the technologies and [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) that comprise VoIP. Today, VoIP is a highly efficient method for both audio and video real-time* communications.

VoIP has been widely adopted. In many industries it is the dominant form of telephone system, replacing landlines (whose technical name is "public switched telephone network").

VoIP offers several advantages over landlines. It is more flexible, it is easier to add lines, it is often cheaper than traditional telephone service, it supports video as well as audio, and it can be accessed from anywhere.

However, VoIP is vulnerable to service disruptions and cyber attacks that landline phones are mostly immune to ([such as DDoS attacks](https://blog.cloudflare.com/attacks-on-voip-providers/)). VoIP is also dependent on a reliable Internet connection and power source.

*_Real time means messages from all connected users are delivered as soon as they are created, rather than being stored for later transmission._

## How does audio travel via VoIP?

Suppose Alice calls Bob using a VoIP telephone line. Alice picks up a VoIP-enabled handset, dials Bob's number, and says, "Hello, Bob." What has to happen for Alice's words to reach Bob?

  * **Establish connection:** The VoIP service sets up a digital connection between Alice's handset and Bob's. Specialized networking protocols handle this part of the process.

  * **Analog to digital:** Alice's handset converts the sound of her voice into digital information.

  * **Encoding:** This digital information is [encoded and compressed](https://www.cloudflare.com/learning/video/video-encoding-formats/) so it can travel across the Internet.

  * **Data packets:** The encoded digital version of Alice's voice is divided into smaller chunks called [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/), each with several headers attached by various networking protocols.

  * **Packets travel across the Internet:** The packets are forwarded, first by Alice's local area network ([LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)) [router](https://www.cloudflare.com/learning/network-layer/what-is-a-router/) and then by various other routers, to a VoIP server within the VoIP service provider's private branch exchange (PBX). The server routes the packets to Bob's phone. The packets are forwarded from network to network until they reach Bob's LAN router, which finally forwards the packets to Bob's handset.

  * **Bob hears Alice:** Steps 2 through 4 are reversed: the packets are reassembled into the compressed digital sound of Alice's voice, then decompressed, then played as sound by the speaker in Bob's handset.




Despite the number of steps involved, the entire process should take milliseconds. Ideally, there is no human-discernable delay, and Bob hears Alice say "Hello, Bob" almost as soon as she says it on her end. The amount of delay depends on the efficiency and bandwidth of their local networks, and the distance between Alice and Bob (delays caused by distance are known as [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)).

Once a connection is established, the rest of the process can happen simultaneously on both ends. A VoIP-enabled phone can both send and receive audio data at the same time, so if Alice and Bob accidentally ask each other "How are you doing?" at the same time, they will hear each other as they speak.

## What does the 'Internet Protocol' part of VoIP mean?

Data that transfers over the Internet, whether it is text and code (as in this webpage), images, or audio content (as in VoIP), is divided into small sections called "packets." These packets travel over the wires and equipment that make up the Internet and are then interpreted into usable content by the device that receives them.

The [Internet Protocol (IP)](https://www.cloudflare.com/learning/network-layer/internet-protocol/) is the standardized method of formatting data packets that makes networking possible. IP describes how to address these packets and how to provide information about their contents, among other requirements. Any Internet-capable device can automatically create and interpret IP packets. Essentially all Internet services are built on IP, including VoIP — hence the name "voice over IP."

## What protocols does VoIP use on top of IP?

Several protocols run on top of IP to make different types of Internet services possible. First are transport protocols, which help ensure packets arrive in the right place and are received correctly. IP can be used with the [Transmission Control Protocol (TCP)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) or the [User Datagram Protocol (UDP)](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/).

Most VoIP services use UDP as their transport protocol instead of TCP, because UDP is faster — this contrasts with one-to-many [streaming](https://www.cloudflare.com/learning/video/what-is-streaming/) services, which use the more reliable TCP to ensure every second of audio and video gets delivered.

Application layer protocols are used on top of the transport protocols. These protocols put data into a form that user-facing applications can interpret. Much of the Internet uses the hypertext transfer protocol ([HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)) as the application layer protocol. However, VoIP uses other protocols that are better suited to transferring audio and video data in real time than HTTP is.

VoIP application layer protocols vary depending on the VoIP service. Some providers use open protocols like the following:

  * **Session Initiation Protocol (SIP)** sets up and ends calls. In the example above, Alice's VoIP service probably used SIP to begin the connection between her phone and Bob's phone.

  * **Real-time Transport Protocol (RTP)** carries the actual audio and video content of a call.

  * **Secure Real-time Transport Protocol (SRTP)** is the [encrypted](https://www.cloudflare.com/learning/ssl/what-is-encryption/) version of RTP.

  * **Media Gateway Control Protocol (MGCP)** controls connections between VoIP and the public switched telephone network.

  * **H.323** performs the same function as SIP, but it is binary-based instead of text-based. H.323 is not used as much today.




These protocols are publicly documented and anyone can use them. However, some VoIP providers use proprietary protocols. Unlike the open protocols that make the Internet possible and carry most Internet traffic, these proprietary protocols are closed and reverse-engineering them may be forbidden by the providers' terms of service. They still operate on top of open protocols like TCP, UDP, and IP.

Examples of proprietary protocols for VoIP include:

  * **Skype protocol:** This protocol was developed by Skype for use only with the Skype application. Microsoft deprecated this protocol in 2014 after acquiring Skype and replaced it with:

  * **Microsoft Notification Protocol 24 (MNP24):** Skype has used this protocol since 2014.

  * **Skinny Client Control Protocol (SCCP):** This proprietary protocol belongs to Cisco.

  * **Inter-Asterisk eXchange (IAX):** For use with VoIP services that use a specific type of open-source PBX software called Asterisk.




## What causes VoIP service disruptions?

**Poor Internet connection:** A low-bandwidth Internet connection makes it difficult for packets to get through, impacting the quality of audio. No Internet connection means VoIP cannot work at all.

**Network congestion:** If too much data is being exchanged over a network at once, VoIP calls may not transfer data packets efficiently — just as a large amount of traffic on a highway slows down travel times.

**UDP timeouts:** As described above, VoIP usually runs on the UDP transport protocol. [Firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/) may terminate UDP connections past a certain time for security reasons.

**Cyber attacks:** Like any Internet-based service, VoIP is vulnerable to attack. In particular, VoIP services are often targeted for [distributed denial-of-service (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attacks. These attacks can take VoIP services offline for minutes, hours, or days at a time.

## Why is VoIP vulnerable to distributed denial-of-service (DDoS) attacks?

Almost any networking protocol can be used to initiate a DDoS attack. Attackers are often motivated to target VoIP because such attacks have the immediate effect of hampering business productivity — a business that cannot make phone calls will not get much done.

Broadly speaking, VoIP DDoS attacks fall into two different categories:

**1\. Attacks directed at VoIP service providers.** Such DDoS attacks can potentially knock out service for all the VoIP providers' customers, and they can take many forms, including:

  * Targeting the providers' web applications to prevent users from logging in

  * Targeting the providers' servers to crash their PBX service

  * Taking down [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) resolution so that users cannot navigate to the providers' websites




Some attacks directed at VoIP providers exploit the way VoIP works — for instance, via SIP floods that overwhelm servers that support SIP. Others may use more generic DDoS attack methods that are effective against most unprotected websites and servers, such as [HTTP floods](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/) and [SYN floods](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/).

In addition, [ransom DDoS attacks](https://www.cloudflare.com/learning/ddos/ransom-ddos-attack/) have been carried out against VoIP providers. In a ransom DDoS attack, the attack [continues](https://www.cloudflare.com/the-net/ransom-ddos/) until the victim pays the attacker a ransom.

**2\. Attacks directed at organizations that use VoIP.** These attacks focus on one organization at a time instead of disrupting service for multiple VoIP provider customers. Organizations that host their own VoIP network and servers may be particularly vulnerable. Unlike a large VoIP provider, they likely do not have a large number of backup servers to switch to if their primary VoIP servers are targeted for a SIP flood or another attack.

#### SIP floods in VoIP

One of the most-targeted aspects of VoIP in DDoS attacks is SIP. SIP-based DDoS attacks are difficult to stop because, like HTTP, SIP is a text-based protocol and illegitimate SIP requests are tough to distinguish from legitimate SIP requests.

SIP INVITE floods overwhelm an SIP server with fake "INVITE" requests to start a call. The server has to process each of these requests, slowing or denying service for legitimate calls. SIP REGISTER floods are similar, using "REGISTER" messages instead of "INVITE."

Attackers can also send specially constructed SIP messages that disrupt a server by causing it to restart or partially fail. Sending such messages over and over can deny service for legitimate users for a long period of time.

Cloudflare DDoS mitigation helps protect against VoIP DDoS attacks. Cloudflare has network capacity many times larger than the [largest DDoS attacks](https://www.cloudflare.com/learning/ddos/famous-ddos-attacks/) ever recorded. Learn about [Cloudflare DDoS Protection](https://www.cloudflare.com/ddos/) for web applications or [Magic Transit](https://www.cloudflare.com/magic-transit/) for protecting on-premise networks.
