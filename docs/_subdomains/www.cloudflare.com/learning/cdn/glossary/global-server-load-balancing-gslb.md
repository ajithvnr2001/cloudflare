---
url: https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/
title: What Is GSLB? Load Balancing Explained
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:14.376410+00:00
---

# What Is GSLB? Load Balancing Explained

> Source: https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is global server load balancing (GSLB)? 

Global server load balancing (GSLB) is a method of distributing Internet traffic to a network of servers across the globe, creating a faster and more reliable user experience. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define global server load balancing (GSLB) 
  * Describe how GSLB can create improvements in reliability and performance 



Related content  [ What is a CDN? ](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[ CDN performance ](https://www.cloudflare.com/learning/cdn/performance/)

On this page

  * What is GSLB?

  * What is load balancing?

  * How does GSLB reduce latency?

  * How to enable GSLB




## What is GSLB?

Global server load balancing or GSLB is the practice of distributing Internet traffic amongst a large number of connected servers dispersed around the world. The benefits of GSLB include increased reliability and reductions in [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/).

Imagine a store that sells shoes through the mail to customers all over the world. If that shoe store operates out of a single location, it will take a very long time for faraway customers to submit orders and receive their shoes. During busy shopping seasons, the store might get overloaded with orders and lose the ability to fill all their customers’ orders quickly.

![Too Many Orders](https://www.cloudflare.com/img/learning/cdn/glossary/global-server-load-balancing-gslb/overloaded-truck.png)Too Many Orders

Now imagine that the shoe store opens several more locations all over the world. This means customers can order shoes from a nearby location, cutting down on shipping times and reducing the possibility of one store getting overloaded with orders. This is exactly what GSLB does for web sites and services, making it one of the most popular load balancing solutions for companies with a global user base.

## What is load balancing?

[Load balancing](https://www.cloudflare.com/learning/performance/what-is-load-balancing/) is the practice of distributing traffic among two or more servers. Some load balancing technique utilize a ‘dumb’ load balancing strategy, based on randomizing the distribution of traffic. For example [round-robin DNS](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/), a randomized [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) load balancing technique, sends each request to a different server than the last. There are also ‘smart’ load balancing techniques that analyze data in order to decide which is the best server to handle a request. [Anycast routing](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/), for example, picks a server based in part on the quickest travel time between the client and the server.

## How does GSLB reduce latency?

Even before an [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) overloads and stops fulfilling requests, high amounts of traffic to that server can still cause significant latency issues. A GSLB system can distribute that traffic among several different locations, ensuring that no single location is handling so many requests that it causes delay.

Additionally, GSLB can greatly reduce the travel time of requests and responses between users and servers. If a user is in Los Angeles and they are using a web service with a Paris-based origin server, then both the requests and responses will have to travel a very long distance, cut up into smaller travel segments called ‘hops’. This can cause significant delays in load time.

Using GSLB, a worldwide pool of servers ensures that each user can connect to a server that is geographically close to them, minimizing hops and travel time. In the example above, if the Paris-based company was utilizing GSLB, the Los Angeles user could connect to a server within 100 miles of their location, resulting in a much snappier user experience.

## How to enable GSLB

One of the easiest and most cost-effective ways to implement GSLB is through a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/), such as the [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/). A global CDN service will take data from their customers’ origin servers and cache it on a geographically distributed network of servers, providing fast and reliable delivery of Internet content to users around the world.
