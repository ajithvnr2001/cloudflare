---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/
title: RtkBroadcastMessageModal \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:13.888491+00:00
---

# RtkBroadcastMessageModal · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkBroadcastMessageModal



# RtkBroadcastMessageModal

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States1` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkBroadcastMessageModal } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkBroadcastMessageModal />;
    }

### With Properties
    
    
    import { RtkBroadcastMessageModal } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkBroadcastMessageModal
          meeting={meeting}
        />
      );
    }

[PreviousRtkBreakoutRoomsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomstoggle/)[NextRtkButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkBroadcastMessageModal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
