---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkavatar/
title: RtkAvatar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:56.475501+00:00
---

# RtkAvatar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkavatar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkAvatar



# RtkAvatar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays a participant's avatar image or initials-based fallback avatar.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`participant` | `RTKParticipant | RTKSelf` | ✅ | - | The participant whose avatar to display  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size of the avatar  
`variant` | `'circular' | 'hexagon' | 'square'` | ❌ | `'circular'` | Shape variant of the avatar  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAvatar } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkAvatar participant={participant} />;
    }

### With Properties
    
    
    import { RtkAvatar } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkAvatar participant={participant} size="lg" variant="circular" />;
    }

[PreviousRtkAudioVisualizer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkaudiovisualizer/)[NextRtkBreakoutRoomsManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomsmanager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkAvatar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
