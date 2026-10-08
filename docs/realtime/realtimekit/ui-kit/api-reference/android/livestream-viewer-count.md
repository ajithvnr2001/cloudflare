---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-viewer-count/
title: RtkLivestreamViewerCount \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:13.398971+00:00
---

# RtkLivestreamViewerCount · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-viewer-count/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkLivestreamViewerCount



# RtkLivestreamViewerCount

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-viewer-count/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

Displays the current viewer count for a livestream.

## Methods

Method | Parameters | Description  
---|---|---  
`refresh` | `meeting: RealtimeKitClient` | Update the viewer count based on the current meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkLivestreamViewerCount
        android:id="@+id/rtk_viewer_count"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val viewerCount = findViewById<RtkLivestreamViewerCount>(R.id.rtk_viewer_count)
    viewerCount.refresh(meeting)

[PreviousRtkLivestreamToggleButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-toggle-button/)[NextRtkLoaderView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/loader-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/livestream-viewer-count.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
