---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbarbutton/
title: RtkControlbarButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:03.050259+00:00
---

# RtkControlbarButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbarbutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkControlbarButton



# RtkControlbarButton

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbarbutton/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A reusable button for the control bar with icon, label, loading state, and warning indicator support.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`label` | `string` | ✅ | `' '` | Button label text  
`icon` | `string` | ✅ | - | SVG icon string  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`isLoading` | `boolean` | ❌ | `false` | Show loading spinner instead of icon  
`disabled` | `boolean` | ❌ | `false` | Whether the button is disabled  
`onClick` | `() => void` | ❌ | - | Press handler callback  
`showWarning` | `boolean` | ❌ | `false` | Show warning indicator  
`variant` | `'button' | 'horizontal'` | ❌ | `'button'` | Layout variant  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Icon size  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkControlbarButton } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkControlbarButton label="Mute" icon={muteIcon} />;
    }

### With Properties
    
    
    import { RtkControlbarButton } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkControlbarButton
    			label="Mute"
    			icon={muteIcon}
    			variant="horizontal"
    			size="md"
    			onClick={() => console.log("pressed")}
    		/>
    	);
    }

[PreviousRtkControlbar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbar/)[NextRtkDialog](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkControlbarButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
