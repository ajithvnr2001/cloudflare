---
url: https://developers.cloudflare.com/artifacts/guides/data-localization/
title: Data localization \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:21.563074+00:00
---

# Data localization · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/guides/data-localization/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Guides
  4. /Data localization



# Data localization

Last updated Aug 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/guides/data-localization/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported jurisdictionsCreate a namespace with a jurisdiction

Artifacts jurisdictions ensure repo data is stored and processed only within a selected location. Set a jurisdiction when you create a namespace to apply the restriction to every repo in that namespace.

## Supported jurisdictions

Artifacts supports the following jurisdictions:

Jurisdiction | Location  
---|---  
`eu` | European Union  
`us` | United States  
  
## Create a namespace with a jurisdiction

To restrict a namespace to the European Union, set `jurisdiction` to `eu` when you create the namespace:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "namespace": "my-eu-namespace",
        "jurisdiction": "eu"
      }'

The selected jurisdiction applies to every repo in the namespace. You cannot change the jurisdiction after creating the namespace. The `jurisdiction` parameter is optional. If you omit it, the namespace remains unrestricted.

For endpoint details, refer to the [Artifacts REST API reference](https://developers.cloudflare.com/artifacts/api/rest-api/#create-a-namespace).

[PreviousBuild and deploy Artifacts repos](https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/)[NextHow Artifacts works](https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/guides/data-localization.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
