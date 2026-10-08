---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/
title: RtkScreenShareToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:27.081309+00:00
---

# RtkScreenShareToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkScreenShareToggle



# RtkScreenShareToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles your screenshare.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkScreenShareToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkScreenShareToggle />;
    }

### With Properties
    
    
    import { RtkScreenShareToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkScreenShareToggle
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkRecordingToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingtoggle/)[NextRtkScreenshareView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkScreenShareToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
