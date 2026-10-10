---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/
title: RtkFileMessageView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:44.708952+00:00
---

# RtkFileMessageView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkFileMessageView



# RtkFileMessageView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders a file message.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`name` | `string` | ✅ | - | Name of the file  
`size` | `number` | ✅ | - | Size of the file  
`url` | `string` | ✅ | - | Url of the file  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkFileMessageView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkFileMessageView />;
    }

### With Properties
    
    
    import { RtkFileMessageView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkFileMessageView
          name="example"
          size={42}
          url="example"
        />
      );
    }

[PreviousRtkFileMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/)[NextRtkFilePickerButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkFileMessageView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
