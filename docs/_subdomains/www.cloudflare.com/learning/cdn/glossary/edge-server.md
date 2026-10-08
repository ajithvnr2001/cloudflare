---
url: https://www.cloudflare.com/learning/cdn/glossary/edge-server/
title: What is a CDN edge server?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:13.267177+00:00
---

# What is a CDN edge server?

> Source: https://www.cloudflare.com/learning/cdn/glossary/edge-server/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is a CDN edge server? 

Edge servers are a primary component of making the Internet fast. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a CDN edge server 
  * Understand how data passes across networks 
  * Differentiate between edge and origin servers 



On this page

  * What is a CDN edge server?

  * How does an edge server work?

    * Networks connect across the edge

  * What is the difference between an edge server and an origin server?

  * FAQs

    * What defines an edge server in the context of a CDN?

    * How does an edge server improve website performance?

    * What is the difference between an edge server and an origin server?

    * In what ways does an edge server provide security for a website?

    * What happens when a user requests content that is not cached by the CDN?

    * Why are edge servers often located in Internet exchange points?

    * How do edge servers contribute to the scalability of a website?




## What is a CDN edge server?

A [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) edge server is a computer that exists at the logical extreme or “[edge](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)” of a network. An edge server often serves as the connection between separate networks. A primary purpose of a CDN edge server is to store content as close as possible to a requesting client machine, thereby reducing [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) and improving page load times.

An edge server is a type of edge device that provides an entry point into a network. Other edges devices include routers and routing switches. Edge devices are often placed inside [Internet exchange points (IxPs)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/) to allow different networks to connect and share transit.

## How does an edge server work?

In any particular network layout, a number of different devices will connect to each other using one or more predefined network pattern. If a network wants to connect to another network or the larger Internet, it must have some form of bridge in order for traffic to flow from one location to another. Hardware devices that creates this bridge on the edge of a network are called edge devices.

#### Networks connect across the edge

In a typical home or office network with many devices connected, devices such as mobile phones or computers connect and disconnect to the network through a hub-and-spoke network model. All of the devices exist within the same local area network (LAN), and each device connects to a central router, through which they are able to connect with each other.

In order to connect a second network to the first network, at some point the connection must be made between the networks. The device through which the networks are able to connect with each other is, by definition, an edge device.

![CDN edge network device diagram](https://www.cloudflare.com/img/learning/cdn/glossary/edge-server/cdn-edge-network-device.png)CDN edge network device diagram

Now, if a computer inside Network A needs to connect to a computer inside Network B, the connection must pass from network A, across the network edge, and into the second network. This same paradigm also works in more complex contexts, such when a connection is made across the Internet. The ability for networks to share transit is bottlenecked by the availability of edge devices between them.

When a connection must traverse the Internet, even more intermediary steps must be taken between network A and network B. For the sake of simplicity, let's imagine that each network is a circle, and the place in which the circles touch is the edge of the network. In order for connection to move across the Internet, it will typically touch many networks and move across many network edge nodes. Generally speaking, the farther the connection must travel, the greater the number of networks that must be traversed. A connection may traverse different Internet service providers and Internet backbone infrastructure hardware before reaching its target.

![CDN edge server placement diagram](https://www.cloudflare.com/img/learning/cdn/glossary/edge-server/cdn-edge-server-placement.png)CDN edge server placement diagram

A CDN provider will place servers in many locations, but some of the most important are the connection points at the edge between different networks. These edge servers will connect with multiple different networks and allow for traffic to pass quickly and efficiently between networks. Without a CDN, transit may take a slower and/or more convoluted route between source and destination. In worst case scenarios, traffic will “trombone” large distances; when connecting to another device across the street, a connection may move across the country and back again. By placing edge servers in key locations, a CDN is able to quickly deliver content to users inside different networks. To learn more about the improvements of using CDN, explore how [CDN performance works](https://www.cloudflare.com/learning/cdn/performance/).

## What is the difference between an edge server and an origin server?

An [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) is the web server that receives all Internet traffic when a web property is not using a CDN. Using an origin server without a CDN means that each Internet request must return to the physical location of that origin server, regardless of where in the world it resides. This creates an increase in load times which increases the further the server is from the requesting client machine.

CDN edge servers store ([cache](https://www.cloudflare.com/learning/cdn/what-is-caching/)) content in strategic locations in order to take the load off of one or more origin servers. By moving static assets like images, HTML and JavaScript files (and potentially other content) as close as possible to the requesting client machine, an edge server cache is able to reduce the amount of time it takes for a web resource to load. Origin servers still have an important function to play when using a CDN, as important [server-side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) code such as a database of hashed client credentials used for authentication, typically is maintained at the origin. Learn about the [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) with edge servers all over the globe.

## FAQs

#### What defines an edge server in the context of a CDN?

An edge server is a device located at the network's logical extreme, or edge; such a server reduces latency by processing requests as close to the end user as possible. Within a content delivery network (CDN), these servers serve as the primary connection point between a visitor and the origin server.

#### How does an edge server improve website performance?

By sitting between a user and an origin server, an edge server minimizes the physical distance data must travel. This reduced distance decreases the time it takes for a website to load, providing a faster and more responsive experience for the user.

#### What is the difference between an edge server and an origin server?

An origin server is the central source where a website's original data and content reside. An edge server is part of a distributed network that stores cached versions of that data in multiple global locations to ensure faster delivery to nearby users.

#### In what ways does an edge server provide security for a website?

Edge servers may act as a protective barrier at the network's perimeter. They can be equipped with security tools like a web application firewall (WAF) or DDoS mitigation services to identify and block malicious traffic before it can reach the origin server.

#### What happens when a user requests content that is not cached by the CDN?

If the requested content is not already stored on the edge server, the server forwards the request to the origin server. Once it receives the data, the edge server delivers it to the user and can then cache it to fulfill future requests from other nearby users more quickly.

#### Why are edge servers often located in Internet exchange points (IXPs)?

Placing edge servers in IXPs allows them to connect directly with different Internet service providers (ISPs). This strategic placement reduces the number of hops or network transitions required to deliver content, further reducing latency.

#### How do edge servers contribute to the scalability of a website?

CDN edge servers help a website scale by offloading a significant amount of traffic from the origin server. By handling the majority of requests locally, the edge servers prevent the origin server from becoming overwhelmed during periods of high traffic or sudden surges.
