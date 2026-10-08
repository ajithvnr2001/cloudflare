---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spotlight-grid/
title: rtk-spotlight-grid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:53.471895+00:00
---

# rtk-spotlight-grid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spotlight-grid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-spotlight-grid



# rtk-spotlight-grid

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spotlight-grid/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A grid component that renders two lists of participants: `pinnedParticipants` and `participants`. You can customize the layout to a `column` view, by default is `row`.

  * Participants from `pinnedParticipants[]` are rendered inside a larger grid.
  * Participants from `participants[]` array are rendered in a smaller grid.



## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`aspectRatio` | `string` | ✅ | - | Aspect Ratio of participant tile Format: `width:height`  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`gap` | `number` | ✅ | - | Gap between participant tiles  
`gridSize` | `GridSize1` | ✅ | - | Grid size  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack  
`layout` | `GridLayout1` | ✅ | - | Grid Layout  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`participants` | `Peer[]` | ✅ | - | Participants  
`pinnedParticipants` | `Peer[]` | ✅ | - | Pinned Participants  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-spotlight-grid></rtk-spotlight-grid>

### With Properties
    
    
    <rtk-spotlight-grid
     aspectRatio="example"
     gridSize="md">
    </rtk-spotlight-grid>
    
    
    <script>
      const el = document.querySelector("rtk-spotlight-grid");
    
      el.gap= 42;
    </script>

[Previousrtk-spinner](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spinner/)[Nextrtk-spotlight-indicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spotlight-indicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-spotlight-grid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
