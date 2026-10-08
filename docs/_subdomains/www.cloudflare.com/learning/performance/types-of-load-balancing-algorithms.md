---
url: https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/
title: Types of load balancing algorithms
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:42.252345+00:00
---

# Types of load balancing algorithms

> Source: https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  Types of load balancing algorithms 

Load balancers decide where to route network traffic based on a set of predetermined rules. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define 'load balancing algorithm' 
  * Differentiate between static and dynamic load balancing algorithms 
  * Unpack the types of algorithms within these two categories 



Related content  [ What is load balancing? | How load balancers work ](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[ What is DNS-based load balancing? ](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[ What is server failover? | Failover meaning ](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[ Load balancing for multi-cloud and hybrid cloud: How it works ](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[ What is cloud load balancing? | LBaaS ](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)

On this page

  * What is a load balancing algorithm?

  * What are the different types of load balancing algorithms?

    * Dynamic load balancing algorithms

    * Static load balancing algorithms

  * How does Cloudflare Load Balancing work?




## What is a load balancing algorithm?

A [load balancer](https://www.cloudflare.com/load-balancing/) is a software or hardware device that keeps any one server from becoming overloaded. A load balancing algorithm is the logic that a load balancer uses to distribute network traffic between servers (an algorithm is a set of predefined rules).

There are two primary approaches to [load balancing](https://www.cloudflare.com/learning/performance/what-is-load-balancing/). _Dynamic load balancing_ uses algorithms that take into account the current state of each server and distribute traffic accordingly. _Static load balancing_ distributes traffic without making these adjustments. Some static algorithms send an equal amount of traffic to each server in a group, either in a specified order or at random.

## What are the different types of load balancing algorithms?

#### Dynamic load balancing algorithms

  * _Least connection:_ Checks which servers have the fewest connections open at the time and sends traffic to those servers. This assumes all connections require roughly equal processing power.

  * _Weighted least connection:_ Gives administrators the ability to assign different weights to each server, assuming that some servers can handle more connections than others.

  * _Weighted response time:_ Averages the response time of each server, and combines that with the number of connections each server has open to determine where to send traffic. By sending traffic to the servers with the quickest response time, the algorithm ensures faster service for users.

  * _Resource-based:_ Distributes load based on what resources each server has available at the time. Specialized software (called an "agent") running on each server measures that server's available CPU and memory, and the load balancer queries the agent before distributing traffic to that server.




#### Static load balancing algorithms

  * _Round robin:_ [Round robin load balancing](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/) distributes traffic to a list of servers in rotation using the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/). An authoritative nameserver will have a list of different [A records](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/) for a domain and provides a different one in response to each DNS query.

  * _Weighted round robin:_ Allows an administrator to assign different weights to each server. Servers deemed able to handle more traffic will receive slightly more. Weighting can be configured within [DNS records](https://www.cloudflare.com/learning/dns/dns-records/).

  * _IP hash:_ Combines incoming traffic's source and destination [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) and uses a mathematical function to convert it into a hash. Based on the hash, the connection is assigned to a specific server.




## How does Cloudflare Load Balancing work?

[Cloudflare Load Balancing](https://www.cloudflare.com/load-balancing/) uses health checks to steer traffic toward healthy servers. It also enables administrators to customize where regional traffic is handled in order to reduce the amount of distance that traffic has to travel. This approach is known as [global server load balancing (GSLB)](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/).
