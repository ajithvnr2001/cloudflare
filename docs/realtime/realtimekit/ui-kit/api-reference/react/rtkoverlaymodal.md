---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkoverlaymodal/
title: RtkOverlayModal \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:41.456243+00:00
---

# RtkOverlayModal · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkoverlaymodal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkOverlayModal



# RtkOverlayModal

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A confirmation modal.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkOverlayModal } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkOverlayModal />;
    }

### With Properties
    
    
    import { RtkOverlayModal } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkOverlayModal
          meeting={meeting}
        />
      );
    }

[PreviousRtkNotifications](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/)[NextRtkPaginatedList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpaginatedlist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkOverlayModal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
