---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/
title: RtkDesignTokens \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:11.679934+00:00
---

# RtkDesignTokens · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkDesignTokens



# RtkDesignTokens

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage

The top-level design token container for customizing the look and feel of all UI Kit components.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`colors` | `RtkColorTokens` | ❌ | - | Color theme tokens  
`borderWidth` | `RtkBorderWidthToken` | ❌ | - | Border width token  
`borderRadius` | `RtkBorderRadiusToken` | ❌ | - | Border radius token  
  
## Usage Examples

### Basic Usage
    
    
    val designTokens = RtkDesignTokens(
        colors = RtkColorTokens(
            brand = BrandColor(
                shade300 = Color.parseColor("#497CFD"),
                shade400 = Color.parseColor("#356EFD"),
                shade500 = Color.parseColor("#2160FD"),
                shade600 = Color.parseColor("#0D52FD"),
                shade700 = Color.parseColor("#0046E5")
            ),
            background = BackgroundColor(
                shade600 = Color.parseColor("#2C2C2C"),
                shade700 = Color.parseColor("#242424"),
                shade800 = Color.parseColor("#1C1C1C"),
                shade900 = Color.parseColor("#141414"),
                shade1000 = Color.parseColor("#0C0C0C")
            )
        ),
        borderRadius = RtkBorderRadiusToken.Rounded,
        borderWidth = RtkBorderWidthToken.Thin
    )

[PreviousRtkCreatePollBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/create-poll/)[NextRtkErrorView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/error-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/design-tokens.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
