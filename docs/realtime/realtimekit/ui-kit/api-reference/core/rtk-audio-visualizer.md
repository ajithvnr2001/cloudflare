---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-visualizer/
title: rtk-audio-visualizer \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:37.273703+00:00
---

# rtk-audio-visualizer · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-visualizer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-audio-visualizer



# rtk-audio-visualizer

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-visualizer/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    <rtk-audio-visualizer></rtk-audio-visualizer>

### With Properties
    
    
    <rtk-audio-visualizer>
    </rtk-audio-visualizer>
    
    
    <script>
      const el = document.querySelector("rtk-audio-visualizer");
    
      el.hideMuted= true;
      el.isScreenShare= true;
      el.participant= participant
    </script>

[Previousrtk-audio-tile](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-tile/)[Nextrtk-avatar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-visualizer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
