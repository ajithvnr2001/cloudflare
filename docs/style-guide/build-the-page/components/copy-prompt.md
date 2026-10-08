---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/copy-prompt/
title: CopyPrompt \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:59.867507+00:00
---

# CopyPrompt · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/copy-prompt/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /CopyPrompt



# CopyPrompt

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/copy-prompt/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImportUsage<CopyPrompt> Props text

The `CopyPrompt` component is used `1` times on `1` pages.

See all examples of pages that use CopyPrompt

Used **1** times.

**Pages**

  * [/style-guide/build-the-page/components/copy-prompt/](https://developers.cloudflare.com/style-guide/build-the-page/components/copy-prompt/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/style-guide/build-the-page/components/copy-prompt.mdx)



**Partials**




The `CopyPrompt` component displays a one-line prompt next to a **Copy prompt** button. Use it when readers can complete a task by pasting a prompt into an AI coding agent, such as a quickstart that an agent can run for them.

Build a Cloudflare Worker that returns Hello World, then deploy it with Wrangler.

Copy promptCopied!

## Import
    
    
    import { CopyPrompt } from "~/components";

## Usage
    
    
    import { CopyPrompt } from "~/components";
    
    <CopyPrompt text="Build a Cloudflare Worker that returns Hello World, then deploy it with Wrangler." />

The prompt displays on a single line and is truncated if it does not fit, but the full text is always copied. Keep prompts short so readers can see what they are copying. For longer prompts, use a [code block](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/code-block-guidelines/) with `txt` as the language instead.

## `<CopyPrompt>` Props

### `text`

**type:** `string`

The prompt to display. Selecting **Copy prompt** copies this text to the clipboard.

[PreviousCfNamespace](https://developers.cloudflare.com/style-guide/build-the-page/components/cf-namespace/)[NextCURL](https://developers.cloudflare.com/style-guide/build-the-page/components/curl/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/copy-prompt.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
