---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/
title: RtkMeetingTitle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:21.693272+00:00
---

# RtkMeetingTitle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMeetingTitle



# RtkMeetingTitle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays the title of the meeting.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMeetingTitle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMeetingTitle />;
    }

### With Properties
    
    
    import { RtkMeetingTitle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMeetingTitle
          meeting={meeting}
        />
      );
    }

[PreviousRtkMeeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeeting/)[NextRtkMenu](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenu/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMeetingTitle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
