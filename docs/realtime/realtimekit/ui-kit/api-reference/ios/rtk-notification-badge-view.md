---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-badge-view/
title: RtkNotificationBadgeView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:59.581045+00:00
---

# RtkNotificationBadgeView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-badge-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkNotificationBadgeView



# RtkNotificationBadgeView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-badge-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage Reset badge

A small circular badge view that displays a notification count. Hides automatically when the count is zero and shows "99+" for counts over 99.

## Methods

Method | Return Type | Description  
---|---|---  
`setBadgeCount(_:)` | `Void` | Sets the badge count. Hides the badge at zero and displays "99+" for values over 99.  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let badge = RtkNotificationBadgeView()
    badge.setBadgeCount(5)
    view.addSubview(badge)

### Reset badge
    
    
    import RealtimeKitUI
    
    let badge = RtkNotificationBadgeView()
    badge.setBadgeCount(3)
    view.addSubview(badge)
    
    // Hide the badge by setting count to zero
    badge.setBadgeCount(0)

[PreviousRtkNavigationBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-navigation-bar/)[NextRtkNotificationConfig](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-badge-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
