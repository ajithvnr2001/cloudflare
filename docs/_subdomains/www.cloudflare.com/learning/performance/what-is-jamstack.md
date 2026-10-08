---
url: https://www.cloudflare.com/learning/performance/what-is-jamstack/
title: What is JAMstack?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:04.350043+00:00
---

# What is JAMstack?

> Source: https://www.cloudflare.com/learning/performance/what-is-jamstack/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is JAMstack? 

JAMstack is a method for building fast, lightweight web applications using mostly JavaScript, APIs, and markup (HTML/CSS). 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define 'JAMstack' 
  * Explain how JAMstack applications work 
  * Describe the benefits of using a JAMstack approach 



Related content  [ What is a static site generator? ](https://www.cloudflare.com/learning/performance/static-site-generator/)[ Tips to improve website speed ](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[ How does website speed boost SEO? ](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[ How do DCL and FCP affect SEO? | Web performance metrics ](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[ Why minify JavaScript code? ](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)

On this page

  * What is JAMstack?

  * What does the term &#39

  * What is a static website?

  * How do JAMstack applications handle backend functions?

  * How does JAMstack relate to microservices?

  * What are the benefits of using JAMstack?




## What is JAMstack?

JAMstack is an approach to frontend web development (the construction of content and interfaces that users interact with). It allows developers to [quickly create](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/) and efficiently serve static websites to users.

In a JAMstack web application, as much HTML as possible is pre-built and stored in a [content delivery network (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/). Instead of running a monolithic backend application on the [server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) to generate dynamic content, dynamic components of the application are based on [APIs](https://www.cloudflare.com/learning/security/api/what-is-an-api/). Ideally, this results in a much [faster user experience](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) and a much simpler developer experience.

## What does the term 'JAMstack' stand for?

_JAM_ stands for _J_ avaScript, _A_ PIs, _M_ arkup.

  * JavaScript is the programming language used by web applications

  * An API (application programming interface) is a way to request data from someone else's program or application

    * Markup is code (HTML and CSS) that provides formatting instructions to browsers



_Stack_ refers to the combination of all these things in a way that allows developers to build applications and websites.

A [JAMstack website or application](https://www.cloudflare.com/the-net/jamstack-websites/) is constructed using only these three elements. The static website that the user sees is built out of HTML and CSS markup code. JavaScript is used for any necessary dynamic functionality, and for calling APIs. APIs provide the application's backend.

Suppose Bob builds a web application that provides updates on European football scores. Bob creates a backend application that runs on a server he operates and constantly checks the scores of the latest matches. When a user opens up the web application, Bob's server generates HTML pages that display those scores, then sends those pages to the user. However, Bob's web application is somewhat slow: before a user can view those pages, they have to wait for the backend application to run, for the HTML to be generated, and for the HTML to reach their device.

Now suppose Bob rebuilds his web application using a JAMstack approach. Instead of writing an entire backend application, he creates a series of lightweight HTML pages that he stores in a CDN. When a user opens up the application, the CDN immediately delivers the corresponding HTML pages to the user, since the CDN is far closer to the user than Bob's server. The application also makes an API call in order to fill out the live football match scores on the page. Bob's web application now loads very quickly for the user, and from Bob's perspective, there is much less need to write code that will handle the backend, server-side work of updating the scores.

## What is a static website?

A static website is made up of one or more static webpages, which are HTML files that load in a browser the same way no matter who loads the file. Because static webpages consist solely of HTML, with no additional code that needs to run in the browser, they can load extremely quickly. (To see what HTML code looks like, right-click on a webpage while using the Chrome browser and click "View Page Source".)

By contrast, dynamic webpages are different each time they load. In order to provide a more interactive, personalized user experience, dynamic webpages change based on the user opening the page, the location of the page load, the time of day, and any number of other changing data inputs. When a dynamic webpage loads, code has to run either on the web server that hosts the webpage or within the user's browser. This reliance on running code can slow down the user experience.

Dynamic webpages are not the only way to create a modernized user experience. A mostly static JAMstack website can still provide a dynamic, personalized experience for users by occasionally generating new static content or calling APIs to fill out updated content.

## How do JAMstack applications handle backend functions?

In application development, the backend is the code that runs on a server behind the scenes. Usually a user is not aware of what is happening on the backend while they use a website or application. While JavaScript and markup dictate the way a JAMstack application appears to a user, it still needs backend functions in order to work. JAMstack handles this by calling APIs using JavaScript.

Using APIs means that JAMstack developers do not have to construct their own backend applications. They can build on already-existing APIs to make their websites and apps work.

When developers want to build their own functionality for an application, they can create a new API. APIs can be reused in a variety of contexts, so when developers build their own APIs for the backend, they should only need to construct that functionality once in order to use it in future applications.

## How does JAMstack relate to microservices?

Using APIs allows JAMstack developers to take a microservices approach to the backend. In a [microservices architecture](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/), an application's backend is broken down into smaller chunks that run on command — just as a JAMstack application calls various APIs when necessary, but otherwise does not need backend support.

It is also possible to construct a JAMstack application that uses a partially or fully [serverless](https://www.cloudflare.com/learning/serverless/what-is-serverless/) backend. Serverless functions are small, reusable snippets of code that run on demand. However, a serverless architecture often requires a more hands-on approach to the backend by the developer, since they are essentially building the backend application themselves instead of calling APIs (although they do not have to worry about provisioning servers).

## What are the benefits of using JAMstack?

  * Performance: Almost all of the content in a JAMstack application is made up of static HTML files that are served from a CDN. This is the fastest way to deliver web content to end users.

  * Scalability: If an application is "scalable," that means that it responds well to large increases in usage. Because the JAMstack frontend is fast and the backend is lightweight, JAMstack applications are often extremely scalable.

  * Better developer experience: JAMstack enables developers to focus on building a compelling frontend user experience, without worrying about the backend or performance issues.




Cloudflare enables developers to [build applications that are hosted directly](https://www.cloudflare.com/developer-platform/solutions/hosting/) on the Cloudflare global CDN. [Learn more about Cloudflare Pages](https://pages.cloudflare.com/), our JAMstack platform for building static websites. You can also learn more about deploying a [Gatsby site](https://developers.cloudflare.com/pages/how-to/deploy-a-gatsby-site/), a [Hugo site](https://developers.cloudflare.com/pages/how-to/deploy-a-hugo-site/), a [React application](https://developers.cloudflare.com/pages/how-to/deploy-a-react-application/), and [more](https://developers.cloudflare.com/pages/how-to/) with Cloudflare Pages, and watch [a video overview of Cloudflare Pages](https://youtu.be/mzgmxTa0m8o) from the analyst firm Redmonk.
