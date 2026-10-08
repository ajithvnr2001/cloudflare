---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/more-toggle-button/
title: RtkMoreToggleButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:14.876569+00:00
---

# RtkMoreToggleButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/more-toggle-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkMoreToggleButton



# RtkMoreToggleButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/more-toggle-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A button which toggles visibility of a more menu.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkMoreToggleButton
        android:id="@+id/rtk_more_toggle"
        android:layout_width="50dp"
        android:layout_height="50dp" />

### With Methods
    
    
    val moreToggleButton = findViewById<RtkMoreToggleButton>(R.id.rtk_more_toggle)
    moreToggleButton.activate(meeting)

[PreviousRtkMicToggleButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/mic-toggle/)[NextRtkNameTagView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/name-tag-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/more-toggle-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
