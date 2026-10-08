---
url: https://developers.cloudflare.com/stream/viewing-videos/using-own-player/android/
title: Android \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:50.942951+00:00
---

# Android · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/viewing-videos/using-own-player/android/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /…

Play video

  4. /[Use your own player](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/)
  5. /Android



# Android

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/android/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample AppsUsing ExoPlayer

You can stream both on-demand and live video to native Android apps using [ExoPlayer ↗︎](https://exoplayer.dev/).

Note

Before you can play videos, you must first [upload a video to Cloudflare Stream](https://developers.cloudflare.com/stream/uploading-videos/) or be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live)

## Example Apps

  * [Android](https://developers.cloudflare.com/stream/examples/android/)



## Using ExoPlayer

Play a video from Cloudflare Stream using ExoPlayer:
    
    
    implementation 'com.google.android.exoplayer:exoplayer-hls:2.X.X'
    
    SimpleExoPlayer player = new SimpleExoPlayer.Builder(context).build();
    
    // Set the media item to the Cloudflare Stream HLS Manifest URL:
    player.setMediaItem(MediaItem.fromUri("https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8"));
    
    player.prepare();

[PreviousiOS](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/)[NextOverview](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/viewing-videos/using-own-player/android.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
