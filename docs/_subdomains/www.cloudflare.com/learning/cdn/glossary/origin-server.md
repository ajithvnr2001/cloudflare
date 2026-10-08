---
url: https://www.cloudflare.com/learning/cdn/glossary/origin-server/
title: What is an origin server? | Origin server definition
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:16.121124+00:00
---

# What is an origin server? | Origin server definition

> Source: https://www.cloudflare.com/learning/cdn/glossary/origin-server/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is an origin server? | Origin server definition 

The purpose of an origin server is to process and respond to incoming Internet requests from Internet clients. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define an origin server 
  * Differentiate an origin server from a CDN edge server 
  * Explain the limits of CDN origin server protection 



On this page

  * What is an origin server?

  * What is the difference between an origin server and a CDN edge server?

  * Can an origin server still be attacked while using a CDN?




## What is an origin server?

The purpose of an origin server is to process and respond to incoming Internet requests from Internet clients. The concept of an origin server is typically used in conjunction with the concept of an [edge server](https://www.cloudflare.com/learning/cdn/glossary/edge-server/) or [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) server. At its core, an origin server is a computer running one or more programs that are designed to listen for and process incoming Internet requests. An origin server can take on all the responsibility of serving up the content for an Internet property such as a website, provided that the traffic does not extend beyond what the server is capable of processing and [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) is not a primary concern.

The physical distance between an origin server and a client making a request adds latency to the connection, increasing the time it takes for an internet resource such as a webpage to be loaded. The additional [round-trip time (RTT)](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/) between client and origin server required for a secure Internet connection using [SSL/TLS](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/) also add additional latency to the request, directly impacting the experience of the client requesting data from the origin. By using a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) round-trip time is able to be reduced, and the amount of requests to an origin server are also able to be reduced.

## What is the difference between an origin server and a CDN edge server?

Put simply, CDN edge servers are computers placed in important junctures between major Internet providers in locations across the globe in order to deliver content as quickly as possible. An edge server lives inside a CDN on the “[edge](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)” of a network and is specifically designed to quickly process requests. By placing edge servers strategically inside of the [Internet exchange points (IxPs)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/) that exist between networks, a CDN is able to reduce the amount of time it takes to get to a particular location on the Internet.

These edge servers cache content in order to take the load off of one or more origin servers. By moving static assets like images, HTML, and JavaScript files (and potentially other content) as close as possible to the requesting client machine, an edge server cache is able to reduce the amount of time it takes for a web resource to load. Origin servers still have an important function to play when using a CDN, as important [server-side code](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) such as the database of hashed client credentials used for authentication is typically maintained inside an origin server.

Here's a simple example of how an edge server and an origin server work together to serve up a login page and allow a user to login to a service. A very simple login page requires the following static assets to be downloaded for the webpage to render properly:

  * A HTML file for the webpage

  * A CSS file for the webpage styling

  * Several image files

  * Several JavaScript libraries




These files are all static files; they are not dynamically generated and are the same for all visitors to the website. As a result, these files can be both cached and served to the client from the edge server. All of these files can be loaded closer to the client machine and without any bandwidth consumption by the origin.

![CDN edge cache response](https://www.cloudflare.com/img/learning/cdn/performance/cdn-caching-second-request.png)CDN edge cache response

Next, when the user enters their login and password and presses “login,” the request for dynamic content travels back to the edge server who then proxies the request back to the origin server. The origin then verifies the user's identity in the associated database table before sending back the specific account information.

![CDN uncached origin fetch diagram](https://www.cloudflare.com/img/learning/cdn/glossary/origin-server/origin-fetch-diagram.png)CDN uncached origin fetch diagram

This interplay between edge servers handling static content and origin servers serving up dynamic content is a typical separation of concerns when using a CDN. The capability of some CDNs can also extend beyond this simplistic model.

## Can an origin server still be attacked while using a CDN?

The short answer is yes. A CDN does not render an origin server invincible, but when used properly it can render an origin server invisible, acting as a shield for incoming requests. Hiding the real [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of an origin server is an important part of setting up a CDN. As such, a CDN provider should recommend that the IP address of the origin server be changed when implementing a CDN strategy in order to prevent [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) from going around the shield and hitting the origin directly. [Cloudflare's CDN](https://www.cloudflare.com/application-services/products/cdn/) includes comprehensive DDoS protection.
