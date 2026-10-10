---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/
title: RtkLeaveMeeting \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:43.341296+00:00
---

# RtkLeaveMeeting · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkLeaveMeeting



# RtkLeaveMeeting

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which allows you to leave a meeting or end meeting for all, if you have the permission.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLeaveMeeting } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkLeaveMeeting />;
    }

### With Properties
    
    
    import { RtkLeaveMeeting } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkLeaveMeeting
          meeting={meeting}
        />
      );
    }

[PreviousRtkLeaveButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/)[NextRtkLivestreamIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkLeaveMeeting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
