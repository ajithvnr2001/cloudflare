---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript/
title: rtk-transcript \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:55.116113+00:00
---

# rtk-transcript · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-transcript



# rtk-transcript

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows a transcript. You need to remove the element after you receive the `rtkTranscriptDismiss` event.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`transcript` | `Transcript & { renderedId?: string }` | ❌ | - | Message  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-transcript></rtk-transcript>

### With Properties
    
    
    <rtk-transcript
     transcript="example">
    </rtk-transcript>
    
    
    <script>
      const el = document.querySelector("rtk-transcript");
    
      el.transcript= {};
    </script>

[Previousrtk-tooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/)[Nextrtk-transcripts](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcripts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
