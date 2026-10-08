---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-network-indicator/
title: rtk-network-indicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:28.308149+00:00
---

# rtk-network-indicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-network-indicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-network-indicator



# rtk-network-indicator

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-network-indicator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`isScreenShare` | `boolean` | ✅ | - | Is for screenshare  
`meeting` | `Meeting` | ✅ | - | Meeting  
`participant` | `Peer` | ✅ | - | Participant or Self  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-network-indicator></rtk-network-indicator>

### With Properties
    
    
    <!-- component.html -->
    <rtk-network-indicator
     [isScreenShare]="true"
     [meeting]="meeting"
     [participant]="participant">
    </rtk-network-indicator>

[Previousrtk-name-tag](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-name-tag/)[Nextrtk-notification](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-notification/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-network-indicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
