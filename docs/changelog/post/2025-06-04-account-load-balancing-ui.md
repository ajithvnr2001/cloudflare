---
url: https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/
title: New Account-Level Load Balancing UI and Private Load Balancers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:13.473432+00:00
---

# New Account-Level Load Balancing UI and Private Load Balancers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 4, 2025

## New Account-Level Load Balancing UI and Private Load Balancers

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've made two large changes to load balancing:

  * Redesigned the user interface, now centralized at the **account level**.
  * Introduced [**Private Load Balancers**](https://developers.cloudflare.com/load-balancing/private-network/) to the UI, enabling you to manage traffic for all of your external and internal applications in a single spot.



This update streamlines how you manage load balancers across multiple zones and extends robust traffic management to your private network infrastructure.

![Load Balancing UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=822,format=webp/_astro/account-load-balancing-ui.CoCi7gPb.png)

**Key Enhancements:**

  * **Account-Level UI Consolidation:**

    * **Unified Management:** Say goodbye to navigating individual zones for load balancing tasks. You can now view, configure, and monitor all your load balancers across every zone in your account from a single, intuitive interface at the account level.

    * **Improved Efficiency:** This centralized approach provides a more streamlined workflow, making it faster and easier to manage both your public-facing and internal traffic distribution.

  * **Private Network Load Balancing:**

    * **Secure Internal Application Access:** Create [**Private Load Balancers**](https://developers.cloudflare.com/load-balancing/private-network/) to distribute traffic to applications hosted within your private network, ensuring they are not exposed to the public Internet.

    * **WARP & Magic WAN Integration:** Effortlessly direct internal traffic from users connected via Cloudflare WARP or through your Magic WAN infrastructure to the appropriate internal endpoint pools.

    * **Enhanced Security for Internal Resources:** Combine reliable Load Balancing with Zero Trust access controls to ensure your internal services are both performant and only accessible by verified users.


![Private Load Balancers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=744,format=webp/_astro/private-load-balancer.yti20m_p.png)
