---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/
title: RtkScreenshareView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:10.201398+00:00
---

# RtkScreenshareView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkScreenshareView



# RtkScreenshareView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Renders a participant's screen share with fullscreen toggle, name tag, and audio indicator.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`participant` | `RTKParticipant` | ✅ | - | The participant sharing their screen  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`hideFullScreenButton` | `boolean` | ❌ | `false` | Hide the fullscreen toggle button  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`nameTagPosition` | `'bottom-center' | 'bottom-left' | 'bottom-right' | 'top-center' | 'top-left' | 'top-right'` | ❌ | `'bottom-left'` | Position of the name tag overlay  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`variant` | `'gradient' | 'solid'` | ❌ | `'solid'` | Visual style variant  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkScreenshareView } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkScreenshareView participant={participant} meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkScreenshareView } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkScreenshareView
    			participant={participant}
    			meeting={meeting}
    			nameTagPosition="bottom-left"
    			variant="solid"
    			size="md"
    		/>
    	);
    }

[PreviousRtkScreenShareToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreensharetoggle/)[NextRtkSettings](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkScreenshareView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
