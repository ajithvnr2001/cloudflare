---
url: https://www.cloudflare.com/learning/performance/glossary/application-availability/
title: What is application availability?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:11.301280+00:00
---

# What is application availability?

> Source: https://www.cloudflare.com/learning/performance/glossary/application-availability/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is application availability? 

Application availability is the amount of time when an application is up and running. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Describe application availability and contrast it with reliability 
  * Understand uptime, downtime, and availability levels 
  * Explain the components of high availability architecture 



Related content  [ How to keep a website from going down ](https://www.cloudflare.com/learning/performance/preventing-downtime/)[ What is load balancing? | How load balancers work ](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[ Types of load balancing algorithms ](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[ What is server failover? | Failover meaning ](https://www.cloudflare.com/learning/performance/what-is-server-failover/)

On this page

  * What is application availability?

    * Application reliability vs. availability

    * Calculating application availability levels

  * What is uptime? What is downtime?

  * What affects web application availability?

  * What is high availability?

  * What are the components of a high-availability application architecture?

    * Load balancing

    * Health checks

    * Redundancy and backups

    * Caching

    * Reliable DNS

    * Application availability monitoring

  * What is continuous availability?

  * What level of availability does a web application need?




## What is application availability?

Application availability measures the amount of time an application is operational. An application is available when it is working as expected, fulfilling users' requests; an application is not available if it is not functioning or not reachable by end users.

For web applications, maximizing availability is an important part of development. Application availability can be improved by a combination of backend infrastructure optimization, frontend optimization, and attack mitigation.

Users have high expectations for web application availability. [Downtime](https://www.cloudflare.com/learning/performance/preventing-downtime/) can have a big impact on both revenue and reputation. Think of a store's "open" hours: If a store is closed at unexpected times, customers will go elsewhere. Similarly, users unable to get the service they need from a software application will stop using that application, resulting in fewer customers and lost revenue.

For business-to-business (B2B) applications, availability is usually included as part of a service-level agreement (SLA), expressed as a percentage of time the application is expected to be up and running. Application developers in such cases have a contractual obligation to provide a certain availability level to their customers.

#### Application reliability vs. availability

"Availability" is a concept that applies to systems and services of all kinds, from servers to apps to [APIs](https://www.cloudflare.com/learning/security/api/what-is-an-api/). It is measured as a percentage: An application that is down for 36 seconds every hour has 99% availability.

Reliability refers to the ability of a system or application to deliver services as expected, without errors, over a period of time. An application can be available while still being unreliable, if it performs slowly or produces unexpected, incorrect results. Going back to the previous analogy, an unavailable store is closed; an unreliable store is open but the shelves might have items in the wrong places.

#### Calculating application availability levels

The measurement of application availability is often calculated over the course of a calendar year. This table shows how much downtime an application with various levels of availability will have out of a 365-day period. (Downtime is cumulative, and can happen over several different periods or all at once.)

Availability Total downtime per year

95% 18 days and 6 hours

99% 3 days, 15 hours, and 36 minutes

99.9% 8 hours, 45 minutes, and 36 seconds

99.99% 52 minutes and 34 seconds

99.999% ("five nines") 5 minutes and 15 seconds

## What is uptime? What is downtime?

Uptime is when an application is running as expected. Downtime is when a device or service is not operational. In many contexts, uptime and availability are synonyms.

## What affects web application availability?

The Internet is complex, and a lot of different factors can impact the availability and performance of a web application. Some of the factors are within application developers' control, and some are not. But there are several steps developers can take to account for and mitigate the factors that impact availability.

  * **Attacks:** [Distributed denial-of-service (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attacks or [bot attacks](https://www.cloudflare.com/learning/bots/what-is-a-bot-attack/) can overwhelm an application and make its services unavailable to other users, either by tying up all available bandwidth and computing power or by crashing the application altogether. Attacks that compromise an application from the inside, such as [ransomware attacks](https://www.cloudflare.com/learning/security/ransomware/what-is-ransomware/) or [SQL injection attacks](https://www.cloudflare.com/learning/security/threats/sql-injection/), can also cause an application to stop working.

  * **Infrastructure failures:** Host servers that slow down or crash can cause an application to become unavailable. Server performance can degrade for a variety of reasons, from hardware failure to software bugs to sudden spikes in requests. If requests continue going to servers that are performing slowly or failing, the requests may go unanswered.

  * **High traffic or usage:** Users can overwhelm an application if too many are using it at once. Ecommerce platforms, for example, see usage spikes for product releases, sales, or shopping seasons. This problem can be exacerbated by [bot traffic](https://www.cloudflare.com/learning/bots/what-is-bot-traffic/).

  * **Bugs:** Errors in application software can cause crashes that make an application unavailable.

  * **Client-side problems:** Inefficient code on the frontend can crash a user's device or browser, or cause compatibility issues.




## What is high availability?

High availability is an elite level of consistent availability achieved with backups and by avoiding single points of failure. In a high-availability architecture, no one server or gateway or service going down results in unavailability. A high-availability architecture must prevent cyber attacks as well.

## What are the components of a high-availability application architecture?

#### Load balancing

[Load balancing](https://www.cloudflare.com/learning/performance/what-is-load-balancing/) distributes computational loads and network traffic evenly across groups of servers. This ensures no one server or group of servers gets overwhelmed with more traffic than it can efficiently handle.

There are a variety of [load-balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/): Some load balancers distribute workloads evenly no matter what, while others use dynamic algorithms to respond to real-time network conditions and server status.

#### Health checks

Web servers inevitably go down from time to time. A health check is a service that monitors whether an origin server is online or not. Health checks enable load balancers to respond to server status so that requests are not directed to a server that has gone offline.

#### Redundancy and backups

High-availability applications build redundancy into their architecture. Such applications can revert to a backup copy of an application's data in the event of a ransomware attack or a database becoming unavailable for some other reason. Redundant services and server pools ensure a server's or an API's crash does not impact the application's functionality.

#### Caching

Static elements of a web application can be served by a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) even if the underlying infrastructure has crashed. A [cached](https://www.cloudflare.com/learning/cdn/what-is-caching/) version of a web application might not have full functionality but can be technically available until full service is restored. (Learn more about the [Cloudflare Always Online](https://www.cloudflare.com/always-online/) service.)

#### Reliable DNS

The [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) is what allows users to reach application servers over a network. If DNS goes down or stops being able to find the right IP address, users cannot load the application. Using a reliable DNS provider with global reach and the ability to stop DNS-focused DDoS attacks can ensure DNS does not impact availability.

#### Application availability monitoring

The use of an external app availability monitoring tool can help service providers track availability and respond as quickly as possible when their applications go down.

## What is continuous availability?

Continuous availability is an approach to computing infrastructure design that ensures an application or system remains operational continuously. The goal of continuous availability is _100%_ availability, which may not be possible, practically speaking. The Internet was designed to withstand a nuclear war, yet Internet service still goes down for users sometimes. Nonetheless, continuous availability is a worthy goal that helps provide the best possible service for users.

## What level of availability does a web application need?

The more available an application is, the greater the resources that must be expended in its support. In other words, 99.999% availability can be expensive. Developers must decide how much downtime they or their customers will tolerate, and build accordingly.

Fortunately, Cloudflare makes high availability architecture much more feasible for application developers. Cloudflare includes load balancing, caching, stream delivery, DDoS attack mitigation, and bot management natively built into its service. Cloudflare even offers a [developer platform](https://www.cloudflare.com/developer-platform/) to allow developers to build new features or entirely new applications that run across a global network with a presence in 335+ cities around the world.

Learn how Cloudflare can keep applications [available](https://www.cloudflare.com/performance/ensure-application-availability/).
