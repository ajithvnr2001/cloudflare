---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-setup-view-controller/
title: RtkSetupViewController \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:00.532032+00:00
---

# RtkSetupViewController · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-setup-view-controller/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkSetupViewController



# RtkSetupViewController

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-setup-view-controller/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesUsage Examples Basic Usage With delegate

Pre-meeting setup screen view controller. Provides video preview, audio and video toggles, and name entry before joining a meeting.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meetingInfo` | `RtkMeetingInfo` | ✅ | - | Meeting configuration with auth token and media settings  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`completion` | `@escaping () -> Void` | ✅ | - | Closure called when setup completes  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`delegate` | `SetupViewControllerDelegate?` | ❌ | `nil` | Delegate notified when the participant joins the meeting  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let setupVC = RtkSetupViewController(
        meetingInfo: meetingInfo,
        meeting: rtkClient,
        completion: {
            print("Setup complete")
        }
    )
    self.present(setupVC, animated: true)

### With delegate
    
    
    import RealtimeKitUI
    
    class ViewController: UIViewController, SetupViewControllerDelegate {
        func showSetupScreen() {
            let setupVC = RtkSetupViewController(
                meetingInfo: meetingInfo,
                meeting: rtkClient,
                completion: {
                    self.dismiss(animated: true)
                }
            )
            setupVC.delegate = self
            self.present(setupVC, animated: true)
        }
    }

[PreviousRtkRecordingView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-recording-view/)[NextRtkStageActionButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-stage-action-button-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-setup-view-controller.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
