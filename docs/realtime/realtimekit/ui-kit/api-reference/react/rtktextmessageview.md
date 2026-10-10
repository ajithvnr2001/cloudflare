---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/
title: RtkTextMessageView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:36.658114+00:00
---

# RtkTextMessageView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkTextMessageView



# RtkTextMessageView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders a text message from chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`isMarkdown` | `boolean` | ✅ | - | Renders text as markdown (default = true)  
`text` | `string` | ✅ | - | Text message  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkTextMessageView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkTextMessageView />;
    }

### With Properties
    
    
    import { RtkTextMessageView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkTextMessageView
          isMarkdown={true}
          text="example"
        />
      );
    }

[PreviousRtkTextMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessage/)[NextRtkTooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkTextMessageView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
