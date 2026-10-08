---
url: https://www.cloudflare.com/learning/cdn/cdn-performance/
title: CDN performance | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:02.328133+00:00
---

# CDN performance | Learning Center

> Source: https://www.cloudflare.com/learning/cdn/cdn-performance/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  CDN performance 

CDNs improve web performance by reducing latency, minimizing bandwidth consumption, and optimizing content delivery. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand how CDNs reduce latency 
  * Learn about CDN caching strategies 
  * Explain CDN performance optimization techniques 



Related content  [ What is a CDN? ](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)

On this page

  * How does a CDN improve load times?

  * What is the difference in load times with and without a CDN?

  * How does a CDN load content? What is caching?

  * How does a CDN reduce file sizes to increase speeds?

  * What hardware can a CDN use to improve speeds?




## How does a CDN improve load times?

Virtually everyone on the Internet has experienced the benefits of a content delivery network ([CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)). The majority of technology companies, including companies like Google, Apple, and Microsoft, use CDNs to reduce [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) in loading webpage content. 

A CDN will typically place servers at the exchange points between different networks. These [internet exchange points (IXPs)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/) are the primary locations where different internet providers link to each other in order to provide each other access to resources on their different networks. In addition to IXPs, a CDN will place servers in [data centers](https://www.cloudflare.com/learning/cdn/glossary/data-center/) in locations across the globe in high traffic areas and strategic locations to be able to move traffic as quickly as possible.

A primary benefit of a CDN is its ability to deliver content quickly and efficiently. CDN performance optimizations can be broken into three categories:

  1. **Distance reduction** – reduce the physical distance between a client and the requested data
  2. **Hardware/software optimizations** – improve performance of [server-side infrastructure](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/), such as by using solid-state hard drives and efficient load balancing
  3. **Reduced data transfer** – employ techniques to reduce file sizes so that initial page loads occur quickly



In order to understand the benefits of using a CDN, let’s explore what a normal client/server data transfer looks like without a CDN in place.

## What is the difference in load times with and without a CDN?

Let's imagine that someone in New York needs to access a website hosted on a server in Singapore. The physical separation between these locations is substantial, with a physical distance of about 9,520 miles.

![Distance Without CDN](https://www.cloudflare.com/img/learning/cdn/performance/cdn-distance-1.png)

If a server hosting website content (the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)) is located in Singapore, each request for each webpage asset must travel from New York to Singapore and back again. Much like taking an international flight with many connections along the way, each request must travel through a series of routers along its distant travel from point A to point B.

If you want to see a real example of how many different connections (hops) it takes your computer to reach a particular web service from your present location, explore the traceroute utility using a desktop computer.

![CDN Transit Time Improvements](https://www.cloudflare.com/img/learning/cdn/performance/cdn-distance-2.png)

Because the request from New York to Singapore needs to pass through each of the router locations along the way, the amount of time (latency) is increased both by the total distance and the time it takes each router to process the request. Once the origin server processes the request and responds to the client making the request, it then sends information back through a similar sequence of routers before it returns to New York. The measurement of this total round trip is referred to in telecommunications as [RTT for “round trip time.”](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/) Ignoring for the moment available bandwidth and potential network congestion, let’s walk through an example of the latency factors.

For the sake of illustration, let's say:

  * It takes 250ms for a request to go from New York to Singapore.
  * Establishing a [TCP/IP connection](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) will add 3 instances of 250ms of latency.
  * The webpage requires 5 unique assets consisting of images, JavaScript files and the webpage itself. 



Let's see roughly how long it will take this webpage to load:

  * 750ms: The TCP/IP connection is made between the client in New York and the origin server in Singapore.
  * 250ms: The [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http) request for the webpage travels from New York to Singapore.
  * 250ms: The requester in New York receives a response from the origin server in Singapore with a 200 status code and the webpage including all the additional assets needed.
  * 250ms: Each of the 5 assets are requested by the client in New York.
  * 1500ms: The five assets are delivered asynchronously to the client from the origin server in Singapore.



In this simple example, the total transit time for this webpage to load is about **3000ms**.

As you can see, each time a request is made and a response is sent, the entire path between the client in New York and the origin in Singapore is traversed. As websites becomes larger and require a greater number of assets, the latency between point A and point B continues to increase.

Let's revisit the example of content hosted in Singapore served to a web client in New York, but now the Singapore site is using a CDN with a server in Atlanta that contains a cached copy of the static website:

  * It takes 50ms for a request to go from New York to Atlanta.
  * Establishing a TCP/IP connection will add 3 instances of 50ms of latency
  * The webpage requires 5 unique assets consisting of images, JavaScript files and the webpage itself.



Let's see roughly how long it will take this webpage to load using the CDN:

  * 150ms: The TCP/IP connection is made between the client in New York and the edge server in Atlanta.
  * 50ms: The HTTP GET request for the webpage travels from the client to the edge server.
  * 50ms: The client receives a response from the edge server cache with the webpage including a list of all the additional assets still required.
  * 50ms: Each of the 5 assets are requested by the client.
  * 800ms: The five assets are delivered asynchronously to the client from the edge server.



The total transit time for this webpage to load is about **1100ms**.

![CDN Distance Optimized](https://www.cloudflare.com/img/learning/cdn/performance/cdn-distance-3.png)

In this example, the reduction in distance between the client and the content creates a 1900ms improvement in latency for static content, representing a nearly 2 second improvement in load time.

![CDN Latency Improvement](https://www.cloudflare.com/img/learning/cdn/performance/cdn-latency-graph.png)

By reducing the total distance all the necessary traffic needs to traverse, each user to the website is saving an amount of load time. Because users start to leave the site (bounce) very quickly as wait times increase, this improvement represents both a better user experience and higher user time on page.

## How does a CDN load content? What is caching?

As mentioned earlier, normally when a client requests a file from an origin server, the request needs to go roundtrip to that server and back again. A CDN improves the latency by pulling static content files from the origin server into the distributed CDN network in a process called caching. Some CDNs will have advanced features that allow for the selective caching of dynamic content as well. Once the data is cached, the CDN serves the content to the client from the closest CDN data center.

![Request Without CDN Caching](https://www.cloudflare.com/img/learning/cdn/performance/cdn-origin-client.png)

![Request With CDN Caching](https://www.cloudflare.com/img/learning/cdn/performance/cdn-caching.png)

After a [TCP handshake](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) has been made, the client machine makes a HTTP request to the CDN’s network. If the content has not yet been cached, the CDN will first download content from the origin by making an extra request between the origin server and the CDN’s edge server.

Here are the 4 steps during a typical CDN caching:

  1. When the user requests a webpage, the user's request is routed to the CDN’s nearest [edge server](https://www.cloudflare.com/learning/cdn/glossary/edge-server/).
  2. The edge server then makes a request to the origin server for the content the user requested.
  3. The origin responds to the edge server’s request.
  4. Finally the edge server responds to the client.

![CDN Caching Request](https://www.cloudflare.com/img/learning/cdn/performance/cdn-caching-first-request.png)

The value of a CDN’s proximity to the client occurs after the initial request to the origin server has already been made. Once the data has been cached from the origin server onto the CDN’s network, each subsequent request from the client only needs to go as far as the nearest edge server. This means that if the nearest edge server is closer than the origin server, latency can be reduced and content can be served much faster.

![cached CDN edge response](https://www.cloudflare.com/img/learning/cdn/performance/cdn-caching-second-request.png)

It's important to keep in mind that the amount of time needed to download assets and to process requests and responses is not presently being included; so far only the transit time needed to transfer information between these two locations is being calculated. Other important latency factors that we will be exploring include data reduction, hard disk speed and network congestion.

## How does a CDN reduce file sizes to increase speeds?

In order improve page load times, CDNs reduce overall data transfer amounts between the CDN's cache servers and the client. Both the latency and the required bandwidth are reduced when the overall amount of data transferred goes down. The result is faster page loads and lower bandwidth costs. Two key components go into these reduction:

**Minification** \- minification is the process by which blocks of code are reduced in size by removing all the components that help humans understand what's happening. While an engineer needs to separate ideas into sensible variable names, spaces and comments in order to make code blocks readable and maintainable, computers can successfully run code with those characters removed.

Here's the same code block before and after minification:

Before minification: eight lines of code

![CDN Without Minification](https://www.cloudflare.com/img/learning/cdn/performance/cdn-code-before-minification.png)

After minification: reduced to a single line of code

![CDN Minification](https://www.cloudflare.com/img/learning/cdn/performance/cdn-code-after-minification.png)

Now that the code snippet has been reduced from eight lines down to a single line, the overall file size has also been reduced. This means that it takes less time to transfer the file which reduces the latency and helps load the content faster.

**File compression** \- file compression is an integral component in reducing the latency and bandwidth consumption required when transferring data across the Internet. GZip is a common method of compression and is considered a best practice to use when transferring webpages. Many CDN providers have GZip enabled by default. How substantial is the savings from GZip compression? Typically compressed files will be reduced by around 50% to 70% of the initial file size. 

## What hardware can a CDN use to improve speeds?

As far as CDN hardware optimizations are concerned, a substantial benefit comes from the use of solid-state hard drives (SSD) over traditional hard disk drives (HDD); solid-state drives can open files up to 30% faster than the traditional hard disk drive and are more resilient and reliable.

Akin to a record player, a traditional hard disk drive consists of a spinning circular metal disc with a magnetic coating that stores data. A read/write head on an arm accesses information when the disc spins underneath it. This process is mechanical, and is affected by how fast the disc spins. With the advent of solid-state drives, the older model of hard drives has become less commonly used, though they’re still produced today and are in wide circulation in many computer systems.

A solid-state drive (SSD) is also a form of persistent storage, but functions much more similarly to USB thumb drives or the memory cards commonly found in devices like digital cameras; there are no moving parts. If a regular hard disk is spinning and the system is jostled, the HDD may skip, resulting in read/write errors and potential downtime. Another important SSD benefit is in accessing fragmented files. File fragmentation is a situation where parts of a file are in different locations across the disk, resulting in slower access for HDD drives. Because a SSD can access non-contiguous memory locations efficiently, fragmentation is not a threat to performance.

In the first CDNs, data was stored on hard disk drives. Now with some CDN services all the edge-side caching can occur on solid-state drives. The downside of SSDs is the expense; a SSD can be up to 5 times more expensive than traditional media. For this reason, some CDN services will often avoid using SSDs and will instead opt for the older technology. [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) exclusively uses SSDs.
