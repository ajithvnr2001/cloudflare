---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggeraudio/
title: RtkDebuggerAudio \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:46.172493+00:00
---

# RtkDebuggerAudio · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggeraudio/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkDebuggerAudio



# RtkDebuggerAudio

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States object  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkDebuggerAudio } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkDebuggerAudio />;
    }

### With Properties
    
    
    import { RtkDebuggerAudio } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkDebuggerAudio
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkDebugger](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/)[NextRtkDebuggerScreenshare](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggerscreenshare/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkDebuggerAudio.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
