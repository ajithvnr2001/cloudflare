---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/icons/
title: Icons \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:01.194898+00:00
---

# Icons · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/icons/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /Icons



# Icons

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/icons/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIconCard and LinkCardIcon library

There are two icon components which pull from two different icon sets.

## Icon

The `Icon` component from Nimbus is available as a standalone component.

Primarily, this is used for Cloudflare product icons which are stored in `/src/icons/*.svg`.
    
    
    import { Icon } from "~/components";
    
    <Icon name="workers" class="text-5xl text-orange-400" />

## Card and LinkCard

Components like `Card` and `LinkCard` accept a plain `icon` string prop — any [iconify ↗︎](https://icon-sets.iconify.design/) icon name.
    
    
    import { Card, LinkCard } from "~/components";
    
    <Card title="Example" icon="ph:rocket-launch" />
    <LinkCard title="Example" href="/workers/" icon="ph:rocket-launch" />

Content authored before the Nimbus migration may still use Starlight-style icon names (for example `icon="ph:terminal-window"`). These are automatically mapped to an equivalent iconify icon at build time. New content should use iconify names directly.

## Icon library

Optionally, you can choose a corresponding icon from Starlight’s [Icons ↗︎](https://starlight.astro.build/reference/icons/#all-icons) for cards or tabs.

[PreviousGlossary tooltip](https://developers.cloudflare.com/style-guide/build-the-page/components/glossary-tooltip/)[NextInline badge](https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/icons.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
