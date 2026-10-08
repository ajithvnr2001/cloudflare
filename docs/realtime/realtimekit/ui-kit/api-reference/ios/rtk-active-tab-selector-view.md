---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-active-tab-selector-view/
title: RtkActiveTabSelectorView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:56.646942+00:00
---

# RtkActiveTabSelectorView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-active-tab-selector-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkActiveTabSelectorView



# RtkActiveTabSelectorView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-active-tab-selector-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesMethodsUsage Examples Basic Usage

A horizontally scrollable tab selector for switching between plugins and screen shares.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`buttons` | `[RtkPluginScreenShareTabButton]` | - | - | The array of tab buttons in the selector  
  
## Methods

Method | Return Type | Description  
---|---|---  
`scrollToVisible(button:)` | `Void` | Scrolls the tab selector to make the specified button visible  
`setAndDisplayButtons(_:)` | `Void` | Sets and displays the provided array of tab buttons  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let tabSelector = RtkActiveTabSelectorView()
    let buttons = [
        RtkPluginScreenShareTabButton(image: nil, title: "Screen Share"),
        RtkPluginScreenShareTabButton(image: nil, title: "Whiteboard")
    ]
    tabSelector.setAndDisplayButtons(buttons)
    view.addSubview(tabSelector)

[PreviousMeetingViewController](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/meeting-view-controller/)[NextRtkAudioButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-active-tab-selector-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
