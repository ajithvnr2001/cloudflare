---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-command/
title: WranglerCommand \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:04.344993+00:00
---

# WranglerCommand · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-command/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /WranglerCommand



# WranglerCommand

Last updated Sep 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-command/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImportUsageWith ExtraFlagDetailsArguments

The `WranglerCommand` component is used `96` times on `7` pages.

See all examples of pages that use WranglerCommand

Used **96** times.

**Pages**

  * [/workers/wrangler/commands/certificates/](https://developers.cloudflare.com/workers/wrangler/commands/certificates/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/workers/wrangler/commands/certificates.mdx)
  * [/workers/wrangler/commands/general/](https://developers.cloudflare.com/workers/wrangler/commands/general/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/workers/wrangler/commands/general.mdx)
  * [/workers/wrangler/commands/secrets-store/](https://developers.cloudflare.com/workers/wrangler/commands/secrets-store/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/workers/wrangler/commands/secrets-store.mdx)
  * [/workers/wrangler/commands/workers-for-platforms/](https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/workers/wrangler/commands/workers-for-platforms.mdx)
  * [/workers/wrangler/commands/workers/](https://developers.cloudflare.com/workers/wrangler/commands/workers/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/workers/wrangler/commands/workers.mdx)



**Partials**

  * [src/content/partials/workers/wrangler-commands/kv.mdx](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/workers/wrangler-commands/kv.mdx)
  * [src/content/partials/workers/wrangler-commands/r2.mdx](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/workers/wrangler-commands/r2.mdx)



The `WranglerCommand` component documents the available options for a given command.

This is generated using the Wrangler version in the [`cloudflare-docs` repository ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/package.json).

## Import
    
    
    import { WranglerCommand } from "~/components";

## Usage
    
    
    import { WranglerCommand } from "~/components";
    
    <WranglerCommand
    	command="deploy"
    	description={"Deploy a [Worker](/workers/)"}
    />
    
    <WranglerCommand command="d1 execute" />
    
    <WranglerCommand command="deploy" cfCommand="deploy" />
    
    <WranglerCommand
    	command="d1 execute"
    	cfCommand={["d1 query", "d1 raw"]}
    	includeHiddenCf
    />

## With ExtraFlagDetails

You can add or replace help text for specific flags using the `ExtraFlagDetails` component:
    
    
    import { WranglerCommand } from "~/components";
    import ExtraFlagDetails from "~/components/cf/ExtraFlagDetails.astro";
    
    <WranglerCommand command="deploy">
    	<ExtraFlagDetails key="dry-run">
    		Additional details about the dry-run flag that will be appended to the
    		original help text. Here is a [link](https://cloudflare.com) for more
    		information.
    	</ExtraFlagDetails>
    	<ExtraFlagDetails key="compatibility-date" mode="replace">
    		Custom help text that completely replaces the original description for this
    		flag.
    	</ExtraFlagDetails>
    </WranglerCommand>

## Arguments

  * `command` `string` required
    * The name of the command, i.e `d1 execute`.
  * `headingLevel` `number` (default: 2) optional
    * The heading level that the command name should be added at on the page, i.e `2` for a `h2`.
  * `description` `string` optional
    * A description to render below the command heading. If not set, defaults to the value specified in the Wrangler help API.
  * `cfCommand` `string | string[]` optional
    * One or more reviewed Cloudflare CLI equivalents without the `cf` prefix. Supplying this prop displays the shared CLI selector. Explain partial or non-equivalent workflows in the surrounding page content.
  * `includeHiddenCf` `boolean` (default: false) optional
    * Allows explicitly reviewed `cfCommand` values that the installed Cloudflare CLI marks as hidden.



[PreviousWidth](https://developers.cloudflare.com/style-guide/build-the-page/components/width/)[NextWranglerConfig](https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-config/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/wrangler-command.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
