---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/
title: RtkFileMessage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:18.602837+00:00
---

# RtkFileMessage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkFileMessage



# RtkFileMessage

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated `rtk-file-message` is deprecated and will be removed soon. Use `rtk-file-message-view` instead. A component which renders a file message from chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user  
`message` | `FileMessage` | ✅ | - | Text message object  
`now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates  
`showBubble` | `boolean` | ✅ | - | show message in bubble  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkFileMessage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkFileMessage />;
    }

### With Properties
    
    
    import { RtkFileMessage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkFileMessage
          isContinued={true}
          message={filemessage}
          now={date}
        />
      );
    }

[PreviousRtkFileDropzone](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/)[NextRtkFileMessageView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkFileMessage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
