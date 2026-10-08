---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-notification/
title: rtk-notification \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:47.918038+00:00
---

# rtk-notification · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-notification/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-notification



# rtk-notification

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-notification/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows a notification. You need to remove the element after you receive the `rtkNotificationDismiss` event.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`notification` | `Notification` | ✅ | - | Message  
`paused` | `boolean` | ✅ | - | Stops timeout when true  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-notification></rtk-notification>

### With Properties
    
    
    <rtk-notification
     size="md">
    </rtk-notification>
    
    
    <script>
      const el = document.querySelector("rtk-notification");
    
      el.paused= true;
    </script>

[Previousrtk-network-indicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-network-indicator/)[Nextrtk-notifications](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-notifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-notification.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
