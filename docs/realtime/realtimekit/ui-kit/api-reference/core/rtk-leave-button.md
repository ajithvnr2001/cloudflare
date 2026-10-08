---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-button/
title: rtk-leave-button \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:44.575527+00:00
---

# rtk-leave-button · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-leave-button



# rtk-leave-button

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles visilibility of the leave confirmation dialog.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-leave-button></rtk-leave-button>

### With Properties
    
    
    <rtk-leave-button
     size="md"
     variant"button">
    </rtk-leave-button>
    
    
    <script>
      const el = document.querySelector("rtk-leave-button");
    
    </script>

[Previousrtk-join-stage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-join-stage/)[Nextrtk-leave-meeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-meeting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-leave-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
