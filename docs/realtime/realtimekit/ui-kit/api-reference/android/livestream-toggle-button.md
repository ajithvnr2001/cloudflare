---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-toggle-button/
title: RtkLivestreamToggleButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:13.154904+00:00
---

# RtkLivestreamToggleButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-toggle-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkLivestreamToggleButton



# RtkLivestreamToggleButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-toggle-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A toggle button for starting or stopping a livestream.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkLivestreamToggleButton
        android:id="@+id/rtk_livestream_toggle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val livestreamToggle = findViewById<RtkLivestreamToggleButton>(R.id.rtk_livestream_toggle)
    livestreamToggle.activate(meeting)

[PreviousRtkLivestreamIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-indicator/)[NextRtkLivestreamViewerCount](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-viewer-count/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/livestream-toggle-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
