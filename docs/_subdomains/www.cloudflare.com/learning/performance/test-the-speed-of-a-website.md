---
url: https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/
title: How to Test the Speed of a Website
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:39.554930+00:00
---

# How to Test the Speed of a Website

> Source: https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  How to test the speed of a website 

Testing website performance is an important part of website development and maintenance. A site speed test can help developers identify specific assets or resources that are causing their websites to perform slowly. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Know where to go to test a website's performance 
  * Understand why testing site speed is necessary 
  * Understand how to interpret speed test results 



Related content  [ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[ Mobile performance: How to make a site mobile friendly ](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)

On this page

  * Why test site speed?

  * Why is site speed important?

  * How can developers test the speed of their websites?

  * What performance metrics will a site speed test provide?




## Why test site speed?

When automobile manufacturers develop a new model of a car, it may accelerate quickly and drive smoothly on paper, but the manufacturer can't know how well the car actually runs until a test driver takes it out on the track. Similarly, how a site performs in a local testing environment is not always a good indication of how it will perform in the wider [Internet](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/), which spans across a variety of network conditions and in various locations.

![Site Speed Test](https://www.cloudflare.com/img/learning/performance/test-the-speed-of-a-website/what-is-site-speed.svg)Site Speed Test

Website speed tests aim to simulate real-world conditions and provide data on how well a website actually performs. A website speed test should let developers know not just how fast their site or application is, but also which elements on the page are causing slowdowns.

## Why is site speed important?

[Websites that perform poorly](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) can frustrate users, driving them away. Slow site performance negatively impacts [search rankings (or SEO)](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/), [conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/), and the overall user experience.

## How can developers test the speed of their websites?

A number of organizations, [including Cloudflare](https://developers.cloudflare.com/fundamentals/get-started/basic-tasks/test-speed/), offer website speed tests. Many speed tests are able to identify individual elements of a webpage that are slowing the page down, in addition to providing performance metrics.

Beyond testing speed, Cloudflare also offers free [CDN services](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/), which can boost website performance and reduce latency.

## What performance metrics will a site speed test provide?

The basic Cloudflare speed test measures the following:

  * **Load time:** The time it takes for a web browser to finish downloading and displaying the webpage (measured in milliseconds)

  * **Time to First Byte (TTFB):** How long it takes for the browser to receive the first byte of data from the web server (measured in milliseconds).

  * **Requests:** The number of [HTTP requests](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) for resources that a browser has to make in order to fully load the page.




Not all speed test providers will break down site speed using the same performance metrics. Other performance metrics include:

  * **DOMContentLoaded (DCL):** This measures the time it takes for the full HTML code of the page to be loaded; images, CSS files, and other assets don't have to be loaded.

  * **Time to above-the-fold load:** 'Above the fold' refers to the area of a webpage that fits in a browser window without a user having to scroll down.

  * **First Contentful Paint (FCP):** The time at which content first begins to be 'painted,' or rendered, by the browser. This can be any aspect of the page, including text, images, or non-white background colors.

  * **Page size:** The total file size of all content and assets that appear on the page.

  * **Round trips:** This metric counts the number of round trips necessary to load the webpage. When an HTTP request travels all the way from a browser to the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/), and the server's HTTP response goes all the way back, this constitutes a round trip.

  * **Render-blocking round trips:** A subcategory of round trips. 'Render blocking' refers to resources that have to be loaded before anything else can be loaded.

  * **[Round trip time (RTT)](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/):** The amount of time the round trips take.

  * **Render-blocking resources:** Certain resources, like CSS files, block other parts of the page from being loaded if they are not yet loaded. The more render-blocking resources a webpage has, the more chances there are for the browser to fail to load the page.



