---
url: https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/
title: Delete variants \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:34.953332+00:00
---

# Delete variants · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Optimization

  4. /Hosted images
  5. /Delete variants



# Delete variants

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDelete variants via the Cloudflare dashboardDelete variants via the API

You can delete variants via the Images dashboard or API. The only variant you cannot delete is public.

Caution

Deleting a variant is a global action that will affect other images that contain that variant.

## Delete variants via the Cloudflare dashboard

  1. In the Cloudflare dashboard, go to the **Hosted Images** page.

[ Go to **Hosted images** ↗ ](https://dash.cloudflare.com/?to=/:account/images/hosted)
  2. Select the **Delivery** tab.

  3. Find the variant you want to remove and select **Delete**.




## Delete variants via the API

Make a `DELETE` request to the delete variant endpoint.
    
    
    curl --request DELETE https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/variants/{variant_name} \
    --header "Authorization: Bearer <API_TOKEN>"

After the variant has been deleted, the response returns `"success": true.`

[PreviousApply blur](https://developers.cloudflare.com/images/optimization/hosted-images/blur-variants/)[NextPreserve Content Credentials](https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/hosted-images/delete-variants.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
