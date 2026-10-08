---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-item/
title: rtk-menu-item \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:26.671943+00:00
---

# rtk-menu-item · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-item/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-menu-item



# rtk-menu-item

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-item/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A menu item component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`menuVariant` | `'primary' | 'secondary'` | ✅ | - | Variant  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-menu-item></rtk-menu-item>

### With Properties
    
    
    <!-- component.html -->
    <rtk-menu-item
     [menuVariant]="'primary' | 'secondary'"
     size="md">
    </rtk-menu-item>

[Previousrtk-menu](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu/)[Nextrtk-menu-list](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-list/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-item.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
