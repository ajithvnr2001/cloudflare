---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/
title: RtkClock \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:46.556729+00:00
---

# RtkClock · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkClock



# RtkClock

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Shows the time elapsed in a meeting.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkClock } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkClock />;
    }

### With Properties
    
    
    import { RtkClock } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkClock
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkChatToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchattoggle/)[NextRtkConfirmationModal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkClock.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
