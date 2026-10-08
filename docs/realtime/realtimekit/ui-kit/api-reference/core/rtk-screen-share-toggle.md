---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screen-share-toggle/
title: rtk-screen-share-toggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:51.745704+00:00
---

# rtk-screen-share-toggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screen-share-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-screen-share-toggle



# rtk-screen-share-toggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screen-share-toggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles your screenshare.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-screen-share-toggle></rtk-screen-share-toggle>

### With Properties
    
    
    <rtk-screen-share-toggle
     size="md"
     variant"button">
    </rtk-screen-share-toggle>
    
    
    <script>
      const el = document.querySelector("rtk-screen-share-toggle");
    
      el.meeting= meeting
    </script>

[Previousrtk-recording-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-recording-toggle/)[Nextrtk-screenshare-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screenshare-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-screen-share-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
