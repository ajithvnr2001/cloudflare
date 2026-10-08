---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/
title: RtkNotificationConfig \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:59.720376+00:00
---

# RtkNotificationConfig · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkNotificationConfig



# RtkNotificationConfig

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesRtkNotification propertiesUsage Examples Basic Usage Customize notifications

Configuration class for controlling notification behavior in meetings. Manages sound and toast notifications for participant join/leave events, chat messages, and polls.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`participantJoined` | `RtkNotification` | ❌ | `RtkNotification()` | Notification settings for participant join events  
`participantLeft` | `RtkNotification` | ❌ | `RtkNotification()` | Notification settings for participant leave events  
`newChatArrived` | `RtkNotification` | ❌ | `RtkNotification()` | Notification settings for new chat messages  
`newPollArrived` | `RtkNotification` | ❌ | `RtkNotification()` | Notification settings for new poll events  
  
## RtkNotification properties

Each `RtkNotification` instance contains the following properties:

Property | Type | Required | Default | Description  
---|---|---|---|---  
`playSound` | `Bool` | ❌ | `true` | Whether to play a notification sound  
`showToast` | `Bool` | ❌ | `true` | Whether to show a toast notification  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let rtkUI = RealtimeKitUI(meetingInfo: meetingInfo)
    // Access the default notification config
    let notificationConfig = rtkUI.notification

### Customize notifications
    
    
    import RealtimeKitUI
    
    let rtkUI = RealtimeKitUI(meetingInfo: meetingInfo)
    
    // Disable sound for participant join events
    rtkUI.notification.participantJoined.playSound = false
    
    // Disable toast for chat messages
    rtkUI.notification.newChatArrived.showToast = false

[PreviousRtkNotificationBadgeView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-badge-view/)[NextRtkParticipantCountView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-count-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
