---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimageviewer/
title: RtkImageViewer \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:54.092675+00:00
---

# RtkImageViewer · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimageviewer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkImageViewer



# RtkImageViewer

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Image viewer with fullscreen toggle and download functionality for chat images.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`image` | `any` | ✅ | - | The image message object  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Size variant  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`isContinued` | `boolean` | ❌ | `false` | Whether this message continues from the same sender  
`_id` | `string | number` | ❌ | - | Unique identifier for fullscreen tracking  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkImageViewer } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkImageViewer image={imageMessage} />;
    }

### With Properties
    
    
    import { RtkImageViewer } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkImageViewer image={imageMessage} size="md" _id="viewer-1" />;
    }

[PreviousRtkImageMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkimagemessage/)[NextRtkJoinStage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkjoinstage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkImageViewer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
