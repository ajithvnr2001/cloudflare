---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-title-label/
title: RtkMeetingTitleLabel \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:58.931570+00:00
---

# RtkMeetingTitleLabel · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-title-label/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkMeetingTitleLabel



# RtkMeetingTitleLabel

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-title-label/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With custom appearance

A label that displays the meeting title from the meeting metadata.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance for the active meeting  
`appearance` | `RtkTextAppearance` | ❌ | `AppTheme.shared.meetingTitleAppearance` | Text appearance configuration for font and color  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let titleLabel = RtkMeetingTitleLabel(meeting: rtkClient)
    view.addSubview(titleLabel)

### With custom appearance
    
    
    import RealtimeKitUI
    
    let appearance = RtkTextAppearance(
        font: UIFont.systemFont(ofSize: 18, weight: .bold),
        textColor: .white
    )
    let titleLabel = RtkMeetingTitleLabel(
        meeting: rtkClient,
        appearance: appearance
    )
    view.addSubview(titleLabel)

[PreviousRtkMeetingNameTag](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-name-tag/)[NextRtkMoreButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-button-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-title-label.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
