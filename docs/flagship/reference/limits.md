---
url: https://developers.cloudflare.com/flagship/reference/limits/
title: Limits \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:18.115151+00:00
---

# Limits · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/reference/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /Reference
  4. /Limits



# Limits

Last updated Jun 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/flagship/reference/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPlatform limitsNotes

Flagship enforces the following limits.

## Platform limits

Feature | Limit  
---|---  
Apps per account | 10,000  
Flags per app | 5,000  
Flag, app, and variant keys | 64 chars  
Condition attribute names | 64 chars  
Condition string values | 256 chars  
Variant value size | 10 KB  
Condition nesting depth | 5 levels  
Flag description | 512 chars  
Flag configuration size per app | 25 MB  
  
Note

The apps-per-account and flags-per-app limits are soft limits. If your use case requires higher limits, contact Cloudflare support.

## Notes

  * Condition nesting depth counts from the top-level condition group. A flat list of conditions (no nesting) has a depth of 1.
  * Flag keys, app names, condition set names, and variant keys can contain letters, numbers, hyphens, and underscores.
  * All variants on a flag must use the same value type: boolean, string, number, or JSON.
  * Flag configuration size refers to the total serialized size of all flags within a single app, including their variants and rules.



[PreviousPercentage rollouts](https://developers.cloudflare.com/flagship/targeting/percentage-rollouts/)[NextEvaluation reasons and error codes](https://developers.cloudflare.com/flagship/reference/evaluation-reasons/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/reference/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
