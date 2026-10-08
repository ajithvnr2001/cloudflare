---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-name-tag/
title: rtk-name-tag \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:27.892282+00:00
---

# rtk-name-tag · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-name-tag/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-name-tag



# rtk-name-tag

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-name-tag/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows a participant's name.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isScreenShare` | `boolean` | ✅ | - | Whether it is used in a screen share view  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `RtkNameTagVariant` | ✅ | - | Name tag variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-name-tag></rtk-name-tag>

### With Properties
    
    
    <!-- component.html -->
    <rtk-name-tag
     [isScreenShare]="true"
     [meeting]="meeting"
     [participant]="participant">
    </rtk-name-tag>

[Previousrtk-mute-all-confirmation](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mute-all-confirmation/)[Nextrtk-network-indicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-network-indicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-name-tag.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
