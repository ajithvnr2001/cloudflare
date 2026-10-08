---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participants/
title: RtkParticipantsFragment \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:15.985638+00:00
---

# RtkParticipantsFragment · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participants/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkParticipantsFragment



# RtkParticipantsFragment

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participants/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage

A component which lists all participants, with the ability to run privileged actions on each participant according to your permissions.

## Methods

Method | Parameters | Description  
---|---|---  
`show` | `fragmentManager: FragmentManager, tag: String?` | Display the participant list bottom sheet  
  
## Usage Examples

### Basic Usage
    
    
    val rtkParticipantsFragment = RtkParticipantsFragment()
    rtkParticipantsFragment.show(fragmentManager, "PARTICIPANTS_TAG")

[PreviousRtkParticipantCountView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-count-view/)[NextRtkParticipantTileView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-tile-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/participants.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
