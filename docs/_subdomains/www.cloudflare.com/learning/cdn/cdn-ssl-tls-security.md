---
url: https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/
title: CDN SSL/TLS security | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:02.443220+00:00
---

# CDN SSL/TLS security | Learning Center

> Source: https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/

[ Learning Center ](https://www.cloudflare.com/learning/) / CDNs

##  CDN SSL/TLS security 

CDNs can help improve security by providing SSL/TLS encryption, DDoS protection, and security certificates across distributed edge servers. 

[Learning Center](https://www.cloudflare.com/learning)/CDNs/[Caching static and dynamic content: How does it work?](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)[CDN benefits: Why use a CDN?](https://www.cloudflare.com/learning/cdn/cdn-benefits/)[CDN for WordPress: Key features to look for](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)[Common CDN issues and how to fix them](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)[What is Anycast? | How does Anycast work?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)[What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)[What is a CDN edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)[What is global server load balancing (GSLB)?](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)[What is an Internet exchange point? | How do IXPs work?](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)[What is an origin server? | Origin server definition](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)[What is a reverse proxy? | Proxy servers explained](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)[What is round-trip time? | RTT definition](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)[What is time-to-live (TTL)? | TTL definition](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)[What is cache-control? | Cache explained](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)[How can using a CDN reduce bandwidth costs?](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/)[CDN performance](https://www.cloudflare.com/learning/cdn/performance/)[What is a cache hit ratio?](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)[What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)[What is caching?](https://www.cloudflare.com/learning/cdn/what-is-caching/)[CDN performance](https://www.cloudflare.com/learning/cdn/cdn-performance/)[CDN SSL/TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)[CDN reliability and load balancing](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand how CDNs handle SSL/TLS 
  * Learn about edge SSL certificates 
  * Explain the security benefits of a CDN 



Related content  [ What is a CDN? ](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)

On this page

  * What are the security risks to a CDN?

  * What is SSL/TLS encryption?

    * The TLS protocol is designed to provide 3 components:

  * What is an SSL certificate?

    * First the TCP/IP handshake is made in 3 steps:

    * From a high level, there are three main components to a TLS handshake:

  * How can SSL latency be improved?

  * CDN protection from DDoS attacks




## What are the security risks to a CDN?

Like all networks exposed to the Internet, CDNs must guard against [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/), [data breaches](https://www.cloudflare.com/learning/security/what-is-a-data-breach/), and attempts to overwhelm the network of the targeted [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) using [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/). A [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) can have multiple strategies for mitigating vulnerabilities including proper [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)/[TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) encryption and specialized [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) hardware.

## What is SSL/TLS encryption?

Transport Layer Security (TLS) is a protocol for encrypting data that is sent over the Internet. TLS grew out of Secure Sockets Layer (SSL), the first widely-adopted web encryption protocol, in order to fix most of the earlier protocol’s security flaws. The industry still uses the terms somewhat interchangeably for historical reasons. Any website that you visit starting with [https://](https://www.cloudflare.com/learning/ssl/what-is-https/) rather than http:// is using TLS/SSL for communication between a browser and a server.

Proper encryption practices are a necessity in order to prevent attackers from accessing important data. Because the Internet is designed in such a way that data is transferred across many locations, it is possible to intercept [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) of important information as they move across the globe. Through the utilization of a [cryptographic protocol](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/), only the intended recipient is able to decode and read the information and intermediaries are prevented from decoding the contents of the transferred data.

Get [free SSL certificates from Cloudflare](https://www.cloudflare.com/application-services/products/ssl/). 

#### The TLS protocol is designed to provide 3 components:

  1. **Authentication** \- The ability to verify the validity of the provided identifications
  2. **Encryption** \- The ability to obfuscate information sent from one host to another
  3. **Integrity** \- The ability to detect forgery and tampering



Learn more about [free SSL/TLS from Cloudflare](https://www.cloudflare.com/application-services/products/ssl/).

## What is an SSL certificate?

To enable TLS, a site needs an [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) and a corresponding [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/). Certificates are files containing information about the owner of a site, and the public half of an asymmetric key pair. A certificate authority (CA) digitally signs the certificate to verify that the information in the certificate is correct. By trusting the certificate, you are trusting that the certificate authority has done its due diligence.

![SSL/TLS error graphic](https://images.ctfassets.net/slt3lc6tev37/3itzBHle8bdzqq9jeSsYVd/99431f95209791276245c9dd67832837/https-tls-ssl-not-secure.svg)

Operating systems and browsers typically have a list of certificate authorities that they implicitly trust. If a web site presents a certificate that is signed by an untrusted certificate authority, the browser warns the visitor that something could be afoot.

Certificates and the way they are implemented can also be independently rated based on strength, protocol support and other characteristics. Ratings can change over time as newer, better implementations become available or other factors result in reduction of overall security of a certification implementation. If an origin server has an older lower grade SSL security implementation it will typically be graded more poorly and may be vulnerable to compromise.

A CDN has the added benefit of providing security to visitors of properties hosted within its network using a CDN provided certificate. Because visitors connect to only the CDN, an older or less secure certificate in use between the origin server and the CDN will not affect the client’s experience.

![SSL/TLS self-signed diagram](https://www.cloudflare.com/img/learning/cdn/tls-ssl/origin-ssl-self-signed-certificate-diagram.png)

Realistically, this weaker server-to-edge security still represents a vulnerability and should be avoided, especially given the ease with which it is possible to upgrade the security of an origin server by using [free origin encryption](https://blog.cloudflare.com/cloudflare-ca-encryption-origin/).

![SSL/TLS self-signed diagram](https://www.cloudflare.com/img/learning/cdn/tls-ssl/origin-ssl-protection-diagram.png)

Proper security is also important to organic search; encrypted web properties result in stronger ranking on Google search.

An SSL/TLS connection operates differently than a traditional [TCP/IP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) connection. Once the initial stages of the TCP connection have been made, a separate exchange occurs to set up the secure connection. This article will refer to the device requesting the secure connection as the client and the device serving up the secure connection as the server, as is the case with a user loading a webpage encrypted with SSL/TLS.

#### First the TCP/IP handshake is made in 3 steps:

  1. The client sends a SYN packet to the server in order to initiate the connection.
  2. The server than responds to that initial packet with a SYN/ACK packet, in order to acknowledge the communication.
  3. Finally, the client returns an ACK packet to acknowledge the receipt of the packet from the server. After completing this sequence of packet sending and receiving, the TCP connection is open and able to send and receive data.

![TCP 3-way handshake diagram](https://www.cloudflare.com/img/learning/cdn/tls-ssl/tcp-handshake-diagram.png)

Once the TCP/IP handshake has occurred, the [TLS encryption handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) begins. The detailed processes behind a TLS handshaking implementation are beyond the scope of this guide. Instead we will focus on the core purpose of the handshake and the time required to complete the process.

#### From a high level, there are three main components to a TLS handshake:

  1. The client and the server negotiate TLS versions and the type of cryptography cipher to be used in the communication.
  2. The client and server take steps to ensure mutually authentic communication.
  3. A key is exchanged to be used in future encrypted communications.



In the diagram below, each of the steps involved in a TCP/IP handshake and a TLS handshake are visualized. Keep in mind that each arrow represents a separate communication which must travel physically between the client and the server. Since the total number of messages back and forth are increased when using TLS encryption, web page load times are increased.

![SSL/TLS handshake diagram](https://www.cloudflare.com/img/learning/cdn/tls-ssl/tls-ssl-handshake.png)

For illustrative purposes it can be said the TCP handshake takes about 50ms, the TLS handshake may take about 110ms. This is largely a result of the time it takes for data to be sent both ways between the client and server. The idea of [round-trip time (RTT)](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/), which is the amount of time it takes for information to travel from one device to another and back again, can be used to quantify how “expensive” a connection is to create. If left unoptimized and without the use of a CDN, additional RTT represents increases in [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) and load times for end-users. Luckily, there are optimizations that can be made to improve total load time and reduce the number of trips back and forth.

## How can SSL latency be improved?

SSL optimizations can reduce RTT and improve page load time. Here are 3 of the ways a TLS connection can be optimized:

**TLS Session Resumption** \- a CDN can keep a connection alive between the origin server and the CDN network for longer by resuming the same session for additional requests. Keeping the connection alive saves time spent renegotiating the connection between the CDN and the origin server when the client requires an uncached origin fetch. As long as the origin server receives additional requests while the connection to the CDN is maintained, additional visitors to the site will experience lower latency.

![session resumption real time infographic](https://www.cloudflare.com/img/learning/cdn/tls-ssl/session-resumption-real-time.png)

The overall cost of a session resumption is less than 50% of a full TLS handshake, mainly because session resumption only costs one round-trip while a full TLS handshake requires two. Additionally, a session resumption does not require any large finite field arithmetic (new sessions do), so the CPU cost for the client is almost negligible compared to that in a full TLS handshake. For mobile users, the performance improvement by session resumption means a much more reactive and battery-life-friendly surfing experience.

![session resumption CPU time infographic](https://www.cloudflare.com/img/learning/cdn/tls-ssl/session-resumption-cpu-time.png)

**Enable TLS False Start** \- when a visitor is viewing the site for the first time, the session resumption mentioned above will not be helpful. TLS False Start allows the sender to send application data without a complete TLS handshake.

![SSL/TLS False Start handshake diagram](https://www.cloudflare.com/img/learning/cdn/tls-ssl/tls-ssl-false-start-handshake.png)

The False Start does not modify the TLS protocol itself, it only modifies the timing in which data is transferred. Once the client begins the key exchange, encryption can be assured and data transfer begins. This modification reduces the total number of roundtrips, cutting down the latency required by 60ms.

**Zero Round Trip Time Resumption (0-RTT)** \- 0-RTT allows for session resumption without addition RTT latency added to the connection. For resumed connections using [TLS 1.3](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3/) and 0-RTT, connection speed is improved, leading to a faster and smoother web experience for web sites that users visit regularly. This speed boost is especially noticeable on mobile networks.

0-RTT is an effective improvement, but is not without some security tradeoffs. To overcome the risk of what is known as a replay attack, a CDN service may implement restriction on the type of HTTP requests and the allowed parameters. To learn more, explore an [introduction to 0-RTT](https://blog.cloudflare.com/introducing-0-rtt/).

## CDN protection from DDoS attacks

One of the most substantial security vulnerabilities of web properties on the modern Internet is the use of [distributed denial-of-service (DDoS) attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/). Over time DDoS attacks have increased in size and complexity, with attackers utilizing [botnets](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/) to target websites with attack traffic. A large and properly configured CDN has the potential benefit of scale as a protective factor against DDoS; by having enough data center locations and sizable bandwidth capabilities, a CDN is able to withstand and mitigate an amount of incoming attack traffic that would easily overwhelm the targeted origin server.

Other steps can be taken to secure a TLS connection. Learn more about the [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) and [staying on top of TLS attacks](https://blog.cloudflare.com/staying-on-top-of-tls-attacks/). Check your website for proper HTTPS usage in the [Cloudflare Diagnostic Center](https://www.cloudflare.com/diagnostic-center/).
