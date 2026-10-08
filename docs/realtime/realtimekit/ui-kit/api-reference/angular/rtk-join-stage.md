---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-join-stage/
title: rtk-join-stage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:25.358375+00:00
---

# rtk-join-stage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-join-stage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-join-stage



# rtk-join-stage

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-join-stage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`dataConfig` | `ModalDataConfig` | ✅ | - | Content Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-join-stage></rtk-join-stage>

### With Properties
    
    
    <!-- component.html -->
    <rtk-join-stage
     [dataConfig]="modaldataconfig"
     [meeting]="meeting"
     size="md">
    </rtk-join-stage>

[Previousrtk-information-tooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-information-tooltip/)[Nextrtk-leave-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-leave-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-join-stage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
