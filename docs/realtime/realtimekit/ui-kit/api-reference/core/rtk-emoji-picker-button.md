---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker-button/
title: rtk-emoji-picker-button \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:42.472426+00:00
---

# rtk-emoji-picker-button · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-emoji-picker-button



# rtk-emoji-picker-button

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`isActive` | `boolean` | ✅ | - | Active state indicator  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-emoji-picker-button></rtk-emoji-picker-button>

### With Properties
    
    
    <rtk-emoji-picker-button>
    </rtk-emoji-picker-button>
    
    
    <script>
      const el = document.querySelector("rtk-emoji-picker-button");
    
      el.isActive= true;
    </script>

[Previousrtk-emoji-picker](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/)[Nextrtk-ended-screen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
