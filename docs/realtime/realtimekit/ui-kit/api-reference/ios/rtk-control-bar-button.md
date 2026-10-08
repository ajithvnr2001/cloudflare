---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar-button/
title: RtkControlBarButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:57.225649+00:00
---

# RtkControlBarButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkControlBarButton



# RtkControlBarButton

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesMethodsUsage Examples Basic Usage With state changes

Base button class for control bar items. Supports normal and selected states, notification badges, and theming through appearance configuration.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`image` | `RtkImage` | ✅ | - | The icon image for the button  
`title` | `String` | ❌ | `""` | The title text displayed below the icon  
`appearance` | `RtkControlBarButtonAppearance` | ❌ | - | Appearance configuration for colors and styling  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`selectedStateTintColor` | `UIColor` | ❌ | - | Tint color applied when the button is in the selected state  
`normalStateTintColor` | `UIColor` | ❌ | - | Tint color applied when the button is in the normal state  
`notificationBadge` | `RtkNotificationBadgeView` | - | - | Badge view for displaying notification counts  
  
## Methods

Method | Return Type | Description  
---|---|---  
`setSelected(image:title:)` | `Void` | Sets the button to the selected state with a custom image and title  
`setDefault(image:title:)` | `Void` | Sets the button to the default state with a custom image and title  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let button = RtkControlBarButton(
        image: RtkImage(image: UIImage(systemName: "mic")),
        title: "Mute"
    )
    view.addSubview(button)

### With state changes
    
    
    import RealtimeKitUI
    
    let button = RtkControlBarButton(
        image: RtkImage(image: UIImage(systemName: "mic")),
        title: "Mute"
    )
    
    // Switch to selected state
    button.setSelected(
        image: RtkImage(image: UIImage(systemName: "mic.slash")),
        title: "Unmute"
    )
    
    // Switch back to default state
    button.setDefault(
        image: RtkImage(image: UIImage(systemName: "mic")),
        title: "Mute"
    )
    view.addSubview(button)

[PreviousRtkControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/)[NextRtkEndMeetingControlBarButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-end-meeting-control-bar-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
