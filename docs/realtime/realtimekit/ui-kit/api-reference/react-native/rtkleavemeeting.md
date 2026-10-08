---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavemeeting/
title: RtkLeaveMeeting \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:05.082686+00:00
---

# RtkLeaveMeeting · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavemeeting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkLeaveMeeting



# RtkLeaveMeeting

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavemeeting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Leave meeting confirmation dialog with options to leave or end the meeting for all (if host).

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`onClose` | `any` | ✅ | - | Callback to close the dialog  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLeaveMeeting } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkLeaveMeeting meeting={meeting} onClose={() => setOpen(false)} />;
    }

### With Properties
    
    
    import { RtkLeaveMeeting } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkLeaveMeeting
    			meeting={meeting}
    			onClose={() => setOpen(false)}
    			states={states}
    		/>
    	);
    }

[PreviousRtkLeaveButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavebutton/)[NextRtkLiveStreamIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamindicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkLeaveMeeting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
