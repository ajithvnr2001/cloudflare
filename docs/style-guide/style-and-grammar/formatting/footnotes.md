---
url: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/
title: Footnotes \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:12.293157+00:00
---

# Footnotes · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Style and grammar](https://developers.cloudflare.com/style-guide/style-and-grammar/)

  4. /[Formatting](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/)
  5. /Footnotes



# Footnotes

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/footnotes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Hover-activated footnotes Plain text footnotes

Use footnotes to add details or context about something without distracting from the main content. We recommend using hover-activated footnotes, but you can also use plain text.

### Hover-activated footnotes

To add hover-activated footnotes, use the following syntax:
    
    
    This is a sentence with a footnote.[^1]
    
    [^1]: A footnote adds details or context.

With this type of footnote, you can add the numbers to the MDX file in any order and they will still display in numerical order on the page.

The hover ability of this type of footnote is powered by [tippy.js ↗︎](https://atomiks.github.io/tippyjs/).

Caution

Do not use this syntax inside `<Tabs>` blocks or in partials included inside `<Tabs>` blocks. It generates a `## Footnotes` heading inside each tab panel, which repeats across tabs and breaks agent-readable documentation. Use plain text footnotes or inline the text instead.

### Plain text footnotes

To add plain text footnotes, use the syntax in this example:
    
    
    This is a sentence with a footnote.<sup>1</sup>
    
    <sup>1</sup> A footnote adds details or context.

With this type of footnote, you can add the footnote note anywhere on the page. We recommend adding it to the bottom of the section or table where the footnote is referenced or to the bottom of the page.

[PreviousFile types and extensions](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/file-types-and-extensions/)[NextKeyboard keys](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/keyboard-keys/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/style-and-grammar/formatting/footnotes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
