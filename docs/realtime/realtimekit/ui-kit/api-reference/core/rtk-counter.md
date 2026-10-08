---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter/
title: rtk-counter \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:40.953336+00:00
---

# rtk-counter · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-counter



# rtk-counter

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A number picker with increment and decrement buttons.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`minValue` | `number` | ✅ | - | Minimum value  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`value` | `number` | ✅ | - | Initial value  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-counter></rtk-counter>

### With Properties
    
    
    <rtk-counter
     size="md">
    </rtk-counter>
    
    
    <script>
      const el = document.querySelector("rtk-counter");
    
      el.minValue= 42;
      el.value= 42;
    </script>

[Previousrtk-controlbar-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar-button/)[Nextrtk-debugger](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
