---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipantwaiting/
title: RtkParticipantWaiting \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:08.346820+00:00
---

# RtkParticipantWaiting · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipantwaiting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkParticipantWaiting



# RtkParticipantWaiting

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipantwaiting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A waiting participant card with accept/reject buttons for waitlist and stage request management.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`participant` | `Peer` | ✅ | - | The waiting participant  
`meeting` | `RealtimeKitClient` | ❌ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantWaiting } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkParticipantWaiting participant={waitingParticipant} />;
    }

### With Properties
    
    
    import { RtkParticipantWaiting } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkParticipantWaiting
    			participant={waitingParticipant}
    			meeting={meeting}
    			iconPack={customIconPack}
    		/>
    	);
    }

[PreviousRtkParticipantToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttoggle/)[NextRtkPermissionsMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpermissionsmessage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkParticipantWaiting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
