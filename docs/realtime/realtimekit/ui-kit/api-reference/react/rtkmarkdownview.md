---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/
title: RtkMarkdownView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:21.395513+00:00
---

# RtkMarkdownView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMarkdownView



# RtkMarkdownView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`maxLength` | `number` | ✅ | - | max length of text to render as markdown  
`text` | `string` | ✅ | - | raw text to render as markdown  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMarkdownView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMarkdownView />;
    }

### With Properties
    
    
    import { RtkMarkdownView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMarkdownView
          maxLength={42}
          text="example"
        />
      );
    }

[PreviousRtkLogo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/)[NextRtkMeeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeeting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMarkdownView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
