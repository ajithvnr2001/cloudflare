---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/
title: Subtract IP calculator \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:03.732930+00:00
---

# Subtract IP calculator · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /Subtract IP calculator



# Subtract IP calculator

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImportUsage<SubtractIPCalculator> Props defaults

The `SubtractIPCalculator` component is used `6` times on `5` pages.

See all examples of pages that use SubtractIPCalculator

Used **6** times.

**Pages**

  * [/cloudflare-one/networks/routes/reserved-ips/](https://developers.cloudflare.com/cloudflare-one/networks/routes/reserved-ips/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/cloudflare-one/networks/routes/reserved-ips.mdx)
  * [/style-guide/build-the-page/components/subtract-ip-calculator/](https://developers.cloudflare.com/style-guide/build-the-page/components/subtract-ip-calculator/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/style-guide/build-the-page/components/subtract-ip-calculator.mdx)



**Partials**

  * [src/content/partials/cloudflare-one/tunnel/deployment-guides/cloud-private-ip.mdx](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/cloudflare-one/tunnel/deployment-guides/cloud-private-ip.mdx)
  * [src/content/partials/cloudflare-one/tunnel/warp-to-tunnel-route-ips.mdx](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/cloudflare-one/tunnel/warp-to-tunnel-route-ips.mdx)
  * [src/content/partials/cloudflare-one/warp/add-split-tunnels-route.mdx](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/partials/cloudflare-one/warp/add-split-tunnels-route.mdx)



## Import
    
    
    import { SubtractIPCalculator } from "~/components";

## Usage

  


Base CIDRSubtracted CIDRs

Calculate
    
    
    import { SubtractIPCalculator } from "~/components";
    
    <SubtractIPCalculator client:load />

## `<SubtractIPCalculator>` Props

### `defaults`

**type:** `object`

An optional object containing `base` (`string`) and `subtract` (`string[]`) properties, to set default inputs.

**example:**

Base CIDRSubtracted CIDRs

Calculate
    
    
    import { SubtractIPCalculator } from "~/components";
    
    <SubtractIPCalculator
    	client:load
    	defaults={{
    		base: "10.0.0.0/8",
    		subtract: ["10.0.0.0/24", "10.32.0.0/11"]
    	}}
    />

[PreviousStream](https://developers.cloudflare.com/style-guide/build-the-page/components/stream/)[NextTabs](https://developers.cloudflare.com/style-guide/build-the-page/components/tabs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/subtract-ip-calculator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
