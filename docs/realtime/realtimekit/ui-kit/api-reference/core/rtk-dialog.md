---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog/
title: rtk-dialog \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:41.961025+00:00
---

# rtk-dialog · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-dialog



# rtk-dialog

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A dialog component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`disableEscapeKey` | `boolean` | ✅ | - | Whether Escape key can close the modal  
`hideCloseButton` | `boolean` | ✅ | - | Whether to show the close button  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`open` | `boolean` | ✅ | - | Whether a dialog is open or not  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-dialog></rtk-dialog>

### With Properties
    
    
    <rtk-dialog>
    </rtk-dialog>
    
    
    <script>
      const el = document.querySelector("rtk-dialog");
    
      el.disableEscapeKey= true;
      el.hideCloseButton= true;
      el.meeting= meeting
    </script>

[Previousrtk-debugger-video](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-video/)[Nextrtk-dialog-manager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog-manager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
