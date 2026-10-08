---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/
title: RtkDebugger \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:16.902991+00:00
---

# RtkDebugger · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkDebugger



# RtkDebugger

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A troubleshooting component to identify and fix any issues in the meeting.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkDebugger } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkDebugger />;
    }

### With Properties
    
    
    import { RtkDebugger } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkDebugger
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkCounter](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/)[NextRtkDebuggerAudio](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggeraudio/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkDebugger.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
