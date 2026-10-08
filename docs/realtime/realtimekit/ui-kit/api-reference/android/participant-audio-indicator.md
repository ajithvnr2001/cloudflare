---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-audio-indicator/
title: RtkParticipantAudioIndicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:31.160308+00:00
---

# RtkParticipantAudioIndicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-audio-indicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkParticipantAudioIndicator



# RtkParticipantAudioIndicator

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-audio-indicator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

An audio visualizer component which visualizes a participant's audio.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `participant: RtkMeetingParticipant` | Bind the indicator to a participant  
`refresh` | - | Force a refresh of the audio indicator state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkParticipantAudioIndicator
        android:id="@+id/audio_indicator"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val audioIndicator = findViewById<RtkParticipantAudioIndicator>(R.id.audio_indicator)
    audioIndicator.activate(participant)

[PreviousRtkNameTagView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/name-tag-view/)[NextRtkParticipantCountView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-count-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/participant-audio-indicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
