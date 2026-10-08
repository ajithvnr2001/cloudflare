---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screenshare-view/
title: rtk-screenshare-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:51.857254+00:00
---

# rtk-screenshare-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screenshare-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-screenshare-view



# rtk-screenshare-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screenshare-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which plays a participant's screenshared video. It also allows for placement of other components similar to `rtk-participant-tile`. This component will not render anything if the participant hasn't start screensharing.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`hideFullScreenButton` | `boolean` | ✅ | - | Hide full screen button  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`nameTagPosition` | `| 'bottom-left' | 'bottom-right' | 'bottom-center' | 'top-left' | 'top-right' | 'top-center'` | ✅ | - | Position of name tag  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'gradient'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-screenshare-view></rtk-screenshare-view>

### With Properties
    
    
    <rtk-screenshare-view>
    </rtk-screenshare-view>
    
    
    <script>
      const el = document.querySelector("rtk-screenshare-view");
    
      el.hideFullScreenButton= true;
      el.meeting= meeting
    </script>

[Previousrtk-screen-share-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screen-share-toggle/)[Nextrtk-settings](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-screenshare-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
