---
url: https://developers.cloudflare.com/resource-tagging/
title: Overview \u00b7 Cloudflare Resource Tagging docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:44.766323+00:00
---

# Overview · Cloudflare Resource Tagging docs

> Source: https://developers.cloudflare.com/resource-tagging/

  1. [Home](https://developers.cloudflare.com/)
  2. /Resource Tagging



# Resource Tagging

Last updated Apr 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/resource-tagging/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksLimitationsGet started

Attach custom key-value metadata to Cloudflare resources for organization, access control, and billing attribution.

Available on all plans

Resource Tagging lets you attach key-value pairs to a wide range of [Cloudflare resource types](https://developers.cloudflare.com/resource-tagging/reference/resource-types/) — including zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, and more. Tags are stored separately from the resources themselves, enabling cross-resource queries and policy enforcement without modifying underlying resource configurations.

Public beta

Resource Tagging is in public beta. The API is stable, but behavior may change as we iterate based on feedback.

## How it works

Tags are simple key-value string pairs stored as a JSON object:
    
    
    {
      "environment": "production",
      "team": "platform",
      "region": "us-west-1"
    }

You manage tags through the Tagging API using `GET`, `PUT`, and `DELETE` operations. The API supports [filtering resources by tags](https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/) with AND/OR logic, negation, and key-only matching.

Authentication uses [Account Owned Tokens (AOTs)](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/), which are account-level tokens independent of individual users.

## Limitations

  * The dashboard is in beta. You can view and manage tags in the dashboard under **Manage Account** > **Resource Tagging** , but the API remains the recommended interface for automation workflows.
  * `PUT` replaces all tags. There is no `PATCH` endpoint. The `PUT` operation replaces all tags on a resource. Use the [`GET`, merge, `PUT` workflow](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/#add-a-single-tag) to modify individual tags.
  * `DELETE` removes all tags. There is no way to delete a single tag. Use `PUT` with the remaining tags instead.
  * Querying tags for a resource that has never been tagged returns a `500` error instead of `404`. This is a known beta limitation.



## Get started

Follow the [Get started guide](https://developers.cloudflare.com/resource-tagging/get-started/) to set up authentication and make your first API calls.

[NextGet started](https://developers.cloudflare.com/resource-tagging/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/resource-tagging/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
