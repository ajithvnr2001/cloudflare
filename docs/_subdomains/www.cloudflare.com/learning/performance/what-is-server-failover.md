---
url: https://www.cloudflare.com/learning/performance/what-is-server-failover/
title: What is server failover? | Failover meaning
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:11.487852+00:00
---

# What is server failover? | Failover meaning

> Source: https://www.cloudflare.com/learning/performance/what-is-server-failover/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is server failover? | Failover meaning 

In server failover, a backup server is set up to take over if and when the primary server fails. Learn how server failover works and why it is crucial for disaster recovery. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define server failover 
  * Understand why server failover is important to disaster recovery and increasing site availability 
  * Explain how different server failover configurations work 



Related content  [ What is load balancing? | How load balancers work ](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[ Types of load balancing algorithms ](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[ What is DNS-based load balancing? ](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[ Load balancing for multi-cloud and hybrid cloud: How it works ](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[ What is cloud load balancing? | LBaaS ](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)

On this page

  * What is server failover?

  * What is server redundancy?

  * What is the difference between failover and switchover?

  * How does server failover work?

    * Active-standby

    * Active-active

  * Why is server failover necessary?

  * What is a failover cluster?

  * What is fast failover?




## What is server failover?

Server failover is the practice of having a backup server (or servers) prepared to automatically take over if the primary server goes offline. Server failover works like a backup generator. When the power goes out in a building or home, a backup generator temporarily restores electricity. Similarly, in server failover, a secondary server takes over when the primary server fails. The goal of server failover is to improve a network or website's fault tolerance, or its ability to continue operating when one of its parts fails.

A server's primary job is to store content and data to share with other computers. While there are different types of servers, web servers are perhaps the most well-known because they keep websites and applications operational. When web servers fail, they cannot process requests, which means they cannot serve data to clients. Without server failover, a failed server can cause a loading error or a site outage.

Servers can fail for many reasons, such as:

  * Power outages

  * Natural disasters

  * Unexpected traffic surges

  * Cyber attacks (like [Distributed Denial of Service (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attacks)

  * Hardware complications (like cable problems or overheating)

  * Operating system issues




While no one can fully predict when or how a server might fail, IT leaders know that server failure is inevitable. Failover is a backup plan that helps prevent a complete outage.

Failover often goes hand in hand with a process called [load balancing](https://www.cloudflare.com/learning/performance/what-is-load-balancing/). Load balancers increase [application availability](https://www.cloudflare.com/learning/performance/glossary/application-availability/) and performance by distributing traffic across more than one server. To ensure requests are assigned to servers that can handle the traffic, many load balancers monitor server health and implement failover.

## What is server redundancy?

Server redundancy is a measure of how many backup servers are in place to support a primary server. For example, a site hosted on one server with no backups is not redundant. Configuring failover creates server redundancy that improves availability and prevents outages. "Availability" describes the amount of time a site or application is online.

## What is the difference between failover and switchover?

The terms "failover" and "switchover" are sometimes confused with one another. In failover, the shift to a redundant server happens automatically. Switchover is a similar process, only the shift to the secondary server happens manually, creating a short period of downtime. Because failover happens automatically, there is usually no downtime associated with a switch to a secondary server.

## How does server failover work?

For server failover to work, servers must be connected so that they can sense issues and take over when necessary. Physical “heartbeat” cables can connect servers and allow for monitoring, just like a heartbeat monitor tracks a person’s heartbeat. Server monitoring can also take place over the Internet.

For example, Cloudflare Load Balancing periodically sends [HTTP/HTTPS requests](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) to server pools to monitor their status. If the HTTP/HTTPS check reveals that a server is unhealthy or offline, Cloudflare will reroute traffic to an available server.

Depending on the configuration, failover works slightly differently. Server failover configurations are either active-active or active-standby.

#### Active-standby

In active-standby, there is a primary server and one or more secondary servers. In a two-server setup, the secondary server monitors the primary one but otherwise remains inactive. If the secondary server senses any change with the primary server, it will take over and advise the data center that the primary server needs restoration. Once the primary server is restored, it takes over once again, and the secondary server resumes a standby position. The act of a primary server resuming operations is called failback.

#### Active-active

By contrast, in a two-server active-active configuration, both servers must remain active. An active-active configuration is typically associated with load balancing because the servers are configured in the same way and share the workload. When a server fails in an active-active configuration, the traffic routes to the operational server or servers.

## Why is server failover necessary?

Server failover is important because a single server's failure could knock a site offline without it.

Server availability can impact industries differently. For example, [ecommerce](https://www.cloudflare.com/ecommerce/) and gaming companies are completely dependent on their site working properly. Other industries, like B2B SaaS companies, risk upsetting their end users if they cannot access the information they need to do their job. At the same time, availability is nonnegotiable for industries that meet urgent needs, like medical or emergency services.

Apart from availability, failover is an important component of most disaster recovery plans. Disaster recovery plans encompass scenarios like failed backups, a network going down, or even power outages. Disaster recovery helps companies maintain business continuity and avoid the lost revenue associated with downtime.

## What is a failover cluster?

A failover cluster refers to a group of two or more servers that work together to make failover possible. Failover clusters create the server redundancy that enables high availability (HA) or continuous availability (CA).

Systems that aim for as little downtime as possible (or 99.999% uptime) are considered HA. If an HA system experiences downtime, it should only last for a few seconds or minutes at a time. Highly-regulated industries, like government services, may need to meet high availability standards for compliance purposes.

CA systems, on the other hand, are created to avoid any downtime at all. No downtime means that users can stay connected to a site or application at all times, even during maintenance. One area where CA might be necessary, for example, is in online stock trading, where transactions are highly time-sensitive. CA systems are more complex to build and maintain because they must account for every single point of failure, from servers to physical location to power access.

## What is fast failover?

As failover configurations can operate slightly differently, the speed at which failover happens can vary. Some load balancers offer fast failover, which means the system monitors server health and can quickly failover when needed. Fast failover is essential to achieve HA or CA.

Cloudflare Load Balancing achieves fast failover by actively monitoring servers and instantly rerouting traffic when an issue is detected, resulting in zero downtime. Learn more about [Cloudflare Load Balancing](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/).
