---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-sidebar-ui/
title: rtk-sidebar-ui \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:52.820331+00:00
---

# rtk-sidebar-ui · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-sidebar-ui/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-sidebar-ui



# rtk-sidebar-ui

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-sidebar-ui/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`currentTab` | `string` | ✅ | - | Default tab to open  
`focusCloseButton` | `boolean` | ✅ | - | Option to focus close button when opened  
`hideCloseAction` | `boolean` | ✅ | - | Hide Close Action  
`hideHeader` | `boolean` | ✅ | - | Hide Main Header  
`iconPack` | `{ people: string; people_checked: string; chat: string; poll: string; participants: string; rocket: string; call_end: string; share: string; mic_on: string; mic_off: string; video_on: string; video_off: string; share_screen_start: string; share_screen_stop: string; share_screen_person: string; clock: string; dismiss: string; send: string; search: string; more_vertical: string; chevron_down: string; chevron_up: string; chevron_left: string; chevron_right: string; settings: string; wifi: string; speaker: string; speaker_off: string; download: string; full_screen_maximize: string; full_screen_minimize: string; copy: string; attach: string; image: string; emoji_multiple: string; image_off: string; disconnected: string; wand: string; recording: string; subtract: string; stop_recording: string; warning: string; pin: string; pin_off: string; spinner: string; breakout_rooms: string; add: string; shuffle: string; edit: string; delete: string; back: string; save: string; web: string; checkmark: string; spotlight: string; join_stage: string; leave_stage: string; pip_off: string; pip_on: string; signal_1: string; signal_2: string; signal_3: string; signal_4: string; signal_5: string; start_livestream: string; stop_livestream: string; viewers: string; debug: string; info: string; devices: string; horizontal_dots: string; ai_sparkle: string; meeting_ai: string; captionsOn: string; captionsOff: string; play: string; pause: string; fastForward: string; minimize: string; maximize: string; }` | ✅ | - | Icon Pack  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`tabs` | `RtkSidebarTab1[]` | ✅ | - | Tabs  
`view` | `RtkSidebarView1` | ✅ | - | View  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-sidebar-ui></rtk-sidebar-ui>

### With Properties
    
    
    <rtk-sidebar-ui
     currentTab="example">
    </rtk-sidebar-ui>
    
    
    <script>
      const el = document.querySelector("rtk-sidebar-ui");
    
      el.focusCloseButton= true;
      el.hideCloseAction= true;
    </script>

[Previousrtk-sidebar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-sidebar/)[Nextrtk-simple-grid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-simple-grid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-sidebar-ui.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
