---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/
title: RtkEventSelfListener \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:57.807935+00:00
---

# RtkEventSelfListener · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkEventSelfListener



# RtkEventSelfListener

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage Toggle audio and video Observe meeting end

A helper class that wraps self-participant and meeting event listeners with closure-based callbacks. Provides methods for toggling audio and video, observing state changes, and checking device permissions.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`rtkClient` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`identifier` | `String` | ❌ | `"Default"` | A unique identifier for this listener instance  
  
## Methods

Method | Return Type | Description  
---|---|---  
`toggleLocalAudio(completion:)` | `Void` | Toggles the local microphone on or off  
`toggleLocalVideo(completion:)` | `Void` | Toggles the local camera on or off  
`observeSelfVideo(update:)` | `Void` | Registers a callback for local video state changes  
`observeSelfAudio(update:)` | `Void` | Registers a callback for local audio state changes  
`observeSelfRemoved(update:)` | `Void` | Registers a callback for when the local participant is removed  
`observeSelfMeetingEndForAll(update:)` | `Void` | Registers a callback for when the meeting ends for all participants  
`observeWebinarStageStatus(update:)` | `Void` | Registers a callback for webinar stage status changes  
`observeRequestToJoinStage(update:)` | `Void` | Registers a callback for stage join request events  
`observeSelfPermissionChanged(update:)` | `Void` | Registers a callback for permission changes on the local participant  
`observeMeetingReconnectionState(update:)` | `Void` | Registers a callback for meeting reconnection state changes  
`isCameraPermissionGranted()` | `Bool` | Returns whether camera permission is granted  
`isMicrophonePermissionGranted()` | `Bool` | Returns whether microphone permission is granted  
`clean()` | `Void` | Removes all registered listeners and cleans up resources  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let listener = RtkEventSelfListener(rtkClient: rtkClient)
    
    listener.observeSelfAudio { isEnabled in
        print("Audio enabled: \(isEnabled)")
    }
    
    listener.observeSelfVideo { isEnabled in
        print("Video enabled: \(isEnabled)")
    }

### Toggle audio and video
    
    
    import RealtimeKitUI
    
    let listener = RtkEventSelfListener(rtkClient: rtkClient)
    
    listener.toggleLocalAudio { success in
        print("Audio toggled: \(success)")
    }
    
    listener.toggleLocalVideo { success in
        print("Video toggled: \(success)")
    }

### Observe meeting end
    
    
    import RealtimeKitUI
    
    let listener = RtkEventSelfListener(
        rtkClient: rtkClient,
        identifier: "MeetingObserver"
    )
    
    listener.observeSelfRemoved {
        print("Removed from meeting")
    }
    
    listener.observeSelfMeetingEndForAll {
        print("Meeting ended for all")
    }

[PreviousRtkEndMeetingControlBarButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-end-meeting-control-bar-button/)[NextRtkImage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
