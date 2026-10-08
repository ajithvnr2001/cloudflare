---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle/
title: rtk-fullscreen-toggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:43.329752+00:00
---

# rtk-fullscreen-toggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-fullscreen-toggle



# rtk-fullscreen-toggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles full screen mode for any existing `rtk-meeting` component in the DOM.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`targetElement` | `HTMLElement` | ✅ | - | Target Element to fullscreen  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-fullscreen-toggle></rtk-fullscreen-toggle>

### With Properties
    
    
    <rtk-fullscreen-toggle
     size="md"
     variant"button">
    </rtk-fullscreen-toggle>
    
    
    <script>
      const el = document.querySelector("rtk-fullscreen-toggle");
    
    </script>

[Previousrtk-file-picker-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-picker-button/)[Nextrtk-grid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
