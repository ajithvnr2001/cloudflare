---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkfilemessage/
title: RtkFileMessage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:55.113925+00:00
---

# RtkFileMessage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkfilemessage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkFileMessage



# RtkFileMessage

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Renders a file message in chat with file name, size, extension, and download button.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`message` | `Message` | ✅ | - | The chat message object  
`isContinued` | `boolean` | ❌ | `false` | Whether this message continues from the same sender  
`now` | `Date` | ❌ | `new Date()` | Current time for relative timestamps  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkFileMessage } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkFileMessage message={message} />;
    }

### With Properties
    
    
    import { RtkFileMessage } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkFileMessage message={message} isContinued={true} now={new Date()} />
    	);
    }

[PreviousRtkEndedScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkendedscreen/)[NextRtkGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkFileMessage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
