---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-button-control-bar/
title: RtkVideoButtonControlBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:01.067623+00:00
---

# RtkVideoButtonControlBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-button-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkVideoButtonControlBar



# RtkVideoButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-button-control-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage

A control bar button that toggles the local camera on and off. Checks camera permissions before toggling.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`rtkClient` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let videoButton = RtkVideoButtonControlBar(rtkClient: rtkClient)
    view.addSubview(videoButton)

[PreviousRtkSwitchCameraButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-switch-camera-button-control-bar/)[NextRtkVideoView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-button-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
