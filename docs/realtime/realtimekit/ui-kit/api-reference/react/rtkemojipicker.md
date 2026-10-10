---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/
title: RtkEmojiPicker \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:44.929993+00:00
---

# RtkEmojiPicker · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkEmojiPicker



# RtkEmojiPicker

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A very simple emoji picker component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`focusWhenOpened` | `boolean` | ✅ | - | Controls whether or not to focus on mount  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkEmojiPicker } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkEmojiPicker />;
    }

### With Properties
    
    
    import { RtkEmojiPicker } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkEmojiPicker
          focusWhenOpened={true}
        />
      );
    }

[PreviousRtkDraftAttachmentView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdraftattachmentview/)[NextRtkEmojiPickerButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkEmojiPicker.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
