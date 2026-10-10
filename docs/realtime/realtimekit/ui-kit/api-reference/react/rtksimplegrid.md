---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksimplegrid/
title: RtkSimpleGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:38.086855+00:00
---

# RtkSimpleGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksimplegrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSimpleGrid



# RtkSimpleGrid

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    import { RtkSimpleGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSimpleGrid />;
    }

### With Properties
    
    
    import { RtkSimpleGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSimpleGrid
          aspectRatio="example"
          gap={42}
          meeting={meeting}
        />
      );
    }

[PreviousRtkSidebarUi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebarui/)[NextRtkSpeakerSelector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspeakerselector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSimpleGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
