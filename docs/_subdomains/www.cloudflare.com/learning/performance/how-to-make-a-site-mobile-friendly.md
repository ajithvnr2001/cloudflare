---
url: https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/
title: Mobile Performance | How to Make a Site Mobile Friendly
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:25.868124+00:00
---

# Mobile Performance | How to Make a Site Mobile Friendly

> Source: https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  Mobile performance: How to make a site mobile friendly 

How a website performs on mobile is crucial both for user experience and for search engine rankings. Several strategies can be combined to ensure quick page load speeds on mobile devices. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain why mobile performance matters 
  * Describe the drawbacks of a slow-loading mobile site 
  * Outline strategies to speed up a mobile site 



Related content  [ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[ How to test the speed of a website ](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)

On this page

  * Why does mobile performance matter?

  * How to improve mobile performance

    * Minimize file sizes and file count

    * Cache resources at the edge

    * Cache API Calls

    * Prioritize Visible Content

    * Avoid Redirects

  * Summary




## Why does mobile performance matter?

The web is going mobile. Well over 50% of global webpage views are on mobile devices. In some regions, such as Asia and Africa, the percentage is much higher. In each case, this percentage is steadily growing year over year.

![Mobile vs Desktop Usage Stats](https://images.ctfassets.net/slt3lc6tev37/40IzNY9omFF0nQGFwsXpom/b033eb8a1e7171439316fa5dc1978bbb/mobile-vs-desktop-usage-stats-01.svg)Mobile vs Desktop Usage Stats

The major search engines are aware of this trend, which is why they are prioritizing sites with fast mobile load times. Mobile users may have limited bandwidth but still want to find information quickly. These users tend to have less patience, which means high bounce rates for slow loading sites. (‘Bounce rate’ is the percentage of website visitors who leave the site after viewing just a single page).

Google and other site-speed authorities have determined that the maximum load time for a mobile site should be around three seconds. After three seconds, user retention drops dramatically. Search engines will ‘punish’ sites that load slowly by putting them further down in search results, particularly for mobile users.

A three second load-time limit over a mobile connection is not very forgiving, but there are tried and true strategies to keep mobile load times down.

## How to improve mobile performance

There are a number of factors that affect mobile performance, so a number of strategies and best practices can improve load times.

#### Minimize file sizes and file count

To ensure a quicker load time, all website files should be made as small as possible. Images are often the biggest files requested, and these can be made smaller by using [image optimizers](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/) or converting them to a lightweight image format, such as SVG.

HTML, JavaScript, and CSS files can also be made smaller through minification. [Code minification](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/) means taking all of the white space and comments out of the code and restructuring it in the most compact way possible. This will reduce the file size to the bare minimum. While this makes the code practically unreadable to a human being, a web browser will still be able to execute the code just fine.

In addition to creating smaller file sizes, the number of overall files should be kept to a minimum. Every additional file required to load a website means an additional request and response, and these round trips contribute to load time. Sites with multiple JavaScript and CSS files should consolidate all the JavaScript code into one file, and do the same with CSS. For pages that require very little JavaScript or CSS, using inline styles* can significantly improve load times.

*_Typically web developers write HTML, JavaScript, and CSS code in different files. Using a technique called ‘inline styles’ a developer can write their JavaScript and/or CSS code in the same file as their HTML._

#### Cache resources at the edge

Typically when a user visits a website, the user’s device has to communicate with the web server to get the website files. If the web server is in San Francisco and the user is in Berkeley (10 miles away), this should be pretty quick. But what if the user is in Tokyo (5,000 miles away)? That means each request and response will have to travel thousands of miles, adding significant delay to the website loading.

![Global CDN](https://www.cloudflare.com/img/learning/cdn/what-is-a-cdn/what-is-a-cdn.png)Global CDN

A common way to mitigate this problem is by utilizing a [Content Delivery Network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/). A [global CDN](https://www.cloudflare.com/application-services/products/cdn/) caches content at the [network edge](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/). This means the CDN has [caching servers](https://www.cloudflare.com/learning/cdn/what-is-caching/) that live in data centers all over the globe. Anyone with Internet access is never too far from a data center. These data center servers can communicate with [origin web servers](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) to cache website data so that users visiting a website that utilizes the CDN can get website files from their local data center. This ensures a speedy request-response time for users, regardless of their location.

#### Cache API Calls

API calls are [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) requests to fetch data from external resources. For example, a movie review site like Rotten Tomatoes may make API calls to a ticketing service like Fandango so that users browsing Rotten Tomatoes can see local movie showtimes. While API calls can help create a robust experience and reduce redundant work, they also create new HTTP requests, which can slow down load times.

API calls can be cached to minimize these extra HTTP requests. In our movie showtime example above, Rotten Tomatoes only needs to fetch Los Angeles movie showtimes once per day. They can configure their site to cache this API call once per day. This way, if 10,000 Los Angeles users visit Rotten Tomatoes each day, only the first one of those users will have to wait for the API call to Fandango.

#### Prioritize Visible Content

What a user immediately sees when loading a webpage is often the tip of the iceberg; they must scroll down to see the rest of the page. The content that appears on a user’s screen before any scrolling occurs is called ‘above-the-fold’ content. Web developers should be writing code in such a way that above-the-fold content is always loaded first. One technique to achieve this is called [lazy loading](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/), which works by dynamically loading below-the-fold content as a user scrolls down the page.

#### Avoid Redirects

For various reasons, some websites create redirects on page loads. For example, 301 redirects are commonly used on websites that are renamed or rebranded. This practice should be avoided whenever possible, as redirects consume precious load time.

## Summary

As mobile browsing takes over the web, it becomes more and more important to have a high-performing mobile site. Speedy mobile sites are rewarded with higher engagement and improved conversion rates, plus an SEO boost. Website owners should implement some or all of the strategies outlined above to reap these benefits.
