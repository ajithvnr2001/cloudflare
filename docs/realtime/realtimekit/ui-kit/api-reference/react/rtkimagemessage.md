---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessage/
title: RtkImageMessage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:43.601114+00:00
---

# RtkImageMessage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkImageMessage



# RtkImageMessage

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated `rtk-image-message` is deprecated and will be removed soon. Use `rtk-image-message-view` instead. A component which renders an image message from chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user  
`message` | `ImageMessage` | ✅ | - | Text message object  
`now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates  
`showBubble` | `boolean` | ✅ | - | show message in bubble  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkImageMessage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkImageMessage />;
    }

### With Properties
    
    
    import { RtkImageMessage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkImageMessage
          isContinued={true}
          message={imagemessage}
          now={date}
        />
      );
    }

[PreviousRtkIdleScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/)[NextRtkImageMessageView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessageview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkImageMessage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
