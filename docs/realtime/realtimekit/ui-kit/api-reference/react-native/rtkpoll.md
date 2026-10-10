---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpoll/
title: RtkPoll \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:50.552686+00:00
---

# RtkPoll · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpoll/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkPoll



# RtkPoll

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Renders a single poll with question, votable options, vote counts, and voter avatars.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`poll` | `Poll` | ✅ | - | The poll object to display  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`onRtkVotePoll` | `any` | ❌ | - | Callback when a vote is cast (receives option index)  
`self` | `string` | ❌ | - | Self user ID  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPoll } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPoll poll={poll} meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkPoll } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkPoll
    			poll={poll}
    			meeting={meeting}
    			onRtkVotePoll={(index) => handleVote(index)}
    			self={selfUserId}
    		/>
    	);
    }

[PreviousRtkPluginsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpluginstoggle/)[NextRtkPollForm](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkPoll.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
