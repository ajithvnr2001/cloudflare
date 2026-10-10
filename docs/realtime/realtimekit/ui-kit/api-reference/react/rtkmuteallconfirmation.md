---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/
title: RtkMuteAllConfirmation \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:41.741569+00:00
---

# RtkMuteAllConfirmation · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMuteAllConfirmation



# RtkMuteAllConfirmation

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMuteAllConfirmation } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMuteAllConfirmation />;
    }

### With Properties
    
    
    import { RtkMuteAllConfirmation } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMuteAllConfirmation
          meeting={meeting}
        />
      );
    }

[PreviousRtkMuteAllButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/)[NextRtkNameTag](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknametag/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMuteAllConfirmation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
