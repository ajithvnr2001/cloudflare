---
url: https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/
title: How to manage application performance
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:26.091905+00:00
---

# How to manage application performance

> Source: https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  How to manage application performance 

Slow or unreliable applications can drive away customers and frustrate workforces. Modernizing applications and using caching, load balancing, and other content acceleration techniques can help optimize application performance. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * List the negative outcomes of poor application performance 
  * Understand how to overcome challenges like latency and suboptimal network routing 
  * Understand how application modernization impacts ROI 



Related content  [ What is load balancing? | How load balancers work ](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[ What is observability? ](https://www.cloudflare.com/learning/performance/what-is-observability/)[ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)

On this page

  * How to manage application performance

    * Application performance management

  * What are the consequences of poor application performance?

  * What are the causes of application performance issues?

    * Network and infrastructure factors affecting application performance

    * Internal software factors affecting application performance

  * How to boost application performance

  * FAQs

    * What is application performance?

    * What is application performance management?

    * How does poor application performance impact a business?

    * Why is updating legacy applications important for artificial intelligence?

    * How can organizations improve their application performance?




## How to manage application performance

Application performance refers to the responsiveness, reliability, and scalability of an application. When an application takes too long to load, is unavailable, or slows as more people use it, users quickly become frustrated and look for alternatives. Steps to improving application performance include optimizing code and databases, setting up effective [load balancing](https://www.cloudflare.com/learning/performance/what-is-load-balancing/), optimizing for [availability](https://www.cloudflare.com/learning/performance/glossary/application-availability/) to minimize downtime, using a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/), and architecting applications for efficiency.

Customers and employees alike expect software to respond in milliseconds. An application’s performance determines whether these expectations are met or not. Applications powered by [artificial intelligence (AI)](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) raise the bar for performance. They are supposed to provide dynamic, personalized experiences for customers and improve employee decision-making, but if they fail to deliver fast responses to user input, their benefits tend to dissipate.

#### Application performance management (APM)

Application performance management (APM) refers to the set of practices and technologies that track and enhance application performance. "APM" as an acronym can also refer to application performance monitoring, a concept that most in the industry now refer to as "[observability](https://www.cloudflare.com/learning/performance/what-is-observability/)."

## What are the consequences of poor application performance?

Poor performance for customer-facing applications, like websites and mobile apps, affects:

  * **Revenue:** If an ecommerce site is slow, visitors buy from competitors and spend their money elsewhere.

  * **Customer experience and brand reputation:** When a website gains a reputation for being slow or unreliable, customers view the brand the same way.

  * **Competitive advantage and market share:** As slow experiences compel customers to leave bad reviews and move to faster sites and mobile apps, a business's competitive advantage erodes.




For internal software, poor performance impacts employee productivity and satisfaction.

  * **Reduced productivity and efficiency:** When office productivity applications are slow or offline, key internal processes come to a halt. If that software is unresponsive or unavailable, organizations lose hours and days of work.

  * **Increased frustration:** Ensuring employees have positive experiences with the tools they use is crucial for maintaining satisfaction. Internal websites for payroll, benefits, or HR that load slowly diminish employee morale.




See [Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) to learn more.

## What are the causes of application performance issues?

Causes range from the physical distance between users and data centers to unoptimized code. These causes can be divided into network / infrastructure factors and internal application factors.

#### Network and infrastructure factors affecting application performance

Enterprise networks and infrastructure play key roles in performance. Several factors affect [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/), bandwidth, and congestion, including:

  * **Physical distance:** When users are far from the data centers hosting applications, inputs and responses take longer to reach their destinations. Even with fast Internet connections, a video conferencing app hosted in a centralized data center introduces latency for participants on different continents. Organizations can reduce the latency caused by the distance between users and data centers by using a CDN to [cache](https://www.cloudflare.com/learning/cdn/what-is-caching/) content on distributed [edge servers](https://www.cloudflare.com/learning/cdn/glossary/edge-server/) close to users.

  * **Undercapacity and inefficient routing:** Insufficient networks restrict how much data can move at once. A lack of bandwidth and throughput increases queueing, delays, and drops. Suboptimal network [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) or asymmetric paths add hops and processing delays, which increase response times. [Smart routing](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/) can help eliminate these issues.

  * **Infrastructure resource allocation:**The compute, memory, or storage capacity IT teams allot to each application affects speed and reliability. Server health checks, redundancy, load balancing, and other [availability](https://www.cloudflare.com/learning/performance/glossary/application-availability/) techniques are part of ensuring applications have sufficient resources.




#### Internal software factors affecting application performance

Internal factors — involving how developers code and deploy applications — can affect performance. These include:

  * **Unoptimized code:** When developer teams do not optimize code — or they over-use AI-assisted [vibe coding](https://www.cloudflare.com/learning/ai/ai-vibe-coding/) — they can degrade application performance. Unoptimized code or an excessive reliance on third-party scripts introduces inefficiencies, including redundant computations and poor resource use. Development teams should adopt standards for simplifying, [minifying](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/), and reducing code. Reducing resource requests decreases network overhead and improves performance.

  * **Misconfigured servers:**Misconfigured servers increase latency and cause outages that degrade application performance. These misconfigurations include incorrect settings in configuration files that dictate how servers handle requests, databases, and resources. Test servers to ensure they perform as expected.

  * **Suboptimal load balancing:**Uneven workload distribution across server pools results in slower response times, resource waste, and outages under high demand. Sometimes this occurs due to a reliance on static load balancing when a more dynamic approach should be used instead (see [Types of load balancing](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)).

  * **Legacy applications:** Outdated software introduces architectural bottlenecks, resource inefficiencies, and integration overhead. By contrast, [cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)-native architectures like [serverless computing](https://www.cloudflare.com/learning/serverless/what-is-serverless/) allow organizations to shift from the rigid monolithic designs of legacy software to flexible, scalable applications that perform better.

  * **Monitoring gaps:**Gaps in application monitoring prevent IT teams from identifying and addressing performance issues early. These gaps may occur in complex environments with [microservices](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/) or cloud dependencies. (See [What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/))




## How to boost application performance

Improving performance through application modernization prepares your organization to capitalize on AI, which delivers revenue and efficiency benefits. According to the [2026 Cloudflare App Innovation Report](https://www.cloudflare.com/resource/g/app-innovation-report/2026/), organizations that modernize applications are three times more likely to see ROI from AI investments compared to companies that do not. Likewise, 93% of leaders cite updating software as the most important factor in boosting their company’s AI capabilities.

Cloudflare offers a range of solutions to improve application performance and assist with modernization. For example, the [Cloudflare Developer Platform](https://www.cloudflare.com/developer-platform/) lets development teams deploy serverless code instantly across the globe to increase performance, reliability, and scale. The [global Cloudflare network](https://www.cloudflare.com/network/) and CDN platform — with caching, [image optimization](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/), smart routing, and load balancing included — reduce application latency and improve load times. Using the Cloudflare network with [Workers AI](https://www.cloudflare.com/developer-platform/products/workers-ai/) lets developers run AI-powered applications at the edge, close to users, giving them the responsive experiences they expect.

## FAQs

#### What is application performance?

Application performance encompasses how quickly an application responds, how reliable it is, and how well it scales. When software takes too long to load or becomes unavailable, users often experience frustration and seek alternative options.

#### What is application performance management (APM)?

Application performance management involves the technologies and practices organizations use to track and enhance how their software runs.

#### How does poor application performance impact a business?

For customer-facing software, slow response times lead to lost revenue, damaged brand reputation, and eroded competitive advantage. For internal tools, poor performance halts crucial processes, reduces efficiency, and lowers employee morale.

#### Why is updating legacy applications important for artificial intelligence (AI)?

Modernizing software allows organizations to shift from rigid monolithic architectures to flexible, scalable systems. Companies that update their applications are three times more likely to achieve a return on investment from their AI implementations compared to companies that do not.

#### How can organizations improve their application performance?

Teams can boost responsiveness through several methods: by optimizing code and databases, using dynamic load balancing, implementing a content delivery network (CDN) to cache content on distributed edge servers close to users, and adopting cloud-native architectures.
