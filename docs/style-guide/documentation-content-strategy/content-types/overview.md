---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/overview/
title: Overview \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:10.006081+00:00
---

# Overview · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/overview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)

  4. /[Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/)
  5. /Overview



# Overview

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/overview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use itTitle & descriptionScaffold this pageComponent guidanceFrontmatterManaging overview pagesWriting for AI and agents

An overview is the landing page a reader reaches first in a product area: it answers "what is this, and where do I start?" in one paragraph, then routes onward. The tone is accessible, welcoming, conversational, and outspoken.

## When to use it

Use an overview as the single landing page for a product or major product area, the page its sidebar section opens on. It is not:

  * **A concept page.** Move architecture and tradeoffs to a concept page and link to them. An overview orients rather than explains.
  * **A bare table of contents.** A list of links with no orientation only duplicates the sidebar.
  * **A marketing page.** The reader has already clicked into the docs.



For the full comparison, refer to [Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/). For a live example, refer to the [Argo Smart Routing overview](https://developers.cloudflare.com/argo-smart-routing/).

## Title & description

  * **Title** : the name of the product, product group, or content area, as a noun. Do not append "documentation", use a gerund phrase, or use "Introduction".
  * **Description** : name the Cloudflare product and what it does for whom in one sentence, then state the plans it is available on.



## Scaffold this page

Use the Nimbus overview recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:

npmyarnpnpm
    
    
    npx @cloudflare/nimbus-docs add content-overview
    
    
    yarn @cloudflare/nimbus-docs add content-overview
    
    
    pnpm @cloudflare/nimbus-docs add content-overview

Adapt the frontmatter the recipe emits to Cloudflare's schema: set [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type) and `products` instead of the generic fields the recipe emits, such as `type`.

## Component guidance

  * [**Cards**](https://developers.cloudflare.com/style-guide/build-the-page/components/cards/) are the signature components: this is the one type where cards are the body content, because routing is the body. Keep card text to a name plus one line, because a card that explains is a concept paragraph in a box. In the Markdown twin cards flatten to link-plus-description lists, so write the one-liners so they work in both forms.
  * **Link lists** beat cards when the grid forces padded copy, or when a group genuinely must run past the roughly five-link cap, because prose lists scan better at volume.
  * **What does not fit:** Steps (nothing is performed here), code blocks (nothing is looked up, though inline code in the orientation line is fine), and accordions (an overview with hidden content is hiding its own map).



## Frontmatter
    
    
    pcx_content_type: overview
    products:
      - product-a
      - product-b
      - product-c

For more details, refer to [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type).

## Managing overview pages

Every product or major product area must have an overview, so the answer to a weak one is always to strengthen it, never to remove it. If a page reads like a bare table of contents, add the orientation that says what the area is and where to start. Do not delete it and let the sidebar stand in.

The only page you hide is a structural group node: a folder that exists purely to group its children in the sidebar and was never a content page. You cannot delete a folder's `index.mdx` without a build error, so hide the placeholder and redirect readers past it by setting `group.hideIndex` to `true`:
    
    
    ---
    title: Placeholder
    sidebar:
      group:
        hideIndex: true
    ---

## Writing for AI and agents

  * **Self-contained orientation.** Write the opening paragraph so it stays accurate in isolation, because it is what an agent quotes when asked what the product is. Do not lean on the title or a later section to complete its meaning.
  * **Literal availability.** State availability with literal plan, region, or release-stage names rather than a paraphrase.
  * **Load-bearing links.** Use real, current routes, because a stale route here strands a reader at the front door.



[PreviousAll content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/)[NextGet started](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/content-types/overview.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
