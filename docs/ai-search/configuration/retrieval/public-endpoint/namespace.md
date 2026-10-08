---
url: https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/namespace/
title: Namespace public endpoints \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:40.694134+00:00
---

# Namespace public endpoints · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/namespace/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)Retrieval

  4. /[Public endpoint settings](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/)
  5. /Namespace public endpoints



# Namespace public endpoints

Last updated Aug 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/namespace/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable a namespace public endpointThe instances allowlistSearch a subset of instancesDisable a namespace public endpointErrorsNext steps

A [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/) can expose its own public endpoint. A single URL then searches across several instances in that namespace and merges the results. Use one when a single search experience covers content that lives in several instances, such as documentation, a blog, and a support portal.

A namespace endpoint serves the same paths and takes the same settings as an instance endpoint, including [custom domains](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/) and [Cloudflare Access](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/). Refer to [Public endpoint settings](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/). This page covers what is specific to namespaces.

## Enable a namespace public endpoint

Set `public_endpoint_params` on the namespace and list the instances to expose in `instances_allowed`.
    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/<NAMESPACE>" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "public_endpoint_params": {
          "enabled": true,
          "instances_allowed": ["docs", "blog", "support"]
        }
      }'

The response returns the generated `public_endpoint_id`. A namespace hostname is prefixed with `ns-`:
    
    
    https://ns-<NAMESPACE_ENDPOINT_ID>.search.ai.cloudflare.com/search

Enabling a namespace endpoint does not change the instance endpoints inside it. Each is enabled and disabled separately.

## The instances allowlist

`instances_allowed` controls which instances the endpoint can reach.

  * Every entry must be an existing instance in that namespace. An unknown entry returns error `7097`.
  * The list holds up to 10 instances.
  * An empty list means nothing is searchable. This is the state a namespace starts in when you first enable the endpoint.
  * Deleting an instance, or moving it to another namespace, removes it from the allowlist.



A request that resolves to no searchable instance returns a `404` with error `60013`. This response is identical whether the instance does not exist, is outside the allowlist, or the allowlist is empty, so callers cannot discover which instances a namespace contains.

Caution

`public_endpoint_params` is replaced in full on every update. Send the complete object, including `instances_allowed`, or omitted fields revert to their defaults. Omitting `instances_allowed` resets it to an empty list and makes the endpoint return `404` for every request.

## Search a subset of instances

By default, a request searches every instance in the allowlist. To narrow a single request, set `ai_search_options.instance_ids` in the request body.
    
    
    curl https://ns-<NAMESPACE_ENDPOINT_ID>.search.ai.cloudflare.com/search \
      --header "Content-Type: application/json" \
      --data '{
        "messages": [
          {
            "content": "How do I configure AI Search?",
            "role": "user"
          }
        ],
        "ai_search_options": {
          "instance_ids": ["docs", "support"]
        }
      }'

Every value must be in the allowlist. Rules for this field:

  * Omitting the field, or setting it to `null`, searches the full allowlist.
  * A malformed value, such as an empty array or a non-string entry, returns a `400` with error `60012`.
  * A value outside the allowlist returns a `404` with error `60013`.



Note

The request body must be a JSON object. An array, a string, or an empty body returns a `400` with error `60015`.

## Disable a namespace public endpoint

Set `public_endpoint_params` to `null`. This clears the configuration and stops serving traffic, but keeps the identifier so the URL is reused if you enable the endpoint again.
    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/<NAMESPACE>" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "public_endpoint_params": null
      }'

## Errors

Code | Message | HTTP status | Cause  
---|---|---|---  
`7097` | `instances_allowed_contains_unknown_instances` | 400 | An entry in `instances_allowed` is not an instance in this namespace.  
`7099` | `namespace_modified_concurrently_please_retry` | 409 | Another update changed the namespace at the same time. Retry.  
`60012` | `invalid ai_search_options.instance_ids` | 400 | The `instance_ids` value is malformed.  
`60013` | `ai_search_not_found` | 404 | No searchable instance matched the request.  
`60014` | `path not supported for namespace-kind hash` | 404 | The path is not `/search`, `/chat/completions`, or `/mcp`.  
`60015` | `request body must be a JSON object` | 400 | The request body is not a JSON object.  
  
## Next steps

### [Namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/)

Group instances into namespaces and manage them from a Workers binding.

### [Search across multiple instances](https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/)

Query several instances from a Worker or the REST API.

### [Custom domains](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/)

Serve a namespace public endpoint from a hostname that you own.

[PreviousOverview](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/)[NextCustom domains](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/retrieval/public-endpoint/namespace.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
