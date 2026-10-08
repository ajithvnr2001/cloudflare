---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-tile/
title: rtk-audio-tile \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:37.059357+00:00
---

# rtk-audio-tile · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-tile/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-audio-tile



# rtk-audio-tile

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-tile/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    <rtk-audio-tile></rtk-audio-tile>

### With Properties
    
    
    <rtk-audio-tile>
    </rtk-audio-tile>
    
    
    <script>
      const el = document.querySelector("rtk-audio-tile");
    
      el.config= defaultUiConfig
      el.meeting= meeting
      el.participant= participant
    </script>

[Previousrtk-audio-grid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-grid/)[Nextrtk-audio-visualizer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-visualizer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-tile.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
