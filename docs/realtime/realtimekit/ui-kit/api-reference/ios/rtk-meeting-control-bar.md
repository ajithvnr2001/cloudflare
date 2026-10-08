---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-control-bar/
title: RtkMeetingControlBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:58.425739+00:00
---

# RtkMeetingControlBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkMeetingControlBar



# RtkMeetingControlBar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-control-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesUsage Examples Basic Usage With leave meeting handler

Control bar for group calls that extends `RtkControlBar` with microphone and video toggle buttons.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`delegate` | `RtkTabBarDelegate?` | ✅ | - | Delegate for handling tab bar interactions  
`presentingViewController` | `UIViewController` | ✅ | - | View controller used for presenting modal screens  
`appearance` | `RtkControlBarAppearance` | ❌ | `RtkControlBarAppearanceModel()` | Appearance configuration for the control bar  
`settingViewControllerCompletion` | `(() -> Void)?` | ❌ | `nil` | Closure called when the settings view controller dismisses  
`onLeaveMeetingCompletion` | `(() -> Void)?` | ❌ | `nil` | Closure called when the participant leaves the meeting  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`dataSource` | `RtkMeetingControlBarDataSource?` | ❌ | `nil` | Data source for customizing control bar buttons  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let controlBar = RtkMeetingControlBar(
        meeting: rtkClient,
        delegate: self,
        presentingViewController: self
    )
    view.addSubview(controlBar)

### With leave meeting handler
    
    
    import RealtimeKitUI
    
    let controlBar = RtkMeetingControlBar(
        meeting: rtkClient,
        delegate: self,
        presentingViewController: self,
        onLeaveMeetingCompletion: {
            self.navigationController?.popViewController(animated: true)
        }
    )
    view.addSubview(controlBar)

[PreviousRtkLeaveDialog](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-leave-dialog/)[NextRtkMeetingHeaderView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
