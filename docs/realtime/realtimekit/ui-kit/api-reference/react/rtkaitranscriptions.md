---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/
title: RtkAiTranscriptions \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:12.745532+00:00
---

# RtkAiTranscriptions · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkAiTranscriptions



# RtkAiTranscriptions

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`initialTranscriptions` | `Transcript[]` | ✅ | - | Initial transcriptions  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAiTranscriptions } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkAiTranscriptions />;
    }

### With Properties
    
    
    import { RtkAiTranscriptions } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkAiTranscriptions
          initialTranscriptions={[]}
          meeting={meeting}
        />
      );
    }

[PreviousRtkAiToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/)[NextRtkAudioGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiogrid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkAiTranscriptions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
