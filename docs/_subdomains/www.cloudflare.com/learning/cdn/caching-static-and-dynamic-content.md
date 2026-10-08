---
url: https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/
title: Caching Static and Dynamic Content | How Does It Work?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:01.255328+00:00
---

# Caching Static and Dynamic Content | How Does It Work?

> Source: https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  Caching static and dynamic content: How does it work? 

Unlike static content, dynamic content is different for each user, meaning it cannot be served to multiple users and is difficult to cache. However, caching dynamic content is possible with the right technology. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Differentiate static vs. dynamic content 
  * Learn why dynamic content is difficult to cache, and how new technology makes caching dynamic content possible 
  * Understand the difference between dynamic content caching and dynamic content compression 
  * Learn how Edge Side Includes tags make it possible to cache static parts of a dynamic webpage 



Related content  [ What is caching? ](https://www.cloudflare.com/learning/cdn/what-is-caching/)[ CDN performance ](https://www.cloudflare.com/learning/cdn/performance/)[ CDN reliability and load balancing ](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)[ CDN SSL/TLS security ](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[ How can using a CDN reduce bandwidth costs? ](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)

On this page

  * What is the difference between static and dynamic content?

  * How is static content cached?

  * How does dynamic content caching work?

  * What is the difference between dynamic content caching and dynamic content compression?

  * How does using Edge Side Includes speed up dynamic webpages?




## What is the difference between static and dynamic content?

Static content is any file that is stored in a server and is the same every time it is delivered to users. HTML files and images are examples of this kind of content. Static content is like a newspaper: once an issue of a newspaper is published, it features the same articles and photos all day for everyone who picks up a copy, no matter what new developments transpire during the day.

Dynamic content is content that changes based on factors specific to the user such as time of visit, location, and device. A dynamic webpage will not look the same for everybody, and it can change as users interact with it – like if a newspaper could rewrite itself as someone is reading it. This makes webpages more personalized and more interactive.

![Static webpage](https://images.ctfassets.net/slt3lc6tev37/1wXlf7IjxWvr2ivJyzC9iv/4acfec55339c30d2c01eee7d80c9a183/caching-static-content.svg)Static webpage![Dynamic webpage](https://images.ctfassets.net/slt3lc6tev37/6ijRQV6QxiyG4zyidpgJmi/23088f026f5b01cd671274b9b994096f/caching-dynamic-content.svg)Dynamic webpage

A modern news website is a good example of dynamic content: unlike in a newspaper, articles are updated throughout the day, and the homepage may feature different headlines based on the site visitor's location or login status. Social media pages are another example: the Facebook news feed looks totally different for each user, and users are able to interact with the content in order to change it (by liking, sharing, or commenting on posts).

Dynamic webpages are not stored as static HTML files. Instead, [server-side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) scripts generate an HTML file in response to events, such as user interactions or user logins, and send the HTML file to the web browser. Because dynamic content is generated server-side, it is typically served from [origin servers](https://www.cloudflare.com/learning/cdn/glossary/origin-server/), not a cache.

For a long time, dynamic content was considered uncacheable. But new technologies allow websites to serve dynamic content from a cache, significantly cutting down on [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) while keeping the user experience interactive.

## How is static content cached?

The usual web caching process is for a cache to save a copy of the static file – e.g., an image, – when the content is served, so that it's closer to the user and delivered more quickly the next time. Browsers and [content delivery networks (CDNs)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) can cache static content for a set time period and serve it to users as long as the content continues to be requested. This is possible because static content does not change over time; the same file can be delivered to users over and over.

## How does dynamic content caching work?

Dynamic content is generated by scripts that change the content on a page. By running scripts in a CDN cache instead of in a distant origin server, dynamic content can be generated and delivered from a cache. Dynamic content is thus essentially "cached" and does not have to be served all the way from the origin, reducing the response time to client requests and speeding up dynamic webpages.

[Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/), for example, are [serverless JavaScript functions](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/) that run on the Cloudflare CDN. They can respond to a variety of events and inputs, including device type, time of day, user location, or data from third party APIs. Based on these parameters, dynamic content can be generated and served to client devices, or static content can be altered, cached, or purged from the cache.

Because Cloudflare Workers are JavaScript code, developers can use them to build a wide range of features or an entire application, in addition to caching dynamic content. Additionally, Cloudflare Workers can be deployed and can propagate to CDN locations around the globe in seconds.

Cloudflare Workers run in a lightweight execution environment so that the code can spin up and [execute within milliseconds](https://blog.cloudflare.com/serverless-performance-comparison-workers-lambda/). They allow developers to run code without worrying about configuring a backend. Learn more about [serverless computing](https://www.cloudflare.com/learning/serverless/what-is-serverless/).

## What is the difference between dynamic content caching and dynamic content compression?

Another approach to speeding up dynamic webpages is to compress dynamic content generated by the origin server and deliver it as quickly and efficiently as possible. With dynamic compression, the content still comes from the origin server instead of a cache, but the HTML files generated are made significantly smaller so that they can reach the client device more quickly.

## How does using Edge Side Includes (ESI) speed up dynamic webpages?

Often, a large amount of content on a dynamic webpage remains consistent for all users, and only certain elements on the page are dynamic. This means that much of the HTML code is duplicated in each dynamic copy of the page. To solve for this inefficiency, a number of companies worked together to develop Edge Side Includes (ESI), a markup language that specifies where dynamic content appears on a webpage. (ESI is in use on some CDNs, but is not yet accepted by the W3C, the organization that governs web standards.)

Content with an ESI tag is fetched from somewhere else, while the rest of the webpage's content can be cached. If only some of the webpage is generated dynamically and the rest is cached, the webpage will load much more quickly than if the whole page needed to be generated for each user. [ESI can be combined with Cloudflare Workers](https://blog.cloudflare.com/edge-side-includes-with-cloudflare-workers/) to make the process even more efficient.
