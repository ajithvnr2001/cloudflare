---
url: https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/
title: What Is Cache-Control? Cache Explained
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:19.669950+00:00
---

# What Is Cache-Control? Cache Explained

> Source: https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is cache-control? | Cache explained 

Cache control dictates caching behavior for a website, letting browsers know how often to refresh locally stored resources. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define cache control 
  * Describe browser caching 
  * Outline several cache-control directives 



Related content  [ What is a CDN? ](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[ CDN performance ](https://www.cloudflare.com/learning/cdn/performance/)[ CDN SSL/TLS security ](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)

On this page

  * What is cache-control?

  * What is browser caching?

  * What are HTTP headers?

  * What is in a cache-control header?

    * cache-control: private

    * cache-control: public

    * cache-control: no-store

    * cache-control: no-cache

    * cache-control: max-age

    * cache-control: s-maxage

  * Why does cache-control matter?




## What is cache-control?

Cache-control is an [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) header that dictates browser [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) behavior. In a nutshell, when someone visits a website, their browser will save certain resources, such as images and website data, in a store called the cache. When that user revisits the same website, cache-control sets the rules which determine whether that user will have those resources loaded from their local cache, or whether the browser will have to send a request to the server for fresh resources. In order to understand cache-control in greater depth, a basic understanding of browser caching and HTTP headers is required.

## What is browser caching?

As explained above, browser caching is when a web browser saves website resources so it doesn’t have to fetch them again from a server. For example, a background image on a website might be saved locally in cache so that when a user visits that page for the second time, the image will load from the user’s local files and the page will load much faster.

Browsers will only store these resources for a specified period of time, known as the [time to live (TTL)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/). If a user requests a cached resource after the TTL has expired, the browser will have to reach out to the server again and download a fresh copy of the resource. How do browsers and web servers know the TTL for each resource? This is where HTTP headers come into play.

## What are HTTP headers?

The Hypertext Transfer Protocol (HTTP) outlines the syntax for communications on the World Wide Web, and this communication consists of requests from clients to servers and responses from servers back to clients. These HTTP requests and responses each come stamped with a series of key-value pairs called headers.

These headers contain a lot of important information about each communication. For example, a request header usually contains:

  * Information on what resource is being requested

  * Which browser the client is using

  * What data formats the client will accept




Response headers often include information on:

  * Whether or not the request was successfully fulfilled

  * The language and format of any resources in the body of the response.




A cache-control header can appear in both HTTP requests and responses.

## What is in a cache-control header?

Headers consist of key-value pairs which are separated by a colon. For cache-control, the ‘key’, or the part to the left of the colon, is always ‘cache-control’. The ‘value’ is what’s found on the right of the colon, and there can be one or several comma-separated values for cache control.

![Example Cache Control Header](https://www.cloudflare.com/img/learning/cdn/glossary/what-is-cache-control/cache-control-header.png)Example Cache Control Header

These values are called directives, and they dictate who can cache a resource as well as how long those resources can be cached before they must be updated. Below we go through some of the most common cache-control directives:

#### cache-control: private

A response with a ‘private’ directive can only be cached by the client and never by an intermediary agent, such as a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) or a proxy. These are often resources containing private data, such as a website displaying a user’s personal information.

#### cache-control: public

Conversely, the ‘public’ directive means the resource can be stored by any cache.

#### cache-control: no-store

A response with a ‘no-store’ directive cannot be cached anywhere, ever. This means that every time a user requests this data, a request must be sent to the origin server for a fresh copy. This directive is typically reserved for resources that contain extremely sensitive data, such as bank account information.

#### cache-control: no-cache

This directive means that cached versions of the requested resource cannot be used without first checking to see if there is an updated version. This is typically done using an ETag.

An ETag is another HTTP header which contains a token unique to the version of the resource at the time it was requested. This token is changed on the origin server whenever the resource is updated.

When a user returns to a page with a ‘no-cache’ resource, the client will always have to connect to the origin server and compare the ETag on the cached resource with one on the server. If the ETags are identical, the cached resource will be provided to the user. If not, this means that the resource has been updated and the client will need to download a fresh version to provide to the user. This process ensures that the user is always getting the most up-to-date version of that resource without requiring unnecessary downloads.

#### cache-control: max-age

This directive dictates the time to live, in other words how many seconds a resource can be served from cache after it's been downloaded. For example, if the max age is set to 1800, this means that for 1,800 seconds (30 minutes) after the resource was first requested from the server, the user will be served a cached version of that resource on subsequent requests. If the user requests the resource again after that 30 minutes has expired, the client will have to request a fresh copy from the origin server.

#### cache-control: s-maxage

The ‘s-maxage’ directive is specifically for shared caches such as CDNs, and it dictates how long those shared caches can keep serving up the resource from cache. This directive overrides the ‘max-age’ directive for individual clients.

## Why does cache-control matter?

Browser caching is a great way to both preserve resources and improve user experience on the Internet, but without cache-control, it would be very brittle. Every resource on every site would be bound by the same caching rules, meaning that sensitive information would be cached the same way as public information, and frequently-updated resources would be cached for the same amount of time as ones that rarely change.

Cache-control adds the flexibility that makes browser caching truly useful, letting developers dictate how each resource will be cached. It also lets developers set special rules for intermediaries, which is a factor in why sites that use a CDN, like the [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/), tend to perform better than sites that don’t.
