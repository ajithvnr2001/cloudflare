---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/cf-namespace/
title: CfNamespace \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:59.163282+00:00
---

# CfNamespace · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/cf-namespace/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /CfNamespace



# CfNamespace

Last updated Sep 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/cf-namespace/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImportUsageArguments

The `CfNamespace` component is used `0` times on `0` pages.

See all examples of pages that use CfNamespace

Used **0** times.

**Pages**




**Partials**




The `CfNamespace` component documents every visible command in a Cloudflare CLI namespace using metadata from the version of `cf` installed in the [`cloudflare-docs` repository ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/package.json).

## Import
    
    
    import { CfNamespace } from "~/components";

## Usage
    
    
    import { CfNamespace } from "~/components";
    
    <CfNamespace namespace="hyperdrive" />

## Arguments

`namespace` `string` required is the namespace without the `cf` prefix, such as `hyperdrive`.

`headingLevel` `number` (default: 2) optional sets the heading level for each command name.

[PreviousCfCommand](https://developers.cloudflare.com/style-guide/build-the-page/components/cf-command/)[NextCopyPrompt](https://developers.cloudflare.com/style-guide/build-the-page/components/copy-prompt/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/cf-namespace.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
