---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/cf-command/
title: CfCommand \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:59.202738+00:00
---

# CfCommand · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/cf-command/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /CfCommand



# CfCommand

Last updated Sep 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/cf-command/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImportUsageArguments

The `CfCommand` component is used `0` times on `0` pages.

See all examples of pages that use CfCommand

Used **0** times.

**Pages**




**Partials**




The `CfCommand` component documents one Cloudflare CLI command using metadata from the version of `cf` installed in the [`cloudflare-docs` repository ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/package.json).

## Import
    
    
    import { CfCommand } from "~/components";

## Usage
    
    
    import { CfCommand } from "~/components";
    
    <CfCommand command="deploy" />
    <CfCommand command="auth whoami" headingLevel={3} />

## Arguments

`command` `string` required is the command without the `cf` prefix, such as `deploy` or `auth whoami`.

`headingLevel` `number` (default: 2) optional sets the heading level for the command name.

[PreviousCards](https://developers.cloudflare.com/style-guide/build-the-page/components/cards/)[NextCfNamespace](https://developers.cloudflare.com/style-guide/build-the-page/components/cf-namespace/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/cf-command.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
