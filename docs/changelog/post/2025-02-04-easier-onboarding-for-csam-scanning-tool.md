---
url: https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/
title: Fight CSAM More Easily Than Ever \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:02.396439+00:00
---

# Fight CSAM More Easily Than Ever · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 4, 2025

## Fight CSAM More Easily Than Ever

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now implement our **child safety tooling** , the **[CSAM Scanning Tool](https://developers.cloudflare.com/cache/reference/csam-scanning/)** , more easily. Instead of requiring external reporting credentials, you only need a verified email address for notifications to onboard. This change makes the tool more accessible to a wider range of customers.

**How It Works**

When enabled, the tool automatically [hashes images for enabled websites as they enter the Cloudflare cache ↗︎](https://blog.cloudflare.com/the-csam-scanning-tool/). These hashes are then checked against a database of **known abusive images**.

  * **Potential match detected?**
    * The **content URL is blocked** , and
    * **Cloudflare will notify you** about the found matches via the provided email address.



**Updated Service-Specific Terms**

We have also made updates to our **[Service-Specific Terms ↗︎](https://www.cloudflare.com/service-specific-terms-application-services/#csam-scanning-tool-terms)** to reflect these changes.
