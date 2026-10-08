---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar/
title: rtk-controlbar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:40.830765+00:00
---

# rtk-controlbar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-controlbar



# rtk-controlbar

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Controlbar component provides you with various designs as variants.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`disableRender` | `boolean` | ✅ | - | Whether to render the default UI  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'boxed'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-controlbar></rtk-controlbar>

### With Properties
    
    
    <rtk-controlbar
     size="md">
    </rtk-controlbar>
    
    
    <script>
      const el = document.querySelector("rtk-controlbar");
    
      el.disableRender= true;
      el.meeting= meeting
    </script>

[Previousrtk-confirmation-modal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-confirmation-modal/)[Nextrtk-controlbar-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
