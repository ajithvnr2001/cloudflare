---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/
title: RtkImageMessageView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:43.929852+00:00
---

# RtkImageMessageView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkImageMessageView



# RtkImageMessageView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders an image message.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`url` | `string` | ✅ | - | Url of the image  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkImageMessageView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkImageMessageView />;
    }

### With Properties
    
    
    import { RtkImageMessageView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkImageMessageView
          url="example"
        />
      );
    }

[PreviousRtkImageMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessage/)[NextRtkImageViewer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkImageMessageView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
