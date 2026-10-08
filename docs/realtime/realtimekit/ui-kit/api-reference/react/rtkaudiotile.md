---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/
title: RtkAudioTile \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:12.963981+00:00
---

# RtkAudioTile · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkAudioTile



# RtkAudioTile

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ✅ | - | Config  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAudioTile } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkAudioTile />;
    }

### With Properties
    
    
    import { RtkAudioTile } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkAudioTile
          config={defaultUiConfig}
          meeting={meeting}
          participant={participant}
        />
      );
    }

[PreviousRtkAudioGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiogrid/)[NextRtkAudioVisualizer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkAudioTile.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
