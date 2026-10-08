---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/
title: rtk-switch \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:54.177749+00:00
---

# rtk-switch · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-switch



# rtk-switch

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A switch component which follows RTK Design System.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`checked` | `boolean` | ✅ | - | Whether the switch is enabled/checked  
`disabled` | `boolean` | ✅ | - | Whether switch is readonly  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`readonly` | `boolean` | ✅ | - | Whether switch is readonly  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-switch></rtk-switch>

### With Properties
    
    
    <rtk-switch>
    </rtk-switch>
    
    
    <script>
      const el = document.querySelector("rtk-switch");
    
      el.checked= true;
      el.disabled= true;
      el.readonly= true;
    </script>

[Previousrtk-stage-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-stage-toggle/)[Nextrtk-tab-bar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tab-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
