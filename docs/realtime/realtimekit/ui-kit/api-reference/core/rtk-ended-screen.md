---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/
title: rtk-ended-screen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:42.575477+00:00
---

# rtk-ended-screen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-ended-screen



# rtk-ended-screen

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A screen which shows a meeting has ended.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Global states  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | Global states  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-ended-screen></rtk-ended-screen>

### With Properties
    
    
    <rtk-ended-screen
     size="md">
    </rtk-ended-screen>
    
    
    <script>
      const el = document.querySelector("rtk-ended-screen");
    
      el.meeting= meeting
    </script>

[Previousrtk-emoji-picker-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker-button/)[Nextrtk-file-dropzone](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-dropzone/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
