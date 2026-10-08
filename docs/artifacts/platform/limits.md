---
url: https://developers.cloudflare.com/artifacts/platform/limits/
title: Limits \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:21.974586+00:00
---

# Limits · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Platform
  4. /Limits



# Limits

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Limits that apply to creating, importing, cloning, and pushing Artifacts are detailed below.

These limits cover naming rules, storage, and request rates for control-plane and Git operations.

Feature | Limit  
---|---  
Control-plane request rate | 2,000 requests per 10 seconds per Artifacts namespace  
Git request rate, per artifact | 2,000 requests per 10 seconds per artifact  
Maximum storage per repository | 1 GB  
Maximum individual file or blob size | 32 MB  
Maximum storage per account | 1 TB (can be raised on request)  
Maximum number of repositories | Unlimited  
Maximum number of namespaces | Unlimited  
Namespace name length | 2-63 characters  
Namespace and repo names | Start with a letter or digit. Remaining characters may include letters, digits, `.`, `_`, and `-`.  
  
[PreviousPricing](https://developers.cloudflare.com/artifacts/platform/pricing/)[NextChangelog](https://developers.cloudflare.com/artifacts/platform/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
