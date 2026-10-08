---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference/
title: Reference \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:10.150583+00:00
---

# Reference · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)

  4. /[Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/)
  5. /Reference



# Reference

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use itTitle & descriptionScaffold this pageComponent guidanceFrontmatterCompleteness and source of truthWriting for AI and agents

A reference page enumerates the facts about one nameable surface, such as a file format, a command, or a set of limits, completely and in a uniform structure. The tone is plain and straightforward.

## When to use it

Reach for a reference page when a reader needs to look up exact facts about one surface. Two laws govern the type: completeness, because a missing entry breaks a reference the way a missing word breaks a dictionary, and uniformity, because every entry answers the same questions in the same order. It is not:

  * **A how-to.** Reference describes, never instructs. A "to do this, first ..." entry means you extract a how-to and link it.
  * **A concept.** Opinion and rationale live on the concept page, so one orienting sentence with a concept link is the whole prose allowance at the top.
  * **A dumping ground.** "Miscellaneous" is where facts go to become unfindable. Keep one surface per page and mirror the product's own structure.



For the full comparison, refer to [Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/). For live examples, refer to [Common Cf-Polished statuses](https://developers.cloudflare.com/images/polish/cf-polished-statuses/) and [Logpush API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/).

## Title & description

  * **Title** : the surface's name as the reader searches for it, such as "CLI commands", "Event types", or "Limits". Use "Reference" for a single standalone page, use nouns for a section with child pages, and add "reference" to a noun only when the bare name is ambiguous, as in "Retry policy reference".
  * **Description** : name the entry kinds the surface accepts and the fact categories each entry lists.



## Scaffold this page

Use the Nimbus reference recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:

npmyarnpnpm
    
    
    npx @cloudflare/nimbus-docs add content-reference
    
    
    yarn @cloudflare/nimbus-docs add content-reference
    
    
    pnpm @cloudflare/nimbus-docs add content-reference

Adapt the frontmatter the recipe emits to Cloudflare's schema: set [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type) and `products` instead of the generic fields the recipe emits, such as `type`.

## Component guidance

  * [**Tables**](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/tables/) are the signature component: a quick-reference table before the entries makes the common lookup zero-scroll. Keep tables simple, because merged cells and meaning-by-layout break both scanning and extraction.
  * **Definition lines** carry the same facts in a fixed order, such as type, default, required, and constraints, bolded or badged consistently across every entry.
  * [**DirectoryListing**](https://developers.cloudflare.com/style-guide/build-the-page/components/directory-listing/) links the child pages when the reference is a section rather than a single page.
  * **What does not fit:** Steps, Cards, and callouts (a fact that needs a warning usually belongs in the entry as a constraint), plus tabs or accordions that hide entries (a collapsed entry is invisible to search-and-grab readers and to extraction).



## Frontmatter
    
    
    pcx_content_type: reference
    products:
      - product-a
      - product-b

For more details, refer to [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type).

## Completeness and source of truth

A reference is complete or clearly scoped, with nothing in between, so if a subset lives elsewhere the first line says where. Give every fact exactly one source: generate values that live in code or a schema, and where generation does not yet exist, name the source so maintainers know what to diff against. Hand-maintained fact pages such as limits or quotas carry a visible `reviewed` date. When a surface passes roughly 30 entries, split it along its own seams, such as file layout or command groups, never alphabetically.

## Writing for AI and agents

  * **Self-identifying entries.** Give every entry heading its full name, such as the dotted path `retry.max_attempts` rather than `max_attempts` under a "Retry" heading, so a retrieved chunk carries its own identity.
  * **Machine-checkable values.** State ranges, defaults, and limits as literal values rather than "a reasonable number", and keep examples minimal in fenced blocks with realistic values.
  * **Nothing hidden.** Keep every entry in the open, because a collapsed or tabbed entry is invisible to extraction. The Markdown twin of a reference page is the page.



[PreviousConfiguration](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/)[NextTroubleshooting](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/content-types/reference.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
