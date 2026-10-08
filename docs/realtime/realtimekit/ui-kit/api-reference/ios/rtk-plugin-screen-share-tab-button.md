---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugin-screen-share-tab-button/
title: RtkPluginScreenShareTabButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:00.061300+00:00
---

# RtkPluginScreenShareTabButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugin-screen-share-tab-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkPluginScreenShareTabButton



# RtkPluginScreenShareTabButton

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugin-screen-share-tab-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With identifier

A tab button used in the plugin and screen share tab selector. Represents a single tab in the `RtkActiveTabSelectorView`.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`image` | `RtkImage?` | ✅ | - | The icon image for the tab button  
`title` | `String` | ❌ | `""` | The title text for the tab button  
`id` | `String` | ❌ | `""` | A unique identifier for the tab button  
`appearance` | `RtkPluginScreenShareTabButtonAppearance` | ❌ | - | Appearance configuration for the tab button  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let tabButton = RtkPluginScreenShareTabButton(
        image: RtkImage(image: UIImage(systemName: "square.and.arrow.up")),
        title: "Screen Share"
    )

### With identifier
    
    
    import RealtimeKitUI
    
    let tabButton = RtkPluginScreenShareTabButton(
        image: RtkImage(image: UIImage(systemName: "pencil.tip")),
        title: "Whiteboard",
        id: "whiteboard-plugin"
    )

[PreviousRtkParticipantTileView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-tile-view/)[NextRtkPluginsView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugin-screen-share-tab-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
