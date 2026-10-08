---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-selector/
title: rtk-chat-selector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:39.939104+00:00
---

# rtk-chat-selector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-selector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-chat-selector



# rtk-chat-selector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-selector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Overrides  
`size` | `Size` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-chat-selector></rtk-chat-selector>

### With Properties
    
    
    <rtk-chat-selector
     size="md">
    </rtk-chat-selector>
    
    
    <script>
      const el = document.querySelector("rtk-chat-selector");
    
      el.meeting= meeting
    </script>

[Previousrtk-chat-search-results](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results/)[Nextrtk-chat-selector-ui](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-selector-ui/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-selector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
