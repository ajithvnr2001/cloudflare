---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/
title: RtkLeaveButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:43.525598+00:00
---

# RtkLeaveButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkLeaveButton



# RtkLeaveButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles visilibility of the leave confirmation dialog.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLeaveButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkLeaveButton />;
    }

### With Properties
    
    
    import { RtkLeaveButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkLeaveButton
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkJoinStage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkjoinstage/)[NextRtkLeaveMeeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkLeaveButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
