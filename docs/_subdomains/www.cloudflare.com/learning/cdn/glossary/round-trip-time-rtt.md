---
url: https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/
title: What is round-trip time? | RTT definition
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:16.853476+00:00
---

# What is round-trip time? | RTT definition

> Source: https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is round-trip time? | RTT definition 

Round-trip time (RTT) is the duration in milliseconds (ms) it takes for a network request to go from a starting point to a destination and back again to the starting point 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define round-trip time (RTT) 
  * Understand how to use RTT 
  * Explain factors that can affect RTT 
  * Understand ways in which a CDN can reduce RTT 



On this page

  * What is round-trip time?

  * How does round-trip time work?

  * What are common factors that affect RTT?

    * List of factors affecting RTT:

  * How can a CDN improve RTT?




## What is round-trip time?

Round-trip time (RTT) is the duration in milliseconds (ms) it takes for a network request to go from a starting point to a destination and back again to the starting point. RTT is an important metric in determining the health of a connection on a local network or the larger Internet, and is commonly utilized by network administrators to diagnose the speed and reliability of network connections.

Reducing RTT is a primary goal of a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/). Improvements in [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) can be measured in the reduction of round-trip time and by eliminating instances where roundtrips are required, such as by modifying the standard [TLS/SSL handshake](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/).

The ping utility, available on virtually all computers, is a method of estimating round-trip time. Here's an example of several pings to Google with the round-trip time calculated at the bottom. Notice that one of the ping times - 17.604ms - is higher than the rest.

![Ping RTT example](https://www.cloudflare.com/img/learning/cdn/glossary/round-trip-time-rtt/ping-rtt.png)Ping RTT example

## How does round-trip time work?

Round-trip time represents the amount of time it takes data to go roundtrip to another location. Borrowing from the [lesson on CDN latency benefits](https://www.cloudflare.com/learning/cdn/performance/), let's say that a user in New York wants to contact a server in Singapore.

When the user in New York makes the request, the network traffic is transferred across many different routers in different physical locations before terminating at the server in Singapore. The server in Singapore then sends a response back across the Internet to the location in New York. Once the request terminates in New York, a rough estimate can be made of the amount of time it takes to go round trip between the two locations.

![Round-trip time map](https://www.cloudflare.com/img/learning/cdn/glossary/round-trip-time-rtt/round-trip-time-rtt-map.png)Round-trip time map

It's important to keep in mind that round-trip time is an estimate and not a guarantee; the pathway between the two locations can change over time and other factors such as network congestion can come into play, affecting the overall transit time. Regardless, RTT is an important metric in understanding if a connection can be made, and if so, roughly how long it will take to make the trip.

## What are common factors that affect RTT?

Infrastructure components, network traffic, and physical distance along the path between a source and a destination are all potential factors that can affect RTT.

#### List of factors affecting RTT:

  * **The nature of the transmission medium** \- the way in which connections are made affects how fast the connection moves; connections made over optical fiber will behave differently than connections made over copper. Likewise, a connection made over a wireless frequency will behave differently than that of a satellite communication.

  * **Local area network (LAN) traffic** \- the amount of traffic on the local area network can bottleneck a connection before it ever reaches the larger Internet. For example, if many users are using streaming video service simultaneously, round-trip time may be inhibited even though the external network has excess capacity and is functioning normally.

  * **Server response time** – the amount of time it takes a server to process and respond to a request is a potential bottleneck in network latency. When a server is overwhelmed with requests, such as during a [DDoS attack](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/), its ability to respond efficiently can be inhibited, resulting in increased RTT.

  * **Node count and congestion** – depending on the path that a connection takes across the Internet, it may be routed or “hop” through a different number of intermediate nodes. Generally speaking, the greater the number of nodes a connection touches the slower it will be. A node may also experience network congestion from other network traffic, which will slow down the connection and increase RTT.

  * **Physical distance** – although a connection optimized by a CDN can often reduce the number of hops required to reach a destination, there is no way of getting around the limitation imposed by the speed of light; the distance between a start and end point is a limiting factor in network connectivity that can only be reduced by moving content closer to the requesting users. To overcome this obstacle, a CDN will cache content closer to the requesting users, thereby reducing RTT.




## How can a CDN improve RTT?

By maintaining servers inside [internet exchange points](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/) and by having preferred relationships with Internet service providers and other network carriers, a CDN is able to optimize network pathways between locations, resulting in reduced RTT and improved latency for visitors accessing content cached inside the CDN.

Explore the CDN performance lesson to learn how caching, data center placement, file size reductions, and other optimizations reduce latency and improve RTT. Learn how using the [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) improves RTT.
