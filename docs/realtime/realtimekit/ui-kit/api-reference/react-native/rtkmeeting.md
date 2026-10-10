---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmeeting/
title: RtkMeeting \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:53.199250+00:00
---

# RtkMeeting · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmeeting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkMeeting



# RtkMeeting

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

The top-level meeting component that orchestrates the entire meeting UI. Manages meeting lifecycle (idle, setup, joined, ended, waiting states), applies design system, handles room join/leave events, and renders the appropriate screen. With this component, you do not have to handle all the states, dialogs, and other smaller bits of managing the application.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`applyDesignSystem` | `boolean` | ❌ | `true` | Whether to apply the preset design system colors from the meeting config  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`iconPackUrl` | `string` | ❌ | `''` | URL to fetch a custom icon pack from  
`showSetupScreen` | `boolean` | ❌ | `true` | Whether to show the setup/preview screen before joining  
`iOSScreenshareEnabled` | `boolean` | ❌ | `false` | Turn on screenshare on iOS (requires additional native setup)  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMeeting } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkMeeting meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkMeeting } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkMeeting
    			meeting={meeting}
    			applyDesignSystem={true}
    			showSetupScreen={true}
    			iOSScreenshareEnabled={false}
    		/>
    	);
    }

[PreviousRtkLogo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklogo/)[NextRtkMeetingTitle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmeetingtitle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkMeeting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
