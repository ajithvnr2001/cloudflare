---
url: https://developers.cloudflare.com/resource-tagging/reference/error-codes/
title: Error codes \u00b7 Cloudflare Resource Tagging docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:45.349298+00:00
---

# Error codes · Cloudflare Resource Tagging docs

> Source: https://developers.cloudflare.com/resource-tagging/reference/error-codes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Resource Tagging](https://developers.cloudflare.com/resource-tagging/)
  3. /[Reference](https://developers.cloudflare.com/resource-tagging/reference/)
  4. /Error codes



# Error codes

Last updated Apr 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/resource-tagging/reference/error-codes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError code referenceResource not found behavior

## Error code reference

Code | HTTP status | Message | Likely cause | Resolution  
---|---|---|---|---  
`1002` | 400 | Invalid set payload | Request body is malformed or missing required fields | Verify the body is valid JSON with `resource_type`, `resource_id`, and `tags`  
`1003` | 400 | `resource_type` and `resource_id` are required | Missing query parameters | Include both `resource_type` and `resource_id` in the query string  
`1006` | 400 | Invalid resource type | Unsupported resource type | Use a [supported resource type](https://developers.cloudflare.com/resource-tagging/reference/resource-types/)  
`1007` | 400 | tag parameter must be in format... | Tag filter syntax is incorrect | Refer to [tag filtering syntax](https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/)  
`1009` | 400 | `tag_key` is required | Missing `tag_key` parameter | Include the `tag_key` path parameter  
`1010` | 400 | too many tag filters (maximum 20) | More than 20 `tag` query parameters | Reduce filters to 20 or fewer, or split across multiple requests  
`1011` | 400 | tag key too long (maximum 256 characters) | Tag key exceeds 256 characters | Shorten the tag key  
`1012` | 400 | tag value too long (maximum 1024 characters) | Tag value exceeds 1,024 characters | Shorten the tag value  
`1013` | 400 | too many OR values in tag filter (maximum 10) | More than 10 comma-separated values in a single filter | Split into multiple filters  
`1014` | 400 | Invalid tag key | Key contains invalid characters | Use only letters, digits, `_`, `.`, `-`  
`1015` | 400 | Invalid delete payload | Delete request body is malformed | Verify the body includes `resource_type` and `resource_id`  
  
Error 1007 note

The error message text references `:` as the tag filter separator (for example, `key:value`), but the API implementation uses `=` in query parameters (for example, `tag=key=value`). The error message is outdated — always use `=` when constructing tag filters.

## Resource not found behavior

In the current beta, `GET /accounts/{account_id}/tags` returns `500 Internal Server Error` for resources that do not exist or have never been tagged:
    
    
    "resource not found: type={resource_type} id={resource_id}"

List endpoints (`/tags/resources`, `/tags/keys`, `/tags/values/{key}`) return `200 OK` with an empty result array when no matches are found -- this is expected, not an error.

This `500` behavior is a known beta limitation and may change to `404` in a future release.

[PreviousLimits and validation](https://developers.cloudflare.com/resource-tagging/reference/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/resource-tagging/reference/error-codes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
