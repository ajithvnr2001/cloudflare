---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkuiprovider/
title: RtkUiProvider \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:36.414857+00:00
---

# RtkUiProvider · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkuiprovider/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkUiProvider



# RtkUiProvider

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ✅ | - | Config  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting | null` | ❌ | `null` | Meeting  
`mode` | `MeetingMode1` | ✅ | - | Fill type  
`overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Kit Overrides  
`showSetupScreen` | `boolean` | ✅ | - | Whether to show setup screen or not  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language utility  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkUiProvider } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkUiProvider />;
    }

### With Properties
    
    
    import { RtkUiProvider } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkUiProvider
          config={defaultUiConfig}
          mode={meeting}
          showSetupScreen={true}
        />
      );
    }

[PreviousRtkTranscripts](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscripts/)[NextRtkViewerCount](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkUiProvider.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
