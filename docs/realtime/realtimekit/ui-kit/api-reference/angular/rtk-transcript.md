---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/
title: rtk-transcript \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:35.426219+00:00
---

# rtk-transcript · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-transcript



# rtk-transcript

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows a transcript. You need to remove the element after you receive the `rtkTranscriptDismiss` event.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`transcript` | `Transcript & { renderedId?: string }` | ❌ | - | Message  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-transcript></rtk-transcript>

### With Properties
    
    
    <!-- component.html -->
    <rtk-transcript
     [t]="rtki18n"
     transcript="example">
    </rtk-transcript>

[Previousrtk-tooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tooltip/)[Nextrtk-transcripts](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcripts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
