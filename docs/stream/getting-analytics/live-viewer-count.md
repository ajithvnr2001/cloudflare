---
url: https://developers.cloudflare.com/stream/getting-analytics/live-viewer-count/
title: Get live viewer counts \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:48.120034+00:00
---

# Get live viewer counts · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/getting-analytics/live-viewer-count/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Analytics](https://developers.cloudflare.com/stream/getting-analytics/)
  4. /Get live viewer counts



# Get live viewer counts

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/getting-analytics/live-viewer-count/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Stream player has full support for live viewer counts by default. To get the viewer count for live videos for use with third party players, make a `GET` request to the `/views` endpoint.
    
    
    https://customer-<CODE>.cloudflarestream.com/<INPUT_ID>/views

Below is a response for a live video with several active viewers:
    
    
    { "liveViewers": 113 }

[PreviousGraphQL Analytics API](https://developers.cloudflare.com/stream/getting-analytics/fetching-bulk-analytics/)[NextUltra-low Latency with WebRTC](https://developers.cloudflare.com/stream/webrtc-beta/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/getting-analytics/live-viewer-count.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
