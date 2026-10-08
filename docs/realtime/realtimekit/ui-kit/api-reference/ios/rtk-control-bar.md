---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/
title: RtkControlBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:57.437217+00:00
---

# RtkControlBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkControlBar



# RtkControlBar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesUsage Examples Basic Usage With completion handlers

Base control bar view with a More menu button and an End Call button. Serves as the foundation for `RtkMeetingControlBar` and `RtkWebinarControlBar`.

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
`moreButton` | `RtkMoreButtonControlBar` | - | - | The More menu button (read-only)  
`endCallButton` | `RtkEndMeetingControlBarButton` | - | - | The End Call button  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let controlBar = RtkControlBar(
        meeting: rtkClient,
        delegate: self,
        presentingViewController: self
    )
    view.addSubview(controlBar)

### With completion handlers
    
    
    import RealtimeKitUI
    
    let controlBar = RtkControlBar(
        meeting: rtkClient,
        delegate: self,
        presentingViewController: self,
        onLeaveMeetingCompletion: {
            self.dismiss(animated: true)
        }
    )
    view.addSubview(controlBar)

[PreviousRtkClockView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-clock-view/)[NextRtkControlBarButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
