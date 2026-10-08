---
url: https://developers.cloudflare.com/kv/reference/data-location/
title: Data location \u00b7 Cloudflare Workers KV docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:41.692507+00:00
---

# Data location · Cloudflare Workers KV docs

> Source: https://developers.cloudflare.com/kv/reference/data-location/

  1. [Home](https://developers.cloudflare.com/)
  2. /[KV](https://developers.cloudflare.com/kv/)
  3. /Reference
  4. /Data location



# Data location

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/kv/reference/data-location/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStandard (default)Restrict a namespace to a jurisdiction Supported jurisdictions Use Wrangler Use REST API

Learn how the location of data stored in Workers KV is determined, including how you can restrict a namespace to a specific jurisdiction.

## Standard (default)

By default, data written to a Workers KV namespace is stored in KV's central data stores with no jurisdictional restriction, and then cached globally across Cloudflare's network, allowing your data to be read with low latency from anywhere in the world. Refer to [How KV works](https://developers.cloudflare.com/kv/concepts/how-kv-works/) for more information.

## Restrict a namespace to a jurisdiction

Jurisdictions are used to create Workers KV namespaces that only durably store data within a region, to help comply with data locality regulations such as the [GDPR ↗︎](https://gdpr-info.eu/) or [FedRAMP ↗︎](https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/).

Workers may still access a namespace constrained to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction location on Cloudflare's network. The jurisdiction constraint only controls where the namespace's data is durably stored. Consider using [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/) to control the regions from which Cloudflare responds to requests.

Note

Jurisdictions can only be set when a namespace is created and cannot be added or changed afterwards.

### Supported jurisdictions

Parameter | Data Storage Location  
---|---  
eu | European Union  
fedramp | FedRAMP-compliant data centers  
us | United States of America  
  
### Use Wrangler

To create a namespace restricted to a jurisdiction, pass the `--jurisdiction` flag to [`wrangler kv namespace create`](https://developers.cloudflare.com/kv/reference/kv-commands/#kv-namespace-create):
    
    
    npx wrangler@latest kv namespace create <NAMESPACE_NAME> --jurisdiction=eu

### Use REST API

To create a namespace restricted to a jurisdiction, include the `jurisdiction` field in the request body when you [create a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/create/):

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Workers KV Storage Write`

Create a namespacebash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/storage/kv/namespaces" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"title": "<NAMESPACE_NAME>",
    		"jurisdiction": "eu"
    	}'

[PreviousEnvironments](https://developers.cloudflare.com/kv/reference/environments/)[NextData security](https://developers.cloudflare.com/kv/reference/data-security/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/kv/reference/data-location.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
