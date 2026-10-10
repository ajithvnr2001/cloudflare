---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialogmanager/
title: RtkDialogManager \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:45.158677+00:00
---

# RtkDialogManager · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialogmanager/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkDialogManager



# RtkDialogManager

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which handles all dialog elements in a component such as:

  * rtk-settings
  * rtk-leave-meeting
  * rtk-permissions-message
  * rtk-image-viewer
  * rtk-breakout-rooms-manager This components depends on the values from `states` object.



## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkDialogManager } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkDialogManager />;
    }

### With Properties
    
    
    import { RtkDialogManager } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkDialogManager
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkDialog](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialog/)[NextRtkDraftAttachmentView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdraftattachmentview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkDialogManager.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
