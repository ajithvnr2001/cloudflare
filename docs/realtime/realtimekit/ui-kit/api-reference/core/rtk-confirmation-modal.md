---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-confirmation-modal/
title: rtk-confirmation-modal \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:40.670789+00:00
---

# rtk-confirmation-modal · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-confirmation-modal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-confirmation-modal



# rtk-confirmation-modal

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-confirmation-modal/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A confirmation modal.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-confirmation-modal></rtk-confirmation-modal>

### With Properties
    
    
    <rtk-confirmation-modal>
    </rtk-confirmation-modal>
    
    
    <script>
      const el = document.querySelector("rtk-confirmation-modal");
    
      el.meeting= meeting
    </script>

[Previousrtk-clock](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-clock/)[Nextrtk-controlbar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-confirmation-modal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
