---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkicon/
title: RtkIcon \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:54.921761+00:00
---

# RtkIcon · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkicon/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkIcon



# RtkIcon

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Renders an SVG icon from an icon string, applying the current theme text color.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`icon` | `string` | ✅ | - | SVG icon string to render  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkIcon } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkIcon icon={svgIconString} />;
    }

### With Properties
    
    
    import {
    	RtkIcon,
    	defaultIconPack,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkIcon icon={defaultIconPack.mic_on} />;
    }

[PreviousRtkHeader](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkheader/)[NextRtkIdleScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkidlescreen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkIcon.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
