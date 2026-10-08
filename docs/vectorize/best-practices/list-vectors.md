---
url: https://developers.cloudflare.com/vectorize/best-practices/list-vectors/
title: List vectors \u00b7 Cloudflare Vectorize docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:13.372068+00:00
---

# List vectors · Cloudflare Vectorize docs

> Source: https://developers.cloudflare.com/vectorize/best-practices/list-vectors/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Vectorize](https://developers.cloudflare.com/vectorize/)
  3. /Best practices
  4. /List vectors



# List vectors

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/vectorize/best-practices/list-vectors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use list-vectorsPagination behavior Snapshot consistency Starting a new iteration Response structure Cursor expirationPerformance considerationsExample workflow

The list-vectors operation allows you to enumerate all vector identifiers in a Vectorize index using paginated requests. This guide covers best practices for efficiently using this operation.

Python SDK availability

The `client.vectorize.indexes.list_vectors()` method is not yet available in the current release of the [Cloudflare Python SDK ↗︎](https://pypi.org/project/cloudflare/). While the method appears in the [API reference](https://developers.cloudflare.com/api/python/resources/vectorize/subresources/indexes/methods/list_vectors/), it has not been included in a published SDK version as of v4.3.1. In the meantime, you can use the [REST API](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/list_vectors/) or the Wrangler CLI to list vectors.

## When to use list-vectors

Use list-vectors for:

  * **Bulk operations** : To process all vectors in an index
  * **Auditing** : To verify the contents of your index or generate reports
  * **Data migration** : To move vectors between indexes or systems
  * **Cleanup operations** : To identify and remove outdated vectors



## Pagination behavior

The list-vectors operation uses cursor-based pagination with important consistency guarantees:

### Snapshot consistency

Vector identifiers returned belong to the index snapshot captured at the time of the first list-vectors request. This ensures consistent pagination even when the index is being modified during iteration:

  * **New vectors** : Vectors inserted after the initial request will not appear in subsequent paginated results
  * **Deleted vectors** : Vectors deleted after the initial request will continue to appear in the remaining responses until pagination is complete



### Starting a new iteration

To see recently added or removed vectors, you must start a new list-vectors request sequence (without a cursor). This captures a fresh snapshot of the index.

### Response structure

Each response includes:

  * `count`: Number of vectors returned in this response
  * `totalCount`: Total number of vectors in the index
  * `isTruncated`: Whether there are more vectors available
  * `nextCursor`: Cursor for the next page (null if no more results)
  * `cursorExpirationTimestamp`: Timestamp of when the cursor expires
  * `vectors`: Array of vector identifiers



### Cursor expiration

Cursors have an expiration timestamp. If a cursor expires, you'll need to start a new list-vectors request sequence to continue pagination.

## Performance considerations

Take care to have sufficient gap between consecutive requests to avoid hitting rate-limits.

## Example workflow

Here's a typical pattern for processing all vectors in an index:
    
    
    # Start iteration
    wrangler vectorize list-vectors my-index --count=1000
    
    # Continue with cursor from response
    wrangler vectorize list-vectors my-index --count=1000 --cursor="<cursor-from-response>"
    
    # Repeat until no more results

[PreviousInsert vectors](https://developers.cloudflare.com/vectorize/best-practices/insert-vectors/)[NextQuery vectors](https://developers.cloudflare.com/vectorize/best-practices/query-vectors/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/vectorize/best-practices/list-vectors.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
