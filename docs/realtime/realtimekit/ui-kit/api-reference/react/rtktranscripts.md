---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscripts/
title: RtkTranscripts \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:37.087313+00:00
---

# RtkTranscripts · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscripts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkTranscripts



# RtkTranscripts

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    import { RtkTranscripts } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkTranscripts />;
    }

### With Properties
    
    
    import { RtkTranscripts } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkTranscripts
          meeting={meeting}
        />
      );
    }

[PreviousRtkTranscript](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscript/)[NextRtkUiProvider](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkuiprovider/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkTranscripts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
