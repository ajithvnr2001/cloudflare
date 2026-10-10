---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmixedgrid/
title: RtkMixedGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:42.000718+00:00
---

# RtkMixedGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmixedgrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMixedGrid



# RtkMixedGrid

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    import { RtkMixedGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMixedGrid />;
    }

### With Properties
    
    
    import { RtkMixedGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMixedGrid
          aspectRatio="example"
          gap={42}
          gridSize="md"
        />
      );
    }

[PreviousRtkMicToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmictoggle/)[NextRtkMoreToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmoretoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMixedGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
