---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/
title: RtkImage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:57.913781+00:00
---

# RtkImage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkImage



# RtkImage

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples With a local image With a remote URL

A struct that wraps a `UIImage` or a `URL` for image content. Used throughout the UI Kit for icons, avatars, and custom images.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`image` | `UIImage?` | ❌ | `nil` | A local UIImage to display  
`url` | `URL?` | ❌ | `nil` | A remote URL to load the image from  
  
## Usage Examples

### With a local image
    
    
    import RealtimeKitUI
    
    let rtkImage = RtkImage(image: UIImage(systemName: "mic"))

### With a remote URL
    
    
    import RealtimeKitUI
    
    let rtkImage = RtkImage(url: URL(string: "https://example.com/avatar.png"))

[PreviousRtkEventSelfListener](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/)[NextRtkJoinButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-join-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
