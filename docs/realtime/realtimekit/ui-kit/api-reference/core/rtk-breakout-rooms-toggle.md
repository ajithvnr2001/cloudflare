---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-toggle/
title: rtk-breakout-rooms-toggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:37.963050+00:00
---

# rtk-breakout-rooms-toggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-breakout-rooms-toggle



# rtk-breakout-rooms-toggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-toggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles visibility of breakout rooms. You need to pass the `meeting` object to it.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ✅ | - | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ✅ | - | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-breakout-rooms-toggle></rtk-breakout-rooms-toggle>

### With Properties
    
    
    <rtk-breakout-rooms-toggle
     size="md">
    </rtk-breakout-rooms-toggle>
    
    
    <script>
      const el = document.querySelector("rtk-breakout-rooms-toggle");
    
      el.iconPack= defaultIconPack
      el.meeting= meeting
    </script>

[Previousrtk-breakout-rooms-manager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-manager/)[Nextrtk-broadcast-message-modal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-broadcast-message-modal/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
