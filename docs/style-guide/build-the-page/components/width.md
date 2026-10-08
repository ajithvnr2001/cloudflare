---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/width/
title: Width \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:04.391958+00:00
---

# Width · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/width/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /Width



# Width

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/width/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImportUsage<Width> Props size center

The `Width` component is used `8` times on `4` pages.

See all examples of pages that use Width

Used **8** times.

**Pages**

  * [/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only.mdx)
  * [/magic-transit/network-flow/](https://developers.cloudflare.com/magic-transit/network-flow/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/magic-transit/network-flow.mdx)



**Partials**

  * [src/content/partials/networking-services/mnm-magic-transit-integration.mdx](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/networking-services/mnm-magic-transit-integration.mdx)
  * [src/content/partials/style-guide/llms-txt.mdx](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/style-guide/llms-txt.mdx)



This component can be used to constrain the width of content, such as text or images.

## Import
    
    
    import { Width } from "~/components";

## Usage
    
    
    import { Width } from "~/components";
    
    <Width size="large">This content will take up 75% of the container width</Width>
    
    <Width size="medium">
    	This content will take up 50% of the container width
    </Width>
    
    <Width size="small">This content will take up 25% of the container width</Width>
    
    <Width size="small" center>
    	This content will take up 25% of the container width and be centered
    </Width>

## `<Width>` Props

### `size`

**required**

**type:** `"large" | "medium" | "small"`

Controls the width of the container:

  * `large`: 75% of container width
  * `medium`: 50% of container width
  * `small`: 25% of container width



### `center`

**type:** `boolean`

Whether to horizontally center the content.

[PreviousTypeScript example](https://developers.cloudflare.com/style-guide/build-the-page/components/typescript-example/)[NextWranglerCommand](https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-command/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/width.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
