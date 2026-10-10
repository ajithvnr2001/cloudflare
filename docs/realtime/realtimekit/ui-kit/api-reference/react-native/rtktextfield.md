---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktextfield/
title: RtkTextField \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:49.482985+00:00
---

# RtkTextField · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktextfield/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkTextField



# RtkTextField

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A themed text input field component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`disabled` | `boolean` | ❌ | `false` | Whether the input is disabled  
`placeholder` | `string` | ❌ | `''` | Placeholder text  
`type` | `string` | ❌ | `'text'` | Input type  
`style` | `StyleProp<any>` | ❌ | - | Custom styles  
`onChangeText` | `(s: string) => void` | ❌ | - | Callback when text changes  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkTextField } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkTextField placeholder="Enter your name" />;
    }

### With Properties
    
    
    import { RtkTextField } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkTextField
    			placeholder="Enter display name"
    			onChangeText={(text) => setName(text)}
    			disabled={false}
    		/>
    	);
    }

[PreviousRtkText](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktext/)[NextRtkUIProvider](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkuiprovider/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkTextField.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
