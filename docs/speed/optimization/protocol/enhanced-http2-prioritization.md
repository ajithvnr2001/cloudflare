---
url: https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/
title: Enhanced HTTP/2 Prioritization \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:35.752986+00:00
---

# Enhanced HTTP/2 Prioritization · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

Settings

  4. /Protocol optimization
  5. /Enhanced HTTP/2 Prioritization



# Enhanced HTTP/2 Prioritization

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityHow it worksEnable Enhanced HTTP/2 Prioritization

With Enhanced HTTP/2 Prioritization, Cloudflare delivers resources in the optimal order for the fastest experience across all browsers. It also supports control of content delivery when used in conjunction with [Workers](https://developers.cloudflare.com/workers/).

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | No | Yes | Yes | Yes  
  
## How it works

The speed of loading web content, from the user’s perspective, is dependent on the order in which the resources load. With HTTP/2, by default, Cloudflare will follow the order requested by the browser. This ordering varies from browser to browser, causing a significant difference in performance.

With Enhanced HTTP/2 Prioritization, Cloudflare overrides the default browser behavior to optimize the order of resource delivery, independent of the browser. The greatest improvements will be experienced by visitors using Safari and Edge browsers.

For more details, refer to [the introductory blog post ↗︎](https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/).

## Enable Enhanced HTTP/2 Prioritization

To enable **Enhanced HTTP/2 Prioritization** in the Cloudflare dashboard:

  1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com).
  2. Select your account and zone.
  3. Go to **Speed** > **Settings**.
  4. Go to **Protocol Optimization**.
  5. For **Enhanced HTTP/2 Prioritization** , switch the toggle to **On**.



To enable **Enhanced HTTP/2 Prioritization** using the Cloudflare API, send a [`PATCH` request](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) with `h2_prioritization` as the setting name in the URI path, and the `value` parameter set to `"on"`.

[PreviousHTTP/3 (with QUIC)](https://developers.cloudflare.com/speed/optimization/protocol/http3/)[Next0-RTT Connection Resumption](https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/protocol/enhanced-http2-prioritization.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
