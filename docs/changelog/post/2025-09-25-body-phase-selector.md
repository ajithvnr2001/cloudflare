---
url: https://developers.cloudflare.com/changelog/post/2025-09-25-body-phase-selector/
title: Refine DLP Scans with New Body Phase Selector \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.490578+00:00
---

# Refine DLP Scans with New Body Phase Selector · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-25-body-phase-selector/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2025

## Refine DLP Scans with New Body Phase Selector

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.

In the Gateway HTTP policy builder, you will find a new selector called _Body Phase_. This allows you to define the direction of traffic the DLP engine will inspect:

  * _Request Body_ : Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.
  * _Response Body_ : Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.



For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the **Body Phase** to _Request Body_ , the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.

All policies without this selector will continue to scan both request and response bodies to ensure continued protection.

For more information, refer to [Gateway HTTP policy selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#body-phase).
