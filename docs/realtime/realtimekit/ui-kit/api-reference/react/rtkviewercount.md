---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/
title: RtkViewerCount \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:30.679019+00:00
---

# RtkViewerCount · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkViewerCount



# RtkViewerCount

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows count of total joined participants in a meeting.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ViewerCountVariant` | ✅ | - | Viewer count variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkViewerCount } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkViewerCount />;
    }

### With Properties
    
    
    import { RtkViewerCount } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkViewerCount
          meeting={meeting}
          variant="primary"
        />
      );
    }

[PreviousRtkUiProvider](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkuiprovider/)[NextRtkVirtualizedParticipantList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkvirtualizedparticipantlist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkViewerCount.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
