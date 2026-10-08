---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenu/
title: RtkMenu \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:06.392485+00:00
---

# RtkMenu · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenu/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkMenu



# RtkMenu

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenu/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A menu container component with placement options.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`children` | `ReactNode` | ✅ | - | Menu content  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ✅ | - | Size variant  
`placement` | `'bottom' | 'bottom-end' | 'bottom-start' | 'left' | 'left-end' | 'left-start' | 'right' | 'right-end' | 'right-start' | 'top' | 'top-end' | 'top-start'` | ✅ | - | Menu placement relative to trigger  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMenu } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkMenu size="md" placement="bottom">
    			<Text>Menu content</Text>
    		</RtkMenu>
    	);
    }

### With Properties
    
    
    import { RtkMenu } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkMenu size="lg" placement="bottom-start">
    			<Text>Menu content</Text>
    		</RtkMenu>
    	);
    }

[PreviousRtkMeetingTitle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmeetingtitle/)[NextRtkMenuItem](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmenuitem/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkMenu.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
