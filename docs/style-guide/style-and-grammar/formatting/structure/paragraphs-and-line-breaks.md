---
url: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/
title: Paragraphs and line breaks \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:12.772251+00:00
---

# Paragraphs and line breaks · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Style and grammar](https://developers.cloudflare.com/style-guide/style-and-grammar/)[Formatting](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/)

  4. /[Structure](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/)
  5. /Paragraphs and line breaks



# Paragraphs and line breaks

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewParagraphs in MarkdownLine breaks in Markdown

## Paragraphs in Markdown

To start a new paragraph, leave an empty line (with no spaces) before adding the new paragraph content.
    
    
    This sentence is the first one in this paragraph.
    This second sentence also belongs to the first paragraph.
    
    This is the first sentence of the second paragraph.

## Line breaks in Markdown

Avoid line breaks when possible. Considering creating a separate paragraph, even inside numbered lists.

If you need to add a line break, use the `<br/>` HTML element.

Example inside a table:
    
    
    | Feature                          | Enabled |
    |----------------------------------|---------|
    | Feature name<br/>Additional info | Yes     |

This is how the table looks:

Feature | Enabled  
---|---  
Feature name  
Additional info | Yes  
  
Caution

Do not use two spaces at the end of a sentence to create a forced line break. Although this Markdown syntax is supported, it is not immediately visible and can easily miss these line breaks during peer reviews.

[PreviousLists](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/lists/)[NextSentence structure](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/sentence-structure/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/style-and-grammar/formatting/structure/paragraphs-and-line-breaks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
