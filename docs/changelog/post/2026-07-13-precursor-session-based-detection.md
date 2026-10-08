---
url: https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/
title: Precursor introduces session-based bot detection \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:02.989165+00:00
---

# Precursor introduces session-based bot detection · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 13, 2026

## Precursor introduces session-based bot detection

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Precursor is rolling out to all customers starting today. Precursor is client-side JavaScript that enables session-based bot detection.

You can [read the announcement blog ↗︎](https://blog.cloudflare.com/introducing-precursor) for background on why we built Precursor and how session-level behavioral detection works.

With Precursor enabled, Cloudflare can:

  * Continuously evaluate behavioral signals across a session
  * Re-validate challenge clearance as behavior changes
  * Update bot scores with session context
  * Provide client-side visibility where none previously existed



It integrates with existing protections, including Security Rules, and can be enabled directly from the Cloudflare dashboard with configurable modes to balance security and user experience.

![Animated walkthrough of enabling Precursor in the Cloudflare dashboard](https://developers.cloudflare.com/images/precursor/enabling_precursor.gif)

To learn more, refer to the [Precursor documentation](https://developers.cloudflare.com/cloudflare-challenges/precursor/).
