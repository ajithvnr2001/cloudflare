---
url: https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/
title: Enable flexible variants \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:35.614252+00:00
---

# Enable flexible variants · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Optimization

  4. /Hosted images
  5. /Enable flexible variants



# Enable flexible variants

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable flexible variants via the Cloudflare dashboardEnable flexible variants via the API

Flexible variants allow you to create variants with dynamic resizing which can provide more options than regular variants allow. This option is not enabled by default.

## Enable flexible variants via the Cloudflare dashboard

  1. In the Cloudflare dashboard, go to the **Hosted Images** page.

[ Go to **Hosted images** ↗ ](https://dash.cloudflare.com/?to=/:account/images/hosted)
  2. Select the **Delivery** tab.

  3. Enable **Flexible variants**.




## Enable flexible variants via the API

Make a `PATCH` request to the [Update a variant endpoint](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/edit/).
    
    
    curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{"flexible_variants": true}'

After activation, you can use [optimization parameters](https://developers.cloudflare.com/images/optimization/features/#parameters) on any Cloudflare image. For example,

`https://imagedelivery.net/{account_hash}/{image_id}/w=400,sharpen=3`

Note

Flexible variants cannot be used for images that require a [signed delivery URL](https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/).

[PreviousCreate predefined variants](https://developers.cloudflare.com/images/optimization/hosted-images/create-variants/)[NextApply blur](https://developers.cloudflare.com/images/optimization/hosted-images/blur-variants/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/hosted-images/enable-flexible-variants.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
