---
url: https://developers.cloudflare.com/realtime/realtimekit/core/ios-screen-sharing/
title: iOS screen sharing \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:59.223048+00:00
---

# iOS screen sharing · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/ios-screen-sharing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)
  5. /iOS screen sharing



# iOS screen sharing

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/ios-screen-sharing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNative iOS Add a Broadcast Upload Extension Configure app groups Configure SampleHandler Update Info.plist Enable screen sharingReact Native Add a Broadcast Upload Extension Configure app groups Add screen-sharing sources through the Podfile Configure SampleHandler Update Info.plist Enable screen sharing

Configure a Broadcast Upload Extension to add screen sharing to your RealtimeKit iOS application.

## Native iOS

### Add a Broadcast Upload Extension

In Xcode, add a Broadcast Upload Extension through `File` → `New` → `Target`. Choose `iOS` → `Broadcast Upload Extension` and fill out the required information.

### Configure app groups

Add your extension to an app group:

  1. Go to your extension's target in the project.
  2. In the **Signing & Capabilities** tab, select **+**.
  3. Add **App Groups**.
  4. Add **App Groups** to your main app, using the same identifier for both targets.



### Configure `SampleHandler`

Edit your `SampleHandler` class:
    
    
    import RealtimeKit
    
    class SampleHandler: RtkSampleHandler {}

You can find the source to `RtkSampleHandler` and a full implementation of the ScreenShareExtension [on GitHub ↗︎](https://github.com/cloudflare/realtimekit-ios-core/tree/main/ScreenShareExtension).

### Update `Info.plist`

Ensure both the app and extension `Info.plist` files contain these keys:
    
    
    <key>RTKRTCAppGroupIdentifier</key>
    <string>(name of the group you have created)</string>

Add this key to the main app `Info.plist`:
    
    
    <key>RTKRTCScreenSharingExtension</key>
    <string>(Bundle Identifier of the Broadcast Upload Extension)</string>

### Enable screen sharing

Launch the Broadcast Upload Extension and enable screen sharing:
    
    
    meeting.localUser.enableScreenShare()

To stop screen sharing:
    
    
    meeting.localUser.disableScreenShare()

## React Native

### Add a Broadcast Upload Extension

In Xcode, add a Broadcast Upload Extension through `File` → `New` → `Target`. Choose `iOS` → `Broadcast Upload Extension` and fill out the required information.

### Configure app groups

Add your extension to an app group:

  1. Go to your extension's target in the project.
  2. In the **Signing & Capabilities** tab, select **+** and add **App Groups**.
  3. Add the same App Group to your main app target, using the same identifier for both.



### Add screen-sharing sources through the Podfile

The SDK includes a Ruby helper script that adds the required screen-sharing Swift source files to your Broadcast Upload Extension target. Add the following to your `Podfile`:
    
    
    # Add this line at the top
    require Pod::Executable.execute_command('node', ['-p',
      'require.resolve(
        "@cloudflare/realtimekit-react-native/ios/scripts/screenshare_sources.rb",
        {paths: [process.argv[1]]},
      )', __dir__]).strip
    
    target 'YourApp' do
      ...
      post_install do |installer|
        ...
        # Add this line here
        add_screenshare_sources(
          installer,
          project_name: 'YourApp',              # your Xcode project name (without .xcodeproj)
          extension_target_name: 'YourAppScreenshare' # your Broadcast Upload Extension target name
        )
        ...
      end
    end
    
    target 'YourAppScreenshare' do
    # Remove the old steps added if any
    end

Then run:
    
    
    pod install

### Configure `SampleHandler`

In your Broadcast Upload Extension, edit `SampleHandler.swift`:
    
    
    class SampleHandler: RTKScreenshareHandler {
      override init() {
        super.init(
          appGroupIdentifier: "<YOUR_APP_GROUP_IDENTIFIER>",
          bundleIdentifier: "<YOUR_APP_BUNDLE_IDENTIFIER>"
        )
      }
    }

Replace `<YOUR_APP_GROUP_IDENTIFIER>` with the App Group you created. Replace `<YOUR_APP_BUNDLE_IDENTIFIER>` with your main app's bundle identifier.

### Update `Info.plist`

Add the following key to both your main app and extension `Info.plist` files:
    
    
    <key>RTCAppGroupIdentifier</key>
    <string>(YOUR_APP_GROUP_IDENTIFIER)</string>

Add this key to the main app `Info.plist` only:
    
    
    <key>RTCAppScreenSharingExtension</key>
    <string>(Bundle Identifier of the Broadcast Upload Extension)</string>

### Enable screen sharing
    
    
    meeting.self.enableScreenShare();

To stop screen sharing:
    
    
    meeting.self.disableScreenShare();

[PreviousLocal Participant](https://developers.cloudflare.com/realtime/realtimekit/core/local-participant/)[NextOverview](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/ios-screen-sharing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
