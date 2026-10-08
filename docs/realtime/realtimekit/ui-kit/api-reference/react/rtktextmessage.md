---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessage/
title: RtkTextMessage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:30.239067+00:00
---

# RtkTextMessage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkTextMessage



# RtkTextMessage

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated `rtk-text-message` is deprecated and will be removed soon. Use `rtk-text-message-view` instead. A component which renders a text message from chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user  
`message` | `TextMessage` | ✅ | - | Text message object  
`now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates  
`showBubble` | `boolean` | ✅ | - | show message in bubble  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkTextMessage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkTextMessage />;
    }

### With Properties
    
    
    import { RtkTextMessage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkTextMessage
          isContinued={true}
          message={textmessage}
          now={date}
        />
      );
    }

[PreviousRtkTextComposerView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextcomposerview/)[NextRtkTextMessageView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkTextMessage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
