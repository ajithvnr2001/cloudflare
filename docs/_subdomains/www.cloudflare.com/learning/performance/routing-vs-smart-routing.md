---
url: https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/
title: What is the Difference Between Routing and Smart Routing?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:37.202423+00:00
---

# What is the Difference Between Routing and Smart Routing?

> Source: https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is the difference between routing and smart routing? 

Smart routing improves upon BGP routing by taking network conditions and reliability into account, and choosing less direct routes that are faster. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand how BGP works 
  * Learn what smart routing is and how it differs from standard routing 



Related content  [ How to test the speed of a website ](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[ Mobile performance: How to make a site mobile friendly ](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)

On this page

  * How does network routing usually work on the Internet?

  * How does BGP help route data across networks?

  * How does BGP decide on routes?

  * What is smart routing?

  * What is Cloudflare Argo?




## How does network routing usually work on the Internet?

The Internet is very fast relative to other modes of communication, but information does not instantly arrive where it is requested. Communication between two machines (usually, a client device like a smartphone or laptop, and a web server) via the Internet has to travel through a variety of interconnected large networks, and each network is known as an [autonomous system (AS)](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/). Data passes from AS to AS until it arrives at its destination. Each AS is responsible for certain [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/).

## How does BGP help route data across networks?

[BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/), or Border Gateway Protocol, is what makes all this possible. BGP is the protocol that selects the shortest path from one IP address to another when ASes connect at [Internet Exchange Points (IXPs)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/).

BGP is like a driver who looks at a map and selects the geographically shortest route to a destination. Without BGP, packets could blindly travel through ASes around the world in order to reach an IP address that was mere miles away; with BGP, packets take the most direct route.

## How does BGP decide on routes?

BGP always chooses the shortest path, in order for network traffic to reach its destination with the fewest network hops possible. BGP routers maintain records of the shortest routes; these records are known as 'routing tables.' The [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) tables are generated based on which IP addresses each AS claims they own. BGP routing tables will change in response to ASes advertising new or different IP addresses.

Unlike when a driver looks at a map, the Internet is changing all the time, with networks coming on and offline, ASes taking on new IP addresses, and so on. BGP keeps an updated list of all these changes based on the information ASes advertise across the Internet.

When ASes [broadcast inaccurate routing information](https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/), it can redirect network traffic to the wrong places, potentially impacting users around the world. For instance, in 2018, Google experienced an outage when an ISP in Nigeria accidentally broadcast incorrect routing information across the web. (See our blog post '[How a Nigerian ISP Accidentally Knocked Google Offline](https://blog.cloudflare.com/how-a-nigerian-isp-knocked-google-offline/)'.)

Overall, BGP is effective enough for the Internet to function at a scale never imagined by its original creators. However, it can't detect or adjust to real-time network conditions. It makes routing decisions only based on what the shortest route is. As anyone who has gotten stuck in traffic on a major freeway knows, the shortest route is not necessarily the fastest route.

## What is smart routing?

Smart routing is faster than standard routing using BGP. It's like using Google Maps or Waze instead of just measuring distances on a printed map. Drivers may be able to figure out the shortest route with a map, but to figure out the fastest route at that moment, they need real-time traffic data.

Just as a commute can be made faster by driving the long way around to avoid heavy traffic, smart routing chooses less congested routes to avoid network congestion. This optimizes the speed at which data is able to traverse the web and reach its destination.

Smart routing is not an alternative routing system to BGP; rather, it runs on top of BGP to optimize traffic routes.

## What is Cloudflare Argo?

[Argo is a smart routing service](https://www.cloudflare.com/products/argo-smart-routing/) that selects routes based on network congestion and reliability. Because Internet requests for millions of websites run through Cloudflare’s network, Argo has enough of a sample size to be able to make informed decisions on which routes are most and least trafficked. It also avoids dropped packets by cutting out unreliable network connections.
