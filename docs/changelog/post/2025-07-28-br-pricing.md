---
url: https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/
title: Introducing pricing for the Browser Rendering API \u2014 $0.09 per browser hour \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:17.613539+00:00
---

# Introducing pricing for the Browser Rendering API — $0.09 per browser hour · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 28, 2025

## Introducing pricing for the Browser Rendering API — $0.09 per browser hour

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-28-br-pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve launched pricing for [Browser Rendering](https://developers.cloudflare.com/browser-run/), including a free tier and a pay-as-you-go model that scales with your needs. Starting **August 20, 2025** , Cloudflare will begin billing for Browser Rendering.

There are two ways to use Browser Rendering. Depending on the method you use, here’s how billing will work:

  * [**REST API**](https://developers.cloudflare.com/browser-run/quick-actions/): Charged for **Duration** only ($/browser hour)
  * [**Browser Sessions**](https://developers.cloudflare.com/browser-run/#integration-methods): Charged for both **Duration** and **Concurrency** ($/browser hour and # of concurrent browsers)



Included usage and pricing by plan

Plan | Included duration | Included concurrency | Price (beyond included)  
---|---|---|---  
**Workers Free** | 10 minutes per day | 3 concurrent browsers | N/A  
**Workers Paid** | 10 hours per month | 10 concurrent browsers (averaged monthly) | **1\. REST API** : $0.09 per additional browser hour   
**2\. Workers Bindings** : $0.09 per additional browser hour   
$2.00 per additional concurrent browser  
  
What you need to know:

  * **Workers Free Plan:** 10 minutes of browser usage per day with 3 concurrent browsers at no charge.
  * **Workers Paid Plan:** 10 hours of browser usage per month with 10 concurrent browsers (averaged monthly) at no charge. Additional usage is charged as shown above.



You can monitor usage via the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/browser-run). Go to **Compute** > **Browser Run**.

![Browser Rendering dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1880,height=1080,format=webp/_astro/dashboard.BQnX87lT.png)

If you've been using Browser Rendering and do not wish to incur charges, ensure your usage stays within your plan's [included usage](https://developers.cloudflare.com/browser-run/pricing/). To estimate costs, take a look at these [example pricing scenarios](https://developers.cloudflare.com/browser-run/pricing/#examples-of-workers-paid-pricing).
