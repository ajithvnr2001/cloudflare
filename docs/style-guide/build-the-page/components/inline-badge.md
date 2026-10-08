---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/
title: Inline badge \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:01.143963+00:00
---

# Inline badge · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /Inline badge



# Inline badge

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewComponentInputs Presets Text Variant

The `InlineBadge` component is used `10` times on `10` pages.

See all examples of pages that use InlineBadge

Used **10** times.

**Pages**

  * [/agents/communication-channels/voice/](https://developers.cloudflare.com/agents/communication-channels/voice/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/agents/communication-channels/voice.mdx)
  * [/agents/examples/browser-agent/](https://developers.cloudflare.com/agents/examples/browser-agent/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/agents/examples/browser-agent.mdx)
  * [/agents/examples/voice-agent/](https://developers.cloudflare.com/agents/examples/voice-agent/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/agents/examples/voice-agent.mdx)
  * [/agents/tools/browser/](https://developers.cloudflare.com/agents/tools/browser/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/agents/tools/browser.mdx)
  * [/browser-run/features/session-recording/](https://developers.cloudflare.com/browser-run/features/session-recording/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/browser-run/features/session-recording.mdx)
  * [/ddos-protection/about/attack-coverage/](https://developers.cloudflare.com/ddos-protection/about/attack-coverage/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/ddos-protection/about/attack-coverage.mdx)
  * [/ssl/edge-certificates/geokey-manager/setup/](https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/ssl/edge-certificates/geokey-manager/setup.mdx)
  * [/stream/stream-live/start-stream-live/](https://developers.cloudflare.com/stream/stream-live/start-stream-live/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/stream/stream-live/start-stream-live.mdx)
  * [/stream/viewing-videos/using-the-stream-player/](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/stream/viewing-videos/using-the-stream-player/index.mdx)
  * [/workers/wrangler/commands/artifacts/](https://developers.cloudflare.com/workers/wrangler/commands/artifacts/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/workers/wrangler/commands/artifacts.mdx)



**Partials**




Recommendation: Avoid inline badges

Our current recommendation is to avoid inline badges, since they may hurt readability.

Guidelines:

  * Mention beta/alpha/early access in the feature's main documentation page (use the [`<Badge>`](https://developers.cloudflare.com/style-guide/build-the-page/components/badges/) component for this purpose).
  * If an additional reference is needed in the middle of the text, use "(beta)", with no special formatting, after the feature name.
  * For instructions related to the feature (such as instructions on turning the feature on or off), you may mention again it's in beta, and also include "(beta)" in the side nav.



## Component

To adopt this styling in a React component, apply the `sl-badge` class to a `span` element.
    
    
    import { InlineBadge } from '~/components';
    
    ### Alpha <InlineBadge preset="alpha" />
    
    ### Beta <InlineBadge preset="beta" />
    
    ### Deprecated <InlineBadge preset="deprecated" />
    
    ### Early Access <InlineBadge preset="early-access" />
    
    ### Legacy <InlineBadge preset="legacy" />
    
    ### Default <InlineBadge text="Default" />

## Inputs

Either `preset` or `text` and `variant` must be specified.

### Presets

  * `alpha`

    * **Text** : `Alpha`
    * **Variant** `success`
  * `beta`

    * **Text** : `Beta`
    * **Variant** `caution`
  * `deprecated`

    * **Text** : `Deprecated`
    * **Variant** `danger`
  * `early-access`

    * **Text** : `Early Access`
    * **Variant** `note`
  * `legacy`

    * **Text** : `Legacy`
    * **Variant** `danger`



### Text

Any string.

### Variant

  * `note`

    * **Color** : Blue
  * `tip`

    * **Color** : Purple
  * `danger`

    * **Color** : Red
  * `caution`

    * **Color** : Orange
  * `success`

    * **Color** : Green



[PreviousIcons](https://developers.cloudflare.com/style-guide/build-the-page/components/icons/)[NextLink cards](https://developers.cloudflare.com/style-guide/build-the-page/components/link-cards/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/inline-badge.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
