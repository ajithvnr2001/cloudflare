---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message-view/
title: rtk-image-message-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:46.254725+00:00
---

# rtk-image-message-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-image-message-view



# rtk-image-message-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders an image message.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`url` | `string` | ✅ | - | Url of the image  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-image-message-view></rtk-image-message-view>

### With Properties
    
    
    <rtk-image-message-view
     url="example">
    </rtk-image-message-view>
    
    
    <script>
      const el = document.querySelector("rtk-image-message-view");
    
    </script>

[Previousrtk-image-message](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message/)[Nextrtk-image-viewer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-viewer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
