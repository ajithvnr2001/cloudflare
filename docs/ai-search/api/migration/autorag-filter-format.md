---
url: https://developers.cloudflare.com/ai-search/api/migration/autorag-filter-format/
title: Metadata filter (legacy) \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:37.472830+00:00
---

# Metadata filter (legacy) · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/api/migration/autorag-filter-format/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

API

  4. /API Migration
  5. /Metadata filter (legacy)



# Metadata filter (legacy)

Last updated Jun 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/api/migration/autorag-filter-format/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewComparison filter OperatorsCompound filter Limitations"Starts with" filter for foldersRelated

This page documents the filter format used by the legacy AutoRAG REST API. For the new AI Search REST API filter syntax, refer to [Metadata filtering](https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/).

## Comparison filter

Compare a metadata attribute (for example, `folder` or `timestamp`) with a target value:
    
    
    filters: {
      type: "eq",
      key: "folder",
      value: "customer-a/"
    }

### Operators

Operator | Description  
---|---  
`eq` | Equals  
`ne` | Not equals  
`gt` | Greater than  
`gte` | Greater than or equal to  
`lt` | Less than  
`lte` | Less than or equal to  
  
## Compound filter

Combine multiple comparison filters with a logical operator:
    
    
    filters: {
      type: "and",
      filters: [
        { type: "eq", key: "folder", value: "customer-a/" },
        { type: "gte", key: "timestamp", value: "1735689600000" }
      ]
    }

The available compound operators are `and` and `or`.

### Limitations

  * No nested combinations of `and` and `or`. You can only use one compound operator at a time.
  * When using `or`, only the `eq` operator is allowed and all conditions must filter on the same key.



## "Starts with" filter for folders

To filter for all files within a folder and its subfolders, use a compound filter with range operators.

For example, consider this file structure:

  * customer-a - profile.md - contracts - property - contract-1.pdf



Using `{ type: "eq", key: "folder", value: "customer-a/" }` only matches files directly in that folder (like `profile.md`), not files in subfolders.

To match all files starting with `customer-a/`, use a compound filter:
    
    
    filters: {
      type: "and",
      filters: [
        { type: "gt", key: "folder", value: "customer-a//" },
        { type: "lte", key: "folder", value: "customer-a/z" }
      ]
    }

This filter matches all paths starting with `customer-a/` by using:

  * `gt` with `customer-a//` to include paths greater than the `/` ASCII character
  * `lte` with `customer-a/z` to include paths up to and including the lowercase `z` ASCII character



## Related

  * [Metadata filtering](https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/) \- New AI Search REST API filter format
  * [Migrate from AutoRAG Search API](https://developers.cloudflare.com/ai-search/api/migration/rest-api/) \- Migration guide with before/after examples



[PreviousWorkers binding (legacy)](https://developers.cloudflare.com/ai-search/api/migration/workers-binding-legacy/)[NextWrangler CLI](https://developers.cloudflare.com/ai-search/wrangler-commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/api/migration/autorag-filter-format.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
