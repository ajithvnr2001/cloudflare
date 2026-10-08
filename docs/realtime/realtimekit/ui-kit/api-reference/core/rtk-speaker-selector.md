---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-speaker-selector/
title: rtk-speaker-selector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:53.264559+00:00
---

# rtk-speaker-selector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-speaker-selector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-speaker-selector



# rtk-speaker-selector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-speaker-selector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lets to manage your audio devices and audio preferences. Emits `rtkStateUpdate` event with data for muting notification sounds:
    
    
    {
     prefs: {
       muteNotificationSounds: boolean
     }
    }

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'full' | 'inline'` | ✅ | - | variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-speaker-selector></rtk-speaker-selector>

### With Properties
    
    
    <rtk-speaker-selector
     size="md">
    </rtk-speaker-selector>
    
    
    <script>
      const el = document.querySelector("rtk-speaker-selector");
    
      el.meeting= meeting
    </script>

[Previousrtk-simple-grid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-simple-grid/)[Nextrtk-spinner](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-spinner/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-speaker-selector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
