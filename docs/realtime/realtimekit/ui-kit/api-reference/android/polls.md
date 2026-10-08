---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/polls/
title: RtkPollsBottomSheet \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:15.494514+00:00
---

# RtkPollsBottomSheet · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/polls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkPollsBottomSheet



# RtkPollsBottomSheet

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/polls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage

A component which lists all available polls a user can access.

## Methods

Method | Parameters | Description  
---|---|---  
`show` | `fragmentManager: FragmentManager, tag: String?` | Display the polls bottom sheet  
  
## Usage Examples

### Basic Usage
    
    
    val rtkPollsBottomSheet = RtkPollsBottomSheet()
    rtkPollsBottomSheet.show(fragmentManager, "POLLS_TAG")

[PreviousRtkPluginsBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/plugins/)[NextRtkRecordingIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/recording-indicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/polls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
