---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-picker-button/
title: rtk-file-picker-button \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:43.121763+00:00
---

# rtk-file-picker-button · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-picker-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-file-picker-button



# rtk-file-picker-button

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-picker-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`filter` | `string` | ✅ | - | File type filter to open file picker with  
`icon` | `keyof IconPack1` | ✅ | - | Icon  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`label` | `string` | ✅ | - | Label for tooltip  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-file-picker-button></rtk-file-picker-button>

### With Properties
    
    
    <rtk-file-picker-button
     filter="example"
     label="example">
    </rtk-file-picker-button>
    
    
    <script>
      const el = document.querySelector("rtk-file-picker-button");
    
      el.icon= defaultIconPack
    </script>

[Previousrtk-file-message-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message-view/)[Nextrtk-fullscreen-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-fullscreen-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-picker-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
