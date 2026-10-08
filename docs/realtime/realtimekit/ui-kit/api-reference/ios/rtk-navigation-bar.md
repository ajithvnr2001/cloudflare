---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-navigation-bar/
title: RtkNavigationBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:59.244896+00:00
---

# RtkNavigationBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-navigation-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkNavigationBar



# RtkNavigationBar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-navigation-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesMethodsUsage Examples Basic Usage With back button handler

A navigation bar with a title label and a close or back button. Used for modal screens such as chat, polls, and participant lists.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`title` | `String` | ✅ | - | The title text displayed in the navigation bar  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`titleLabel` | `RtkLabel` | - | - | The label displaying the navigation bar title (read-only)  
`leftButton` | `RtkControlBarButton` | - | - | The close or back button on the left side (read-only)  
  
## Methods

Method | Return Type | Description  
---|---|---  
`setBackButtonClick(callBack:)` | `Void` | Sets the tap handler for the back or close button  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let navBar = RtkNavigationBar(title: "Participants")
    view.addSubview(navBar)

### With back button handler
    
    
    import RealtimeKitUI
    
    let navBar = RtkNavigationBar(title: "Chat")
    navBar.setBackButtonClick {
        self.dismiss(animated: true)
    }
    view.addSubview(navBar)

[PreviousRtkNameTag](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-name-tag/)[NextRtkNotificationBadgeView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-badge-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-navigation-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
