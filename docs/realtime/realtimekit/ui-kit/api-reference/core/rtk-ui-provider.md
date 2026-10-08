---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ui-provider/
title: rtk-ui-provider \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:55.844090+00:00
---

# rtk-ui-provider · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ui-provider/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-ui-provider



# rtk-ui-provider

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ui-provider/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ✅ | - | Config  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting | null` | ❌ | `null` | Meeting  
`mode` | `MeetingMode1` | ✅ | - | Fill type  
`overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Kit Overrides  
`showSetupScreen` | `boolean` | ✅ | - | Whether to show setup screen or not  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language utility  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-ui-provider></rtk-ui-provider>

### With Properties
    
    
    <rtk-ui-provider>
    </rtk-ui-provider>
    
    
    <script>
      const el = document.querySelector("rtk-ui-provider");
    
      el.config= defaultUiConfig
      el.mode= meeting
      el.showSetupScreen= true;
    </script>

[Previousrtk-transcripts](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcripts/)[Nextrtk-viewer-count](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-viewer-count/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-ui-provider.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
