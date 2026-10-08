---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-paginator/
title: RtkGridPaginatorView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:11.797438+00:00
---

# RtkGridPaginatorView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-paginator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkGridPaginatorView



# RtkGridPaginatorView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-paginator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A component which allows you to change the current page of the active participants grid.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `rtkAndroidClient: RealtimeKitClient, uiTokens: RtkDesignTokens` | Bind the paginator to the meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkGridPaginatorView
        android:id="@+id/rtk_grid_paginator"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val paginatorView = findViewById<RtkGridPaginatorView>(R.id.rtk_grid_paginator)
    paginatorView.activate(meeting)

[PreviousRtkErrorView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/error-view/)[NextRtkGridView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/grid-paginator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
