---
url: https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/
title: What are the Core Web Vitals (CWV)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:43.373708+00:00
---

# What are the Core Web Vitals (CWV)?

> Source: https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What are the Core Web Vitals (CWV)? 

The Core Web Vitals (CWVs) are three web performance measurements that impact where a website shows up in search engine results: Largest Contentful Paint (LCP), First Input Delay (FID), and Cumulative Layout Shift (CLS). 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * List the three Core Web Vitals 
  * Describe how the Core Web Vitals affect search engine optimization (SEO) 
  * Know how to improve a website's Core Web Vitals 



Related content  [ How does website speed boost SEO? ](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[ How do DCL and FCP affect SEO? | Web performance metrics ](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[ Why minify JavaScript code? ](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)

On this page

  * What are the Core Web Vitals?

  * What is the Google page experience update?

  * How do the Core Web Vitals affect SEO?

  * Why does Google incorporate web performance into ranking decisions?

  * What is Largest Contentful Paint?

  * What is First Input Delay?

  * What is Cumulative Layout Shift?

    * How CLS is measured

  * How to measure Core Web Vitals

  * How to improve Core Web Vitals

    * How to improve LCP

    * How to improve FID

    * How to improve CLS

  * What other performance metrics are important?

  * How Cloudflare can help improve CWVs




## What are the Core Web Vitals (CWV)?

The Core Web Vitals (CWV) are a set of three [web performance](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) metrics. Google's search engine measures these three metrics and incorporates them into its decisions about which pages to display in search results. This means [search engine optimization (SEO)](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/) practitioners should optimize their webpages' core web vitals as part of a holistic strategy to improve those pages' rankings.

The CWVs are:

  * Largest Contentful Paint (LCP), which measures loading speed

  * First Input Delay (FID), which measures page interactivity

  * Cumulative Layout Shift (CLS), which measures visual stability




## What is the Google page experience update?

While page load time has long been an important part of SEO, Google [announced in 2020](https://developers.google.com/search/blog/2020/11/timing-for-page-experience) that CWVs would become a part of its ranking algorithm in mid-2021. This is known as the Google page experience update.

In the announcement, Google stated that the CWVs would be factored into page experience signals that help determine a page's search ranking. Other page experience factors include [HTTPS-security](https://www.cloudflare.com/learning/ssl/what-is-https/), mobile friendliness, and the absense or presence of intrusive interstitials (like pop-ups). The update's goal was to reward webpages that provide a positive user experience.

## How do the Core Web Vitals affect SEO?

All search engines use [bots](https://www.cloudflare.com/learning/bots/what-is-a-bot/) called [web crawlers or web spiders](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/) to analyze websites. These bots determine what the content on each website is about and help determine when that website should be displayed in response to a search query. Web performance is one of the aspects of a website that Google's bots check.

It is not known precisely how much LCP, FID, and CLS affect SEO, since Google keeps its ranking algorithms mostly secret. But the CWVs do impact SEO to a significant degree. Many industry observers have conducted case studies demonstrating improvements or losses in search rankings based on changes in a website's CWVs.

How does this play out in reality? Suppose Google has to choose between putting Website A and Website B at the top of the search results for the search query "[What is ARPANET?](https://blog.cloudflare.com/fifty-years-ago/)" Website A and Website B both have strong reputations for providing facts about Internet history, and both provide similarly detailed information on the subject of ARPANET. All else being equal, if Website A loads faster, responds more quickly, and jumps around on loading less than Website B, Google's algorithm will probably decide to show Website A at the top of the search results — even though the websites provide a similar caliber of information.

![SEO Ranking Example - Website A at top of search results](https://images.ctfassets.net/slt3lc6tev37/4Zh4sBboPBKWY7V9ZcZ7bE/91181ad7893279d9827227b662be6faa/core_web_vitals_seo_ranking_example.png)SEO Ranking Example - Website A at top of search results

(Search engine rankings are more complex than depicted in this example, and dozens of factors affect where a website will show up in search.)

## Why does Google incorporate web performance into ranking decisions?

Search engines like Google want to provide searchers with the most relevant information as quickly as possible. Delays in load time tend to [frustrate users](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) — whereas fast-loading pages increase the odds that users will return. While Google has the vast majority of the English-speaking search market today, a poor user experience may cause searchers to turn to other sources for information.

For similar reasons, other search engines like DuckDuckGo and Bing may take web performance into account as well — although, as with Google, it is not known for certain how their page ranking algorithms work.

## What is Largest Contentful Paint (LCP)?

Largest Contentful Paint measures the amount of time it takes to load the largest piece of a webpage, which is usually an image or a block of text.

Google's guidlines classify a LCP measurement as 'good' if it is under 2.5 seconds. However, faster is always better.

LCP does not measure how long it takes to load an entire webpage, but it provides a good benchmark to indicate how fast a webpage is loading. And typically the biggest element on a webpage is its main content, so the time when it loads is often well-aligned with the time when the user perceives that the page has loaded.

An earlier version of the LCP metric is First Meaningful Paint (FMP) which measures when the primary content on a page becomes visible. Google found that this metric was unreliable and has since removed it from some of its reporting tools.

## What is First Input Delay (FID)?

First Input Delay is a measurement of the time between a user's first attempt to interact with a webpage and when it responds. In other words, FID quantifies how quickly a person can first click on the screen and make something happen. According to Google's guidelines, a 'good' FID is 100 milliseconds or less.

For an example of FID, suppose Alan visits a webpage titled "How to polish your shoes." He sees a carousel of photos of shoe polish and clicks on the right arrow to navigate to the next photo. The FID is the time that elapses from when he clicks the arrow to when the next photo starts to load.

FID does not measure how long it takes for the requested event to actually occur — how long it takes Alan's browser to finish loading the next photo. It only measures the time between the request and when the request starts to be fulfilled.

Note that FID is a “field metric,” or something that is measured based on observation of real users rather than hypothetically or in a “lab.”

Some “lab metric” alternatives include Total Blocking Time (TBT) and Time to Interactive (TTI). TBT measures the time that elapses between First Contentful Paint (FCP) and TTI. FCP measures the time between when loading begins and when items load on the user’s screen. Like its name suggests, TTI measures the time it takes for items to appear to have been loaded and when a user is actually able to interact with them.

## What is Cumulative Layout Shift (CLS)?

CLS measures how much a webpage "jumps around" as it loads. Specifically, it measures the largest "burst" of shifts in the page's layout. Google’s guidelines say that a ‘good’ CLS measurement is equal to or less than 0.1.

A layout shift is when page content moves up, down, or in any other direction from where it originally appeared. In the context of this metric, a burst is a group of layout shifts that all happen within a second of each other. A burst can be up to five seconds long and contain any number of layout shifts.

Imagine that after Alan loads the "How to polish your shoes" page, he tries to click on the right arrow to see the next image in the carousel. However, the image carousel suddenly moves further down the page and Alan ends up clicking on text that loads above the carousel. The webpage has shifted because it did not all load at the same time, and Alan is left feeling confused.

Such a webpage likely has a poor CLS score. It clearly moved around quite a bit, shifting the photo carousel downward by dozens or hundreds of pixels.

#### How CLS is measured

Google calculates CLS scores with the following equation:

_impact fraction * distance fraction = layout shift score_

  * _Impact fraction_ is the percentage of the screen that changes when a layout shift occurs.

  * _Distance fraction_ measures how far an element moves on the screen, also as a percentage of the screen.




If a webpage loads on a screen that is 400 pixels high, and then 200 of those pixels shift when a new element loads, the impact fraction is 200/400, or 50%. If the new element moved another element down by 50 pixels, the distance fraction is 50/400, or 12.5%.

![Core Web Vitals - CLS example - Impact fraction of 200 pixels and distance fraction of 50 pixels](https://images.ctfassets.net/slt3lc6tev37/jAmZ1ECSlGCNtLyfhdoZy/5fa3f6a87aef3603baae1f43de8513f1/core_web_vitals_measuring_CLS.png)Core Web Vitals - CLS example - Impact fraction of 200 pixels and distance fraction of 50 pixels

To calculate the layout shift score, take those two percentages and write them as decimals, then multiply them together:

_0.50 * 0.125 = 0.0625_

If this is the largest amount of movement that the webpage has, the webpage's CLS score is 0.0625.

While ideally a webpage will not shift at all when it loads, this is still a decent score. Experts recommend that webpages have a CLS score of 0.10 or less.

## How to measure Core Web Vitals

There are many tools that can be used to check CWVs. The following are all offerings directly from Google:

  * [Chrome UX Report (CrUX)](https://developer.chrome.com/docs/crux/) offers field data reported by Chrome users, giving site owners data about how actual users experience their website.

  * [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) is a free tool that provides lab metrics about CWVs. It offers actionable insights for improving performance, SEO, accessibility, and more.

  * [Google PageSpeed Insights](https://pagespeed.web.dev/) combines the functionality of CrUX and Lighthouse, offering both field and lab data on CWVs and other web vitals. Users can check performance for websites whether or not they own them using PageSpeed Insights. Here is an example of a PageSpeed Insights report.

  * [Google Search Console](https://search.google.com/search-console/about) is based in part on CrUX field data and gives CWV performance data by URL or groups of URLs.




## How to improve Core Web Vitals

#### How to improve LCP

  * **Use a content delivery network ([CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)):** CDNs cache content in locations all over the world so that content reaches users more quickly.

  * **[Optimize images](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/):** Images are often the largest element of a page. Reducing image file size can help speed up an image's load time.

  * **Implement lazy-loading:** In lazy-loading, website resources are only loaded when a user needs them. This makes website loading more efficient to a point, but research suggests that overuse of this feature correlates with lower LCP. For this reason, Google suggests limiting lazy-loading images “below the fold” or to the parts of the webpage a user has to scroll to see.




#### How to improve FID

  * **Reduce the size of JavaScript functions:** Code-heavy dynamic webpages can cause input delays because the browser has to wait for all the code to load before it can execute it. [JavaScript minification](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/) can help this process go faster.

  * **Build static webpages:** Static HTML webpages load far faster than dynamic pages, especially when distributed via CDN. Learn about [static site generators](https://www.cloudflare.com/learning/performance/static-site-generator/) or about [Jamstack](https://www.cloudflare.com/learning/performance/what-is-jamstack/), a development philosophy that emphasizes static content.

  * **Remove unnecessary third-party tools and scripts:** Loading additional tools on your website can also slow down performance. Reducing the amount of third-party tools on a website can improve FID and website speed in general.




#### How to improve CLS

  * **Minimize third-party page elements:** Third-party elements on a page load from separate locations compared to the rest of the page. Because of this, they may load at a slightly different time, changing the page's layout as they load. Minimizing the use of these third-party elements reduces the number of resulting layout shifts.

  * **Reserve space for embedded content:** Many third-party elements, such as ads, are essential to a website's functionality or business model and cannot be eliminated. Developers can reserve space on the webpage for these elements to load before the browser fetches the actual element.

  * **Ensure images load in the optimal size:** This is a slightly different process than optimizing images in general. Desktop computers, tablets, and smartphones all need images at slightly different sizes because their screens vary in size. If a browser loads the large, desktop-optimized image first, then needs to get the mobile-optimized image because the device in use is a smartphone, this can cause the content on the page to jump around when the differently sized image loads.

  * **Include height and width for images and video:** The height and width properties tell browsers how large an image will be so they can reserve that space before the image or video loads. Our [HTML5 video article](https://www.cloudflare.com/learning/video/how-html5-video-works/) has further information on how to do this for video.

  * **Use CSS aspect ratio boxes:** There are a number of CSS techniques developers can use to preserve space for a page element using aspect ratios — [learn more here](https://css-tricks.com/aspect-ratio-boxes/).




## What other performance metrics are important?

While CWVs are the metrics Google has told SEO practitioners they should prioritize, they are not the only web vitals that exist. [First Contentful Paint (FCP), DOMContentLoaded (DCL)](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/), Time to Interactive (TTI), and Time to First Byte (TTFB) do not impact SEO to the same degree, but they can help developers identify issues that impact the CWVs.

(On its own, TTFB is [not a particularly useful metric](https://blog.cloudflare.com/ttfb-time-to-first-byte-considered-meaningles/). But it can be an indication of additional issues that developers need to fix.)

## How Cloudflare can help improve CWVs

Cloudflare offers a variety of services that can help boost CWVs:

  * Cloudflare's [Content Delivery Network](https://www.cloudflare.com/application-services/products/cdn/) (CDN) caches static and dynamic content across a global network spanning more than 335+ cities in over 120+ countries. This allows websites to load faster, something all three CWVs benefit from.

  * [Cloudflare Images](https://www.cloudflare.com/developer-platform/cloudflare-images/) offers resizing functionality that can compress images and further increase website loading speed, especially for LCP.

  * [Cloudflare Zaraz](https://www.cloudflare.com/products/zaraz/) loads third-party resources in the cloud and away from the browser, improving metrics like FID and CLS.



