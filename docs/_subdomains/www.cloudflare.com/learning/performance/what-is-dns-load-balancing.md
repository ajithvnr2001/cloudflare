---
url: https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/
title: What is DNS-based load balancing?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:59.393096+00:00
---

# What is DNS-based load balancing?

> Source: https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is DNS-based load balancing? 

DNS load balancing improves application availability and performance by directing users to multiple IP addresses for a single domain. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define DNS-based load balancing 
  * Explain how round-robin DNS works 
  * Understand various DNS-based load balancing configurations 



Related content  [ What is load balancing? | How load balancers work ](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[ What is server failover? | Failover meaning ](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[ Types of load balancing algorithms ](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[ Load balancing for multi-cloud and hybrid cloud: How it works ](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[ What is cloud load balancing? | LBaaS ](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)

On this page

  * What is Domain Name System based load balancing?

  * What is round-robin DNS?

  * How does round-robin DNS work?

  * What other types of DNS-based load balancing are there?

  * How does Cloudflare&#39




## What is Domain Name System (DNS) based load balancing?

[Load balancing](https://www.cloudflare.com/learning/performance/what-is-load-balancing/) is the practice of distributing traffic across more than one server to improve performance and [availability](https://www.cloudflare.com/learning/performance/glossary/application-availability/). Organizations use different forms of load balancing to speed up both websites and private networks. Without load balancing, most Internet applications and websites would not handle traffic effectively or function correctly.

[DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) is often referred to as the Internet's phonebook because it translates website domains (like google.com or nytimes.com) into IP addresses. An IP address is a long numerical label servers use to identify websites and any device connected to the Internet. By translating [domain names](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) to IP addresses — a process called DNS resolution — DNS saves people from memorizing long sequences of numbers to access websites and applications.

In DNS resolution, an Internet user's browser contacts a DNS server to request the destination website's correct IP address. The act of requesting an IP address from a domain is called a DNS query.

DNS-based load balancing is a specific type of load balancing that uses the DNS to distribute traffic across several servers. It does this by providing different IP addresses in response to DNS queries. Load balancers can use various methods or rules for choosing which IP address to share in response to a DNS query.

One of the most common DNS load balancing techniques is called [round-robin DNS](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/).

## What is round-robin DNS?

Round-robin DNS has the same goal as other types of DNS-based load balancing: improving a site's performance and reliability by distributing traffic. However, as opposed to using a specialized software-based or hardware-based load balancer, round-robin DNS performs load balancing using a type of DNS server called an [authoritative nameserver](https://www.cloudflare.com/learning/dns/dns-server-types/#authoritative-nameserver).

Authoritative nameservers hold DNS records called [A records](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/) or AAAA records, which contain a domain’s name and its matching IP address. When a client submits a DNS query, the query's goal is to find the A (or AAAA) record. A domain will have a single A record tied to a single IP address in a basic setup, meaning a DNS query will always return the same IP address.

However, in round-robin DNS, domains have multiple A records, each tied to a different IP address. As DNS queries come in, IP addresses rotate in a round-robin fashion, spreading the requests across the associated servers.

## How does round-robin DNS work?

If there are five IP addresses in round-robin DNS, a DNS query would only return IP address #1 for every sixth request. Because each IP address corresponds to a different server, this setup reduces each server's workload, making it less likely to become overwhelmed by requests.

To understand how round-robin DNS works, compare the act of visiting a website to sending a company a piece of mail. Suppose the company uses a PO box to receive customer mail, but they receive more mail than their singular PO box can handle. To help solve this problem, the company could purchase more PO boxes.

For the multiple PO box strategy to work, the company must ensure that no one box overflows with mail. That means that the PO box address that appears when customers look up the company's mailing address would need to alternate sequentially. Customer #1 would see PO box address #1; then, customer #2 would see PO box address #2. This method would help reduce the burden on the individual PO boxes by increasing overall capacity. Without the additional mailboxes, a single PO box could easily overflow, delaying incoming mail.

Like in the PO box example, round-robin DNS protects servers from becoming overwhelmed with requests, avoiding any delays in processing them.

## What other types of DNS-based load balancing are there?

While the round-robin approach is popular, it is not the only method for routing traffic. Most load balancers allow domain owners to choose from several traffic routing rules.

One example of a DNS-based load balancing configuration is a weighted algorithm where different servers are assigned relative weights based on their capacity to handle traffic. Traffic is then assigned proportionately. For example, if server A has twice the capacity of server B, then the load balancer would give twice the amount of traffic to server A compared to server B. It would do this by returning server A's IP address in response to DNS queries. Weighted round-robin or weighted least connection are examples of this type of load balancing algorithm.

Many of the DNS-based load balancing approaches are dynamic, meaning that the load balancers consider server health and server response times when assigning requests. Dynamic algorithms can take many forms. "Least connection" is one type of dynamic load balancing algorithm. In the least connection configuration, server monitoring determines which server currently has the fewest open connections and then assigns incoming traffic to that server by providing its IP address in response to DNS queries.

Geo-location is another widely used dynamic algorithm. In this configuration, the load balancer assigns requests from a region to a defined server or server set. For example, all requests coming from France might go to ‘server F,’ and all requests coming from Spain might go to ‘server S.’

A proximity-based algorithm accomplishes something similar. In this configuration, load balancers dynamically assign traffic to the server closest to the user.

Dynamic algorithms follow slightly different rules but ultimately do the same thing: monitor server health and optimize how traffic is assigned.

## How does Cloudflare's DNS-based load balancing work?

Cloudflare Load Balancing is a DNS-based load balancing solution that actively monitors server health via HTTP/HTTPS requests. Based on the results of these health checks, Cloudflare steers traffic toward healthy origin servers and away from unhealthy servers. Cloudflare Load Balancing also offers customers who [reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/) their traffic the additional security benefit of masking their origin server's IP address. Learn more about [Cloudflare Load Balancing](https://www.cloudflare.com/load-balancing/).
