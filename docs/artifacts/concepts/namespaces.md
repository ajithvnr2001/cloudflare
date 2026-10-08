---
url: https://developers.cloudflare.com/artifacts/concepts/namespaces/
title: Namespaces \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:20.574526+00:00
---

# Namespaces · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/concepts/namespaces/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Concepts
  4. /Namespaces



# Namespaces

Last updated Aug 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/concepts/namespaces/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse namespaces as containersChoose a namespace nameChoose a data locationUse the same namespace everywhereSplit namespaces when needed

Artifacts uses namespaces as top-level containers for repositories. Use them to separate repositories by environment, such as `prod`, `staging`, and `dev`, by tenant, or shard.

You can create a namespace explicitly or let Artifacts create one automatically. If you create a repo under a namespace name that does not exist, Artifacts creates the namespace automatically.

## Use namespaces as containers

Start with one namespace per environment or tenant boundary.

  * Use environment namespaces such as `prod`, `staging`, or `dev`.
  * Use tenant or shard namespaces when one shared namespace would become too hot or too large.
  * Keep repository names unique within each namespace.



## Choose a namespace name

Start with a stable name such as `default`, `staging`, or `agents-realtime`.

Namespace names follow the same public naming rules as repo names:

  * start with a letter or digit
  * use letters, digits, `.`, `_`, or `-` after the first character
  * keep the name stable across your Workers, API clients, and Git workflows



If you have not chosen a namespace strategy yet, use `default` in the examples throughout this docset.

## Choose a data location

Select a jurisdiction when you create a namespace to restrict where Artifacts stores and processes repo data. Every repo in that namespace uses the selected jurisdiction.

You cannot change a namespace jurisdiction after creation. For supported jurisdictions and creation instructions, refer to [Data localization](https://developers.cloudflare.com/artifacts/guides/data-localization/).

## Use the same namespace everywhere

Use the same namespace name in your Wrangler binding:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "artifacts": [
        {
          "binding": "ARTIFACTS",
          "namespace": "default"
        }
      ]
    }
    
    
    [[artifacts]]
    binding = "ARTIFACTS"
    namespace = "default"

Use that same namespace in your REST base URL:
    
    
    export ACCOUNT_ID="<YOUR_ACCOUNT_ID>"
    export ARTIFACTS_NAMESPACE="default"
    export ARTIFACTS_BASE_URL="https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE"

## Split namespaces when needed

Start with one namespace when you are learning the product. Add more namespaces when you need clearer boundaries between environments, teams, or high-rate workloads.

For more information, refer to [Best practices for Artifacts](https://developers.cloudflare.com/artifacts/concepts/best-practices/#partition-namespaces-deliberately).

[PreviousHow Artifacts works](https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/)[NextRepositories](https://developers.cloudflare.com/artifacts/concepts/repositories/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/concepts/namespaces.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
