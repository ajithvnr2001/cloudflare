---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/
title: DesignLibrary \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:56.209141+00:00
---

# DesignLibrary · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /DesignLibrary



# DesignLibrary

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccessPropertiesUsage Examples Access design tokens

The central design token library providing color, spacing, border width, and border radius tokens. Access through the `DesignLibrary.shared` singleton.

## Access
    
    
    let designLibrary = DesignLibrary.shared

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`color` | `ColorTokens` | - | - | Color tokens for backgrounds, text, and brand colors  
`space` | `SpaceToken` | - | - | Spacing tokens for margins and padding  
`borderSize` | `BorderWidthToken` | - | - | Border width tokens  
`borderRadius` | `BorderRadiusToken` | - | - | Border radius tokens for corner rounding  
  
## Usage Examples

### Access design tokens
    
    
    import RealtimeKitUI
    
    let designLibrary = DesignLibrary.shared
    
    // Access color tokens
    let backgroundColor = designLibrary.color.background
    let textColor = designLibrary.color.text
    
    // Access spacing tokens
    let padding = designLibrary.space.space4
    
    // Access border tokens
    let borderWidth = designLibrary.borderSize.thin
    let cornerRadius = designLibrary.borderRadius.rounded

[PreviousAppTheme](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/)[NextGridView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/grid-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/design-library.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
