---
url: https://www.cloudflare.com/learning/performance/what-is-lazy-loading/
title: What is lazy loading?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:05.051948+00:00
---

# What is lazy loading?

> Source: https://www.cloudflare.com/learning/performance/what-is-lazy-loading/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is lazy loading? 

Lazy loading means waiting to render content on a webpage until the user or the browser needs it. Lazy loading can help speed up webpage load times. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define lazy loading 
  * Describe how to lazy load images, JavaScript, CSS, and iframes 
  * List the pros and cons of lazy loading 



Related content  [ Why minify JavaScript code? ](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[ Mobile performance: How to make a site mobile friendly ](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[ What is JAMstack? ](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[ Tips to improve website speed ](https://www.cloudflare.com/learning/performance/speed-up-a-website/)

On this page

  * What is lazy loading?

  * How does lazy loading images work?

    * How to implement lazy loading for images

  * What other page resources can use lazy loading?

  * What are the advantages of lazy loading?

  * What are the disadvantages of lazy loading?

  * What is eager loading?

  * How else can developers speed up a webpage?




## What is lazy loading?

Lazy loading is a technique for waiting to load certain parts of a webpage — especially images — until they are needed. Instead of loading everything all at once, known as "eager" loading, the browser does not request certain resources until the user interacts in such a way that the resources are needed. When implemented properly, lazy loading can [speed up page load times](https://www.cloudflare.com/learning/performance/speed-up-a-website/).

This type of loading is called "lazy" because it encourages a web browser to procrastinate. When displaying a lazy loading webpage, a browser essentially says, "I will wait to load these images until I really _need_ to." When displaying an eager loading webpage, a browser takes the opposite attitude: "I will take care of everything right away!" While procrastination sometimes carries negative connotations in the real world, in this case it is often more efficient.

For instance, a blog post might have an image at the top of the page and a diagram near the bottom. Someone reading the blog post might not reach the bottom of the text for several minutes, so the browser waits to load the diagram until the reader scrolls to that section. This way, the page loads more quickly at first, because the browser is loading one image instead of two.

## How does lazy loading images work?

User navigation typically is what triggers lazy loading images. In particular, when a user scrolls down on a page, that tells the browser to load the images that appear there.

When a webpage loads, the part that a user sees is called "above the fold," while the part that the user does not see yet is called "below the fold."* Images that are above the fold need to load right away, or else the user experience will be impacted. But the user does not see images below the fold until they scroll down. Thus, images below the fold can use lazy loading.

*_What does "fold" mean? "Above the fold" and "below the fold" originated from newspaper layouts. Newspapers typically come folded in half horizontally, and the front half — the area above the fold — is what the reader sees first. When the term is applied to a web layout, the "fold" is the bottom of the user's screen._

#### How to implement lazy loading for images

One way to implement lazy loading is to use the HTML attribute loading in an image tag. Adding `loading="lazy"`, as in the example below, tells the browser to wait to load the image until the user scrolls close to it:
    
    
    `<img src="example.com/image" alt="example image" width="100" height="100" loading="lazy">`
    

Web developers can also use programming frameworks to implement more sophisticated lazy loading. Angular is commonly used for this purpose. The JavaScript library React also supports lazy loading.

[Cloudflare Mirage](https://support.cloudflare.com/hc/en-us/articles/219178057-Configuring-Cloudflare-Mirage) is another way to implement lazy loading. In addition to automatically resizing images, Mirage acts as a lazy loader, only loading images on demand. The Cloudflare Mirage feature is available to Cloudflare customers on the Pro and Business [self-serve plans](https://www.cloudflare.com/plans/), as well as [Enterprise customers](https://www.cloudflare.com/plans/enterprise/externa/).

## What other page resources can use lazy loading?

  * **JavaScript:** JavaScript is what is known as a render-blocking resource — meaning a browser cannot render the page until JavaScript code loads. JavaScript code can be divided into smaller modules that are loaded when needed, reducing the load time for pages that need to execute JavaScript ([learn more](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)).

  * **CSS:** CSS is also a render-blocking resource. Splitting a CSS file into multiple files that only load when necessary can help reduce the amount of time that a browser is blocked from rendering the rest of the page. Non-blocking CSS files should have their own link with a `media` property added to tell the browser when to load them ([learn more](https://developer.mozilla.org/en-US/docs/Learn/Performance/CSS)).

  * **iframes:** iframes are used to embed content from an external source into a webpage. iframe tags can include the same HTML `loading` attribute described above for images.




## What are the advantages of lazy loading?

**Faster page load:** All else being equal, webpages with smaller file sizes load faster. With lazy loading, a webpage starts off smaller than its full size and thus loads faster. [Speedy web performance](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) has numerous benefits, including [better SEO](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/), [higher conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/), and an improved user experience.

**No unnecessary content:** Suppose a page loads multiple below-the-fold images but the user exits the page before scrolling down. In such a case, the bandwidth used to deliver the images and the browser's time spent requesting and rendering the images were essentially wasted. In contrast, lazy loading ensures that these images only load when necessary. This saves time and processing power, and it may save money for the website owner because less [bandwidth](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/) is used.

## What are the disadvantages of lazy loading?

**Users may request resources faster than expected:** For instance, if a user scrolls quickly down a page, they might have to wait for the images to load. This could negatively impact user experience.

**Additional communication with server:** Instead of requesting all the page content at once, the browser might have to send multiple requests to the website's servers for content as the user interacts with the page. The use of a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) minimizes this potential drawback, because the images are [cached](https://www.cloudflare.com/learning/cdn/what-is-caching/) by the CDN and the browser does not have to send a request all the way to the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) to fetch them.

**Additional code for the browser to process:** If a developer adds several lines of JavaScript to a webpage to tell the browser how to lazy load page resources, this adds to the amount of code that the browser has to load and process. If done inefficiently, this slight additional loading and processing time might outweigh the time saved by lazy loading.

## What is eager loading?

Eager loading is loading all webpage resources at the same time, or as soon as possible. Some applications that use eager loading may display a "Loading" screen. Complex, code-heavy web applications, such as online games, may prefer to use eager loading.

## How else can developers speed up a webpage?

A number of factors impact web performance, but these three steps are a good starting point for making a website faster:

  * **Use a CDN:** When web content is cached in a CDN, communication with the origin server is kept to a minimum whether lazy loading is used or not. CDNs also deliver content to users more quickly because they are usually closer to the user than the origin server.

  * **Optimize images:** Overly large images will impact performance even if lazy loading is used. [Decreasing image file size](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/) whenever possible helps ensure that images load quickly.

  * **Minify code:** [Minification](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/) is the process of removing all unnecessary characters from CSS and JavaScript code without altering its functionality. This includes removing whitespace, comments, and semicolons. Minification reduces code file size, increasing load speed.




See more ways to improve webpage performance: [Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)
