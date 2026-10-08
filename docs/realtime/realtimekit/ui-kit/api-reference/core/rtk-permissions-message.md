---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-permissions-message/
title: rtk-permissions-message \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:49.902622+00:00
---

# rtk-permissions-message · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-permissions-message/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-permissions-message



# rtk-permissions-message

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-permissions-message/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows permission related troubleshooting information.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-permissions-message></rtk-permissions-message>

### With Properties
    
    
    <rtk-permissions-message>
    </rtk-permissions-message>
    
    
    <script>
      const el = document.querySelector("rtk-permissions-message");
    
      el.meeting= meeting
    </script>

[Previousrtk-participants-waiting-list](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-waiting-list/)[Nextrtk-pinned-message-selector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-pinned-message-selector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-permissions-message.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
