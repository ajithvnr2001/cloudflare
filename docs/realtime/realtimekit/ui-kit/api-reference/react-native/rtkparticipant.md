---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipant/
title: RtkParticipant \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:07.833506+00:00
---

# RtkParticipant · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipant/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkParticipant



# RtkParticipant

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipant/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A participant list item card showing avatar, name, audio/video status icons, and host control options (pin, kick, mute, stage management).

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`participant` | `Peer` | ✅ | - | The participant to display  
`meeting` | `RealtimeKitClient` | ❌ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipant } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkParticipant participant={participant} />;
    }

### With Properties
    
    
    import { RtkParticipant } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkParticipant
    			participant={participant}
    			meeting={meeting}
    			iconPack={customIconPack}
    		/>
    	);
    }

[PreviousRtkNotifications](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknotifications/)[NextRtkParticipantCount](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipantcount/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkParticipant.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
