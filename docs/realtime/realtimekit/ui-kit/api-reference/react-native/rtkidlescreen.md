---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkidlescreen/
title: RtkIdleScreen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:04.253315+00:00
---

# RtkIdleScreen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkidlescreen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkIdleScreen



# RtkIdleScreen

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkidlescreen/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Loading/idle screen displayed while the meeting is initializing, showing a logo and spinner.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ✅ | - | UI configuration object (used for logo URL)  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkIdleScreen } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkIdleScreen config={config} />;
    }

### With Properties
    
    
    import {
    	RtkIdleScreen,
    	defaultConfig,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkIdleScreen config={defaultConfig} />;
    }

[PreviousRtkIcon](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkicon/)[NextRtkImageMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimagemessage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkIdleScreen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
