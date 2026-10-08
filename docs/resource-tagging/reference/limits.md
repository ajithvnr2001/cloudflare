---
url: https://developers.cloudflare.com/resource-tagging/reference/limits/
title: Limits and validation \u00b7 Cloudflare Resource Tagging docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:45.056619+00:00
---

# Limits and validation · Cloudflare Resource Tagging docs

> Source: https://developers.cloudflare.com/resource-tagging/reference/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Resource Tagging](https://developers.cloudflare.com/resource-tagging/)
  3. /[Reference](https://developers.cloudflare.com/resource-tagging/reference/)
  4. /Limits and validation



# Limits and validation

Last updated Apr 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/resource-tagging/reference/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAPI limitsCase sensitivityTag key validation Allowed Not allowed ExamplesPagination

## API limits

Limit | Value | Error code  
---|---|---  
Maximum tags per account | 10,000 (beta) | N/A  
Maximum tag key length | 256 characters | `1011`  
Maximum tag value length | 1,024 characters | `1012`  
Maximum tag filters per query | 20 | `1010`  
Maximum OR values per filter | 10 | `1013`  
Results per page | 100 (fixed) | N/A  
  
When a limit is exceeded, the API returns `400 Bad Request` with the corresponding error code.

During the beta, each account is limited to 10,000 total tags. If you need a higher limit, contact [Cloudflare support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

## Case sensitivity

Tag keys and values are case-sensitive. `Environment`, `environment`, and `ENVIRONMENT` are treated as three distinct keys. Be consistent with casing conventions across your organization to avoid duplicate keys.

## Tag key validation

Tag keys must follow these character rules:

### Allowed

  * Unicode letters (any language)
  * Unicode digits (0-9)
  * Underscores (`_`)
  * Periods (`.`)
  * Hyphens (`-`)



### Not allowed

  * Empty strings
  * Spaces
  * Special characters (except `_`, `.`, `-`)



### Examples

Key | Valid | Reason  
---|---|---  
`environment` | Yes | Letters only  
`team_name` | Yes | Underscore  
`cost-center` | Yes | Hyphen  
`owner.email` | Yes | Period  
`env123` | Yes | Letters and digits  
`env name` | **No** | Contains space  
`team@work` | **No** | Special character `@`  
(empty) | **No** | Empty string  
  
Invalid tag keys return `400 Bad Request` with error code `1014`.

## Pagination

List endpoints use cursor-based pagination with a fixed page size of 100. The page size is not configurable.

Paginated endpoints:

  * `GET /accounts/{account_id}/tags/keys`
  * `GET /accounts/{account_id}/tags/resources`
  * `GET /accounts/{account_id}/tags/values/{tag_key}`



Refer to [Filter resources by tag](https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/#pagination) for pagination examples.

[PreviousSupported resource types](https://developers.cloudflare.com/resource-tagging/reference/resource-types/)[NextError codes](https://developers.cloudflare.com/resource-tagging/reference/error-codes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/resource-tagging/reference/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
