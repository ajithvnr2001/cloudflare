---
url: https://developers.cloudflare.com/speed/optimization/protocol/http3/
title: HTTP/3 (with QUIC) \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:35.905429+00:00
---

# HTTP/3 (with QUIC) · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/protocol/http3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

Settings

  4. /Protocol optimization
  5. /HTTP/3 (with QUIC)



# HTTP/3 (with QUIC)

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/protocol/http3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityEnable HTTP/3

HTTP/3 uses QUIC, which is a secure-by-default transport protocol. HTTP/3 improves page load times in a similar way to HTTP/2. However, the QUIC transport protocol solves TCP's head-of-line blocking problem, meaning that performance over lossy networks can be better.

Note

For more background on HTTP/3, visit the [Learning Center ↗︎](https://www.cloudflare.com/learning/performance/what-is-http3/).

Note

This setting is for connection between the user and Cloudflare. HTTP/3 connection to the origin is not yet supported.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
## Enable HTTP/3

HTTP/3 is available to all plans (though it does require an [SSL certificate at Cloudflare’s edge network](https://developers.cloudflare.com/ssl/get-started/)).

To enable **HTTP/3** in the dashboard:

  1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com).
  2. Select your account and zone.
  3. Go to **Speed** > **Settings**.
  4. Go to **Protocol Optimization**.
  5. For **HTTP/3** , switch the toggle to **On**.



To enable **HTTP/3** with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `http3` as the setting name in the URI path, and the `value` parameter set to `"on"`.

[PreviousHTTP/2](https://developers.cloudflare.com/speed/optimization/protocol/http2/)[NextEnhanced HTTP/2 Prioritization](https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/protocol/http3.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
