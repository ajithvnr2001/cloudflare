---
url: https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/
title: Markdown and MDX \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:08.227804+00:00
---

# Markdown and MDX · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)
  4. /Markdown and MDX



# Markdown and MDX

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBody contentImport componentsEscape special charactersCode blocks

Cloudflare docs pages are authored in MDX, which is Markdown extended with JSX components. Every page is a `.mdx` file with a [frontmatter](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/) block at the top, followed by the body content.

## Body content

The body is standard Markdown. Use it for headings, paragraphs, lists, tables, links, and code:
    
    
    ## A heading
    
    A paragraph with a [link](/style-guide/) and `inline code`.
    
    - A list item
    - Another list item

Refer to the [formatting](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/) section for the rules that govern how to write each of these elements.

## Import components

Components add formatting that plain Markdown cannot, such as tabs, asides, and collapsible sections. Import them from `~/components` after the frontmatter block, then add them anywhere in the body:
    
    
    ---
    title: Example page
    ---
    
    import { Aside } from "~/components";
    
    <Aside type="note">This is an aside.</Aside>

Refer to the [components](https://developers.cloudflare.com/style-guide/build-the-page/components/) section for the props and requirements of each component.

## Escape special characters

MDX treats `{`, `}`, `<`, and `>` as syntax. When these characters are part of your content rather than code, wrap them in backticks so they render literally:
    
    
    Set the value to `{"key": "value"}`.

Characters inside a fenced code block are already literal and do not need escaping.

## Code blocks

Open a fenced code block with a lowercase language identifier so the code is highlighted correctly. Use `txt` for generic output that has no language:
    
    
    ```js
    const value = 1;
    ```
    
    ```txt
    Deployment complete.
    ```

[PreviousOverview](https://developers.cloudflare.com/style-guide/build-the-page/)[NextOverview](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/markdown-and-mdx.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
