---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-setup/
title: rtk-participant-setup \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:29.086705+00:00
---

# rtk-participant-setup · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-setup/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-participant-setup



# rtk-participant-setup

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-setup/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isPreview` | `boolean` | ✅ | - | Whether tile is used for preview  
`nameTagPosition` | `| 'bottom-left' | 'bottom-right' | 'bottom-center' | 'top-left' | 'top-right' | 'top-center'` | ✅ | - | Position of name tag  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'gradient'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-participant-setup></rtk-participant-setup>

### With Properties
    
    
    <!-- component.html -->
    <rtk-participant-setup
     [isPreview]="true"
     [nameTagPosition]="| 'bottom-left'
        | 'bottom-right'
        | 'bottom-center'
        | 'top-left'
        | 'top-right'
        | 'top-center'"
     [participant]="participant">
    </rtk-participant-setup>

[Previousrtk-participant-count](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-count/)[Nextrtk-participant-tile](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-tile/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-setup.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
