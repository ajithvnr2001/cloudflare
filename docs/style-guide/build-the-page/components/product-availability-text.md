---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/
title: Product availability text \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:01.950529+00:00
---

# Product availability text · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /Product availability text



# Product availability text

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/product-availability-text/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropsBehavior

The `ProductAvailabilityText` component is used `2` times on `2` pages.

See all examples of pages that use ProductAvailabilityText

Used **2** times.

**Pages**

  * [/rules/cloud-connector/](https://developers.cloudflare.com/rules/cloud-connector/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/rules/cloud-connector/index.mdx)
  * [/rules/trace-request/](https://developers.cloudflare.com/rules/trace-request/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/rules/trace-request/index.mdx)



**Partials**




The `ProductAvailabilityText` component dynamically renders a product's lifecycle status (such as "Beta" or "Alpha") inline with the product name. It renders nothing for generally available (GA) products, so it is safe to leave in place as a product matures.

The `product` prop must match a file in `src/content/directory/`.
    
    
    import { ProductAvailabilityText } from "~/components";
    
    Cloud Connector <ProductAvailabilityText product="cloud-connector" /> allows you to route matching traffic to a public cloud provider.

## Props

Prop | Type | Required | Default | Description  
---|---|---|---|---  
`product` | `string` | Yes | — | Product slug matching a file in `src/content/directory/`.  
`parentheses` | `string` | No | `"true"` | When `"true"`, wraps the output in parentheses (for example, `(Beta)`). Set to `"false"` for the raw text.  
  
## Behavior

  * If the product availability is **GA** , the component renders nothing.
  * If the product or its availability data is not found, the component renders nothing (and logs a warning at build time).



[PreviousPlan](https://developers.cloudflare.com/style-guide/build-the-page/components/plan/)[NextProduct changelog](https://developers.cloudflare.com/style-guide/build-the-page/components/product-changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/product-availability-text.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
