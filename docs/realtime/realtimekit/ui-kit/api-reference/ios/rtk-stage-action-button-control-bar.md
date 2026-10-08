---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-stage-action-button-control-bar/
title: RtkStageActionButtonControlBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:00.653820+00:00
---

# RtkStageActionButtonControlBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-stage-action-button-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkStageActionButtonControlBar



# RtkStageActionButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-stage-action-button-control-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesUsage Examples Basic Usage

A control bar button for webinar stage actions. Supports requesting to join, joining, leaving, and canceling stage requests based on the current stage status.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`rtkClient` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`buttonState` | `WebinarStageStatus` | ✅ | - | The current stage status that determines the button action  
`presentingViewController` | `UIViewController` | ✅ | - | View controller used for presenting confirmation dialogs  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`dataSource` | `RtkStageActionButtonControlBarDataSource?` | ❌ | `nil` | Data source for customizing stage action button behavior  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let stageButton = RtkStageActionButtonControlBar(
        rtkClient: rtkClient,
        buttonState: .requestToJoinStage,
        presentingViewController: self
    )
    view.addSubview(stageButton)

[PreviousRtkSetupViewController](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-setup-view-controller/)[NextRtkSwitchCameraButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-switch-camera-button-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-stage-action-button-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
