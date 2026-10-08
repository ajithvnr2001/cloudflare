---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/
title: RtkRecordingToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:26.863574+00:00
---

# RtkRecordingToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkRecordingToggle



# RtkRecordingToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles recording state of a meeting. Only a privileged user can perform this action, thus the button will not be visible for participants who don't have the permission to record a meeting.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`disabled` | `boolean` | ✅ | - | Disable the button  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkRecordingToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkRecordingToggle />;
    }

### With Properties
    
    
    import { RtkRecordingToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkRecordingToggle
          disabled={true}
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkRecordingIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingindicator/)[NextRtkScreenShareToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkRecordingToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
