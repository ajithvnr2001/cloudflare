---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-room-manager/
title: rtk-breakout-room-manager \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:18.221969+00:00
---

# rtk-breakout-room-manager · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-room-manager/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-breakout-room-manager



# rtk-breakout-room-manager

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-room-manager/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`allowDelete` | `boolean` | ✅ | - | allow room delete  
`assigningParticipants` | `boolean` | ✅ | - | Enable updating participants  
`defaultExpanded` | `boolean` | ✅ | - | display expanded card by default  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isDragMode` | `boolean` | ✅ | - | Drag mode  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`mode` | `'edit' | 'create'` | ✅ | - | Mode in which selector is used  
`room` | `DraftMeeting` | ✅ | - | Connected Room Config Object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-breakout-room-manager></rtk-breakout-room-manager>

### With Properties
    
    
    <!-- component.html -->
    <rtk-breakout-room-manager
     [allowDelete]="true"
     [assigningParticipants]="true"
     [defaultExpanded]="true">
    </rtk-breakout-room-manager>

[Previousrtk-avatar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-avatar/)[Nextrtk-breakout-room-participants](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-room-participants/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-room-manager.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
