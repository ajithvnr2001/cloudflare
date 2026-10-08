---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar/
title: rtk-controlbar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:21.524814+00:00
---

# rtk-controlbar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-controlbar



# rtk-controlbar

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Controlbar component provides you with various designs as variants.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`disableRender` | `boolean` | ✅ | - | Whether to render the default UI  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'boxed'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-controlbar></rtk-controlbar>

### With Properties
    
    
    <!-- component.html -->
    <rtk-controlbar
     [disableRender]="true"
     [meeting]="meeting"
     size="md">
    </rtk-controlbar>

[Previousrtk-confirmation-modal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-confirmation-modal/)[Nextrtk-controlbar-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
