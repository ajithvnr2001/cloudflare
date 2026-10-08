---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-switch/
title: rtk-switch \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:34.770683+00:00
---

# rtk-switch · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-switch/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-switch



# rtk-switch

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-switch/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A switch component which follows RTK Design System.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`checked` | `boolean` | ✅ | - | Whether the switch is enabled/checked  
`disabled` | `boolean` | ✅ | - | Whether switch is readonly  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`readonly` | `boolean` | ✅ | - | Whether switch is readonly  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-switch></rtk-switch>

### With Properties
    
    
    <!-- component.html -->
    <rtk-switch
     [checked]="true"
     [disabled]="true"
     [readonly]="true">
    </rtk-switch>

[Previousrtk-stage-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-stage-toggle/)[Nextrtk-tab-bar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tab-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-switch.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
