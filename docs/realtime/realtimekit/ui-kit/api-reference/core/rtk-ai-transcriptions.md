---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions/
title: rtk-ai-transcriptions \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:36.730159+00:00
---

# rtk-ai-transcriptions · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-ai-transcriptions



# rtk-ai-transcriptions

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`initialTranscriptions` | `Transcript[]` | ✅ | - | Initial transcriptions  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-ai-transcriptions></rtk-ai-transcriptions>

### With Properties
    
    
    <rtk-ai-transcriptions>
    </rtk-ai-transcriptions>
    
    
    <script>
      const el = document.querySelector("rtk-ai-transcriptions");
    
      el.initialTranscriptions= [];
      el.meeting= meeting
    </script>

[Previousrtk-ai-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-toggle/)[Nextrtk-audio-grid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-grid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
