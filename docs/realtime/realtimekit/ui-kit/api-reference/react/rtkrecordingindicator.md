---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingindicator/
title: RtkRecordingIndicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:39.233447+00:00
---

# RtkRecordingIndicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingindicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkRecordingIndicator



# RtkRecordingIndicator

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which indicates the recording status of a meeting. It will not render anything if no recording is taking place.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkRecordingIndicator } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkRecordingIndicator />;
    }

### With Properties
    
    
    import { RtkRecordingIndicator } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkRecordingIndicator
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkPollsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollstoggle/)[NextRtkRecordingToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkRecordingIndicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
