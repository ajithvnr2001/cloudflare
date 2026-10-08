---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-audio-grid/
title: rtk-audio-grid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:17.663930+00:00
---

# rtk-audio-grid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-audio-grid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-audio-grid



# rtk-audio-grid

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-audio-grid/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ✅ | - | Config  
`hideSelf` | `boolean` | ✅ | - | Whether to hide self in the grid  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`size` | `Size1` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-audio-grid></rtk-audio-grid>

### With Properties
    
    
    <!-- component.html -->
    <rtk-audio-grid
     [config]="defaultUiConfig"
     [hideSelf]="true"
     [meeting]="meeting">
    </rtk-audio-grid>

[Previousrtk-ai-transcriptions](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ai-transcriptions/)[Nextrtk-audio-tile](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-audio-tile/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-audio-grid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
