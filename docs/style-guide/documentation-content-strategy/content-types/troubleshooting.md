---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/troubleshooting/
title: Troubleshooting \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:10.062201+00:00
---

# Troubleshooting · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)

  4. /[Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/)
  5. /Troubleshooting



# Troubleshooting

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use itTitle & descriptionScaffold this pageComponent guidanceFrontmatterOrganizing entriesWriting for AI and agents

A troubleshooting page pairs each failure a reader hits with its cause and the steps that resolve it, organized by symptom rather than by question. The tone is guiding, straightforward, and solution-oriented.

## When to use it

Troubleshooting lives in two places: inline as a "What if ..." callout or accordion on the page where the failure happens, and on a dedicated troubleshooting page per product area once the inline entries pass roughly five or the same failure spans several pages. Reach for it to help a reader recover from a failure. It is not:

  * **A how-to.** A how-to pursues a goal, whereas troubleshooting recovers from a failure.
  * **An error reference.** A complete per-code catalog is reference material. This page covers symptoms, multi-cause problems, and the "it is slow or flaky" cases that error codes do not capture.
  * **A global FAQ.** A troubleshooting page is organized by failure, not by question.



For the full comparison, refer to [Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/).

## Title & description

  * **Page title** : "Troubleshooting" followed by the product, feature, or area, as in "Troubleshooting delivery".
  * **Entry titles** : the verbatim symptom, ideally the exact error message, because "Error: signature timestamp outside tolerance" beats "Signature problems" in search and in a sidebar scan. Trim a long message to its distinctive substring of roughly 70 characters with an ASCII "..." marking the cut, and keep the message type such as "Error:". A symptom with no message gets observable phrasing, as in "Deliveries succeed but arrive twice".
  * **Description** : state that the page fixes the common failures in the area, by symptom.



## Scaffold this page

Use the Nimbus troubleshooting recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:

npmyarnpnpm
    
    
    npx @cloudflare/nimbus-docs add content-troubleshooting
    
    
    yarn @cloudflare/nimbus-docs add content-troubleshooting
    
    
    pnpm @cloudflare/nimbus-docs add content-troubleshooting

Adapt the frontmatter the recipe emits to Cloudflare's schema: set [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type) and `products` instead of the generic fields the recipe emits, such as `type`.

## Component guidance

  * **Fenced code blocks** carry the verbatim error message, the match target for search, readers, and retrieval. Show one realistic concrete instance with real values, and never paraphrase the message or elide its distinctive part.
  * **Bold Cause, Fix, and Verify labels** give every entry the same internal order, so a panicking reader can skip straight to the fix.
  * [**Details**](https://developers.cloudflare.com/style-guide/build-the-page/components/details/) accordions fit the inline form at a feature page's end, but on a dedicated page the entries stay open, because a hidden symptom is unfindable.
  * **What does not fit:** Cards, a marketing tone, and reassurance offered without a fix.



## Frontmatter
    
    
    pcx_content_type: troubleshooting
    products:
      - product-a
      - product-b

For more details, refer to [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type).

## Organizing entries

Order entries by frequency, most common failure first, and let a data-loss failure jump the queue. Keep troubleshooting inline until a product area passes roughly five entries, then move it to a dedicated page and leave a link behind at the inline site. Every workaround states its cost and names its permanent alternative. A dedicated page ends with a "Still stuck?" section that gives the escalation path and a collect-this-first list, which is the type's honesty clause: a page implying completeness strands the reader with the one failure it missed.

## Writing for AI and agents

  * **Self-contained entries.** Write each entry so it stands alone, because entry N is retrieved without the entry before it and without the page intro. Give it the full symptom, cause, and fix.
  * **Executable fixes.** Structure cause and fix as declaratives an agent can run: "check your configuration" is not a fix, a concrete command such as `hookline test-event --endpoint <id>` is.
  * **Verbatim symptoms.** Show the error message verbatim in a fenced block as one concrete instance, so search, readers, and retrieval all match on the literal text.



[PreviousReference](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference/)[NextFAQ](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/content-types/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
