---
url: https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/geographic-traffic-routing/
title: Cloudflare traffic not being sent to the geographically closest data center \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:52.697535+00:00
---

# Cloudflare traffic not being sent to the geographically closest data center · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/geographic-traffic-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)

  4. /[General Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/)
  5. /Cloudflare traffic not being sent to the geographically closest data center



# Cloudflare traffic not being sent to the geographically closest data center

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/geographic-traffic-routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Due to the way routing on [Cloudflare's Anycast network ↗︎](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) works, requests may be sent to data center locations that are not necessarily the closest geographically. We are continuously adding capacity to our global network and enhancing our automated traffic engineering systems to intelligently manage congestion and other network events. While we always strive to provide the best possible performance by serving traffic from the closest location, our top priority is reliability.

In instances where performance and reliability are in conflict, our systems are designed to prioritize a stable connection over a local one.

[PreviousCannot locate dashboard account](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/cannot-locate-dashboard-account/)[NextGathering information for troubleshooting sites](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/)

Was this helpful?

YesNo
