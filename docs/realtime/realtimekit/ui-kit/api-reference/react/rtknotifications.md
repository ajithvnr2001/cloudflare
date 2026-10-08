---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/
title: RtkNotifications \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:23.933472+00:00
---

# RtkNotifications · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkNotifications



# RtkNotifications

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which handles notifications. You can configure which notifications you want to see and which ones you want to hear. There are also certain limits which you can set as well.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkNotifications } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkNotifications />;
    }

### With Properties
    
    
    import { RtkNotifications } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkNotifications
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkNotification](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotification/)[NextRtkOverlayModal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkoverlaymodal/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkNotifications.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
