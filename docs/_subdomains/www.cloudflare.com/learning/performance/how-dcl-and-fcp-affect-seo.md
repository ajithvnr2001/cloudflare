---
url: https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/
title: How do DCL and FCP affect SEO? | Web performance metrics
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:23.042491+00:00
---

# How do DCL and FCP affect SEO? | Web performance metrics

> Source: https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  How do DCL and FCP affect SEO? | Web performance metrics 

DCL and FCP are both important metrics that Google uses in assessing a webpage's performance. These metrics dig deeper than merely measuring a page's total load time or time to first byte (TTFB). 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define DCL and FCP 
  * Understand how browsers use the Document Object Model (DOM) 
  * Explain how SEO is impacted by these performance metrics 



Related content  [ Why does site speed matter? ](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[ How to test the speed of a website ](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[ Mobile performance: How to make a site mobile friendly ](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)

On this page

  * What is DCL?

  * What is the DOM?

  * What is FCP?

  * How do DCL and FCP affect SEO?

  * How does Cloudflare improve DCL and FCP?

  * Brief note on how webpages work




## What is DCL?

DCL, short for DOMContentLoaded, is an important [webpage performance](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) metric. DCL measures the point when a browser is ready to implement any [client-side scripting](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/). In more technical terms, DCL is the time during the process of loading a webpage when the DOM (Document Object Model) has been assembled by the browser, and no stylesheets are preventing JavaScript from executing. (For help understanding these terms, see 'Brief note on how webpages work' below.)

## What is the DOM (Document Object Model)?

DOM is an acronym that stands for Document Object Model. The Document Object Model is a representation of the structure of a webpage, not unlike an outline of a research paper, with points and sub-points. Another way to think of the DOM is as a tree, with the page itself as the root, branching off into the different HTML elements of the page.

![Document Object Model](https://www.cloudflare.com/img/learning/performance/how-dcl-and-fcp-affect-seo/document-object-model.svg)Document Object Model

DOMContentLoaded means that the browser has generated this model of the page from the HTML code it received. This also means it's ready to carry out scripts and display dynamic content.

## What is FCP?

First Contentful Paint, or FCP, is another crucial performance metric. FCP measures the point in time when the first content from the DOM is rendered – meaning the first HTML element is displayed. This can be text, images, or anything that a user will recognize as being part of the webpage. First Contentful Paint is different from First Paint (FP), which measures when any element of the page is rendered.

There are several other performance metrics that measure the 'first' thing to occur. For instance, Time To First Byte (TTFB) measures when the very first byte from a web server reaches the browser. However, FCP measures the first point at which a user can see that a page is beginning to load successfully. Because the user's perception of web performance is what's important for keeping users engaged on a website, [TTFB is almost irrelevant](https://blog.cloudflare.com/ttfb-time-to-first-byte-considered-meaningles/) from a user's perspective.

## How do DCL and FCP affect SEO?

Website speed is a crucial part of a solid SEO (search engine optimization) strategy. Performance is an especially important factor for Google search engine rankings. DCL and FCP are two metrics that Google emphasizes in its assessment of performance, and Google PageSpeed Insights helps developers measure them. (Although Google doesn't share precisely how much these two performance metrics factor into its search rankings, it certainly takes them into account.)

Developers can take a number of steps for improving these performance metrics for a site. Taking advantage of [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) and leveraging a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) are two essential steps for improving DCL and FCP times.

## How does Cloudflare improve DCL and FCP?

The [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) vastly speeds up websites by caching content in locations around the world, so that HTTP requests are responded to much more quickly. As a result, browsers receive page HTML more quickly, improving both of these metrics.

## Brief note on how webpages work

A webpage is made up of a combination of HTML code, CSS code, and JavaScript code. When a browser makes a request for a webpage, the relevant web server sends an HTML file which contains, among other things, a list of all the CSS, JavaScript and other assets that the browser than must request separately.

  * HTML (Hypertext Markup Language) is code that provides instructions for browsers on how to display content and request other assets.

  * CSS (Cascading Style Sheets) is code that provides further instructions on how HTML content should appear and how webpages are laid out.

  * JavaScript is a programming language that can take HTML content and change it when certain specified conditions are met. Additionally, JavaScript can be used for more complex tasks like 3D rendering, games, or other technically complex activities.




The HTML file contains the content that appears on the page, instructions on how to display that content, and instructions for loading other content, such as images, from other sources. It links to CSS files (stylesheets) and to JavaScript libraries with further instructions. The browser then takes that code, interprets it, and displays the resulting webpage.

In most browsers, it is possible to view the HTML file that the browser is interpreting by right-clicking on any webpage and selecting 'View Page Source' in the drop-down menu. The HTML file will then open up in a new tab. The text of the file will almost always start with ''.
