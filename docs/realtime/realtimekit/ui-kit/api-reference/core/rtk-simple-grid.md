---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-simple-grid/
title: rtk-simple-grid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:53.363326+00:00
---

# rtk-simple-grid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-simple-grid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-simple-grid



# rtk-simple-grid

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-simple-grid/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A grid component which renders only the participants in a simple grid.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`aspectRatio` | `string` | ✅ | - | Aspect Ratio of participant tile Format: `width:height`  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`gap` | `number` | ✅ | - | Gap between participant tiles  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`participants` | `Peer[]` | ✅ | - | Participants  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-simple-grid></rtk-simple-grid>

### With Properties
    
    
    <rtk-simple-grid
     aspectRatio="example">
    </rtk-simple-grid>
    
    
    <script>
      const el = document.querySelector("rtk-simple-grid");
    
      el.gap= 42;
      el.meeting= meeting
    </script>

[Previousrtk-sidebar-ui](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-sidebar-ui/)[Nextrtk-speaker-selector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-speaker-selector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-simple-grid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
