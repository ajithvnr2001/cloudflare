---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/
title: RtkMuteAllButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:23.352933+00:00
---

# RtkMuteAllButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMuteAllButton



# RtkMuteAllButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMuteAllButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMuteAllButton />;
    }

### With Properties
    
    
    import { RtkMuteAllButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMuteAllButton
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkMoreToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmoretoggle/)[NextRtkMuteAllConfirmation](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallconfirmation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMuteAllButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
