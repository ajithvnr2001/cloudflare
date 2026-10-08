---
url: https://www.cloudflare.com/learning/cdn/what-is-caching/
title: What is Caching? | How is a Website Cached?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:55.173777+00:00
---

# What is Caching? | How is a Website Cached?

> Source: https://www.cloudflare.com/learning/cdn/what-is-caching/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is caching? 

Caches store copies of files in order to deliver them more quickly where they are needed. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how caching works 
  * Understand how and when content is cached 
  * Understand the different kinds of caching 
  * Learn how CDNs cache content 



Related content  [ CDN performance ](https://www.cloudflare.com/learning/cdn/performance/)[ What is a CDN? ](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)

On this page

  * What is caching?

  * What does a browser cache do?

  * What does clearing a browser cache accomplish?

  * What is CDN caching?

  * What is a CDN cache hit? What is a cache miss?

  * Where are CDN caching servers located?

  * How long does cached data remain in a CDN server?

  * How do other kinds of caching work?

  * How does Cloudflare use caching?




## What is caching?

Caching is the process of storing copies of files in a cache, or temporary storage location, so that they can be accessed more quickly. Technically, a cache is any temporary storage location for copies of files or data, but the term is often used in reference to Internet technologies. Web browsers cache HTML files, JavaScript, and images in order to load websites more quickly, while [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) servers cache [DNS records](https://www.cloudflare.com/learning/dns/dns-records/) for faster lookups and [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) servers cache content to reduce [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/).

To understand how caches work, consider real-world caches of food and other supplies. When explorer Roald Amundsen made his return journey from his trip to the South Pole in 1912, he and his men subsisted on the caches of food they had stored along the way. This was much more efficient than waiting for supplies to be delivered from their base camp as they traveled. Caches on the Internet serve a similar purpose; they temporarily store the 'supplies', or content, needed for users to make their journey across the web.

## What does a browser cache do?

Every time a user loads a webpage, their browser has to download quite a lot of data in order to display that webpage. To shorten [page load times](https://www.cloudflare.com/learning/performance/speed-up-a-website/), browsers cache most of the content that appears on the webpage, saving a copy of the webpage's content on the device’s hard drive. This way, the next time the user loads the page, most of the content is already stored locally and the page will load much more quickly.

Browsers store these files until their [time to live (TTL)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/) expires or until the hard drive cache is full. (TTL is an indication of how long content should be cached.) Users can also clear their browser cache if desired.

## What does clearing a browser cache accomplish?

Once a browser cache is cleared, every webpage that loads will load as if it is the first time the user has visited the page. If something loaded incorrectly the first time and was cached, clearing the cache can allow it to load correctly. However, clearing one's browser cache can also temporarily slow page load times.

## What is CDN caching?

A CDN, or content delivery network, caches content (such as images, videos, or webpages) in proxy servers that are located closer to end users than [origin servers](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). (A proxy server is a server that receives requests from [clients](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) and passes them along to other servers.) Because the servers are closer to the user making the request, a CDN is able to deliver content more quickly.

![Content Delivery Network \(CDN\)](https://www.cloudflare.com/img/learning/cdn/what-is-a-cdn/what-is-a-cdn.png)Content Delivery Network (CDN)

Think of a CDN as being like a chain of grocery stores: Instead of going all the way to the farms where food is grown, which could be hundreds of miles away, shoppers go to their local grocery store, which still requires some travel but is much closer. Because grocery stores stock food from faraway farms, grocery shopping takes minutes instead of days. Similarly, CDN caches 'stock' the content that appears on the Internet so that webpages load much more quickly.

When a user requests content from a website using a CDN, the CDN fetches that content from an origin server, and then saves a copy of the content for future requests. Cached content remains in the CDN cache as long as users continue to request it.

## What is a CDN cache hit? What is a cache miss?

A [cache hit](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/) is when a client device makes a request to the cache for content, and the cache has that content saved. A cache miss occurs when the cache does not have the requested content.

A cache hit means that the content will be able to load much more quickly, since the CDN can immediately deliver it to the end user. In the case of a cache miss, a CDN server will pass the request along to the origin server, then cache the content once the origin server responds, so that subsequent requests will result in a cache hit.

## Where are CDN caching servers located?

CDN caching servers are located in [data centers](https://www.cloudflare.com/learning/cdn/glossary/data-center/) all over the globe. Cloudflare has CDN servers in 335+ cities spread out throughout the world in order to be as close to end users accessing the content as possible. A location where CDN servers are present is also called a data center.

## How long does cached data remain in a CDN server?

When websites respond to CDN servers with the requested content, they attach the content’s TTL as well, letting the servers know how long to store it. The TTL is stored in a part of the response called the [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) header, and it specifies for how many seconds, minutes, or hours content will be cached. When the TTL expires, the cache removes the content. Some CDNs will also purge files from the cache early if the content is not requested for a while, or if a CDN customer manually purges certain content.

## How do other kinds of caching work?

**DNS caching** takes place on DNS servers. The servers store recent DNS lookups in their cache so that they do not have to query nameservers and can instantly reply with the [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of a domain.

**Search engines** may cache webpages that frequently appear in search results in order to answer user queries even if the website they are attempting to access is temporarily down or unable to respond.

## How does Cloudflare use caching?

Cloudflare [offers a CDN](https://www.cloudflare.com/application-services/products/cdn/) with 335+ PoPs distributed internationally. Cloudflare offers free CDN caching services, while paid CDN customers are able to customize how their content is cached. The network is [Anycast](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/), meaning the same content can be delivered from any of these data centers. A user in London and a user in Sydney can both view the same content loaded from CDN servers only a few miles away.
