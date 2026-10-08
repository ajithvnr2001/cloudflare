---
url: https://developers.cloudflare.com/stream/examples/android/
title: Android (ExoPlayer) \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:46.645753+00:00
---

# Android (ExoPlayer) · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/examples/android/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Examples](https://developers.cloudflare.com/stream/examples/)
  4. /Android



# Android (ExoPlayer)

Example of video playback on Android using ExoPlayer

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/examples/android/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Download and run an example app

Note

Before you can play videos, you must first [upload a video to Cloudflare Stream](https://developers.cloudflare.com/stream/uploading-videos/) or be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live)
    
    
    implementation 'com.google.android.exoplayer:exoplayer-hls:2.X.X'
    
    SimpleExoPlayer player = new SimpleExoPlayer.Builder(context).build();
    
    // Set the media item to the Cloudflare Stream HLS Manifest URL:
    player.setMediaItem(MediaItem.fromUri("https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8"));
    
    player.prepare();

### Download and run an example app

  1. Download [this example app ↗︎](https://github.com/googlecodelabs/exoplayer-intro.git) from the official Android developer docs, following [this guide ↗︎](https://developer.android.com/codelabs/exoplayer-intro#4).
  2. Open and run the [exoplayer-codelab-04 example app ↗︎](https://github.com/googlecodelabs/exoplayer-intro/tree/main/exoplayer-codelab-04) using [Android Studio ↗︎](https://developer.android.com/studio).
  3. Replace the `media_url_dash` URL on [this line ↗︎](https://github.com/googlecodelabs/exoplayer-intro/blob/main/exoplayer-codelab-04/src/main/res/values/strings.xml#L21) with the DASH manifest URL for your video.



For more, see [read the docs](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/).

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/examples/android.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
