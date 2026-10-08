---
url: https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/
title: What is time-to-live (TTL)? | TTL definition
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:18.254605+00:00
---

# What is time-to-live (TTL)? | TTL definition

> Source: https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is time-to-live (TTL)? | TTL definition 

Time to live (TTL) refers to the amount of time or “hops” that a packet is set to exist inside a network before being discarded by a router. TTL is also used in other contexts including CDN caching and DNS caching. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define time-to-live (TTL) 
  * Explain how TTL is used in networking 
  * Know a few other contexts that use TTL 



Related content  [ CDN reliability and load balancing ](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

On this page

  * What is time-to-live in networking?

  * How does TTL work?

  * In what other circumstances is TTL used?




## What is time-to-live (TTL) in networking?

Time to live (TTL) refers to the amount of time or “hops” that a packet is set to exist inside a network before being discarded by a router. TTL is also used in other contexts including [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) caching and DNS caching.

## How does TTL work?

When a packet of information is created and sent out across the Internet, there is a risk that it will continue to pass from router to router indefinitely. To mitigate this possibility, packets are designed with an expiration called a time-to-live or hop limit. Packet TTL can also be useful in determining how long a packet has been in circulation, and allow the sender to receive information about a packet’s path through the Internet.

Each packet has a place where it stores a numerical value determining how much longer it should continue to move through the network. Every time a [router](https://www.cloudflare.com/learning/network-layer/what-is-a-router/) receives a packet, it subtracts one from the TTL count and then passes it onto the next location in the network. If at any point the TTL count is equal to zero after the subtraction, the router will discard the packet and send an [ICMP message](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/) back to the originating host.

The commonly used network commands ping and traceroute both utilize TTL. When using the traceroute command, a stream of packets with increasingly higher sequential TTLs are sent across the Internet towards a destination. Because each step along the connection is the last stop for one of the packets, each location will return an ICMP message to the sender after discarding the packet. The time it takes for the ICMP message to return to the sender is then used to determine how long it takes to get to each successive hop along the network.

![ICMP traceroute diagram](https://www.cloudflare.com/img/learning/cdn/glossary/ttl/icmp-traceroute-diagram.png)ICMP traceroute diagram

## In what other circumstances is TTL used?

Apart from tracing the route packets take across the Internet, time-to-live is used in the context of [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) information for a set period of time. Instead of measuring time in hops between routers, each of which can take a variable amount of time, some networking use cases operate in a more traditional fashion.

CDN's like [Cloudflare's CDN](https://www.cloudflare.com/application-services/products/cdn/) commonly use a TTL to determine how long cached content should be served from a CDN edge server before a new copy will be fetched from an origin server. By properly setting the amount of time between origin server pulls, a CDN is able to serve updated content without requests continuously propagating back to the origin. This optimization allows a CDN to efficiently serve content closer to a user while reducing the bandwidth required from the origin.

In the context of a [DNS record](https://www.cloudflare.com/learning/dns/dns-records/), TTL is a numerical value that determines how long a DNS cache server can serve a DNS record before reaching out to the authoritative DNS server and getting a new copy of the record.
