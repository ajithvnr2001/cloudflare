---
url: https://www.cloudflare.com/learning/cdn/glossary/anycast-network/
title: What is Anycast? How does Anycast Work?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:11.173212+00:00
---

# What is Anycast? How does Anycast Work?

> Source: https://www.cloudflare.com/learning/cdn/glossary/anycast-network/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is Anycast? | How does Anycast work? 

Anycast is a network addressing and routing method in which incoming requests can be routed to a variety of different locations. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain Anycast network routing 
  * Differentiate between Anycast and Unicast 
  * See how Anycast mitigates DDoS attacks 



Related content  [ What is a CDN? ](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[ CDN performance ](https://www.cloudflare.com/learning/cdn/performance/)

On this page

  * What is Anycast?

  * How does Anycast work?

  * Why use an Anycast network?

  * What is the difference between Anycast and Unicast?

  * How does an Anycast network mitigate a DDoS attack?




## What is Anycast?

Anycast is a network addressing and routing method in which incoming requests can be routed to a variety of different locations or “nodes.” In the context of a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/), Anycast typically routes incoming traffic to the nearest [data center](https://www.cloudflare.com/learning/cdn/glossary/data-center/) with the capacity to process the request efficiently. Selective routing allows an Anycast network to be resilient in the face of high traffic volume, network congestion, and [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/).

![Anycast CDN diagram](https://www.cloudflare.com/img/learning/cdn/glossary/anycast/anycast-cdn.png)Anycast CDN diagram

## How does Anycast work?

Anycast network routing is able to route incoming connection requests across multiple data centers. When requests come into a single [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) associated with the Anycast network, the network distributes the data based on some prioritization methodology. The selection process behind choosing a particular data center will typically be optimized to reduce [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) by selecting the data center with the shortest distance from the requester. Anycast is characterized by a 1-to-1 of many association, and is one of the 5 main network protocol methods used in the Internet protocol.

## Why use an Anycast network?

If many requests are made simultaneously to the same [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/), the server may become overwhelmed with traffic and be unable to respond efficiently to additional incoming requests. With an Anycast network, instead of one origin server taking the brunt of the traffic, the load can also be spread across other available data centers, each of which will have servers capable of processing and responding to the incoming request. This [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) method can prevent an origin server from extending capacity and avoids service interruptions to clients requesting content from the origin server.

## What is the difference between Anycast and Unicast?

Most of the Internet works via a routing scheme called Unicast. Under Unicast, every node on the network gets a unique IP address. Home and office networks use Unicast; when a computer is connected to a wireless network and gets a message saying the IP address is already in use, an IP address conflict has occurred because another computer on the same Unicast network is already using the same IP. In most cases, that isn't allowed.

![Unicast CDN diagram](https://www.cloudflare.com/img/learning/cdn/glossary/anycast/unicast-cdn.png)Unicast CDN diagram

When a CDN is using a Unicast address, traffic is routed directly to the specific node. This creates a vulnerability when the network experiences extraordinary traffic such as during a DDoS attack. Because the traffic is routed directly to a particular data center, the location or its surrounding infrastructure may become overwhelmed with traffic, potentially resulting in [denial-of-service](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/) to legitimate requests.

Using Anycast means the network can be extremely resilient. Because traffic will find the best path, an entire data center can be taken offline and traffic will automatically flow to a proximal data center.

## How does an Anycast network mitigate a DDoS attack?

After other DDoS mitigation tools filter out some of the attack traffic, Anycast distributes the remaining attack traffic across multiple data centers, preventing any one location from becoming overwhelmed with requests. If the capacity of the Anycast network is greater than the attack traffic, the attack is effectively mitigated. In most DDoS attacks, many compromised "zombie" or [“bot”](https://www.cloudflare.com/learning/bots/what-is-a-bot/) computers are used to form what is known as a [botnet](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/). These machines can be scattered around the web and generate so much traffic that they can overwhelm a typical Unicast-connected machine.

![Anycast/Unicast under attack](https://www.cloudflare.com/img/learning/cdn/glossary/anycast/anycast-unicast-botnet-attack.png)Anycast/Unicast under attack

A properly Anycasted CDN increases the surface area of the receiving network so that the unfiltered denial-of-service traffic from a distributed botnet will be absorbed by each of the CDN’s data centers. As a result, as a network continues to grow in size and capacity it becomes harder and harder to launch an effective DDoS against anyone using the CDN.

It is not easy to setup a true Anycasted network. Proper implementation requires that a CDN provider maintains their own network hardware, builds direct relationships with their upstream carriers, and tunes their networking routes to ensure traffic doesn't "flap" between multiple locations. This [Cloudflare blog post](https://blog.cloudflare.com/cloudflares-architecture-eliminating-single-p/) explains how Cloudflare uses Anycast to load balance without load balancers.
