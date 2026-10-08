---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkjoinstage/
title: RtkJoinStage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:04.742327+00:00
---

# RtkJoinStage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkjoinstage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkJoinStage



# RtkJoinStage

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkjoinstage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Join stage confirmation dialog with video preview and mic/camera toggles for webinar/livestream participants.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkJoinStage } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkJoinStage meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkJoinStage } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkJoinStage meeting={meeting} iconPack={customIconPack} states={states} />
    	);
    }

[PreviousRtkImageViewer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimageviewer/)[NextRtkLeaveButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavebutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkJoinStage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
