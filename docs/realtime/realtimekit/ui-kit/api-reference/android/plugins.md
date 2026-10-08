---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/plugins/
title: RtkPluginsBottomSheet \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:15.368478+00:00
---

# RtkPluginsBottomSheet · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/plugins/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkPluginsBottomSheet



# RtkPluginsBottomSheet

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/plugins/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage

A component which lists all available plugins from their preset, with the ability to enable or disable plugins.

## Methods

Method | Parameters | Description  
---|---|---  
`show` | `fragmentManager: FragmentManager, tag: String?` | Display the plugins bottom sheet  
  
## Usage Examples

### Basic Usage
    
    
    val rtkPluginsBottomSheet = RtkPluginsBottomSheet()
    rtkPluginsBottomSheet.show(fragmentManager, "PLUGINS_TAG")

[PreviousRtkParticipantVideoIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-video-indicator/)[NextRtkPollsBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/polls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/plugins.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
