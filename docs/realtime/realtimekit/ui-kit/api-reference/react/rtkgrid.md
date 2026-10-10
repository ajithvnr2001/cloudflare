---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/
title: RtkGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:44.180541+00:00
---

# RtkGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkGrid



# RtkGrid

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    import { RtkGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkGrid />;
    }

### With Properties
    
    
    import { RtkGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkGrid
          aspectRatio="example"
          gap={42}
          gridSize="md"
        />
      );
    }

[PreviousRtkFullscreenToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/)[NextRtkGridPagination](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
