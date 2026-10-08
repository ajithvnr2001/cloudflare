---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-button-control-bar/
title: RtkMoreButtonControlBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:59.054803+00:00
---

# RtkMoreButtonControlBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-button-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkMoreButtonControlBar



# RtkMoreButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-button-control-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage With settings completion

A control bar button that opens a bottom sheet menu with meeting actions such as chat, polls, and participant list.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`presentingViewController` | `UIViewController` | ✅ | - | View controller used to present the bottom sheet  
`settingViewControllerCompletion` | `(() -> Void)?` | ❌ | `nil` | Closure called when the settings view controller dismisses  
  
## Methods

Method | Return Type | Description  
---|---|---  
`hideBottomSheet()` | `Void` | Programmatically dismisses the bottom sheet menu  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let moreButton = RtkMoreButtonControlBar(
        meeting: rtkClient,
        presentingViewController: self
    )
    view.addSubview(moreButton)

### With settings completion
    
    
    import RealtimeKitUI
    
    let moreButton = RtkMoreButtonControlBar(
        meeting: rtkClient,
        presentingViewController: self,
        settingViewControllerCompletion: {
            print("Settings dismissed")
        }
    )
    view.addSubview(moreButton)

[PreviousRtkMeetingTitleLabel](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-title-label/)[NextRtkMoreMenu](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-button-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
