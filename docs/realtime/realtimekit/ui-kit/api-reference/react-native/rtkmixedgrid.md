---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmixedgrid/
title: RtkMixedGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:52.448742+00:00
---

# RtkMixedGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmixedgrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkMixedGrid



# RtkMixedGrid

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A grid layout that handles mixed content: participants, screenshares, plugins, and pinned participants. Automatically switches between simple, spotlight, and highlighted grid layouts.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`participants` | `Peer[]` | ✅ | `[]` | Array of active participants  
`pinnedParticipants` | `Peer[]` | ✅ | `[]` | Array of pinned participants  
`screenShareParticipants` | `Peer[]` | ✅ | `[]` | Array of participants sharing their screen  
`plugins` | `RTKPlugin[]` | ✅ | `[]` | Array of active plugins  
`aspectRatio` | `string` | ❌ | `'16:9'` | Aspect ratio for grid tiles  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`gap` | `number` | ❌ | `8` | Gap between grid tiles in pixels  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`variant` | `'boxed' | 'solid'` | ❌ | `'solid'` | Visual style variant  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMixedGrid } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkMixedGrid
    			meeting={meeting}
    			participants={participants}
    			pinnedParticipants={[]}
    			screenShareParticipants={[]}
    			plugins={[]}
    		/>
    	);
    }

### With Properties
    
    
    import { RtkMixedGrid } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkMixedGrid
    			meeting={meeting}
    			participants={participants}
    			pinnedParticipants={pinned}
    			screenShareParticipants={screenshares}
    			plugins={activePlugins}
    			aspectRatio="16:9"
    			gap={12}
    			size="md"
    		/>
    	);
    }

[PreviousRtkMicToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmictoggle/)[NextRtkMoreToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmoretoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkMixedGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
