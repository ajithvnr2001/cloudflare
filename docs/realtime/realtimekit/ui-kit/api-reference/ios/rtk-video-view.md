---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/
title: RtkVideoView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:01.370634+00:00
---

# RtkVideoView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkVideoView



# RtkVideoView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage Self-preview Screen share

Renders a participant's video stream. Supports self-preview, remote participant video, and screen share rendering.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`participant` | `RtkMeetingParticipant` | ✅ | - | The participant whose video to render  
`showSelfPreview` | `Bool` | ❌ | `false` | Whether to show the local camera preview  
`showScreenShare` | `Bool` | ❌ | `false` | Whether to show the screen share stream instead of camera  
  
## Methods

Method | Return Type | Description  
---|---|---  
`reattachRenderer()` | `Void` | Reattaches the video renderer to the participant stream  
`prepareForReuse()` | `Void` | Prepares the view for reuse in a collection or table view  
`clean()` | `Void` | Releases the video renderer and cleans up resources  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let videoView = RtkVideoView(participant: participant)
    view.addSubview(videoView)

### Self-preview
    
    
    import RealtimeKitUI
    
    let previewView = RtkVideoView(
        participant: localParticipant,
        showSelfPreview: true
    )
    view.addSubview(previewView)

### Screen share
    
    
    import RealtimeKitUI
    
    let screenShareView = RtkVideoView(
        participant: participant,
        showScreenShare: true
    )
    view.addSubview(screenShareView)

[PreviousRtkVideoButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-button-control-bar/)[NextRtkWaitListParticipantUpdateEventListener](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
