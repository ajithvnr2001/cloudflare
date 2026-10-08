---
url: https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/
title: Banner \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:08.118334+00:00
---

# Banner · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/

Do **not** use banners in the [Frontmatter](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/) unless a change will cause customer application to break.

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Frontmatter](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/)
  5. /Banner



# Banner

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExampleStyles / Types Note Tip Caution Danger Default

One of the fields you can add to the [Frontmatter](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/) is `banner`. It displays a prominent section at the top of the page and supports the use of HTML for links and formatting.

Only use it to alert about disruptive situations and take note to remove it when applicable.

## Example
    
    
    ---
    title: Banner
    description: How to display a banner at the top of the page and when to use it.
    banner:
      content: Do <strong>not</strong> use banners in the <a href="/style-guide/build-the-page/frontmatter/">Frontmatter</a> unless a change will cause customer application to break.
    ---

## Styles / Types

### Note

The note banner is used to alert about important information.
    
    
    ---
    title: Banner
    description: How to display a banner at the top of the page and when to use it.
    banner:
      content: Ensure you read this!
      type: note
    ---

### Tip

The tip banner is used to alert about important suggestions.
    
    
    ---
    title: Banner
    description: How to display a banner at the top of the page and when to use it.
    banner:
      content: Consider this alternative!
      type: tip
    ---

### Caution

The caution banner is used to warn readers of upcoming disruptive changes.
    
    
    ---
    title: Banner
    description: How to display a banner at the top of the page and when to use it.
    banner:
      content: This is deprecated and will break on <strong>1970-01-01</strong>!
      type: caution
    ---

### Danger

The danger banner is used to alert about errors.
    
    
    ---
    title: Banner
    description: How to display a banner at the top of the page and when to use it.
    banner:
      content: This has been removed!
      type: danger
    ---

### Default

The default banner is used in all other circumstances.
    
    
    ---
    title: Banner
    description: How to display a banner at the top of the page and when to use it.
    banner:
      content: Do <strong>not</strong> use banners in the <a href="/style-guide/build-the-page/frontmatter/">Frontmatter</a> unless a change will cause customer application to break.
    ---

[PreviousCustom properties](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/)[NextSidebar](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/sidebar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/frontmatter/banner.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
