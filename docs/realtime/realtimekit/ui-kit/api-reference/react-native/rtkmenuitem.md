---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenuitem/
title: RtkMenuItem \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:52.590867+00:00
---

# RtkMenuItem · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenuitem/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkMenuItem



# RtkMenuItem

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A pressable menu item within a menu.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`children` | `ReactNode` | ✅ | - | Menu item content  
`onClick` | `(ev) => {}` | ❌ | - | Press handler callback  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Size variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMenuItem } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkMenuItem onClick={() => ({})}>
    			<Text>Option 1</Text>
    		</RtkMenuItem>
    	);
    }

### With Properties
    
    
    import { RtkMenuItem } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkMenuItem onClick={(ev) => ({})} size="md">
    			<Text>Option 1</Text>
    		</RtkMenuItem>
    	);
    }

[PreviousRtkMenu](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenu/)[NextRtkMenuList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenulist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkMenuItem.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
