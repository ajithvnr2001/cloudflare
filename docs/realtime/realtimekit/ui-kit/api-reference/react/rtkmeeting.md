---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeeting/
title: RtkMeeting \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:43.012296+00:00
---

# RtkMeeting · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeeting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMeeting



# RtkMeeting

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A single component which renders an entire meeting UI. It loads your preset and renders the UI based on it. With this component, you don't have to handle all the states, dialogs and other smaller bits of managing the application.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`applyDesignSystem` | `boolean` | ✅ | - | Whether to apply the design system on the document root from config  
`config` | `UIConfig` | ✅ | - | UI Config  
`gridLayout` | `GridLayout1` | ✅ | - | Grid layout  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`leaveOnUnmount` | `boolean` | ✅ | - | Whether participant should leave when this component gets unmounted  
`loadConfigFromPreset` | `boolean` | ✅ | - | Whether to load config from preset  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`mode` | `MeetingMode` | ✅ | - | Fill type  
`overrides` | `Overrides` | ❌ | `defaultOverrides` | UI Kit Overrides  
`showSetupScreen` | `boolean` | ✅ | - | Whether to show setup screen or not  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMeeting } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMeeting />;
    }

### With Properties
    
    
    import { RtkMeeting } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMeeting
          applyDesignSystem={true}
          config={defaultUiConfig}
          gridLayout={gridlayout1}
        />
      );
    }

[PreviousRtkMarkdownView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/)[NextRtkMeetingTitle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmeetingtitle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMeeting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
