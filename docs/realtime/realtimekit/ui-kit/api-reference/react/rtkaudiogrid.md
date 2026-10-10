---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiogrid/
title: RtkAudioGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:48.934019+00:00
---

# RtkAudioGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiogrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkAudioGrid



# RtkAudioGrid

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ✅ | - | Config  
`hideSelf` | `boolean` | ✅ | - | Whether to hide self in the grid  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`size` | `Size1` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAudioGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkAudioGrid />;
    }

### With Properties
    
    
    import { RtkAudioGrid } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkAudioGrid
          config={defaultUiConfig}
          hideSelf={true}
          meeting={meeting}
        />
      );
    }

[PreviousRtkAiTranscriptions](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/)[NextRtkAudioTile](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkAudioGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
