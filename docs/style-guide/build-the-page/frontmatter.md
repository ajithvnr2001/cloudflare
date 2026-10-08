---
url: https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/
title: Frontmatter \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:07.686140+00:00
---

# Frontmatter · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)
  4. /Frontmatter



# Frontmatter

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequired fieldsWriting a description ExamplesOptional fields

Frontmatter contains the metadata for a page, such as the `title`. It is written as YAML, between `---`, at the top of the page.

For example:
    
    
    ---
    title: Create a Cloudflare Tunnel
    pcx_content_type: how-to
    products:
      - cloudflare-tunnel
    description: Set the required and optional frontmatter fields that carry a page's metadata, such as title, description, and pcx_content_type.
    sidebar:
      order: 2
    ---

For more information on the available fields, refer to [Nimbus's documentation ↗︎](https://nimbus-docs.com/writing/frontmatter/).

## Required fields

Every page with a `pcx_content_type` must include:

Field | Description  
---|---  
`title` | The page title. Plain text.  
`pcx_content_type` | The content type of the page. Refer to [content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/).  
`description` | A 1-2 sentence summary used for the `<meta name="description">` tag. Refer to writing a description.  
  
## Writing a description

The `description` field populates the `<meta name="description">` tag in the HTML head. This is the single most important metadata field for search engines, AI crawlers, and `llms.txt` consumers when deciding whether to surface or cite a page.

A strong description:

  * Is 1-2 self-contained sentences (aim for 50-160 characters).
  * Names the product or feature.
  * States what the page helps the reader do or understand.
  * Works as a standalone answer snippet when extracted from the page.



Do not start with generic openers like "This page describes...", "Learn more about...", or "This document explains...". These waste the most valuable metadata space without adding information.

The existing `summary` field remains useful for the on-page experience but is secondary to `description` for AI and search purposes.

### Examples

Weak description (generic, not extractable)yaml
    
    
    description: Set the required and optional frontmatter fields that carry a page's metadata, such as title, description, and pcx_content_type.

Strong description (self-contained, citable)yaml
    
    
    description: Set the required and optional frontmatter fields that carry a page's metadata, such as title, description, and pcx_content_type.

Weak description (repeats title)yaml
    
    
    description: Set the required and optional frontmatter fields that carry a page's metadata, such as title, description, and pcx_content_type.

Strong description (adds value beyond the title)yaml
    
    
    description: Set the required and optional frontmatter fields that carry a page's metadata, such as title, description, and pcx_content_type.

## Optional fields

For optional fields such as `sidebar`, `tags`, `products`, `difficulty`, and `reviewed`, refer to [Custom properties](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/).

For more information on the available fields, refer to [Nimbus's documentation ↗︎](https://nimbus-docs.com/writing/frontmatter/).

[PreviousMarkdown and MDX](https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/)[NextCustom properties](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/frontmatter/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
