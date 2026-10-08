---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/
title: RtkEmojiPickerButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:19.523543+00:00
---

# RtkEmojiPickerButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkEmojiPickerButton



# RtkEmojiPickerButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`isActive` | `boolean` | ✅ | - | Active state indicator  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkEmojiPickerButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkEmojiPickerButton />;
    }

### With Properties
    
    
    import { RtkEmojiPickerButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkEmojiPickerButton
          isActive={true}
        />
      );
    }

[PreviousRtkEmojiPicker](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/)[NextRtkEndedScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkEmojiPickerButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
