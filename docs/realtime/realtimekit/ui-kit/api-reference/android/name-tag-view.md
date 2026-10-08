---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/name-tag-view/
title: RtkNameTagView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:14.360025+00:00
---

# RtkNameTagView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/name-tag-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkNameTagView



# RtkNameTagView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/name-tag-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

Displays a participant's name and an audio indicator.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `participant: RtkMeetingParticipant, isScreenShare: Boolean` | Bind the name tag to a participant  
`setMaxLength` | `length: Int` | Set the maximum length for the displayed name  
`refresh` | - | Refresh the name and audio indicator  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.nametagview.RtkNameTagView
        android:id="@+id/rtk_name_tag"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val nameTag = findViewById<RtkNameTagView>(R.id.rtk_name_tag)
    nameTag.activate(participant)

[PreviousRtkMoreToggleButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/more-toggle-button/)[NextRtkParticipantAudioIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-audio-indicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/name-tag-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
