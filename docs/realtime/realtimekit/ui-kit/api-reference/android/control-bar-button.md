---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-button/
title: RtkControlBarButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:11.461911+00:00
---

# RtkControlBarButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkControlBarButton



# RtkControlBarButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesMethodsUsage Examples Basic Usage With Methods

A skeleton component used for composing custom controlbar buttons.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`rtk_cbb_icon` | `reference` | ❌ | - | Drawable resource for the button icon  
`rtk_cbb_variant` | `button | horizontal` | ❌ | `button` | Layout variant  
`rtk_cbb_showText` | `boolean` | ❌ | `true` | Whether to show the label text  
`rtk_cbb_iconSize` | `dimension` | ❌ | - | Size of the icon  
`rtk_cbb_iconPadding` | `dimension` | ❌ | - | Padding between icon and label  
  
## Methods

Method | Parameters | Description  
---|---|---  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
`setIconDrawable` | `drawable: Drawable?` | Set the button icon  
`setIconTint` | `color: Int` | Set the icon tint color  
`setText` | `text: String?` | Set the button label text  
`setProcessingState` | `processing: Boolean` | Show or hide a loading spinner  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkControlBarButton
        android:id="@+id/rtk_control_bar_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:rtk_cbb_showText="true"
        app:rtk_cbb_variant="button" />

### With Methods
    
    
    val buttonView = findViewById<RtkControlBarButton>(R.id.rtk_control_bar_button)
    buttonView.setOnClickListener { }

[PreviousRtkClockView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/clock-view/)[NextRtkControlBarView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/control-bar-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
