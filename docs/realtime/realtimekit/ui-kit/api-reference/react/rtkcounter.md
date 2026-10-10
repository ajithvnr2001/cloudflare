---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/
title: RtkCounter \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:45.849832+00:00
---

# RtkCounter · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkCounter



# RtkCounter

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A number picker with increment and decrement buttons.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`minValue` | `number` | ✅ | - | Minimum value  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`value` | `number` | ✅ | - | Initial value  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkCounter } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkCounter />;
    }

### With Properties
    
    
    import { RtkCounter } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkCounter
          minValue={42}
          size="md"
          value={42}
        />
      );
    }

[PreviousRtkControlbarButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbarbutton/)[NextRtkDebugger](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkCounter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
