---
url: https://www.cloudflare.com/learning/performance/glossary/what-is-latency/
title: What Is Latency? | How to Fix Latency
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:22.557360+00:00
---

# What Is Latency? | How to Fix Latency

> Source: https://www.cloudflare.com/learning/performance/glossary/what-is-latency/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is latency? | How to fix latency 

Network latency is the amount of time it takes for a data packet to go from one place to another. Lowering latency is an important part of building a good user experience. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what latency is and what causes it 
  * Explain the differences between network latency, bandwidth, and throughput 
  * Learn how to reduce latency 



Related content  [ How to test the speed of a website ](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[ Mobile performance: How to make a site mobile friendly ](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)

On this page

  * What is latency?

  * What causes Internet latency?

    * Network latency, throughput, and bandwidth

  * How can latency be reduced?

  * How can users fix latency on their end?




## What is latency?

Latency is the time it takes for data to pass from one point on a network to another. Suppose Server A in New York sends a [data packet](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) to Server B in London. Server A sends the packet at 04:38:00.000 GMT and Server B receives it at 04:38:00.145 GMT. The amount of latency on this path is the difference between these two times: 0.145 seconds or 145 milliseconds.

Most often, latency is measured between a user's device (the "client" device) and a [data center](https://www.cloudflare.com/learning/cdn/glossary/data-center/). This measurement helps developers understand how quickly a webpage or application will load for users.

Although data on the Internet travels at the speed of light, the effects of distance and delays caused by Internet infrastructure equipment mean that latency can never be eliminated completely. It can and should, however, be minimized. A high amount of latency results in poor website performance, [negatively affects SEO](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/), and can induce users to leave the site or application altogether.

Improve security

Defend against “Top 10” attack techniques

[Learn more →](https://www.cloudflare.com/application-services/products/waf/)

## What causes Internet latency?

One of the principal causes of network latency is distance, specifically the distance between [client](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) devices making requests and the servers responding to those requests. If a website is hosted in a data center in Columbus, Ohio, it will receive requests fairly quickly from users in Cincinnati (about 100 miles away), likely within 5-10 milliseconds. On the other hand, requests from users in Los Angeles (about 2,200 miles away) will take longer to arrive, closer to 40-50 milliseconds.

An increase of a few milliseconds may not seem like a lot, but this is compounded by all the back-and-forth communication necessary for the client and server to establish a connection, the total size and load time of the page, and any problems with the network equipment the data passes through along the way. The amount of time it takes for a response to reach a client device after a client request is known as [round trip time (RTT)](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/). RTT is equal to double the amount of latency, since data has to travel in both directions — there and back again.

Data traversing the Internet usually has to cross not just one, but multiple networks. The more networks that an [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) response needs to pass through, the more opportunities there are for delays. For example, as data packets cross between networks, they go through [Internet Exchange Points (IXPs)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/). There, routers have to process and route the data packets, and at times routers may need to [break them up into smaller packets](https://www.cloudflare.com/learning/network-layer/what-is-mtu/), all of which adds a few milliseconds to RTT.

#### Network latency, throughput, and bandwidth

Latency, bandwidth, and throughput are all interrelated, but they all measure different things. Bandwidth is the maximum amount of data that can pass through the network at any given time. Throughput is the average amount of data that actually passes through over a given period of time. Throughput is not necessarily equivalent to bandwidth, because it is affected by latency and other factors. Latency is a measurement of time, not of how much data is downloaded over time.

Whitepaper

Optimize web performance load balancing best practices

[Read the whitepaper →](https://www.cloudflare.com/lp/load-balancing-best-practices/)

## How can latency be reduced?

Use of a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) (content delivery network) is a major step towards reducing latency. A CDN [caches](https://www.cloudflare.com/learning/cdn/what-is-caching/) static content and serves it to users. (The Cloudflare CDN makes it possible to cache dynamic content as well with [Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/).) CDN servers are distributed in multiple locations so that content is stored closer to end users and does not need to travel as far to reach them. This means that loading a webpage will take less time, [improving website speed and performance](https://www.cloudflare.com/learning/performance/speed-up-a-website/).

Other factors aside from latency can slow down performance as well. Web developers can minimize the number of render-blocking resources (loading JavaScript last, for example), [optimize images](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/) for faster loading, and reduce file sizes wherever possible. [Code minification](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/) is one way of reducing the size of JavaScript and CSS files.

It is possible to improve perceived page performance by strategically loading certain assets first. A webpage can be configured to load the above-the-fold area of a page first so that users can begin interacting with the page even before it finishes loading (above the fold refers to what appears in a browser window before the user scrolls down). Webpages can also load assets only as they are needed, using a technique known as [lazy loading](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/). These approaches do not actually improve network latency, but they do improve the user's perception of page speed.

## How can users fix latency on their end?

Sometimes, network "latency" (slow network performance) is caused by issues on the user's side, not the server side. Consumers always have the option of purchasing more bandwidth if slow network performance is a consistent issue, although bandwidth is not a guarantee of website performance. Switching to Ethernet instead of WiFi will result in a more consistent Internet connection and typically improves Internet speed. Users should also make sure their Internet equipment is up to date by applying firmware updates regularly and replacing equipment altogether as necessary.
