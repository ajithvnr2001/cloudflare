---
url: https://www.cloudflare.com/learning/performance/what-is-http3/
title: What is HTTP/3?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:02.776763+00:00
---

# What is HTTP/3?

> Source: https://www.cloudflare.com/learning/performance/what-is-http3/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is HTTP/3? 

HTTP/3 is the next major revision of the hypertext transfer protocol (HTTP). It will improve speed, security, and reliability. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what improvements are expected in HTTP/3 
  * Recognize how the protocol will shape user experience 
  * Describe anticipated security benefits 



Related content  [ HTTP/2 vs. HTTP/1.1: How do they affect web performance? ](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[ How to test the speed of a website ](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[ Tips to improve website speed ](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[ How does website speed boost SEO? ](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)

On this page

  * What is HTTP/3?

  * What is new in HTTP/3?

  * Why is a new version of HTTP needed?

  * What is encrypting by default?

  * Is HTTP/3 available now?




## What is HTTP/3?

The Hypertext Transfer Protocol (HTTP) is an essential backbone of the Internet — it dictates how communications platforms and devices exchange information and fetch resources. In short, it is what allows users to load websites.

HTTP/3 is the latest major version of [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/). Web browsers and servers can use it for significant upgrades to user experience, including performance, reliability, and security. Negotiating HTTP versions happens seamlessly, requiring no changes to website code.

## What is new in HTTP/3?

HTTP/3 is the first major upgrade to HTTP since [HTTP/2](https://www.cloudflare.com/learning/performance/http2-vs-http1.1/) was approved in 2015. It was published and made available to all Cloudflare customers in 2021.

An important difference in HTTP/3 is that it runs on QUIC, a new transport protocol. QUIC is designed to be fast and to support switching rapidly between networks. It relies on the User Datagram Protocol ([UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)) rather than the Transmission Control Protocol ([TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)), which mitigates an issue called head-of-line blocking in TCP, where network packet loss or reordering can slow down high-transaction connections. Furthermore, QUIC separates out the layer 4 transport connection from the layer 3 IP flow, allowing for migration between different networks without disruption.

QUIC can better support mobile-heavy Internet usage in which people carry smartphones and constantly switch from one network to another as they move about their day. This type of Internet usage was not common when the first Internet protocols were developed: devices were less portable and did not switch networks very often.

Google started work on an early version of QUIC in 2012. In 2016 it was adopted by the Internet Engineering Task Force (IETF) — a vendor-neutral standards organization — as they started creating the new HTTP/3 standard. After consulting with experts around the world, the IETF has made a host of changes to develop the now-standard version of QUIC published as [RFC 9000](https://datatracker.ietf.org/doc/html/rfc9000).

## Why is a new version of HTTP needed?

QUIC helps fix some of HTTP/2's biggest shortcomings:

  * Decreasing the effects of packet loss — when one [packet](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) of information does not make it to its destination, it will no longer block all streams of information, a problem known as "head-of-line blocking"

  * Faster connection establishment: QUIC combines the cryptographic and transport [handshakes](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)

  * Zero [round-trip time](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/) (0-RTT): For servers they have already connected to, clients can skip the handshake requirement (the process of acknowledging and verifying each other to determine how they will communicate)

  * More comprehensive encryption: QUIC is [encrypted](https://www.cloudflare.com/learning/ssl/what-is-encryption/) by default, making HTTP/3 more secure than HTTP/2 (more on this below)

  * Protecting against HTTP/2 "[Rapid Reset](https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack)" distributed denial-of-service (DDoS) attacks, which can slow down or crash a web server, by using a credit-based system for streams (a "stream" is a single HTTP request and response exchange) to allow HTTP/3 servers fine-grained control over stream concurrency

  * Developing a workaround for the sluggish performance when a smartphone switches from WiFi to cellular data, such as when leaving the house or office




## What is encrypting by default?

Requiring encryption within the transport layer, rather than at the application layer, has important implications for security. It means that the connection will always be encrypted. Previously, in HTTPS, the encryption and transport-layer connections occurred separately. TCP connections could carry data that was either encrypted or unencrypted, and the TCP handshake and Transport Layer Security ([TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)) handshake were distinct events. However, QUIC sets up encrypted connections by default at the transport layer — application-layer data will always be encrypted.

QUIC accomplishes this by combining the two handshakes into one action, reducing latency since applications must wait for only one handshake to finish before sending data. It also encrypts metadata about each connection, including packet numbers and some other parts of the header, to help keep information about user behavior out of attackers' hands. This feature was not possible with HTTP/2 because it relied on TCP and TLS.

HTTP historically used [plaintext](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/) TCP, which has negative consequences for security, since anyone monitoring communications can read requests and responses. Today, websites and web browsers prefer to encrypt all HTTP communications to help keep everyone safer and protect sensitive data. QUIC's encryption by default supports that goal.

## Is HTTP/3 available now?

Yes. HTTP/3 is implemented as standard in all major Web browsers and can be enabled by all Cloudflare customers without any changes to their origin. Learn how to make the switch for [your domain](https://developers.cloudflare.com/speed/optimization/protocol/).

Cloudflare Radar maintains up-to-date statistics on [HTTP version usage](https://radar.cloudflare.com/adoption-and-usage).
