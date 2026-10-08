---
url: https://developers.cloudflare.com/stream/examples/ios/
title: iOS (AVPlayer) \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:46.925023+00:00
---

# iOS (AVPlayer) · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/examples/ios/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Examples](https://developers.cloudflare.com/stream/examples/)
  4. /Ios



# iOS (AVPlayer)

Example of video playback on iOS using AVPlayer

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/examples/ios/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Download and run an example app

Note

Before you can play videos, you must first [upload a video to Cloudflare Stream](https://developers.cloudflare.com/stream/uploading-videos/) or be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live)
    
    
    import SwiftUI
    import AVKit
    
    struct MyView: View {
        // Change the url to the Cloudflare Stream HLS manifest URL
        private let player = AVPlayer(url: URL(string: "https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8")!)
    
        var body: some View {
            VideoPlayer(player: player)
                .onAppear() {
                    player.play()
                }
        }
    }
    
    struct MyView_Previews: PreviewProvider {
        static var previews: some View {
            MyView()
        }
    }

### Download and run an example app

  1. Download [this example app ↗︎](https://developer.apple.com/documentation/avfoundation/offline_playback_and_storage/using_avfoundation_to_play_and_persist_http_live_streams) from Apple's developer docs
  2. Open and run the app using [Xcode ↗︎](https://developer.apple.com/xcode/).
  3. Search in Xcode for `m3u8`, and open the `Streams` file
  4. Replace the value of `playlist_url` with the HLS manifest URL for your video.

![Screenshot of a video with Cloudflare watermark at top right](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2928,height=762,format=webp/_astro/ios-example-screenshot-edit-hls-url.CK2bGBBG.png)

  5. Click the Play button in Xcode to run the app, and play your video.



For more, see [read the docs](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/).

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/examples/ios.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
