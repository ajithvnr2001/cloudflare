---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-toggle/
title: rtk-debugger-toggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:41.838599+00:00
---

# rtk-debugger-toggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-debugger-toggle



# rtk-debugger-toggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-toggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-debugger-toggle></rtk-debugger-toggle>

### With Properties
    
    
    <rtk-debugger-toggle
     size="md"
     variant"button">
    </rtk-debugger-toggle>
    
    
    <script>
      const el = document.querySelector("rtk-debugger-toggle");
    
      el.meeting= meeting
    </script>

[Previousrtk-debugger-system](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-system/)[Nextrtk-debugger-video](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-video/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
