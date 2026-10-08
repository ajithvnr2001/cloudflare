---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavebutton/
title: RtkLeaveButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:04.992632+00:00
---

# RtkLeaveButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavebutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkLeaveButton



# RtkLeaveButton

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavebutton/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Button to trigger the leave meeting confirmation dialog.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`variant` | `'button' | 'horizontal'` | ❌ | - | Layout variant  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Button size  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLeaveButton } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkLeaveButton />;
    }

### With Properties
    
    
    import { RtkLeaveButton } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkLeaveButton variant="button" size="md" />;
    }

[PreviousRtkJoinStage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkjoinstage/)[NextRtkLeaveMeeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavemeeting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkLeaveButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
