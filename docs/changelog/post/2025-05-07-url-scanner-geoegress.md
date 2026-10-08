---
url: https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/
title: URL Scanner now supports geo-specific scanning \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:11.417216+00:00
---

# URL Scanner now supports geo-specific scanning · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 8, 2025

## URL Scanner now supports geo-specific scanning

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-07-url-scanner-geoegress/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now choose the geographic location from which a URL scan is performed — either via [Security Center](https://developers.cloudflare.com/security-center/investigate/) in the Cloudflare dashboard or via the [URL Scanner API](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/create/).

This feature gives security teams greater insight into how a website behaves across different regions, helping uncover targeted, location-specific threats.

**What’s new:**

  * Location Picker: Select a location for the scan via **Security Center → Investigate** in the dashboard or through the API.
  * Region-aware scanning: Understand how content changes by location — useful for detecting regionally tailored attacks.
  * Default behavior: If no location is set, scans default to the user’s current geographic region.



Learn more in the [Security Center documentation](https://developers.cloudflare.com/security-center/).
