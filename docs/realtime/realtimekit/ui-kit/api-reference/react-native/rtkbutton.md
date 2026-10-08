---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/
title: RtkButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:02.443554+00:00
---

# RtkButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkButton



# RtkButton

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A general-purpose button component with multiple variants and sizes.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`children` | `ReactNode` | ❌ | - | Button content/label  
`onClick` | `any` | ✅ | - | Press handler callback  
`kind` | `'button' | 'icon' | 'wide'` | ❌ | `'button'` | Button kind  
`variant` | `'danger' | 'ghost' | 'primary' | 'secondary'` | ❌ | - | Visual style variant  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Button size  
`reverse` | `boolean` | ❌ | `false` | Reverse the button content order  
`disabled` | `boolean` | ❌ | - | Whether the button is disabled  
`style` | `StyleProp<any>` | ❌ | - | Custom React Native styles  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkButton } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkButton onClick={() => console.log("pressed")}>Press Me</RtkButton>;
    }

### With Properties
    
    
    import { RtkButton } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkButton
    			onClick={() => console.log("pressed")}
    			variant="primary"
    			size="md"
    			kind="wide"
    		>
    			Join Meeting
    		</RtkButton>
    	);
    }

[PreviousRtkBreakoutRoomsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomstoggle/)[NextRtkCameraToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcameratoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
