---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkaudiovisualizer/
title: RtkAudioVisualizer \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:56.599147+00:00
---

# RtkAudioVisualizer · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkaudiovisualizer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkAudioVisualizer



# RtkAudioVisualizer

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays an audio visualizer with animated bars representing a participant's audio levels.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`participant` | `Peer | RTKParticipant` | ✅ | - | The participant whose audio to visualize  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack for icons  
`isScreenshare` | `boolean` | ❌ | `false` | Whether this is a screenshare audio visualizer  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size of the visualizer  
`variant` | `'bar'` | ❌ | `'bar'` | Visual variant of the visualizer  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAudioVisualizer } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkAudioVisualizer participant={participant} />;
    }

### With Properties
    
    
    import { RtkAudioVisualizer } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkAudioVisualizer participant={participant} size="md" variant="bar" />
    	);
    }

[PreviousRtkWaitingScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/)[NextRtkAvatar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkavatar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkAudioVisualizer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
