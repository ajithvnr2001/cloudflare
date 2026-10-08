---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-tile/
title: rtk-participant-tile \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:29.283610+00:00
---

# rtk-participant-tile · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-tile/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-participant-tile



# rtk-participant-tile

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-tile/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which plays a participants video and allows for placement of components like `rtk-name-tag`, `rtk-audio-visualizer` or any other component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isPreview` | `boolean` | ✅ | - | Whether tile is used for preview  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`nameTagPosition` | `| 'bottom-left' | 'bottom-right' | 'bottom-center' | 'top-left' | 'top-right' | 'top-center'` | ✅ | - | Position of name tag  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'gradient'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-participant-tile></rtk-participant-tile>

### With Properties
    
    
    <!-- component.html -->
    <rtk-participant-tile
     [isPreview]="true"
     [meeting]="meeting"
     [nameTagPosition]="| 'bottom-left'
        | 'bottom-right'
        | 'bottom-center'
        | 'top-left'
        | 'top-right'
        | 'top-center'">
    </rtk-participant-tile>

[Previousrtk-participant-setup](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-setup/)[Nextrtk-participants](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant-tile.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
