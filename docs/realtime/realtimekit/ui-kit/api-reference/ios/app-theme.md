---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/
title: AppTheme \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:56.066114+00:00
---

# AppTheme · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /AppTheme



# AppTheme

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccessMethodsUsage Examples Access default theme Apply a custom theme

The application theme singleton that provides pre-configured appearance objects for UI components. Use `AppTheme.shared` to access default appearances or call `setUp(theme:)` to apply a custom theme.

## Access
    
    
    let theme = AppTheme.shared

## Methods

Method | Return Type | Description  
---|---|---  
`setUp(theme: AppThemeProtocol)` | `Void` | Applies a custom theme conforming to `AppThemeProtocol`  
  
## Usage Examples

### Access default theme
    
    
    import RealtimeKitUI
    
    let theme = AppTheme.shared
    let titleAppearance = theme.meetingTitleAppearance
    let clockAppearance = theme.clockViewAppearance

### Apply a custom theme
    
    
    import RealtimeKitUI
    
    class CustomTheme: AppThemeProtocol {
        // Implement required appearance properties
    }
    
    let customTheme = CustomTheme()
    AppTheme.shared.setUp(theme: customTheme)

[Previousrtk-waiting-screen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-waiting-screen/)[NextDesignLibrary](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/app-theme.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
