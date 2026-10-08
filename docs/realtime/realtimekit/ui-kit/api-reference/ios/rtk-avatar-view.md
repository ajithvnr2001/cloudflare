---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-avatar-view/
title: RtkAvatarView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:56.873060+00:00
---

# RtkAvatarView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-avatar-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkAvatarView



# RtkAvatarView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-avatar-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage Update participant

A circular avatar view that displays a participant's profile image or name initials as a fallback.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`participant` | `RtkMeetingParticipant` | ✅ | - | The participant whose avatar to display  
  
## Methods

Method | Return Type | Description  
---|---|---  
`set(participant:)` | `Void` | Updates the avatar to display a different participant  
`refresh()` | `Void` | Refreshes the avatar image or initials  
`setInitialName(font:)` | `Void` | Sets the font used for rendering name initials  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let avatarView = RtkAvatarView(participant: participant)
    view.addSubview(avatarView)

### Update participant
    
    
    import RealtimeKitUI
    
    let avatarView = RtkAvatarView(participant: participant)
    view.addSubview(avatarView)
    
    // Update to a different participant
    avatarView.set(participant: newParticipant)
    avatarView.refresh()

[PreviousRtkAudioButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/)[NextRtkButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-avatar-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
