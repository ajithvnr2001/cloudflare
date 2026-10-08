---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/
title: RtkScreenshareView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:27.190703+00:00
---

# RtkScreenshareView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkScreenshareView



# RtkScreenshareView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which plays a participant's screenshared video. It also allows for placement of other components similar to `rtk-participant-tile`. This component will not render anything if the participant hasn't start screensharing.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`hideFullScreenButton` | `boolean` | ✅ | - | Hide full screen button  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`nameTagPosition` | `| 'bottom-left' | 'bottom-right' | 'bottom-center' | 'top-left' | 'top-right' | 'top-center'` | ✅ | - | Position of name tag  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'gradient'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkScreenshareView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkScreenshareView />;
    }

### With Properties
    
    
    import { RtkScreenshareView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkScreenshareView
          hideFullScreenButton={true}
          meeting={meeting}
          nameTagPosition={| 'bottom-left'
        | 'bottom-right'
        | 'bottom-center'
        | 'top-left'
        | 'top-right'
        | 'top-center'}
        />
      );
    }

[PreviousRtkScreenShareToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/)[NextRtkSettings](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkScreenshareView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
