---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/
title: RtkPoll \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:26.242993+00:00
---

# RtkPoll · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkPoll



# RtkPoll

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A poll component. Shows a poll where a user can vote.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`permissions` | `RTKPermissionsPreset` | ✅ | - | Permissions Object  
`poll` | `Poll` | ✅ | - | Poll  
`self` | `string` | ✅ | - | Self ID  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPoll } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkPoll />;
    }

### With Properties
    
    
    import { RtkPoll } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkPoll
          permissions={rtkpermissionspreset}
          poll={poll}
          self="example"
        />
      );
    }

[PreviousRtkPluginsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginstoggle/)[NextRtkPollForm](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkPoll.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
