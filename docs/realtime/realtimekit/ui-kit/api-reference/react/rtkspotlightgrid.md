---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightgrid/
title: RtkSpotlightGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:37.888274+00:00
---

# RtkSpotlightGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightgrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSpotlightGrid



# RtkSpotlightGrid

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    import { RtkSpotlightGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSpotlightGrid />;
    }

### With Properties
    
    
    import { RtkSpotlightGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSpotlightGrid
          aspectRatio="example"
          gap={42}
          gridSize="md"
        />
      );
    }

[PreviousRtkSpinner](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/)[NextRtkSpotlightIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightindicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSpotlightGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
