---
url: https://developers.cloudflare.com/stream/examples/rtmps_playback/
title: RTMPS playback \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:46.962197+00:00
---

# RTMPS playback · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/examples/rtmps_playback/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Examples](https://developers.cloudflare.com/stream/examples/)
  4. /Rtmps_playback



# RTMPS playback

Example of sub 1s latency video playback using RTMPS and ffplay

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/examples/rtmps_playback/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Before you can play live video, you must first be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live/start-stream-live).

Copy the RTMPS _playback_ key for your live input from either:

  * The **Live inputs** page of the Cloudflare dashboard.

[ Go to **Live inputs** ↗ ](https://dash.cloudflare.com/?to=/:account/stream/inputs)
  * The [Stream API](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#use-the-api)




Paste it into the URL below, replacing `<RTMPS_PLAYBACK_KEY>`:

RTMPS playback with ffplaysh
    
    
    ffplay -analyzeduration 1 -fflags -nobuffer -sync ext 'rtmps://live.cloudflare.com:443/live/<RTMPS_PLAYBACK_KEY>'

For more, refer to [Play live video in native apps with less than one second latency](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/#play-live-video-in-native-apps-with-less-than-1-second-latency).

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/examples/rtmps_playback.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
