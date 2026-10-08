---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/
title: RtkEndedScreen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:18.292908+00:00
---

# RtkEndedScreen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkEndedScreen



# RtkEndedScreen

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A screen which shows a meeting has ended.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Global states  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | Global states  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkEndedScreen } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkEndedScreen />;
    }

### With Properties
    
    
    import { RtkEndedScreen } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkEndedScreen
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkEmojiPickerButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/)[NextRtkFileDropzone](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfiledropzone/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkEndedScreen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
