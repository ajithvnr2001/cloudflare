---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/
title: RtkPluginsView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:00.310344+00:00
---

# RtkPluginsView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkPluginsView



# RtkPluginsView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesMethodsUsage Examples Basic Usage With tab buttons

A composite view for displaying plugins and screen share content. Includes a tab selector, plugin content area, and a floating active speaker view.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`videoPeerViewModel` | `VideoPeerViewModel` | ✅ | - | The view model for the active speaker video  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`activeListView` | `RtkActiveTabSelectorView` | - | - | The tab selector for switching between plugins and screen shares  
`pluginVideoView` | `UIView` | - | - | The container view for plugin content  
`syncButton` | `UIButton` | - | - | Button to sync the plugin view with the presenter  
  
## Methods

Method | Return Type | Description  
---|---|---  
`setButtons(buttons:selectedIndex:clickAction:)` | `Void` | Configures the tab selector buttons with a selection handler  
`show(pluginView:)` | `Void` | Displays a plugin view in the content area  
`showVideoView(participant:)` | `Void` | Displays a participant's video in the content area  
`showPinnedView(participant:)` | `Void` | Displays a pinned participant's video  
`showActiveSpeakerView(participant:)` | `Void` | Shows the floating active speaker overlay  
`hideActiveSpeaker()` | `Void` | Hides the floating active speaker overlay  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let viewModel = VideoPeerViewModel(
        meeting: rtkClient,
        participant: participant,
        showSelfPreviewVideo: false
    )
    let pluginsView = RtkPluginsView(videoPeerViewModel: viewModel)
    view.addSubview(pluginsView)

### With tab buttons
    
    
    import RealtimeKitUI
    
    let viewModel = VideoPeerViewModel(
        meeting: rtkClient,
        participant: participant,
        showSelfPreviewVideo: false
    )
    let pluginsView = RtkPluginsView(videoPeerViewModel: viewModel)
    
    let buttons = [
        RtkPluginScreenShareTabButton(image: nil, title: "Screen Share"),
        RtkPluginScreenShareTabButton(image: nil, title: "Whiteboard")
    ]
    pluginsView.setButtons(
        buttons: buttons,
        selectedIndex: 0,
        clickAction: { index in
            print("Selected tab: \(index)")
        }
    )
    view.addSubview(pluginsView)

[PreviousRtkPluginScreenShareTabButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugin-screen-share-tab-button/)[NextRtkRecordingView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-recording-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
