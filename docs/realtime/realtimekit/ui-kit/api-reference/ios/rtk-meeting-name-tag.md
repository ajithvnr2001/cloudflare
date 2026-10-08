---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-name-tag/
title: RtkMeetingNameTag \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:58.535753+00:00
---

# RtkMeetingNameTag · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-name-tag/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkMeetingNameTag



# RtkMeetingNameTag

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-name-tag/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage Update participant

A name tag view that displays the participant name and a microphone status icon. Automatically updates when the participant's audio state changes.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`participant` | `RtkMeetingParticipant` | ✅ | - | The participant whose name and mic status to display  
`appearance` | `RtkNameTagAppearance` | ❌ | - | Appearance configuration for the name tag  
  
## Methods

Method | Return Type | Description  
---|---|---  
`set(participant:)` | `Void` | Updates the name tag to display a different participant  
`refresh()` | `Void` | Refreshes the name and microphone status display  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let nameTag = RtkMeetingNameTag(
        meeting: rtkClient,
        participant: participant
    )
    view.addSubview(nameTag)

### Update participant
    
    
    import RealtimeKitUI
    
    let nameTag = RtkMeetingNameTag(
        meeting: rtkClient,
        participant: participant
    )
    view.addSubview(nameTag)
    
    // Switch to a different participant
    nameTag.set(participant: newParticipant)
    nameTag.refresh()

[PreviousRtkMeetingHeaderView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/)[NextRtkMeetingTitleLabel](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-title-label/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-name-tag.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
