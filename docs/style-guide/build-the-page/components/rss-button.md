---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/
title: RSSButton \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:03.117873+00:00
---

# RSSButton · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /RSSButton



# RSSButton

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/rss-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExampleProps text icon changelog or href

## Example
    
    
    import { RSSButton } from "~/components";
    
    <RSSButton changelog="Workers" />
    <br />
    <RSSButton href="/custom/feed.xml" text="Custom Feed" icon="ph:arrow-square-out" />

## Props

### `text`

**type:** `string`

**default:** `"Subscribe to RSS"`

The text to display in the button.

### `icon`

**type:** `string`

**default:** `"rss"`

The icon to display next to the text. Renders via the Nimbus `Icon` component; accepts any iconify icon name (for example, `ph:rss-simple`). The default `"rss"` maps to `ph:rss-simple`.

### `changelog` or `href`

You must provide either `changelog` or `href`, but not both:

#### `changelog`

**type:** `string`

The name of the changelog to link to. This will be transformed into a lowercase, hyphen-separated string and used to construct the RSS feed URL in the format `/changelog/rss/{changelog}.xml`.

#### `href`

**type:** `string`

A custom URL to link to. Use this when you need to link to an RSS feed that doesn't follow the standard changelog URL pattern.

[PreviousResources by selector](https://developers.cloudflare.com/style-guide/build-the-page/components/resources-by-selector/)[NextRule ID](https://developers.cloudflare.com/style-guide/build-the-page/components/rule-id/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/rss-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
