---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/webinar-stage-toggle/
title: RtkWebinarStageToggleButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:16.978403+00:00
---

# RtkWebinarStageToggleButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/webinar-stage-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkWebinarStageToggleButton



# RtkWebinarStageToggleButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/webinar-stage-toggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

Component that lets you add provision for the local user to join the webinar stage.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state  
`deactivate` | - | Unbind the button and remove event listeners  
`refresh` | - | Force a refresh of the button state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbarbuttons.webinarstagetogglebutton.RtkWebinarStageToggleButton
        android:id="@+id/rtk_webinar_stage_toggle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val stageToggleButton = findViewById<RtkWebinarStageToggleButton>(R.id.rtk_webinar_stage_toggle)
    stageToggleButton.activate(meeting)

[PreviousRtkWebinarControlBarView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/webinar-control-bar/)[Nextrtk-ai](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/webinar-stage-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
