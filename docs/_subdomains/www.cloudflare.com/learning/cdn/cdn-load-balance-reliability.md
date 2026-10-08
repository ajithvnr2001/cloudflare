---
url: https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/
title: CDN reliability and load balancing | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:02.112899+00:00
---

# CDN reliability and load balancing | Learning Center

> Source: https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  CDN reliability and load balancing 

CDNs improve reliability through load balancing, failover mechanisms, and redundant infrastructure across global edge networks. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how CDNs provide redundancy 
  * Understand CDN load balancing 
  * Describe failover in CDN architecture 



Related content  [ What is a CDN? ](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)

On this page

  * CDN benefits – reliability & redundancy

  * What is load balancing? How does a CDN load balance traffic?

  * What is failover? How does a CDN failover between servers?

  * How does a CDN reliably serve content across the Internet?

  * How can a CDN use an Anycast network to increase reliability?




## CDN benefits – reliability & redundancy

One of the important characteristics about a CDN is its ability to keep website content online in the face of the common network problems including hardware failures and network congestion. By load balancing Internet traffic, using intelligent failover, and by maintaining servers across many [data centers](https://www.cloudflare.com/learning/cdn/glossary/data-center/), a CDN is designed to circumvent network congestion and be resilient against service interruption.

## What is load balancing? How does a CDN load balance traffic?

The purpose of a load balancer is to distribute network traffic equally across a number of servers. Load balancing can be either hardware or software based. A CDN uses load balancing in a data center to distribute incoming requests across the available server pool to ensure that spikes in traffic are handled in the most efficient manner possible. By efficiently using available resources, load balancing is able to increase processing speeds and effectively utilize server capacity. Properly load balancing incoming traffic is a key component in mitigating spikes in traffic that occur during atypical Internet activity such as when a website is experiencing an unusually high number of visitors or during a [distributed denial-of-service attack](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/).

![CDN load balancer diagram](https://www.cloudflare.com/img/learning/cdn/reliability/load-balance-diagram.png)

A CDN also uses load balancing to make changes quickly and efficiently when the availability of server resources fluctuates up or down. In the event that a server fails and failover occurs, a load balancer will redirect the traffic allocated for the failed server and distribute it proportionally across the remaining servers. This provides resiliency and reliability by increasing likelihood that hardware failures will not disrupt the flow of traffic. When a new server comes online in the data center, a load balancer will proportionately remove load from other servers and increase the utilization of the new hardware. [Software-based load balancing](https://www.cloudflare.com/application-services/products/load-balancing/) services allow a CDN to scale load balancing capacity quickly without the bottlenecks present when using physical load-balancing hardware.

## What is failover? How does a CDN failover between servers?

In computer systems that require a high degree of reliability and near continuous availability, failover is used to prevent traffic from being lost when a server is unavailable. When a server goes down, the traffic needs to be rerouted to a server that is still functional. By automatically offloading tasks to a standby system or another machine with available capacity, intelligent failover can prevent disruption of service to users.

![CDN failover diagram](https://www.cloudflare.com/img/learning/cdn/reliability/load-balance-failover.png)

## How does a CDN reliably serve content across the Internet?

A CDN is like a GPS system coupled with express toll roads; a CDN will be able to find the optimal path to reach a distant location and will be able to use its own network to find the optimal route to get there as quickly as possible.

When a user loads content from an Internet property such a webpage or web application, a series of connections are made in order to reach the location at which the content is served. Network traffic can be thought of metaphorically as a road and highway system; smaller surface streets move local traffic around the same area and interstate highways transfer traffic into different states. When something goes wrong, like a tanker truck blocks all lanes of an interstate highway on the primary path into different state, traffic must find another path around. Like a highway crossing different states, traffic often has to move across different networks to reach its final destination. If a blockage exists in a particular network, the traffic must be redirected down a different pathway. This process can be time-consuming and inefficient.

Let's say a user in San Francisco is loading a website in Los Angeles. The connection makes many steps, but in this example, one of the most important steps is where the network signal passes through a telecommunications provider based in in San Jose on its way towards the final destination. When a network engineer accidentally pours coffee on routing equipment in San Jose, the provider goes offline, breaking the connection (stranger things have happened). When this occurs the user is no longer able to load their Internet content unless the networked traffic is rerouted to accommodate for the new network landscape. The user's request now needs to go through a different telecom provider if it ever wants to arrive in Los Angeles.

Now that the traffic is no longer able to pass through the intended network, it must instead step into an entirely different network maintained by a different organization. This process of renegotiation and switching networks may occur multiple times in a network request and instances like this can add [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) and may push the traffic onto a congested pathway, resulting in a delay. A CDN of sufficient size will typically control its own network connections by placing servers in [Internet exchange points (IXPs)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/) and other strategic locations. These optimized network schemas allow CDN providers to optimize the route and reduce latency.

## How can a CDN use an Anycast network to increase reliability?

Some CDNs will use an [Anycast](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) routing method to transfer Internet traffic to specific available data centers. This occurs in order to ensure improved response time and to prevent any one data center from becoming overwhelmed with traffic in the event of extraordinary demand such as during a DDoS attack.

With Anycast, multiple machines can share the same [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). When a request is sent to an Anycast IP address, routers will direct it to the machine on the network that is closest. In the event that an entire data center fails or is otherwise incapacitated with heavy traffic, an Anycast network can respond to the outage somewhat similarly to how a load balancer transfers traffic across multiple servers inside a data center; the data is routed away from the failing location and instead is routed towards another data center that is still online and functional.

![Anycast network diagram diagram](https://www.cloudflare.com/img/learning/cdn/reliability/anycast-network-diagram.png)

DDoS attacks are currently one of the most substantial threats to the reliability of Internet properties. CDNs that use Anycast have additional flexibility in mitigating DDoS attacks. In most modern DDoS attacks many compromise computers or [“bots”](https://www.cloudflare.com/learning/bots/what-is-a-bot/) are used to form what is known as a [botnet](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/). These compromised machines can generate so much Internet traffic that they can overwhelm a typical Unicast-connected machine. With an Anycast network, a portion of the botnet attack traffic can be distributed across multiple data centers, reducing the impact of the attack. Learn about the [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) with Anycast routing.
