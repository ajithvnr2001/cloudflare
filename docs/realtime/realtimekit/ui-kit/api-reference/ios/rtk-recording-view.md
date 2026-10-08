---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-recording-view/
title: RtkRecordingView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:00.421509+00:00
---

# RtkRecordingView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-recording-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkRecordingView



# RtkRecordingView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-recording-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage With custom title

A blinking recording indicator displayed when the meeting is being recorded. Shows a red dot with configurable text and image.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance for the active meeting  
`title` | `String` | ❌ | `"Rec"` | Text label displayed next to the recording indicator  
`image` | `RtkImage?` | ❌ | `nil` | Custom image for the recording indicator  
`appearance` | `RtkRecordingViewAppearance` | ❌ | - | Appearance configuration for the recording indicator  
  
## Methods

Method | Return Type | Description  
---|---|---  
`blinking(start: Bool)` | `Void` | Starts or stops the blinking animation on the recording indicator  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let recordingView = RtkRecordingView(meeting: rtkClient)
    view.addSubview(recordingView)

### With custom title
    
    
    import RealtimeKitUI
    
    let recordingView = RtkRecordingView(
        meeting: rtkClient,
        title: "Recording"
    )
    view.addSubview(recordingView)

[PreviousRtkPluginsView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/)[NextRtkSetupViewController](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-setup-view-controller/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-recording-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
