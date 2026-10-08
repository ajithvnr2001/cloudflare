---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid/
title: rtk-grid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:43.476110+00:00
---

# rtk-grid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-grid



# rtk-grid

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

The main grid component which abstracts all the grid handling logic and renders it for you.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`aspectRatio` | `string` | ✅ | - | The aspect ratio of each participant  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`gap` | `number` | ✅ | - | Gap between participants  
`gridSize` | `GridSize` | ✅ | - | Grid size  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`layout` | `GridLayout` | ✅ | - | Grid Layout  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`overrides` | `any` | ✅ | - | @deprecated  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-grid></rtk-grid>

### With Properties
    
    
    <rtk-grid
     aspectRatio="example"
     gridSize="md">
    </rtk-grid>
    
    
    <script>
      const el = document.querySelector("rtk-grid");
    
      el.gap= 42;
    </script>

[Previousrtk-fullscreen-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle/)[Nextrtk-grid-pagination](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid-pagination/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
