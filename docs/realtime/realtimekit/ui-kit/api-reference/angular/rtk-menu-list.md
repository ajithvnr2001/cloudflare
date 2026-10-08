---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-list/
title: rtk-menu-list \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:26.793616+00:00
---

# rtk-menu-list · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-menu-list



# rtk-menu-list

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A menu list component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`menuVariant` | `'primary' | 'secondary'` | ✅ | - | Variant  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-menu-list></rtk-menu-list>

### With Properties
    
    
    <!-- component.html -->
    <rtk-menu-list
     [menuVariant]="'primary' | 'secondary'">
    </rtk-menu-list>

[Previousrtk-menu-item](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-item/)[Nextrtk-message-list-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-message-list-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
