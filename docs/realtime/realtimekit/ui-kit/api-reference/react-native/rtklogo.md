---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklogo/
title: RtkLogo \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:52.964518+00:00
---

# RtkLogo · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklogo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkLogo



# RtkLogo

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays a logo from a URL (SVG format) in the meeting header.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `any` | ❌ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | - | UI configuration object  
`logoUrl` | `string` | ❌ | - | URL of the logo SVG to display  
`style` | `StyleProps` | ❌ | - | Style object with width/height for the logo  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLogo } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkLogo logoUrl="https://example.com/logo.svg" />;
    }

### With Properties
    
    
    import { RtkLogo } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkLogo
    			logoUrl="https://example.com/logo.svg"
    			style={{ width: 120, height: 40 }}
    			config={customConfig}
    		/>
    	);
    }

[PreviousRtkLiveStreamViewerCount](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamviewercount/)[NextRtkMeeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkmeeting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkLogo.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
