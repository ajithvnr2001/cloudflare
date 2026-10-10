---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknametag/
title: RtkNameTag \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:41.517793+00:00
---

# RtkNameTag · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknametag/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkNameTag



# RtkNameTag

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows a participant's name.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isScreenShare` | `boolean` | ✅ | - | Whether it is used in a screen share view  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `RtkNameTagVariant` | ✅ | - | Name tag variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkNameTag } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkNameTag />;
    }

### With Properties
    
    
    import { RtkNameTag } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkNameTag
          isScreenShare={true}
          meeting={meeting}
          participant={participant}
        />
      );
    }

[PreviousRtkMuteAllConfirmation](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/)[NextRtkNetworkIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknetworkindicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkNameTag.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
