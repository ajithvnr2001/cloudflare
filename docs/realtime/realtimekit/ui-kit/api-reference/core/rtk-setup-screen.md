---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-setup-screen/
title: rtk-setup-screen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:52.919357+00:00
---

# rtk-setup-screen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-setup-screen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-setup-screen



# rtk-setup-screen

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-setup-screen/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A screen shown before joining the meeting, where you can edit your display name, and media settings.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-setup-screen></rtk-setup-screen>

### With Properties
    
    
    <rtk-setup-screen
     size="md">
    </rtk-setup-screen>
    
    
    <script>
      const el = document.querySelector("rtk-setup-screen");
    
      el.meeting= meeting
    </script>

[Previousrtk-settings-video](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-video/)[Nextrtk-sidebar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-sidebar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-setup-screen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
