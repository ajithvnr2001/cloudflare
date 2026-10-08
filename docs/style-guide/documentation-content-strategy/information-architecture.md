---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/information-architecture/
title: Information architecture \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:10.421073+00:00
---

# Information architecture · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/information-architecture/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)
  4. /Information architecture



# Information architecture

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/information-architecture/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequired sectionsCore sectionsStructure and ordering rulesBring an existing product into lineProduct categories

Every product's documentation is built from the same core set of sections, so a reader who knows one product's docs can predict where to find things in another.

Consistency is enforced, not optional. A product may add sections that it genuinely needs, but those additions are additive: a product never renames, restructures, or redefines a core section because a different shape "makes more sense" for it. Keep the core the same, and grow around it.

This page defines the shared core at the section (folder) level. To choose the type of an individual page, refer to [Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/).

## Required sections

Every product includes at least these two pages, from its first release:

  * [Overview](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/overview/), which orients a new reader and routes them onward.
  * [Get started](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/get-started/), which takes a new user from nothing to a first working result.



## Core sections

Beyond the required pair, use these standard sections whenever your product has the content they describe. Use the standard name so that readers and agents navigate every product's docs the same way.

Section | What it contains | Related content type  
---|---|---  
Overview | Orients a new reader to the product and routes them onward. Required. | [Overview](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/overview/)  
Get started | The shortest path from nothing to a first working result. Required. | [Get started](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/get-started/)  
Concepts | What the product's key ideas are and why they work the way they do. | [Concept](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/concept/)  
Features | Groups the task and settings content for a major feature of the product. | [How to](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/how-to/)  
Guides | Task-focused pages for completing one specific job. | [How to](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/how-to/)  
Tutorials | End-to-end lessons where the reader builds a real project. | [Tutorial](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/tutorial/)  
Examples | Complete, runnable samples that show how something is done. | None  
Configuration | The settings, values, and options for a configuration-intensive feature. | [Configuration](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/)  
Reference | Complete, neutral lookup details such as parameters, values, and options. | [Reference](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference/)  
API | The product's API documentation and command guidance. | [API content strategy](https://developers.cloudflare.com/style-guide/api-content-strategy/)  
Models | The available models and their details, for AI products. | [Reference](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference/)  
Observability | Testing, metrics, analytics, and local development. | None  
Best practices | Recommended patterns and guidance for using the product well. | None  
Platform | Product-wide pages such as pricing, limits, changelog, betas, and known issues. | [Changelog](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/changelog/)  
Glossary | The product's defined terms. | [Glossary](https://developers.cloudflare.com/style-guide/build-the-page/components/glossary/)  
  
## Structure and ordering rules

  * Keep the Overview at the product root `index.mdx`. Make every other core section a folder, even when it currently holds a single page. A lone `get-started.mdx` becomes a `get-started/` folder.
  * Place the core folders before any product-specific folders, in the order given under Core sections.
  * Give every product a Platform folder that holds at least one page, so this section is present consistently rather than only on some products.
  * Name any product-specific folder uniquely and clearly. A product-specific folder is additive: it adds to the core, and it never replaces or reshapes a core section.
  * Add sections freely, but do not edit the core. If a core section does not fit your product as written, raise it through docs governance rather than renaming or restructuring it locally.



## Bring an existing product into line

Audit the product against the core, then close the gaps:

  * Rename non-standard folders to the standard names. For example, rename a `getting-started` folder to `get-started`, and rename a `how-to` folder to the standard `guides`.
  * Fold loose files into their core folder. A single `concepts.mdx` becomes a `concepts/` folder.
  * Pull core content up to the top level when it sits inside `platform/` but belongs to a core section.
  * Create the core sections your product is missing.
  * Keep useful product-specific folders, and confirm each one is uniquely named and additive.



## Product categories

The core applies across every product category, including Compute, Storage, AI, Media, and the vertical products. A category can share additional sections that its products all need. For example, AI products commonly add a Models section. As a product matures it keeps the same core and grows by adding sections, not by reshaping the core.

[PreviousReference architecture](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/)[NextFile conventions](https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/information-architecture.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
