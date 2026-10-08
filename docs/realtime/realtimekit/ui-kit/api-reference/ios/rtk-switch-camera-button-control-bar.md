---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-switch-camera-button-control-bar/
title: RtkSwitchCameraButtonControlBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:00.940675+00:00
---

# RtkSwitchCameraButtonControlBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-switch-camera-button-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkSwitchCameraButtonControlBar



# RtkSwitchCameraButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-switch-camera-button-control-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage

A control bar button that switches between the front and rear cameras.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let switchCameraButton = RtkSwitchCameraButtonControlBar(meeting: rtkClient)
    view.addSubview(switchCameraButton)

[PreviousRtkStageActionButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-stage-action-button-control-bar/)[NextRtkVideoButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-button-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-switch-camera-button-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
