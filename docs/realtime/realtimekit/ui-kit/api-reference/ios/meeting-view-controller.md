---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/meeting-view-controller/
title: MeetingViewController \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:56.534973+00:00
---

# MeetingViewController · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/meeting-view-controller/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /MeetingViewController



# MeetingViewController

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/meeting-view-controller/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesMeetingViewControllerDataSource protocolUsage Examples Basic Usage With custom data source

The main meeting screen view controller. Displays the participant grid, plugins, screen share, header, and control bar.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance for the active meeting  
`completion` | `@escaping () -> Void` | ✅ | - | Closure called when the meeting ends  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`dataSource` | `MeetingViewControllerDataSource?` | ❌ | `nil` | Data source for providing custom topbar, middle view, and bottom bar  
  
## MeetingViewControllerDataSource protocol

Implement this protocol to provide custom UI sections within the meeting screen.

Method | Return Type | Description  
---|---|---  
`getTopbar(viewController:)` | `RtkMeetingHeaderView?` | Returns a custom header view for the meeting screen  
`getMiddleView(viewController:)` | `UIView?` | Returns a custom middle view between the header and control bar  
`getBottomTabbar(viewController:)` | `RtkMeetingControlBar?` | Returns a custom control bar for the meeting screen  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let meetingVC = MeetingViewController(
        meeting: rtkClient,
        completion: {
            self.dismiss(animated: true)
        }
    )
    meetingVC.modalPresentationStyle = .fullScreen
    self.present(meetingVC, animated: true)

### With custom data source
    
    
    import RealtimeKitUI
    
    class CustomDataSource: MeetingViewControllerDataSource {
        func getTopbar(viewController: MeetingViewController) -> RtkMeetingHeaderView? {
            return RtkMeetingHeaderView(meeting: rtkClient)
        }
    
        func getMiddleView(viewController: MeetingViewController) -> UIView? {
            return nil
        }
    
        func getBottomTabbar(viewController: MeetingViewController) -> RtkMeetingControlBar? {
            return nil
        }
    }
    
    let meetingVC = MeetingViewController(
        meeting: rtkClient,
        completion: {
            self.dismiss(animated: true)
        }
    )
    meetingVC.dataSource = CustomDataSource()
    self.present(meetingVC, animated: true)

[PreviousGridView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/grid-view/)[NextRtkActiveTabSelectorView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-active-tab-selector-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/meeting-view-controller.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
