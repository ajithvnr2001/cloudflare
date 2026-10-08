---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/
title: RtkAudioVisualizer \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:13.057339+00:00
---

# RtkAudioVisualizer · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkAudioVisualizer



# RtkAudioVisualizer

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

An audio visualizer component which visualizes a participants audio. Commonly used inside `rtk-name-tag`.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`hideMuted` | `boolean` | ✅ | - | Hide the visualizer if audio is muted  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isScreenShare` | `boolean` | ✅ | - | Audio visualizer for screensharing, it will use screenShareTracks.audio instead of audioTrack  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `AudioVisualizerVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAudioVisualizer } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkAudioVisualizer />;
    }

### With Properties
    
    
    import { RtkAudioVisualizer } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkAudioVisualizer
          hideMuted={true}
          isScreenShare={true}
          participant={participant}
        />
      );
    }

[PreviousRtkAudioTile](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/)[NextRtkAvatar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkavatar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkAudioVisualizer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
