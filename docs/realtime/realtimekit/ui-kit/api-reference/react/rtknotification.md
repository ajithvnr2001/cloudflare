---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotification/
title: RtkNotification \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:41.396761+00:00
---

# RtkNotification · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotification/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkNotification



# RtkNotification

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows a notification. You need to remove the element after you receive the `rtkNotificationDismiss` event.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`notification` | `Notification` | ✅ | - | Message  
`paused` | `boolean` | ✅ | - | Stops timeout when true  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkNotification } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkNotification />;
    }

### With Properties
    
    
    import { RtkNotification } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkNotification
          notification={notification}
          paused={true}
          size="md"
        />
      );
    }

[PreviousRtkNetworkIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknetworkindicator/)[NextRtkNotifications](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkNotification.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
