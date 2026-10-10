---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerui/
title: RtkChatComposerUi \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:47.473737+00:00
---

# RtkChatComposerUi · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerui/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChatComposerUi



# RtkChatComposerUi

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated . This component is deprecated, please use rtk-chat-composer-view instead.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages  
`canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`prefill` | `{ suggestedReplies?: string[]; editMessage?: TextMessage; replyMessage?: TextMessage; }` | ❌ | - | prefill the composer  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkChatComposerUi } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChatComposerUi />;
    }

### With Properties
    
    
    import { RtkChatComposerUi } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChatComposerUi
          canSendFiles={true}
          canSendTextMessage={true}
          size="md"
        />
      );
    }

[PreviousRtkChat](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/)[NextRtkChatComposerView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChatComposerUi.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
