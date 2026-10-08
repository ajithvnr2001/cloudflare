---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/
title: RtkFileDropzone \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:18.403149+00:00
---

# RtkFileDropzone · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkFileDropzone



# RtkFileDropzone

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`hostEl` | `HTMLElement` | ✅ | - | Host element on which drop events to attach  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkFileDropzone } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkFileDropzone />;
    }

### With Properties
    
    
    import { RtkFileDropzone } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkFileDropzone
          hostEl={htmlelement}
        />
      );
    }

[PreviousRtkEndedScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/)[NextRtkFileMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkFileDropzone.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
