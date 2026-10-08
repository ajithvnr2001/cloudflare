---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkjoinstage/
title: RtkJoinStage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:20.271488+00:00
---

# RtkJoinStage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkjoinstage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkJoinStage



# RtkJoinStage

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkjoinstage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`dataConfig` | `ModalDataConfig` | ✅ | - | Content Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkJoinStage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkJoinStage />;
    }

### With Properties
    
    
    import { RtkJoinStage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkJoinStage
          dataConfig={modaldataconfig}
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkInformationTooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/)[NextRtkLeaveButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkJoinStage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
