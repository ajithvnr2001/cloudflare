---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/
title: RtkImageViewer \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:43.869125+00:00
---

# RtkImageViewer · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkImageViewer



# RtkImageViewer

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows an image sent via chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`image` | `ImageMessage` | ✅ | - | Image message  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkImageViewer } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkImageViewer />;
    }

### With Properties
    
    
    import { RtkImageViewer } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkImageViewer
          image={imagemessage}
          size="md"
        />
      );
    }

[PreviousRtkImageMessageView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/)[NextRtkInformationTooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkImageViewer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
