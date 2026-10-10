---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknotification/
title: RtkNotification \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:52.108699+00:00
---

# RtkNotification · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknotification/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkNotification



# RtkNotification

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A single notification toast with slide-in/slide-out animation, avatar, message text, and dismiss button.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`notification` | `Notification` | ✅ | - | Notification object with id, message, image, duration, and button  
`onRtkNotificationDismiss` | `any` | ❌ | - | Callback when notification is dismissed  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkNotification } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkNotification notification={notification} />;
    }

### With Properties
    
    
    import { RtkNotification } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkNotification
    			notification={notification}
    			onRtkNotificationDismiss={(id) => handleDismiss(id)}
    			size="md"
    		/>
    	);
    }

[PreviousRtkNameTag](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknametag/)[NextRtkNotifications](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknotifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkNotification.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
