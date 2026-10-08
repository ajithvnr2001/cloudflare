---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-button/
title: RtkJoinButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:14.764214+00:00
---

# RtkJoinButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkJoinButton



# RtkJoinButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A button that performs the room join operation. Displays "Join" by default and changes to "Joining..." during the join process. Automatically disables after a successful join.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient, localUserNameField: EditText?` | Bind the button to the meeting state. Pass an optional `EditText` reference to validate the display name before joining — if the user has `canEditDisplayName` permission and the field is blank, the button shows a "Please enter name" toast and blocks the join.  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkJoinButton
        android:id="@+id/rtk_join_button"
        android:layout_width="wrap_content"
        android:layout_height="48dp"
        app:rtk_btn_variant="primary" />

### With Methods
    
    
    val joinButton = findViewById<RtkJoinButton>(R.id.rtk_join_button)
    val nameField = findViewById<EditText>(R.id.name_field)
    joinButton.activate(meeting, nameField)

[PreviousRtkHeaderView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/header-view/)[NextRtkJoinLivestreamButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-livestream-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/join-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
