---
url: https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/
title: What is a Cache Hit Ratio?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:44.951008+00:00
---

# What is a Cache Hit Ratio?

> Source: https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is a cache hit ratio? 

A cache hit ratio is calculated by dividing the number of cache hits by the total number of cache hits and misses, and it measures how effective a cache is at fulfilling requests for content. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the difference between a cache hit and a cache miss 
  * Learn how to calculate cache hit ratio 
  * Understand the importance of cache hit ratio for CDNs 



Related content  [ What is caching? ](https://www.cloudflare.com/learning/cdn/what-is-caching/)[ CDN performance ](https://www.cloudflare.com/learning/cdn/performance/)[ CDN reliability and load balancing ](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)[ CDN SSL/TLS security ](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[ How can using a CDN reduce bandwidth costs? ](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)

On this page

  * What is a cache hit ratio?

  * What is a cache hit?

  * What is a cache miss?

  * What is a good CDN cache hit ratio for most websites?

  * Does a high cache hit ratio always mean a CDN is effective?




## What is a cache hit ratio?

Cache hit ratio is a measurement of how many content requests a cache is able to fill successfully, compared to how many requests it receives. A [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) provides a type of [cache](https://www.cloudflare.com/learning/cdn/what-is-caching/), and a high-performing CDN will have a high cache hit ratio.

The formula for calculating a cache hit ratio is as follows:

![Cache hit ratio equation](https://images.ctfassets.net/slt3lc6tev37/9tqnmxxbqjmGcBQPvMgJN/a804f98a247f09bd21e42c398c507e96/cache-hit-ratio.svg)Cache hit ratio equation

For example, if a CDN has 39 cache hits and 2 cache misses over a given timeframe, then the cache hit ratio is equal to 39 divided by 41, or 0.951. The cache hit ratio can also be expressed as a percentage by multiplying this result by 100. As a percentage, this would be a cache hit ratio of 95.1%.

Cache hit ratio is a metric that applies to any cache; it's not just for measuring [CDN performance](https://www.cloudflare.com/learning/cdn/performance/). However, it is an especially important benchmark for CDNs. Most CDN services will provide customers with this metric within their user interface or dashboard.

## What is a cache hit?

A "cache hit" occurs when a file is requested from a cache and the cache is able to fulfill that request. For instance, if a user visits a webpage that's supposed to display a picture of a cat playing a piano, the browser may send a request to the webpage's CDN for this picture. If the CDN has a copy of the picture in its storage, then the request results in a cache hit, and the picture is sent to the browser.

## What is a cache miss?

A cache miss is when the cache does not contain the requested content. If a copy of the cat-playing-piano picture is not currently in the CDN cache, this request results in a cache miss, and the request is passed along to the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) for the original picture. The CDN server will cache the photo once the origin server responds, so that additional requests for it will result in a cache hit.

## What is a good CDN cache hit ratio for most websites?

A typical website that's mostly made up of static content could easily have a cache hit ratio in the 95-99% range. However, getting this metric as high as possible isn't the only goal of a CDN. Additionally, a website with lots of dynamic content may have a much lower cache hit ratio (although caching dynamic content is becoming possible).

## Does a high cache hit ratio always mean a CDN is effective?

Cache hit ratio is not the last word in CDN performance; other factors are extremely important in assessing a CDN's effectiveness as well. For instance, [where the content is served from](https://www.cloudflare.com/learning/cdn/performance/) is also important. Ideally, a CDN will serve content from the CDN server closest to the end user. If this doesn't occur, the CDN's performance will not be optimal. The [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) is built to serve any content from any of our 335+ locations around the world. Any content that is cached in one data center) can be served from every other data center as well.

[Caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) is an important part of what a CDN does, but its main purpose is to make web properties faster and more reliable in general. A variety of [performance metrics](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/) help measure how much a CDN has helped to speed up a web app or website.
