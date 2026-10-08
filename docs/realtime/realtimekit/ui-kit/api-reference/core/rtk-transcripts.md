---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcripts/
title: rtk-transcripts \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:55.215996+00:00
---

# rtk-transcripts · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcripts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-transcripts



# rtk-transcripts

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcripts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which handles transcripts. You can configure which transcripts you want to see and which ones you want to hear. There are also certain limits which you can set as well.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-transcripts></rtk-transcripts>

### With Properties
    
    
    <rtk-transcripts>
    </rtk-transcripts>
    
    
    <script>
      const el = document.querySelector("rtk-transcripts");
    
      el.meeting= meeting
    </script>

[Previousrtk-transcript](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript/)[Nextrtk-ui-provider](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ui-provider/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcripts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
