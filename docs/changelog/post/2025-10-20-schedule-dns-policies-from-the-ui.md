---
url: https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/
title: Schedule DNS policies from the UI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:26.633921+00:00
---

# Schedule DNS policies from the UI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 20, 2025

## Schedule DNS policies from the UI

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Admins can now create [scheduled DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/timed-policies/) directly from the Zero Trust dashboard, without using the API. You can configure policies to be active during specific, recurring times, such as blocking social media during business hours or gaming sites on school nights.

  * **Preset Schedules** : Use built-in templates for common scenarios like Business Hours, School Days, Weekends, and more.
  * **Custom Schedules** : Define your own schedule with specific days and up to three non-overlapping time ranges per day.
  * **Timezone Control** : Choose to enforce a schedule in a specific timezone (for example, US Eastern) or based on the local time of each user.
  * **Combined with Duration** : Policies can have both a schedule and a duration. If both are set, the duration's expiration takes precedence.



You can see the flow in the demo GIF:

![Schedule DNS policies demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1053,height=879,format=webp/_astro/gateway-dns-scheduled-policies-ui.Cf4l1OTE.gif)

This update makes time-based DNS policies accessible to all Gateway customers, removing the technical barrier of the API.
