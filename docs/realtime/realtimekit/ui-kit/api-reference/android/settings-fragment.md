---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-fragment/
title: RtkSettingsFragment \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:16.190436+00:00
---

# RtkSettingsFragment · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-fragment/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkSettingsFragment



# RtkSettingsFragment

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-fragment/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage

A settings dialog that contains audio and video device selectors and a self-preview tile. Used in landscape orientation.

## Methods

Method | Parameters | Description  
---|---|---  
`show` | `fragmentManager: FragmentManager, tag: String?` | Display the settings dialog  
`setBottomSheetEnabled` | `onClick: () -> Unit` | Enable a button to switch to the bottom sheet view  
  
## Usage Examples

### Basic Usage
    
    
    val settingsFragment = RtkSettingsFragment()
    settingsFragment.show(fragmentManager, "SETTINGS_TAG")

[PreviousRtkSettingsBottomsheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-bottomsheet/)[NextRtkSetupFragment](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/setup-screen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/settings-fragment.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
