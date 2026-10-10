---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/
title: RtkAi \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:48.999452+00:00
---

# RtkAi · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkAi



# RtkAi

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`view` | `AIView` | ✅ | - | View type  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAi } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkAi />;
    }

### With Properties
    
    
    import { RtkAi } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkAi
          meeting={meeting}
          size="md"
          view={aiview}
        />
      );
    }

[PreviousRtkWaitListParticipantUpdateEventListener](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/)[NextRtkAiToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkAi.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
