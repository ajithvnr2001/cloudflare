---
url: https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/
title: What Is A Reverse Proxy? | Proxy Servers Explained
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:16.659725+00:00
---

# What Is A Reverse Proxy? | Proxy Servers Explained

> Source: https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  What is a reverse proxy? | Proxy servers explained 

A reverse proxy protects web servers from attacks and can provide performance and reliability benefits. Learn more about forward and reverse proxies. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a proxy server 
  * Describe the differences between a forward and reverse proxy 
  * Outline the benefits of using a reverse proxy 



Related content  [ CDN SSL/TLS security ](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)

On this page

  * What is a reverse proxy?

  * What is a proxy server?

  * How is a reverse proxy different?

  * How to implement a reverse proxy

  * FAQs

    * What is the primary function of a reverse proxy?

    * How does a reverse proxy differ from a forward proxy?

    * In what way can a reverse proxy help with load balancing?

    * How can a reverse proxy enhance a website&#39

    * How does a reverse proxy improve performance through caching?

    * What is global server load balancing in the context of reverse proxies?

    * What is the benefit of using a reverse proxy for SSL encryption?




## What is a reverse proxy?

A reverse proxy is a server that sits in front of web servers and forwards client (e.g. web browser) requests to those web servers. Reverse proxies are typically implemented to help increase [security](https://www.cloudflare.com/learning/security/what-is-web-application-security/), [performance](https://www.cloudflare.com/learning/performance/why-site-speed-matters/), and reliability. In order to better understand how a reverse proxy works and the benefits it can provide, let’s first define what a proxy server is.

Report

2024 IDC Marketscape for Edge Delivery Services

[Get the report →](https://www.cloudflare.com/lp/idc-marketscape-for-worldwide-commercial-edge-delivery-services-2024/)

## What is a proxy server?

A forward proxy, often called a proxy, proxy server, or web proxy, is a server that sits in front of a group of client machines. When those computers make requests to sites and services on the Internet, the proxy server intercepts those requests and then communicates with web servers on behalf of those clients, like a middleman.

For example, let’s name 3 computers involved in a typical forward proxy communication:

  * A: This is a user’s home computer

  * B: This is a forward proxy server

  * C: This is a website’s origin server (where the website data is stored)


![Forward proxy flow: traffic flows from user](https://images.ctfassets.net/slt3lc6tev37/2MZmHGnCdYbQBIsZ4V11C6/25b48def8b56b63f7527d6ad65829676/forward_proxy_flow.png)Forward proxy flow: traffic flows from user

In a standard Internet communication, computer A would reach out directly to computer C, with the client sending requests to the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) and the origin server responding to the client. When a forward proxy is in place, A will instead send requests to B, which will then forward the request to C. C will then send a response to B, which will forward the response back to A.

Ultra-fast CDN

Boost performance using Cloudflare CDN

[Start for free →](https://www.cloudflare.com/plans/)

Why would anyone add this extra middleman to their Internet activity? There are a few reasons one might want to use a forward proxy:

  * **To avoid state or institutional browsing restrictions** \- Some governments, schools, and other organizations use firewalls to give their users access to a limited version of the Internet. A forward proxy can be used to get around these restrictions, as they let the user connect to the proxy rather than directly to the sites they are visiting.

  * **To block access to certain content** \- Conversely, proxies can also be set up to block a group of users from accessing certain sites. For example, a school network might be configured to connect to the web through a proxy which enables content filtering rules, refusing to forward responses from Facebook and other social media sites.

  * **To protect their identity online** \- In some cases, regular Internet users simply desire increased anonymity online, but in other cases, Internet users live in places where the government can impose serious consequences to political dissidents. Criticizing the government in a web forum or on social media can lead to fines or imprisonment for these users. If one of these dissidents uses a forward proxy to connect to a website where they post politically sensitive comments, the [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) used to post the comments will be harder to trace back to the dissident. Only the IP address of the proxy server will be visible.




## How is a reverse proxy different?

A reverse proxy is a server that sits in front of one or more web servers, intercepting requests from clients. This is different from a forward proxy, where the proxy sits in front of the clients. With a reverse proxy, when clients send requests to the origin server of a website, those requests are intercepted at the [network edge](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/) by the reverse proxy server. The reverse proxy server will then send requests to and receive responses from the origin server.

The difference between a forward and reverse proxy is subtle but important. A simplified way to sum it up would be to say that a forward proxy sits in front of a client and ensures that no origin server ever communicates directly with that specific client. On the other hand, a reverse proxy sits in front of an origin server and ensures that no client ever communicates directly with that origin server.

Once again, let’s illustrate by naming the computers involved:

  * D: Any number of users’ home computers

  * E: This is a reverse proxy server

  * F: One or more origin servers


![Reverse proxy flow: traffic flows from user](https://images.ctfassets.net/slt3lc6tev37/3msJRtqxDysQslvrKvEf8x/f7f54c9a2cad3e4586f58e8e0e305389/reverse_proxy_flow.png)Reverse proxy flow: traffic flows from user

Typically all requests from D would go directly to F, and F would send responses directly to D. With a reverse proxy, all requests from D will go directly to E, and E will send its requests to and receive responses from F. E will then pass along the appropriate responses to D.

Below we outline some of the benefits of a reverse proxy:

  * **[Load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)** \- A popular website that gets millions of users every day may not be able to handle all of its incoming site traffic with a single origin server. Instead, the site can be distributed among a pool of different servers, all handling requests for the same site. In this case, a reverse proxy can provide a load balancing solution which will distribute the incoming traffic evenly among the different servers to prevent any single server from becoming overloaded. In the event that a server fails completely, other servers can step up to handle the traffic.

  * **Protection from attacks** \- With a reverse proxy in place, a web site or service never needs to reveal the IP address of their origin server(s). This makes it much harder for attackers to leverage a targeted attack against them, such as a [DDoS attack](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/). Instead the attackers will only be able to target the reverse proxy, such as Cloudflare’s [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/), which will have tighter security and more resources to fend off a cyber attack.

  * **[Global server load balancing](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/) (GSLB)** \- In this form of load balancing, a website can be distributed on several servers around the globe and the reverse proxy will send clients to the server that’s geographically closest to them. This decreases the distances that requests and responses need to travel, minimizing load times.

  * **Caching** \- A reverse proxy can also [cache](https://www.cloudflare.com/learning/cdn/what-is-caching/) content, resulting in faster performance. For example, if a user in Paris visits a reverse-proxied website with web servers in Los Angeles, the user might actually connect to a local reverse proxy server in Paris, which will then have to communicate with an origin server in L.A. The proxy server can then cache (or temporarily save) the response data. Subsequent Parisian users who browse the site will then get the locally cached version from the Parisian reverse proxy server, resulting in much faster performance.

    * **SSL encryption** \- [Encrypting](https://www.cloudflare.com/learning/ssl/what-is-encryption/) and decrypting [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/) (or [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)) communications for each client can be computationally expensive for an origin server. A reverse proxy can be configured to decrypt all incoming requests and encrypt all outgoing responses, freeing up valuable resources on the origin server.



## How to implement a reverse proxy

Some companies build their own reverse proxies, but this requires intensive software and hardware engineering resources, as well as a significant investment in physical hardware. One of the easiest and most cost-effective ways to reap all the benefits of a reverse proxy is by signing up for a CDN service. For example, the [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) provides all the performance and security features listed above, as well as many others.

## FAQs

#### What is the primary function of a reverse proxy?

A reverse proxy is a server that sits in front of one or more web servers to intercept and forward requests from clients. It acts as an intermediary, ensuring that no client communicates directly with the origin server.

#### How does a reverse proxy differ from a forward proxy?

A forward proxy sits in front of clients (users) to forward their requests to the Internet. In contrast, a reverse proxy sits in front of servers to manage incoming traffic from the Internet.

[Image comparing forward proxy vs reverse proxy architecture]

#### In what way can a reverse proxy help with load balancing?

For websites with high traffic, a reverse proxy can act as a load balancer by distributing incoming requests evenly across a pool of several origin servers. This prevents any single server from becoming overloaded and ensures the site remains available even if one server fails.

#### How can a reverse proxy enhance a website's security?

By using a reverse proxy, a website never has to reveal the actual IP address of its origin servers. This makes it significantly harder for attackers to launch targeted efforts, such as DDoS attacks, against the source. Instead, the proxy handles the traffic and can use its specialized resources to fend off cyber threats.

#### How does a reverse proxy improve performance through caching?

A reverse proxy can cache, or temporarily save, copies of website content at locations closer to the users. For example, if a user in Chicago accesses a site hosted in London, a local reverse proxy in Chicago can store the data. Future visitors from the same area can then receive the content directly from that local proxy, which greatly reduces load times.

#### What is global server load balancing (GSLB) in the context of reverse proxies?

GSLB is a performance optimization where a reverse proxy directs users to the specific web server that is geographically closest to them. By minimizing the physical distance that data must travel between the client and the server, the proxy reduces latency and speeds up the user experience.

#### What is the benefit of using a reverse proxy for SSL encryption?

Encrypting and decrypting SSL/TLS communications can be a heavy task for an origin server. A reverse proxy can take over this responsibility by handling the decryption of incoming requests and the encryption of outgoing responses. This process clears up valuable processing power for the origin server to focus on other tasks.
