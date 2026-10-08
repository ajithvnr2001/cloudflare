---
url: https://developers.cloudflare.com/kv/concepts/kv-namespaces/
title: KV namespaces \u00b7 Cloudflare Workers KV docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:40.231173+00:00
---

# KV namespaces · Cloudflare Workers KV docs

> Source: https://developers.cloudflare.com/kv/concepts/kv-namespaces/

  1. [Home](https://developers.cloudflare.com/)
  2. /[KV](https://developers.cloudflare.com/kv/)
  3. /Key concepts
  4. /KV namespaces



# KV namespaces

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/kv/concepts/kv-namespaces/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewJurisdictionsBind your KV namespace through WranglerBind your KV namespace via the dashboard

A KV namespace is a key-value database replicated to Cloudflare’s global network.

Bind your KV namespaces through Wrangler or via the Cloudflare dashboard.

Note

KV namespace IDs are public and bound to your account.

## Jurisdictions

Namespaces can optionally be restricted to a jurisdiction to durably store data only within a specific region. Refer to [Data location](https://developers.cloudflare.com/kv/reference/data-location/) for more information.

## Bind your KV namespace through Wrangler

To bind KV namespaces to your Worker, assign an array of the below object to the `kv_namespaces` key.

  * `binding` `string` required

    * The binding name used to refer to the KV namespace.
  * `id` `string` required

    * The ID of the KV namespace.
  * `preview_id` `string` optional

    * The ID of the KV namespace used during `wrangler dev`.



Example:
    
    
    {
    	"kv_namespaces": [
    		{
    			"binding": "<TEST_NAMESPACE>",
    			"id": "<TEST_ID>"
    		}
    	]
    }
    
    
    [[kv_namespaces]]
    binding = "<TEST_NAMESPACE>"
    id = "<TEST_ID>"

## Bind your KV namespace via the dashboard

To bind the namespace to your Worker in the Cloudflare dashboard:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your **Worker**.

  3. Select **Settings** > **Bindings**.

  4. Select **Add**.

  5. Select **KV Namespace**.

  6. Enter your desired variable name (the name of the binding).

  7. Select the KV namespace you wish to bind the Worker to.

  8. Select **Deploy**.




[PreviousKV bindings](https://developers.cloudflare.com/kv/concepts/kv-bindings/)[NextRead key-value pairs](https://developers.cloudflare.com/kv/api/read-key-value-pairs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/kv/concepts/kv-namespaces.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
