---
url: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/
title: How it works \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:58.345793+00:00
---

# How it works · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features

  4. /[Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/)
  5. /How it works



# How it works

Last updated Jul 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPre-processing HTML Images PDFs

## Pre-processing

When parsing files before converting them to Markdown, there are some cleanup tasks we do depending on the type of file you are trying to convert.

### HTML

When we detect an HTML file, a series of things happen to the HTML content before it is converted:

  * Some elements are ignored, including `script` and `style` tags.
  * Meta tags are extracted. These include `title`, `description`, `og:title`, `og:description` and `og:image`.
  * [JSON-LD ↗︎](https://json-ld.org/) content is extracted, if it exists. This will be appended at the end of the converted markdown.
  * The base URL to use for resolving relative links is extracted from the `<base>` element1, if it exists, according to the spec (that is, only the first instance of the base URL is counted).
  * If the `cssSelector` option is: 
    * present, then only those elements that match the selector are kept for further processing;
    * missing, then elements such as `<header>`, `<footer>` and `<head>` are removed from the text.
  * If a base URL was obtained previously, relative links in the remaining HTML are resolved to fully qualified URLs



1 The host can also be set per request, using the HTML conversion options. Refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/#html) for more details.

### Images

Images take a bit more work to prepare for conversion.

For animated GIF files, only the first frame is extracted and analyzed. The remaining frames are discarded.

As a first step, we detect what type the image is. If it is an SVG (Scalable Vector Graphics) file, we need to convert it into a raster format so that using the necessary Workers AI models does not fail. In this case, SVGs are converted into PNGs internally.

Afterwards:

  * We try to determine the image's dimensions. If successful, we determine if the image is considered "too big" or not. An image is "too big" if its width is bigger than 1280px or its height is bigger than 720px.
  * If the image is too big, we try to resize it to conform with those dimensions. If resizing fails, we simply try to use the original image data
  * The image is sent to an **object-detection model**. Specifically, we use the [`@cf/facebook/detr-resnet-50`](https://developers.cloudflare.com/workers-ai/models/detr-resnet-50/) from Workers AI.
  * If any objects were detected in the previous step, they are appended to a prompt that is used to instruct an **image-to-text model** on how to describe the image.
  * If a preferred conversion language is specified in the request's conversion options, the previous prompt is enriched with a directive for the model to output the content in the desired language. Refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/#images) for more details.
  * The final prompt is sent, along with the image data, to the [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/) model, also from Workers AI.



### PDFs

  * Metadata is extracted. This can be removed from the final result. Refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/#pdf) for more details.
  * Each page is parsed in sequence.
  * We try to obtain a `StructTree` object from the PDF file. This data structure is a tree of tagged elements that make up the PDF contents, as specified by [ISO 14289 (PDF/UA) ↗︎](https://www.iso.org/standard/64599.html).
  * If none is obtained, we extract the text of the page _as-is_ and return it.
  * If we manage to obtain a `StructTree`, we traverse its nodes to build a semantic Markdown representation of its contents.



[PreviousSupported Formats](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/)[NextConversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/markdown-conversion/how-it-works.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
