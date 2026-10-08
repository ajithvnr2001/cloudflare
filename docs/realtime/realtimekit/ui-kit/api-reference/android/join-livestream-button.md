---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-livestream-button/
title: RtkJoinLivestreamButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:12.303586+00:00
---

# RtkJoinLivestreamButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-livestream-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkJoinLivestreamButton



# RtkJoinLivestreamButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-livestream-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A button for joining or leaving the livestream stage.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkJoinLivestreamButton
        android:id="@+id/rtk_join_livestream"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val joinLivestreamButton = findViewById<RtkJoinLivestreamButton>(R.id.rtk_join_livestream)
    joinLivestreamButton.activate(meeting)

[PreviousRtkJoinButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-button/)[NextRtkJoinStageDialog](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-stage-dialog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/join-livestream-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
