---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/get-started/
title: Get started \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:09.703435+00:00
---

# Get started · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)

  4. /[Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/)
  5. /Get started



# Get started

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use itTitle & descriptionScaffold this pageComponent guidanceFrontmatterExamplesWriting for AI and agents

A get-started page takes a new user from not using a product to a first working setup by the shortest honest path. The tone is instructional and encouraging.

## When to use it

Write a get-started page when a new user needs the shortest path from nothing to one working result, before they explore the product in depth. It is not:

  * **A how-to.** A how-to completes one specific task for a reader who already uses the product, whereas a get-started page delivers a new user's first success end to end.
  * **A tutorial.** A tutorial teaches through a longer guided project, whereas a get-started page stops at the first working result and routes the reader onward.



For the full comparison, refer to [Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/).

## Title & description

  * **Title** : the page title is Get started.
  * **Description** : name the product, summarize the first setup the reader completes, and note the key prerequisites.



## Scaffold this page

Use the Nimbus get-started recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:

npmyarnpnpm
    
    
    npx @cloudflare/nimbus-docs add content-quickstart
    
    
    yarn @cloudflare/nimbus-docs add content-quickstart
    
    
    pnpm @cloudflare/nimbus-docs add content-quickstart

Adapt the frontmatter the recipe emits to Cloudflare's schema: set [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type) and `products` instead of the generic fields the recipe emits, such as `type`.

## Component guidance

  * [**Prerequisites**](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/prerequisites/) list what the reader needs before starting, such as an active zone, a subscription or plan, or setup outside Cloudflare.
  * [**Steps**](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/steps-tasks-procedures/) lead the reader to product adoption, covering the minimum setup plus the most general use case, and often reuse partials from the how-to pages.
  * [**Links**](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/links/) close the page with next steps that point the reader toward deeper configuration once they have a working setup.
  * **What does not fit:** exhaustive configuration or edge cases. Keep those in how-tos and reference pages, and link to them.



## Frontmatter
    
    
    pcx_content_type: get-started
    products:
      - product-a
      - product-b

For more details, refer to [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type).

## Examples

  * [Waiting Room: Get started](https://developers.cloudflare.com/waiting-room/get-started/)



## Writing for AI and agents

  * **Shortest honest path.** Include only the steps that reach a first working result, because a get-started page is judged by how quickly a reader or agent reaches success, not by coverage.
  * **Show the result.** State and show the working outcome the steps produce, so a reader or agent can verify success before moving on.
  * **Complete prerequisites.** State exactly what the reader needs before starting, because an agent cannot begin a setup it is not equipped to reach.



[PreviousOverview](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/overview/)[NextConcept](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/concept/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/content-types/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
