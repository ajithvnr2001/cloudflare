---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/
title: RtkFilePickerButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:44.771503+00:00
---

# RtkFilePickerButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkFilePickerButton



# RtkFilePickerButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`filter` | `string` | ✅ | - | File type filter to open file picker with  
`icon` | `keyof IconPack1` | ✅ | - | Icon  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`label` | `string` | ✅ | - | Label for tooltip  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkFilePickerButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkFilePickerButton />;
    }

### With Properties
    
    
    import { RtkFilePickerButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkFilePickerButton
          filter="example"
          icon={defaultIconPack}
          label="example"
        />
      );
    }

[PreviousRtkFileMessageView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/)[NextRtkFullscreenToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkFilePickerButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
