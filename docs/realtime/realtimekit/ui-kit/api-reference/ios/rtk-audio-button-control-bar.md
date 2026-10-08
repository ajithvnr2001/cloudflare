---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/
title: RtkAudioButtonControlBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:56.770784+00:00
---

# RtkAudioButtonControlBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkAudioButtonControlBar



# RtkAudioButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With tap handler

A control bar button that toggles the local microphone on and off. Checks microphone permissions before toggling.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`onClick` | `((RtkAudioButtonControlBar) -> Void)?` | ❌ | `nil` | Closure called when the button is tapped  
`appearance` | `RtkControlBarButtonAppearance` | ❌ | - | Appearance configuration for the button  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let audioButton = RtkAudioButtonControlBar(meeting: rtkClient)
    view.addSubview(audioButton)

### With tap handler
    
    
    import RealtimeKitUI
    
    let audioButton = RtkAudioButtonControlBar(
        meeting: rtkClient,
        onClick: { button in
            print("Audio toggled")
        }
    )
    view.addSubview(audioButton)

[PreviousRtkActiveTabSelectorView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-active-tab-selector-view/)[NextRtkAvatarView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-avatar-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
