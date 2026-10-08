---
url: https://www.cloudflare.com/learning/performance/speed-up-a-website/
title: Tips to improve website speed | How to speed up websites
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:38.998967+00:00
---

# Tips to improve website speed | How to speed up websites

> Source: https://www.cloudflare.com/learning/performance/speed-up-a-website/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  Tips to improve website speed 

If a website is performing poorly, developers can take several steps to diagnose and fix its problems. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn how to get started on optimizing website performance 
  * Understand some of the factors that affect website speed 
  * Choose between various performance-improving strategies 



Related content  [ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[ How to test the speed of a website ](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[ Mobile performance: How to make a site mobile friendly ](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)

On this page

  * How to test website performance

  * How to improve website performance

    * Optimize images

    * Limit the number of HTTP requests

    * Use browser HTTP caching

    * Remove unnecessary render-blocking JavaScript

    * Limit the use of external scripts

    * Limit redirect usage

    * Use effective third-party services for important website functions

  * How Cloudflare helps improve web performance




Web performance is a catch-all term for the measurable and perceived quality of a website’s user experience — with a particular emphasis on the page’s speed and reliability.

Developers and website owners can take a number of steps to improve their website’s performance. These steps include optimizing web design factors like image sizes, code formatting, and external script usage, along with choosing good providers for [hosting](https://www.cloudflare.com/developer-platform/solutions/hosting/), content caching, and load balancing.

When webpages load faster and more reliably, they not only offer a better user experience, but also tend to rank higher in organic search results, are more visible to potential visitors, and often see [higher conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/).

![site speed](https://www.cloudflare.com/img/learning/performance/speed-up-a-website/site-speed-page-loading.svg)site speed

## How to test website performance

A critical first step in improving a website’s performance is measuring its current performance. A variety of factors determine how users (and other parties) perceive a website’s speed and reliability, and measuring these factors is the only way to know which actions will drive the most improvement.

A number of free tools exist for performance measurements, including [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) (available in Google Chrome web browser’s [DevTools suite](https://developer.chrome.com/docs/devtools/)) and Cloudflare Observatory (available to any Cloudflare user in their dashboard).

What should website owners use these tools to evaluate? A good place to start is the [Core Web Vitals](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/) — a set of three metrics which measure important web performance aspects:

  * **Largest Contentful Paint** measures how quickly the largest element on a page loads

  * **First Input Delay** measures how quickly a page responds to user input

  * **Cumulative Layout Shift** measures the visual stability of a page’s elements




In addition to providing valuable user experience signals, improving a page’s Core Web Vitals [can make it rank higher in organic Google search results](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/).

Other important metrics to evaluate include Time to First Byte (how quickly a page begins loading), DNS lookup speed (how quickly a page’s [Domain Name Service](https://www.cloudflare.com/learning/dns/what-is-dns/) translates a [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) into an IP address), and Time to Interactive (how quickly a user can interact with a page).

To see how measuring these metrics might translate into action, consider the following examples:

  * A webpage with a slow Largest Contentful Paint is taking too long to show users its biggest component. The webpage’s owner could investigate whether any unnecessary code is loading before that component — and consider whether to remove said code. A webpage with a slow Time to First Byte is taking too long to retrieve website resources from its [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). The webpage’s owner could investigate response times for their DNS provider and website host — with an eye towards reconfiguring or replacing one or both services.



## How to improve website performance

While there is no guaranteed blueprint for strong web performance, website owners can use the following best practices to help boost site speed and reliability:

#### Optimize images

Images often take the longest to load on a website since image files tend to be larger in size than HTML and CSS files. Luckily, image load time can be reduced via [image optimization](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/), which typically involves reducing its resolution and dimensions, and [compressing the image file](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/) itself.

#### Limit the number of HTTP requests

Most webpages require browsers to make multiple [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) requests for various assets on the page, including images, scripts, and CSS files. In fact, many webpages require dozens of these requests. Each request results in a round trip to and from the server hosting the resource, which can add to the overall load time for a webpage.

Because of these potential issues, the total number of assets each page needs to load should be kept to a minimum. A speed test should help identify which HTTP requests are taking the most time.

#### Use browser HTTP caching

The browser cache is a temporary storage location where browsers save copies of static files so that they can load recently visited webpages more quickly. Developers can instruct browsers to cache elements of a webpage that will not change often. Instructions for browser caching go in the headers of HTTP responses from the hosting server. This greatly reduces the amount of data that the server needs to transfer to the browser, shortening load times for users who frequently visit certain pages.

#### Remove unnecessary render-blocking JavaScript

Webpages may have unnecessary code that loads before more important page content, slowing down the overall load time. This is especially common on large websites with many owners independently adding code and content. Web page owners can use a web performance tool to identify unnecessary code on poorly performing pages.

#### Limit the use of external scripts

Any scripted webpage elements that are loaded from somewhere else — such as external commenting systems, CTA buttons, CMS plugins, or lead-generation popups — need to be loaded each time a page loads.

Depending on the size of the script, these can slow a webpage down, or cause the webpage to not load all at once (this is called 'content jumping' or 'layout shifting' and can be especially frustrating for mobile users, who often have to scroll to see the entire webpage).

#### Limit redirect usage

A redirect is when visitors to one webpage get forwarded to a different page instead. Redirects add a few fractions of a second, or sometimes even whole seconds, to page load times. Redirects are sometimes unavoidable, but they can be overused — and may accumulate over time on larger websites with multiple owners. Website owners should institute clear guidelines on redirect usage and periodically scan important web pages for unnecessary redirects.

Minify CSS and JavaScript files

Minifying code means removing anything that a computer doesn't need in order to understand and carry out the code, including code comments, whitespace, and unnecessary semicolons. This makes CSS and JavaScript files slightly smaller so that they load faster in the browser and take up less bandwidth. Although minification usually provides marginal performance improvements, it is still an important best practice.

#### Use effective third-party services for important website functions

  * **Hosting:** Even the best-designed website will load slowly if its origin server responds slowly to requests. Website owners should choose a server with an average response time of under 200 ms, and with a good record for reliability.

  * **DNS:** DNS is a system that translates domains (e.g. example.com) into IP addresses — an important part of the page loading process. Website owners should choose DNS services that [deliver results (‘resolve’) quickly and reliably](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/), rather than relying on their web host’s DNS.

  * **Caching:** The closer website content sits to the people requesting it, the faster they’ll be able to receive it. Website owners should use a [content delivery network](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) (CDN) to [cache](https://www.cloudflare.com/learning/cdn/what-is-caching/) web content in many locations around the world, so user requests do not have to travel hundreds or thousands of miles (and across many [autonomous networks](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)) to reach the website’s origin server.

  * **Cybersecurity:** DDoS attacks, malicious bots, and other cyber attacks can degrade a website’s performance. This topic is too broad to cover in detail here, but website owners should choose a [web application security](https://www.cloudflare.com/learning/security/what-is-web-application-security/) provider which filters out malicious traffic without slowing down legitimate traffic.




## How Cloudflare helps improve web performance

Cloudflare is a global platform for Internet security and performance. The platform can help websites of any size and complexity improve their performance by connecting to a 335+-city global network.

For [personal websites](https://www.cloudflare.com/personal/) and [small businesses](https://www.cloudflare.com/small-business/), Cloudflare offers [free and low-cost plans](https://www.cloudflare.com/plans/) that activate in minutes and automatically include important website performance enhancements:

  * High-performing DNS services

  * CDN

  * Image optimization

  * Mobile optimization

  * Protection against DDoS attacks and common malicious bots




For larger businesses, Cloudflare also offers [enterprise-grade performance services](https://www.cloudflare.com/performance/) that work with any sort of web application or infrastructure.
