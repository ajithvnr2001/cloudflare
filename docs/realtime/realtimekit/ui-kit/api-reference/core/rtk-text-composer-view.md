---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-composer-view/
title: rtk-text-composer-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:54.641247+00:00
---

# rtk-text-composer-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-composer-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-text-composer-view



# rtk-text-composer-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-composer-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders a text composer

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`disabled` | `boolean` | ✅ | - | Disable the text input (default = false)  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`keyDownHandler` | `(e: KeyboardEvent)` | ✅ | - | Keydown event handler function  
`maxLength` | `number` | ✅ | - | Max length for text input  
`placeholder` | `string` | ✅ | - | Placeholder text  
`rateLimitBreached` | `boolean` | ✅ | - | Boolean to indicate if rate limit is breached  
`setText` | `(text: string, focus?: boolean)` | ❌ | - | Sets value of the text input  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`value` | `string` | ✅ | - | Default value for text input  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-text-composer-view></rtk-text-composer-view>

### With Properties
    
    
    <rtk-text-composer-view>
    </rtk-text-composer-view>
    
    
    <script>
      const el = document.querySelector("rtk-text-composer-view");
    
      el.disabled= true;
      el.maxLength= 42;
    </script>

[Previousrtk-tab-bar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tab-bar/)[Nextrtk-text-message](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-message/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-composer-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
