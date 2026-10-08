---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-leave-dialog/
title: RtkLeaveDialog \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:58.317787+00:00
---

# RtkLeaveDialog · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-leave-dialog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkLeaveDialog



# RtkLeaveDialog

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-leave-dialog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage With selection handler

A dialog that presents leave and end meeting options. Displays different options based on host permissions.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`onClick` | `((RtkLeaveDialogAlertButtonType) -> Void)?` | ❌ | `nil` | Closure called when the user selects a dialog option  
  
## Methods

Method | Return Type | Description  
---|---|---  
`show(on:)` | `Void` | Presents the leave dialog on the specified view controller  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let leaveDialog = RtkLeaveDialog(meeting: rtkClient)
    leaveDialog.show(on: self)

### With selection handler
    
    
    import RealtimeKitUI
    
    let leaveDialog = RtkLeaveDialog(
        meeting: rtkClient,
        onClick: { buttonType in
            switch buttonType {
            case .leaveMeeting:
                print("Leaving meeting")
            case .endMeeting:
                print("Ending meeting for all")
            default:
                break
            }
        }
    )
    leaveDialog.show(on: self)

[PreviousRtkLabel](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-label/)[NextRtkMeetingControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-leave-dialog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
