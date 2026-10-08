---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-button/
title: rtk-mute-all-button \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:47.671676+00:00
---

# rtk-mute-all-button · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-mute-all-button



# rtk-mute-all-button

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-mute-all-button></rtk-mute-all-button>

### With Properties
    
    
    <rtk-mute-all-button
     size="md"
     variant"button">
    </rtk-mute-all-button>
    
    
    <script>
      const el = document.querySelector("rtk-mute-all-button");
    
      el.meeting= meeting
    </script>

[Previousrtk-more-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-more-toggle/)[Nextrtk-mute-all-confirmation](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-confirmation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
