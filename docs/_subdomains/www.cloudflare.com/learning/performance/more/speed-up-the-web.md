---
url: https://www.cloudflare.com/learning/performance/more/speed-up-the-web/
title: How to Make the Internet Faster for Everyone
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:31.094048+00:00
---

# How to Make the Internet Faster for Everyone

> Source: https://www.cloudflare.com/learning/performance/more/speed-up-the-web/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  How to make the Internet faster for everyone 

A number of factors affect Internet speed. To speed up the Internet, solutions for network congestion, DNS resolving, and network latency are needed. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the factors that impact Internet speed 
  * Learn how the Internet as a whole can be made faster 



Related content  [ How to test the speed of a website ](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[ Mobile performance: How to make a site mobile friendly ](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)

On this page

  * What are some of the factors that slow down internet performance?

    * Network latency

    * Slowly performing websites

    * Cyber attacks

    * Network congestion

    * Issues on the client device

  * How does DNS affect internet speed?

  * How do CDNs speed up the Internet?

  * How can developers increase page speed?

  * How can Internet routing be improved and network congestion reduced?




## What are some of the factors that slow down internet performance?

#### Network latency

Distance is one of the principal causes of latency. For the Internet to function, computers, servers, and routers need to communicate back and forth, exchanging information in the form of pulses of electricity across cables that stretch for hundreds of miles. A certain amount of latency is built into the Internet because of the physical laws of the universe – the speed of light is a hard limit on how fast information can travel. That's very fast, but it still means that it will take information from a few milliseconds up to nearly a second to travel through cables from the client to the server and back (see [What is latency?](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)).

#### Slowly performing websites

Websites can be slow for a number of reasons. Sites that have to load one or more large CSS files, high-definition images, or multiple JavaScript files in order to function properly may take a long time to render. Additionally, where the site is [hosted](https://www.cloudflare.com/developer-platform/solutions/hosting/) makes a difference to website speed, especially if it doesn't use a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/); a website hosted in Toronto may load just fine for Toronto users but take a long time to load in Houston. A [website speed test](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/) can help developers determine how their web properties are performing and where the inefficiencies are.

#### Cyber attacks

Malicious activity often hinders Internet speed. For example, [DDoS attacks on websites](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) can significantly slow a website's performance or crash the website altogether.

#### Network congestion

The amount of data that can pass through a network at any given time is limited; the maximum amount that can pass through is known as the bandwidth. When incoming network traffic exceeds bandwidth at a certain point on the network, whether that's within an [Internet Exchange Point (IXP)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/), in a [data center](https://www.cloudflare.com/learning/cdn/glossary/data-center/), or on a [LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/) [router](https://www.cloudflare.com/learning/network-layer/what-is-routing/) in a private home, the resulting network congestion leads to slower Internet speeds, the same way too many cars on the freeway results in slower traffic.

Network congestion may be limited to a certain geographic area, may affect an entire ISP's network, or may take place inside a home (for instance, if multiple people are trying to stream high-definition video at the same time).

#### Issues on the client device

A variety of conditions can cause websites and web applications to perform poorly on user devices (the 'client' in the [client-server model](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)). For example:

  * Too many open browser tabs or processes running on the device can slow browser performance.

  * The device itself can run slowly due to hardware issues or [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/) infections.

  * Too many extensions and plugins running in the browser can also slow webpage speed.




## How does DNS affect internet speed?

The [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) maps, or 'resolves,' [domain names](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) to [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/), and because this has to be done before a browser can navigate to and display a website, DNS resolution affects how quickly websites load. For most consumers, their ISP (Internet service provider) assigns DNS resolvers by default, and if the ISP's DNS servers are performing slowly, this slows down Internet speed for that ISP's users.

Users also have the ability to use a DNS resolver other than their ISP's, although many users are unaware of this option. [1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/) is currently the fastest DNS resolver and is designed to reduce these delays. Typically, 1.1.1.1 responds in about 10-20 milliseconds; other resolvers may take well over 100 milliseconds.

## How do CDNs speed up the Internet?

[CDNs](https://www.cloudflare.com/application-services/products/cdn/) (content delivery networks) greatly reduce network latency. A CDN caches content in servers around the world so that it does not have to travel as far to reach end users. This reduces network latency and speeds up websites that use the CDN. Some CDNs also perform [load balancing](https://www.cloudflare.com/load-balancing/), which helps prevent network congestion. The Cloudflare CDN has data centers in 200 cities worldwide. This helps to bring web content closer to users and speed up website performance.

## How can developers increase page speed?

[Website speed is essential](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) for making the Internet faster. Developers can keep pages fast by [optimizing images](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/), keeping code as short as possible, and in general keeping page file size as small as possible. They can also load render-blocking resources* last, which does not actually make webpages load faster but does allow the browser to render the content that the user sees more quickly. Use of a CDN also allows webpages to load faster.

*Render-blocking resources are the files that need to be loaded before anything else can be loaded, such as CSS and JavaScript.

## How can Internet routing be improved and network congestion reduced?

Vehicular traffic jams are an all too common occurrence in major cities. To get around congestion and bad road conditions, some drivers opt to use smart maps apps like Waze, which reroute them onto less congested streets. Internet routing, just like many drivers' commuting routes, forwards network traffic to the shortest distance between two points. But in reality, that's not always the fastest route. The main Internet routing protocol, [BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/), is effective at keeping the internet infrastructure globally connected, but is not 'smart' when it comes to traffic levels – it can't pick a different route based on traffic and/or network congestion. BGP is vital for the general operation of the Internet. What’s needed next is a smart layer above BGP.

[Argo smart routing](https://www.cloudflare.com/products/argo-smart-routing/) is an example of a service that does just this. Improving Internet routing so that network traffic can be rerouted based on these factors makes the Internet as a whole faster. Argo builds on BGP's excellent resilience and handles the nitty-gritty of finding ways around congested paths.
