---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mixed-grid/
title: rtk-mixed-grid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:46.973382+00:00
---

# rtk-mixed-grid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mixed-grid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-mixed-grid



# rtk-mixed-grid

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mixed-grid/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A grid component which handles screenshares, plugins and participants.

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
`plugins` | `RTKPlugin[]` | ✅ | - | Active Plugins  
`screenShareParticipants` | `Peer[]` | ✅ | - | Screenshare Participants  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-mixed-grid></rtk-mixed-grid>

### With Properties
    
    
    <rtk-mixed-grid
     aspectRatio="example"
     gridSize="md">
    </rtk-mixed-grid>
    
    
    <script>
      const el = document.querySelector("rtk-mixed-grid");
    
      el.gap= 42;
    </script>

[Previousrtk-microphone-selector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-microphone-selector/)[Nextrtk-more-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-more-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-mixed-grid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
