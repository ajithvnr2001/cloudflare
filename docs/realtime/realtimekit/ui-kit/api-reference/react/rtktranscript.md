---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscript/
title: RtkTranscript \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:29.935744+00:00
---

# RtkTranscript · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscript/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkTranscript



# RtkTranscript

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscript/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows a transcript. You need to remove the element after you receive the `rtkTranscriptDismiss` event.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`transcript` | `Transcript & { renderedId?: string }` | ❌ | - | Message  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkTranscript } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkTranscript />;
    }

### With Properties
    
    
    import { RtkTranscript } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkTranscript
          t={rtki18n}
          transcript="example"
        />
      );
    }

[PreviousRtkTooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/)[NextRtkTranscripts](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscripts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkTranscript.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
