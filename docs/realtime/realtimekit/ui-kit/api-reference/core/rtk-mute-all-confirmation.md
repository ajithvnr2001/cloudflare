---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-confirmation/
title: rtk-mute-all-confirmation \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:47.185803+00:00
---

# rtk-mute-all-confirmation · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-confirmation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-mute-all-confirmation



# rtk-mute-all-confirmation

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-confirmation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-mute-all-confirmation></rtk-mute-all-confirmation>

### With Properties
    
    
    <rtk-mute-all-confirmation>
    </rtk-mute-all-confirmation>
    
    
    <script>
      const el = document.querySelector("rtk-mute-all-confirmation");
    
      el.meeting= meeting
    </script>

[Previousrtk-mute-all-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-button/)[Nextrtk-name-tag](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-name-tag/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-mute-all-confirmation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
