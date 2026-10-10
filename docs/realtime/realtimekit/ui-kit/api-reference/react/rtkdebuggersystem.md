---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggersystem/
title: RtkDebuggerSystem \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:45.691261+00:00
---

# RtkDebuggerSystem · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggersystem/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkDebuggerSystem



# RtkDebuggerSystem

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
    
    
    import { RtkDebuggerSystem } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkDebuggerSystem />;
    }

### With Properties
    
    
    import { RtkDebuggerSystem } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkDebuggerSystem
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkDebuggerScreenshare](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggerscreenshare/)[NextRtkDebuggerToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggertoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkDebuggerSystem.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
