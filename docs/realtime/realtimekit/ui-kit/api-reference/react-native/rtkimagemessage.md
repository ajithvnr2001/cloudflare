---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimagemessage/
title: RtkImageMessage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:04.385254+00:00
---

# RtkImageMessage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimagemessage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkImageMessage



# RtkImageMessage

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimagemessage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Renders an image message in chat with loading indicator and fullscreen support.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`message` | `any` | ✅ | - | The image message object with link property  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`isContinued` | `boolean` | ❌ | `false` | Whether this message continues from the same sender  
`now` | `Date` | ❌ | `new Date()` | Current time for relative timestamps  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkImageMessage } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkImageMessage message={imageMessage} />;
    }

### With Properties
    
    
    import { RtkImageMessage } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkImageMessage
    			message={imageMessage}
    			isContinued={false}
    			now={new Date()}
    		/>
    	);
    }

[PreviousRtkIdleScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkidlescreen/)[NextRtkImageViewer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimageviewer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkImageMessage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
