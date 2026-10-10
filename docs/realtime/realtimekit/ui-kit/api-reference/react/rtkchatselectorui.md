---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/
title: RtkChatSelectorUi \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:46.379039+00:00
---

# RtkChatSelectorUi · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChatSelectorUi



# RtkChatSelectorUi

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`groups` | `ChatGroup[]` | ✅ | - | Participants  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`selectedGroupId` | `string` | ✅ | - | Selected participant  
`selfUserId` | `string` | ✅ | - | Self User ID  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`unreadCounts` | `Record<string, number>` | ✅ | - | Unread counts  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkChatSelectorUi } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChatSelectorUi />;
    }

### With Properties
    
    
    import { RtkChatSelectorUi } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChatSelectorUi
          groups={[]}
          selectedGroupId="example"
          selfUserId="example"
        />
      );
    }

[PreviousRtkChatSelector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/)[NextRtkChatToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchattoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChatSelectorUi.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
