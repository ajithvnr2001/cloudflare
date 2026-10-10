---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttoggle/
title: RtkParticipantToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:51.458815+00:00
---

# RtkParticipantToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkParticipantToggle



# RtkParticipantToggle

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Toggle button to open the participants sidebar panel. Shows a badge with pending request count.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Icon size  
`variant` | `'button' | 'horizontal'` | ❌ | - | Layout variant  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkParticipantToggle meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkParticipantToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkParticipantToggle meeting={meeting} size="md" variant="button" />;
    }

[PreviousRtkParticipantTile](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipanttile/)[NextRtkParticipantWaiting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipantwaiting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkParticipantToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
