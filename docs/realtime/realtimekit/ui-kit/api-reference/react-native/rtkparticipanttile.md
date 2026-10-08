---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttile/
title: RtkParticipantTile \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:08.022472+00:00
---

# RtkParticipantTile · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttile/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkParticipantTile



# RtkParticipantTile

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttile/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A video tile for a single participant showing their video feed, name tag with audio indicator, avatar (when video is off), and pin indicator.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`participant` | `RTKParticipant | RTKSelf` | ✅ | - | The participant to render  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`style` | `StyleProp<any>` | ❌ | - | Custom styles (typically width/height for grid sizing)  
`nameTagPosition` | `'bottom-center' | 'bottom-left' | 'bottom-right' | 'top-center' | 'top-left' | 'top-right' | 'none'` | ❌ | `'bottom-left'` | Position of the name tag overlay  
`isPreview` | `boolean` | ❌ | `false` | Whether this is a preview tile (setup screen)  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`children` | `ReactNode` | ❌ | - | Additional content to overlay on the tile  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantTile } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkParticipantTile meeting={meeting} participant={participant} />;
    }

### With Properties
    
    
    import { RtkParticipantTile } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkParticipantTile
    			meeting={meeting}
    			participant={participant}
    			nameTagPosition="bottom-left"
    			isPreview={false}
    			size="md"
    		/>
    	);
    }

[PreviousRtkParticipants](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipants/)[NextRtkParticipantToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkParticipantTile.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
