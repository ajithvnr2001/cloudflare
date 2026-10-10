---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknametag/
title: RtkNameTag \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:51.998393+00:00
---

# RtkNameTag · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknametag/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkNameTag



# RtkNameTag

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays a participant's name with optional child content (such as an audio visualizer icon). Used as an overlay on participant tiles.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`participant` | `Peer` | ✅ | - | The participant to display the name for  
`meeting` | `RealtimeKitClient` | ❌ | - | The RealtimeKit meeting instance (used to identify self)  
`isScreenshare` | `boolean` | ❌ | `false` | Whether this is a screenshare name tag  
`maxLength` | `number` | ❌ | `20` | Maximum width offset for the name tag  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Text size  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`children` | `ReactNode` | ❌ | - | Content to render before the name  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkNameTag } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkNameTag participant={participant} />;
    }

### With Properties
    
    
    import { RtkNameTag } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkNameTag
    			participant={participant}
    			meeting={meeting}
    			size="md"
    			maxLength={25}
    		/>
    	);
    }

[PreviousRtkMuteToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmutetoggle/)[NextRtkNotification](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknotification/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkNameTag.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
