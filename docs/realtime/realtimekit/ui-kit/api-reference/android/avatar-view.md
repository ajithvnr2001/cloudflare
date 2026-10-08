---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/avatar-view/
title: RtkAvatarView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:10.762738+00:00
---

# RtkAvatarView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/avatar-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkAvatarView



# RtkAvatarView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/avatar-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

Avatar component which renders a participant's profile picture or their initials.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `participant: RtkMeetingParticipant` | Bind the avatar to a participant  
`refresh` | - | Refresh the avatar based on the participant's name  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.avatarview.RtkAvatarView
        android:id="@+id/rtk_avatar"
        android:layout_width="48dp"
        android:layout_height="48dp" />

### With Methods
    
    
    val avatar = findViewById<RtkAvatarView>(R.id.rtk_avatar)
    avatar.activate(participant)

[PreviousRtkAudioDeviceSelector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/audio-device-selector/)[NextRtkButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/avatar-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
