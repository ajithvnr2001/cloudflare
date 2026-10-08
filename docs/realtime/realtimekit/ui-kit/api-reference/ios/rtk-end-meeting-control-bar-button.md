---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-end-meeting-control-bar-button/
title: RtkEndMeetingControlBarButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:57.532290+00:00
---

# RtkEndMeetingControlBarButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-end-meeting-control-bar-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkEndMeetingControlBarButton



# RtkEndMeetingControlBarButton

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-end-meeting-control-bar-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesUsage Examples Basic Usage Without confirmation dialog

A control bar button that ends or leaves the meeting. Optionally displays a confirmation dialog before ending the meeting.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`alertViewController` | `UIViewController` | ✅ | - | View controller used to present the confirmation alert  
`onClick` | `((RtkEndMeetingControlBarButton, RtkLeaveDialog.RtkLeaveDialogAlertButtonType) -> Void)?` | ❌ | `nil` | Closure called after the user confirms leaving or ending the meeting, receiving the button and the selected action type  
`appearance` | `RtkControlBarButtonAppearance` | ❌ | - | Appearance configuration for the button  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`shouldShowAlertOnClick` | `Bool` | ❌ | `true` | Whether to show a confirmation alert before ending the meeting  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let endButton = RtkEndMeetingControlBarButton(
        meeting: rtkClient,
        alertViewController: self
    )
    view.addSubview(endButton)

### Without confirmation dialog
    
    
    import RealtimeKitUI
    
    let endButton = RtkEndMeetingControlBarButton(
        meeting: rtkClient,
        alertViewController: self,
        onClick: { button, actionType in
            print("Action: \(actionType)")
        }
    )
    endButton.shouldShowAlertOnClick = false
    view.addSubview(endButton)

[PreviousRtkControlBarButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar-button/)[NextRtkEventSelfListener](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-end-meeting-control-bar-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
