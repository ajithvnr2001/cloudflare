---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/
title: RtkParticipantTileView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:14.972802+00:00
---

# RtkParticipantTileView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkParticipantTileView



# RtkParticipantTileView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesMethodsUsage Examples Basic Usage With Methods

A component which plays a participant's video and allows for placement of components like name tag and avatar.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`rtk_ptv_nameTagPosition` | `BOTTOM_LEFT | TOP_CENTER` | ❌ | `BOTTOM_LEFT` | Position of the name tag  
`cardBackgroundColor` | `color` | ❌ | - | Background color of the tile  
`cardCornerRadius` | `dimension` | ❌ | - | Corner radius of the tile  
  
## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `participant: RtkMeetingParticipant` | Bind the tile to a specific participant  
`refreshParticipantName` | - | Refresh the name tag and avatar  
`refreshParticipantVideo` | - | Refresh the video view state  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.participanttile.RtkParticipantTileView
        android:id="@+id/rtk_participant_tile"
        android:layout_width="match_parent"
        android:layout_height="200dp"
        app:rtk_ptv_nameTagPosition="BOTTOM_LEFT" />

### With Methods
    
    
    val tile = findViewById<RtkParticipantTileView>(R.id.rtk_participant_tile)
    tile.activate(participant)

[PreviousRtkParticipantsFragment](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participants/)[NextRtkParticipantVideoIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-video-indicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
