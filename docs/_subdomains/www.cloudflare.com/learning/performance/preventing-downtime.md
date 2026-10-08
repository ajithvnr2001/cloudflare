---
url: https://www.cloudflare.com/learning/performance/preventing-downtime/
title: How to keep a website from going down
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:33.659356+00:00
---

# How to keep a website from going down

> Source: https://www.cloudflare.com/learning/performance/preventing-downtime/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  How to keep a website from going down 

Keeping a website from ever going down requires a multi-faceted strategy and some effort, but it’s worth mitigating the risks of conversion loss and SEO penalties associated with downtime. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what downtime is and why it matters 
  * Outline the causes of downtime 



Related content  [ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[ How does website speed boost SEO? ](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)

On this page

  * What is downtime?

  * Why do websites go down?

  * How to avoid downtime




## What is downtime?

On the web, downtime is a period of time when a website is unavailable to any or all of its users. During downtime, users trying to access the site may be redirected to an error page, or see an error page created by their browser. These periods of downtime can carry swift penalties for the site, including loss of conversions and even a decline in search engine optimization (SEO) rankings.

## Why do websites go down?

  * **Hosting maintenance:** Web hosts sometimes have to perform maintenance on the servers where website files live. This maintenance can sometimes require periods of downtime. With a [good host](https://www.cloudflare.com/developer-platform/solutions/hosting/), this maintenance time should be announced in advance, it should be minimal, and it should be scheduled during periods of low activity.

  * **Overloaded servers:** Web servers are only able to handle so many requests at a time, and spikes in traffic can overwhelm servers, preventing users from accessing the site. In some cases hosting companies will use multitenancy, meaning that they host multiple sites on a single server. With multitenancy, a traffic spike to one site can create downtime for another, unrelated site.

  * **Hardware malfunctions:** Although hosting servers are generally kept in protected and controlled environments, sometimes this hardware can still fail. Fans can break, storage disks can become corrupted, and power outages or natural disasters can take down entire data centers. Without a backup plan, these hardware malfunctions can create sustained downtime.

  * **Malicious attacks:** Sites can also be taken offline with distributed denial of service [(DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) and other types of attacks. DDoS attacks aim to deliberately overwhelm a site with traffic to create a denial-of-service. More nefarious attacks involve using [brute force](https://www.cloudflare.com/learning/bots/brute-force-attack/) or other means to gain access to the [domain name registrar](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/) or hosting accounts associated with the site. The attackers then use this forged authorization to take down or modify the website.

  * **Programming bugs:** A website’s functionality depends on code executing correctly, and even a single error in this code can bring a website down. Some bugs won’t get triggered until certain rare conditions are met; these are referred to as ‘edge cases’. These edge case bugs may not appear until several hours, or even days, after the bad code was pushed live to the site.

    * **Expired domains:** When a site’s [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) registration expires, the registrar will sever the link between that site’s [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address) and domain name. Once this happens, users will no longer be able to access the site using that domain name.



## How to avoid downtime

While 100% uptime can be difficult to achieve (even Google and Facebook have encountered occasional downtime due to various issues), site owners can take steps to minimize the amount of downtime a site experiences. Here are several key strategies for maximizing [availability](https://www.cloudflare.com/learning/performance/glossary/application-availability/).

**Pick the right host and hosting plan

**

While issues like unplanned server maintenance and hardware failure can affect any web host, some have better uptime records than others. Uptime comparisons of different hosting providers can be found online, and choosing a host with an excellent uptime record will help improve the chances a site stays up. Choosing a host that offers a good monitoring service is also important; the first step to mitigating downtime is knowing that the downtime exists.

Hosting plans with hard usage limits should be avoided. Some hosts will apply daily or monthly bandwidth limits to their users. This means that a spike in traffic, even one that isn’t big enough to overload a server, can result in the host suspending the account and taking the site offline. To avoid downtime, hosting plans with unlimited bandwidth or pay-as-you-go fees for bandwidth overages make the most sense.

Some hosts also offer [failover](https://www.cloudflare.com/learning/performance/what-is-server-failover/) (or ‘redundant’) plans. This means that if the server hosting the site fails, the host will automatically begin hosting that site from a different server. This is a good protection against hosting-related downtime. It should be noted that a good failover plan will utilize servers in different physical locations. If the failover servers are all located in the same data center as the original host, they won’t be of much help during an outage that affects the entire data center, such as a power failure.

**Enable DDoS Protection**

Many organizations don’t look into DDoS protection until after they’ve endured an attack that has caused them significant amounts of downtime. DDoS mitigation services can be turned on proactively to ensure DDoS attacks are quickly addressed and downtime is minimized.

**Exercise web development best practices**

In order to minimize the risk of coding bugs bringing down a site, developers should take some basic precautions. Developing with a local environment, using version control, and immediately testing all production changes to a site, including edge cases, will help diminish the risk of production bugs bringing down a site.

**Choose the right registrar**

Some [domain name registrars](https://www.cloudflare.com/products/registrar/) are more forgiving than others when it comes to [domain name expirations](https://www.cloudflare.com/learning/dns/glossary/expired-domains/). The best registrars for maximizing uptime are those that both do a good job of informing their customers when domains are nearing expiration, as well as offering a generous grace period after expiration. For more on making this decision, see [How to Choose the Best Domain Name Registrar.](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)

**Use a CDN

**

[Content Delivery Networks](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) (CDNs) cache website data at the [network edge](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/) and are able to serve users temporarily cached website files without contacting a host’s [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). CDNs can help provide coverage during minor downtime blips by serving up the site from cache, even if the hosting server is unresponsive.

Keep in mind that the CDN will only cover brief gaps in downtime, as the cached website files have a [Time-To-Live (TTL)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/), after which the CDN will contact the host server again asking for a new copy of the file. This TTL is typically between 30 seconds and five minutes.

**Careful monitoring

**

Being aware of downtime is important to mitigation. In addition to the monitoring provided by a hosting provider, an independent uptime monitoring service is recommended. These services can send alerts to developers the second a website goes down for any reason.
