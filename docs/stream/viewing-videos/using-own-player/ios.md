---
url: https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/
title: iOS \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:51.013055+00:00
---

# iOS · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /…

Play video

  4. /[Use your own player](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/)
  5. /iOS



# iOS

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample AppsUsing AVPlayer

You can stream both on-demand and live video to native iOS, tvOS and macOS apps using [AVPlayer ↗︎](https://developer.apple.com/documentation/avfoundation/avplayer).

Note

Before you can play videos, you must first [upload a video to Cloudflare Stream](https://developers.cloudflare.com/stream/uploading-videos/) or be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live)

## Example Apps

  * [iOS](https://developers.cloudflare.com/stream/examples/ios/)



## Using AVPlayer

Play a video from Cloudflare Stream using AVPlayer:
    
    
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

[PreviousWeb](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/web/)[NextAndroid](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/android/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/viewing-videos/using-own-player/ios.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
