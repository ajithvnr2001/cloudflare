---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessageview/
title: RtkMessageView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:22.371116+00:00
---

# RtkMessageView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessageview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMessageView



# RtkMessageView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessageview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`actions` | `MessageAction[]` | ✅ | - | List of actions to show in menu  
`authorName` | `string` | ✅ | - | Author display label  
`avatarUrl` | `string` | ✅ | - | Avatar image url  
`hideAuthorName` | `boolean` | ✅ | - | Hides author display label  
`hideAvatar` | `boolean` | ✅ | - | Hides avatar  
`hideMetadata` | `boolean` | ✅ | - | Hides metadata (time)  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`isEdited` | `boolean` | ✅ | - | Has the message been edited  
`isSelf` | `boolean` | ✅ | - | Is the message sent by the current user  
`messageType` | `Message['type']` | ✅ | - | Type of message  
`pinned` | `boolean` | ✅ | - | Is message pinned  
`time` | `Date` | ✅ | - | Time when message was sent  
`variant` | `'plain' | 'bubble'` | ✅ | - | Appearance  
`viewType` | `'incoming' | 'outgoing'` | ✅ | - | Render  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMessageView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMessageView />;
    }

### With Properties
    
    
    import { RtkMessageView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMessageView
          actions={[]}
          authorName="example"
          avatarUrl="example"
        />
      );
    }

[PreviousRtkMessageListView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/)[NextRtkMicrophoneSelector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmicrophoneselector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMessageView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
