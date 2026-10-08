---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/
title: RtkWaitListParticipantUpdateEventListener \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:01.186829+00:00
---

# RtkWaitListParticipantUpdateEventListener · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkWaitListParticipantUpdateEventListener



# RtkWaitListParticipantUpdateEventListener

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersCallback propertiesMethodsUsage Examples Basic Usage Accept or reject requests

A helper class for listening to waitlist participant events. Provides callbacks for join, remove, accept, and reject events, and methods for managing waitlist requests.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`rtkClient` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
  
## Callback properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`participantJoinedCompletion` | `(() -> Void)?` | ❌ | `nil` | Called when a participant joins the waitlist  
`participantRemovedCompletion` | `(() -> Void)?` | ❌ | `nil` | Called when a participant is removed from the waitlist  
`participantRequestAcceptedCompletion` | `(() -> Void)?` | ❌ | `nil` | Called when a waitlist request is accepted  
`participantRequestRejectCompletion` | `(() -> Void)?` | ❌ | `nil` | Called when a waitlist request is rejected  
  
## Methods

Method | Return Type | Description  
---|---|---  
`acceptWaitingRequest(participant:)` | `Void` | Accepts a participant's waitlist request  
`rejectWaitingRequest(participant:)` | `Void` | Rejects a participant's waitlist request  
`clean()` | `Void` | Removes all registered listeners and cleans up resources  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let waitlistListener = RtkWaitListParticipantUpdateEventListener(
        rtkClient: rtkClient
    )
    
    waitlistListener.participantJoinedCompletion = {
        print("New participant in waitlist")
    }
    
    waitlistListener.participantRemovedCompletion = {
        print("Participant removed from waitlist")
    }

### Accept or reject requests
    
    
    import RealtimeKitUI
    
    let waitlistListener = RtkWaitListParticipantUpdateEventListener(
        rtkClient: rtkClient
    )
    
    // Accept a waiting participant
    waitlistListener.acceptWaitingRequest(participant: waitingParticipant)
    
    // Reject a waiting participant
    waitlistListener.rejectWaitingRequest(participant: waitingParticipant)

[PreviousRtkVideoView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/)[NextRtkAi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
