---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-broadcast-message-modal/
title: rtk-broadcast-message-modal \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:38.065432+00:00
---

# rtk-broadcast-message-modal · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-broadcast-message-modal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-broadcast-message-modal



# rtk-broadcast-message-modal

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-broadcast-message-modal/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States1` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-broadcast-message-modal></rtk-broadcast-message-modal>

### With Properties
    
    
    <rtk-broadcast-message-modal>
    </rtk-broadcast-message-modal>
    
    
    <script>
      const el = document.querySelector("rtk-broadcast-message-modal");
    
      el.meeting= meeting
    </script>

[Previousrtk-breakout-rooms-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-toggle/)[Nextrtk-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-broadcast-message-modal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
