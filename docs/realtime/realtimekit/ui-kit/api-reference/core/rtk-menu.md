---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu/
title: rtk-menu \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:46.683276+00:00
---

# rtk-menu · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-menu



# rtk-menu

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A menu component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`offset` | `number` | ✅ | - | Offset in px  
`placement` | `Placement` | ✅ | - | Placement of menu  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-menu></rtk-menu>

### With Properties
    
    
    <rtk-menu
     size="md">
    </rtk-menu>
    
    
    <script>
      const el = document.querySelector("rtk-menu");
    
      el.offset= 42;
    </script>

[Previousrtk-meeting-title](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-meeting-title/)[Nextrtk-menu-item](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu-item/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
