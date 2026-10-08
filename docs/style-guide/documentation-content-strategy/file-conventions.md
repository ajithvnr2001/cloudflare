---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/
title: File conventions \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:10.336312+00:00
---

# File conventions · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)
  4. /File conventions



# File conventions

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNamingFoldersContent filesImage files

Our docs have a few conventions around files.

## Naming

When creating new files, follow specific conventions for your naming.

Filenames should:

  * Semantically communicate the purpose of the file
  * Be lowercased
  * Use dashes between words

Acceptable file namestxt
    
    
    /src/content/docs/fundamentals/concepts/what-is-cloudflare.mdx
    /src/assets/images/api-shield/api-shield-call-sequence.png

Unacceptable file namestxt
    
    
    /src/content/docs/fundamentals/concepts/What is Cloudflare.mdx
    /src/content/docs/fundamentals/concepts/What-is-Cloudflare.mdx
    /src/assets/images/api-shield/API_Image_1.png

These conventions are important for user readability, SEO conventions, and making sure our GitHub actions do not break.

## Folders

Each folder should have a file named `index.mdx`.
    
    
    /src/content/docs/fundamentals/concepts/index.mdx

The content at `/src/content/docs/fundamentals/concepts/index.mdx` will be rendered at `https://developers.cloudflare.com/fundamentals/concepts/`.

## Content files

Add regular content files to the `/src/content/docs/{product_folder}/` directory.
    
    
    /src/content/docs/fundamentals/concepts/what-is-cloudflare.mdx

## Image files

Add image files to the `/src/assets/images/{product_folder}/` directory.
    
    
    /src/assets/images/api-shield/api-shield-call-sequence.png

[PreviousInformation architecture](https://developers.cloudflare.com/style-guide/documentation-content-strategy/information-architecture/)[NextOverview](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/file-conventions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
