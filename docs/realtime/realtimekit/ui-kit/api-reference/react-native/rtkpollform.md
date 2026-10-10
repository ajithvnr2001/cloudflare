---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollform/
title: RtkPollForm \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:50.776921+00:00
---

# RtkPollForm · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkPollForm



# RtkPollForm

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Form for creating a new poll with question, dynamic options, anonymous voting, and hide results toggles.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`onRtkCreatePoll` | `any` | ❌ | - | Callback when poll is created (receives question, options, anonymous, hideVotes)  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPollForm } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPollForm onRtkCreatePoll={(data) => handleCreatePoll(data)} />;
    }

### With Properties
    
    
    import { RtkPollForm } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkPollForm
    			onRtkCreatePoll={(data) => handleCreatePoll(data)}
    			iconPack={customIconPack}
    		/>
    	);
    }

[PreviousRtkPoll](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpoll/)[NextRtkPolls](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpolls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkPollForm.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
