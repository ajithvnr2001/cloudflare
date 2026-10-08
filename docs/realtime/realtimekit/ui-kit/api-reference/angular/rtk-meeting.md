---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-meeting/
title: rtk-meeting \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:26.893257+00:00
---

# rtk-meeting · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-meeting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-meeting



# rtk-meeting

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-meeting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A single component which renders an entire meeting UI. It loads your preset and renders the UI based on it. With this component, you don't have to handle all the states, dialogs and other smaller bits of managing the application.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`applyDesignSystem` | `boolean` | ✅ | - | Whether to apply the design system on the document root from config  
`config` | `UIConfig` | ✅ | - | UI Config  
`gridLayout` | `GridLayout1` | ✅ | - | Grid layout  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`leaveOnUnmount` | `boolean` | ✅ | - | Whether participant should leave when this component gets unmounted  
`loadConfigFromPreset` | `boolean` | ✅ | - | Whether to load config from preset  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`mode` | `MeetingMode` | ✅ | - | Fill type  
`overrides` | `Overrides` | ❌ | `defaultOverrides` | UI Kit Overrides  
`showSetupScreen` | `boolean` | ✅ | - | Whether to show setup screen or not  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-meeting></rtk-meeting>

### With Properties
    
    
    <!-- component.html -->
    <rtk-meeting
     [applyDesignSystem]="true"
     [config]="defaultUiConfig"
     [gridLayout]="gridlayout1">
    </rtk-meeting>

[Previousrtk-markdown-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-markdown-view/)[Nextrtk-meeting-title](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-meeting-title/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-meeting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
