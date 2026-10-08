---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/
title: RtkChatSelector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:15.643346+00:00
---

# RtkChatSelector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChatSelector



# RtkChatSelector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Overrides  
`size` | `Size` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkChatSelector } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChatSelector />;
    }

### With Properties
    
    
    import { RtkChatSelector } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChatSelector
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkChatSearchResults](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/)[NextRtkChatSelectorUi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChatSelector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
