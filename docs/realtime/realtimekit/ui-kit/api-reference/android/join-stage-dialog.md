---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-stage-dialog/
title: RtkJoinStageDialog \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:12.426740+00:00
---

# RtkJoinStageDialog · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-stage-dialog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkJoinStageDialog



# RtkJoinStageDialog

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-stage-dialog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage

A confirmation dialog screen shown when the user's request to join stage is approved or when the host invites the local user to join stage.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the dialog to the meeting state  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
`show` | - | Display the dialog  
`dismiss` | - | Dismiss the dialog  
  
## Usage Examples

### Basic Usage
    
    
    val rtkJoinStage = RtkJoinStageDialog(requireContext())
    rtkJoinStage.show()
    rtkJoinStage.activate(meeting)

[PreviousRtkJoinLivestreamButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-livestream-button/)[NextRtkLeaveButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/join-stage-dialog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
