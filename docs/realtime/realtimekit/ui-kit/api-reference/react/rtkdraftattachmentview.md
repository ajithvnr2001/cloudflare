---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdraftattachmentview/
title: RtkDraftAttachmentView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:45.281543+00:00
---

# RtkDraftAttachmentView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdraftattachmentview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkDraftAttachmentView



# RtkDraftAttachmentView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders the draft attachment to send

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`attachment` | `{ type: 'image' | 'file'; file: File; }` | ✅ | - | Attachment to display  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkDraftAttachmentView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkDraftAttachmentView />;
    }

### With Properties
    
    
    import { RtkDraftAttachmentView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkDraftAttachmentView
          attachment={{}}
        />
      );
    }

[PreviousRtkDialogManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialogmanager/)[NextRtkEmojiPicker](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkDraftAttachmentView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
