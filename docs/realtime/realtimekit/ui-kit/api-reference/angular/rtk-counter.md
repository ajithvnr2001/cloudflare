---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-counter/
title: rtk-counter \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:21.964677+00:00
---

# rtk-counter · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-counter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-counter



# rtk-counter

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-counter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    <!-- component.html -->
    <rtk-counter></rtk-counter>

### With Properties
    
    
    <!-- component.html -->
    <rtk-counter
     minValue="42"
     size="md"
     value="42">
    </rtk-counter>

[Previousrtk-controlbar-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar-button/)[Nextrtk-debugger](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-counter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
