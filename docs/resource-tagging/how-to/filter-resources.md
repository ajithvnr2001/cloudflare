---
url: https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/
title: Filter resources by tag \u00b7 Cloudflare Resource Tagging docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:44.834642+00:00
---

# Filter resources by tag · Cloudflare Resource Tagging docs

> Source: https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Resource Tagging](https://developers.cloudflare.com/resource-tagging/)
  3. /[How-to guides](https://developers.cloudflare.com/resource-tagging/how-to/)
  4. /Filter resources by tag



# Filter resources by tag

Last updated Apr 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFilter types Key-only filter Key-value filter Multiple values (OR) Negate key Negate key-valueCombining filtersDiscover available tags List all tag keys List values for a keyPagination

The `GET /accounts/{account_id}/tags/resources` endpoint supports tag filtering via the `tag` query parameter. Multiple `tag` parameters combine with AND logic. For the full endpoint specification, refer to the [Resource Tagging API reference ↗︎](https://developers.cloudflare.com/api/resources/tags/).

Caution

Use `=` as the separator in tag filters (for example, `tag=key=value`), not `:`. The API error message references `:` but the implementation uses `=`.

## Filter types

### Key-only filter

Match resources that have a specific tag key, regardless of value.
    
    
    # All resources with an "environment" tag (any value)
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment" \
      -H "Authorization: Bearer $API_TOKEN"

### Key-value filter

Match resources where a tag key has a specific value.
    
    
    # All resources with environment=production
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production" \
      -H "Authorization: Bearer $API_TOKEN"

### Multiple values (OR)

Match resources where a tag key has any of the specified values. Separate values with commas.
    
    
    # environment=production OR environment=staging
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production,staging" \
      -H "Authorization: Bearer $API_TOKEN"

Maximum of 10 OR values per filter (error code `1013` if exceeded).

### Negate key

Match resources that do **not** have a specific tag key.
    
    
    # All resources without an "archived" tag
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=!archived" \
      -H "Authorization: Bearer $API_TOKEN"

### Negate key-value

Match resources where a tag key does **not** have a specific value.
    
    
    # All resources where region is NOT us-west-1
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=region!=us-west-1" \
      -H "Authorization: Bearer $API_TOKEN"

## Combining filters

Multiple `tag` parameters combine with AND logic. All conditions must match.
    
    
    # Production resources in US regions, excluding archived
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production&tag=region=us-west-1,us-east-1&tag=!archived" \
      -H "Authorization: Bearer $API_TOKEN"

Maximum of 20 tag filters per query (error code `1010` if exceeded).

## Discover available tags

### List all tag keys
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/keys" \
      -H "Authorization: Bearer $API_TOKEN"

### List values for a key
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/values/environment" \
      -H "Authorization: Bearer $API_TOKEN"

Optionally filter by resource type:
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/values/environment?type=worker" \
      -H "Authorization: Bearer $API_TOKEN"

## Pagination

All list endpoints use cursor-based pagination with a fixed page size of 100 results.

When the response includes a non-null `result_info.cursor`, pass it as a query parameter to get the next page:
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production&cursor=$CURSOR" \
      -H "Authorization: Bearer $API_TOKEN"

When `cursor` is `null`, you have reached the last page. Pagination works seamlessly with tag filters.

[PreviousManage tags](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/)[NextOverview](https://developers.cloudflare.com/resource-tagging/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/resource-tagging/how-to/filter-resources.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
